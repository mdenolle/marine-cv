import re
import textwrap
from datetime import date as Date

from rendercv.exception import RenderCVInternalError
from rendercv.schema.models.cv.entries.publication import PublicationEntry
from rendercv.schema.models.cv.section import Entry
from rendercv.schema.models.design.classic_theme import Templates
from rendercv.schema.models.locale.locale import Locale

from .date import compute_time_span_string, format_date_range, format_single_date
from .string_processor import clean_url, substitute_placeholders

uppercase_word_pattern = re.compile(r"\b[A-Z_]+\b")


def render_entry_templates[EntryType: Entry](
    entry: EntryType,
    *,
    templates: Templates,
    locale: Locale,
    show_time_span: bool,
    current_date: Date,
) -> EntryType:
    """Expand entry templates by substituting field placeholders with processed values.

    Why:
        Entry display is user-customizable through YAML templates. This applies
        templates to entries, processing special fields (dates, highlights, URLs)
        and removing placeholders for missing optional fields.

    Args:
        entry: Entry to process with templates.
        templates: Template collection for entry types and dates.
        locale: Locale for date and text formatting.
        show_time_span: Whether to include duration calculation in dates.
        current_date: Reference date for "present" and time span calculations.

    Returns:
        Entry with template-generated display fields.
    """
    if isinstance(entry, str) or not hasattr(templates, entry.entry_type_in_snake_case):
        # It's a TextEntry, or an entry type without templates. Return it as is:
        return entry

    entry_templates: dict[str, str] = getattr(
        templates, entry.entry_type_in_snake_case
    ).model_dump(exclude_none=True)

    entry_fields: dict[str, str | str] = {
        key.upper(): value for key, value in entry.model_dump(exclude_none=True).items()
    }



    # Handle special placeholders:
    if "HIGHLIGHTS" in entry_fields:
        highlights = getattr(entry, "highlights", None)
        if highlights is None:
            raise RenderCVInternalError("HIGHLIGHTS in fields but highlights is None")
        entry_fields["HIGHLIGHTS"] = process_highlights(highlights)

    if "CITATIONS" in entry_fields:
        citations = getattr(entry, "citations", None)
        if citations is not None:
            entry_fields["CITATIONS"] = process_citations(citations)
        else:
            entry_fields["CITATIONS"] = ""  # Field not present in entry

    if "MEDIA_COVERAGE" in entry_fields:
        media_coverage = getattr(entry, "media_coverage", None)
        if media_coverage is None:
            raise RenderCVInternalError(
                "MEDIA_COVERAGE in fields but media_coverage is None"
            )
        entry_fields["MEDIA_COVERAGE"] = process_media_coverage(
            media_coverage
        )


    # For NormalEntry (e.g., teaching), use 'name' as the title and do not require 'authors'
    if entry.__class__.__name__ == "NormalEntry":
        entry_fields["TITLE"] = entry_fields.get("NAME", "")
        # Do not require AUTHORS for teaching/NormalEntry
    elif "AUTHORS" in entry_fields:
        authors = getattr(entry, "authors", None)
        if authors is not None:
            entry_fields["AUTHORS"] = process_authors(authors)
        else:
            # Remove AUTHORS from fields if None, so placeholder removal will handle it
            entry_fields.pop("AUTHORS", None)

    if (
        "DATE" in entry_fields
        or "START_DATE" in entry_fields
        or "END_DATE" in entry_fields
    ):
        entry_fields["DATE"] = process_date(
            date=getattr(entry, "date", None),
            start_date=getattr(entry, "start_date", None),
            end_date=getattr(entry, "end_date", None),
            locale=locale,
            show_time_span=show_time_span,
            current_date=current_date,
            single_date_template=templates.single_date,
            date_range_template=templates.date_range,
            time_span_template=templates.time_span,
        )

    if "START_DATE" in entry_fields:
        start_date = getattr(entry, "start_date", None)
        if start_date is None:
            raise RenderCVInternalError("START_DATE in fields but start_date is None")
        entry_fields["START_DATE"] = format_single_date(
            start_date,
            locale=locale,
            single_date_template=templates.single_date,
        )

    if "END_DATE" in entry_fields:
        end_date = getattr(entry, "end_date", None)
        if end_date is None:
            raise RenderCVInternalError("END_DATE in fields but end_date is None")
        entry_fields["END_DATE"] = format_single_date(
            end_date,
            locale=locale,
            single_date_template=templates.single_date,
        )

    if "URL" in entry_fields:
        entry_fields["URL"] = process_url(entry)  # ty: ignore[invalid-argument-type]

    if "DOI" in entry_fields:
        entry_fields["URL"] = process_url(entry)  # ty: ignore[invalid-argument-type]
        entry_fields["DOI"] = process_doi(entry)  # ty: ignore[invalid-argument-type]
        # Add JOURNAL_WITH_DOI for inline DOI display
        if "JOURNAL" in entry_fields:
            journal = entry_fields["JOURNAL"]
            doi = entry_fields["DOI"]
            entry_fields["JOURNAL_WITH_DOI"] = f"{journal}, {doi}"

    if "SUMMARY" in entry_fields:
        entry_fields["SUMMARY"] = process_summary(entry_fields["SUMMARY"])

    # Remove or hide fields marked as '__HIDDEN__'
    hidden_keys = {k for k, v in entry_fields.items() if v == "__HIDDEN__" or v == ["__HIDDEN__"]}
    if hidden_keys:
        # Remove these placeholders from templates and entry_fields
        for k in hidden_keys:
            entry_fields.pop(k, None)
        entry_templates = remove_not_provided_placeholders(entry_templates, entry_fields)
    else:
        entry_templates = remove_not_provided_placeholders(entry_templates, entry_fields)

    for template_name, template in (entry_templates | entry_fields).items():
        setattr(
            entry,
            template_name,
            substitute_placeholders(template, entry_fields),
        )

    return entry


def process_highlights(highlights: list[str]) -> str:
    """Convert highlight list to Markdown unordered list with nested items.

    Example:
        ```py
        result = process_highlights(
            [
                "Led team of 5 engineers",
                "Reduced costs - Server optimization - Database indexing",
            ]
        )
        # Returns:
        # - Led team of 5 engineers
        # - Reduced costs
        #   - Server optimization
        #   - Database indexing
        ```

    Args:
        highlights: Highlight strings with optional " - " for sub-bullets.

    Returns:
        Markdown list string with nested indentation.
    """
    highlights = ["- " + highlight.replace(" - ", "\n  - ") for highlight in highlights]
    return "\n".join(highlights)


def process_authors(authors: list[str]) -> str:
    """Join author names with comma separation.

    Args:
        authors: Author names for publication entry.

    Returns:
        Comma-separated author string.
    """
    return ", ".join(authors)


def process_media_coverage(media_coverage: list[str]) -> str:
    """Format media coverage URLs as markdown links with source names.
    
    Extracts the domain name from URLs to use as display text.
    
    Example:
        ```py
        # Entry with multiple URLs
        urls = ['https://news.washington.edu/article', 'https://harvard.edu/gazette']
        result = process_media_coverage(urls)
        # Returns: "Featured in: [UW News](...), [Harvard](...)"
        ```
    
    Args:
        media_coverage: List of media coverage URLs.
        
    Returns:
        Formatted markdown string with links.
    """
    if not media_coverage:
        return ""
    
    def extract_source_name(url: str) -> str:
        """Extract a friendly name from URL domain."""
        # Common patterns for news sources
        domain_map = {
            'news.washington.edu': 'UW News',
            'washington.edu': 'UW News',
            'news.harvard.edu': 'Harvard Gazette',
            'harvard.edu': 'Harvard Gazette',
            'news.stanford.edu': 'Stanford News',
            'sciencedaily.com': 'ScienceDaily',
            'eos.org': 'EOS',
            'science.org': 'Science',
            'sciencemag.org': 'Science',
            'nature.com': 'Nature',
            'youtube.com': 'Video',
            'youtu.be': 'Video',
        }
        
        # Extract domain from URL
        import re
        domain_match = re.search(r'https?://(?:www\.)?([^/]+)', url)
        if not domain_match:
            return 'Coverage'
        
        domain = domain_match.group(1)
        
        # Check for known domains
        for pattern, name in domain_map.items():
            if pattern in domain:
                return name
        
        # Default: use domain name, capitalize first word
        parts = domain.split('.')
        if len(parts) >= 2:
            return parts[0].capitalize()
        return 'Coverage'
    
    links = [
        f"[{extract_source_name(url)}]({url})"
        for url in media_coverage
    ]
    return "Featured in: " + ", ".join(links)


def process_date(
    *,
    date: str | int | None,
    start_date: str | int | None,
    end_date: str | int | None,
    locale: Locale,
    current_date: Date,
    show_time_span: bool,
    single_date_template: str,
    date_range_template: str,
    time_span_template: str,
) -> str:
    """Format date field as single date or range with optional time span.

    Why:
        Entry date fields vary by type: publications use single dates, experience
        uses ranges. This routes to appropriate formatter and optionally appends
        duration calculation for employment sections.

    Example:
        ```py
        # Single date for publication
        result = process_date(
            date="2024-03",
            start_date=None,
            end_date=None,
            locale=english_locale,
            current_date=Date(2025, 1, 1),
            show_time_span=False,
            single_date_template="MONTH_NAME YEAR",
            date_range_template="",
            time_span_template="",
        )
        # Returns: "March 2024"

        # Date range with time span for employment
        result = process_date(
            date=None,
            start_date="2020-06",
            end_date="present",
            locale=english_locale,
            current_date=Date(2025, 1, 1),
            show_time_span=True,
            single_date_template="MONTH_ABBREVIATION YEAR",
            date_range_template="START_DATE to END_DATE",
            time_span_template="HOW_MANY_YEARS YEARS",
        )
        # Returns: "Jun 2020 to present\n\n4 years"
        ```

    Args:
        date: Single date for publications and certifications.
        start_date: Range start for employment and education.
        end_date: Range end for employment and education.
        locale: Locale for date formatting.
        current_date: Reference date for "present" calculation.
        show_time_span: Whether to append duration to date range.
        single_date_template: Template for single date formatting.
        date_range_template: Template for date range formatting.
        time_span_template: Template for duration formatting.

    Returns:
        Formatted date string, optionally with time span on new lines.
    """
    if date and not (start_date or end_date):
        return format_single_date(
            date, locale=locale, single_date_template=single_date_template
        )
    if start_date and end_date:
        date_range = format_date_range(
            start_date,
            end_date,
            locale=locale,
            single_date_template=single_date_template,
            date_range_template=date_range_template,
        )
        if show_time_span:
            time_span = compute_time_span_string(
                start_date,
                end_date,
                locale=locale,
                current_date=current_date,
                time_span_template=time_span_template,
            )
            return f"{date_range}\n\n{time_span}"

        return date_range

    raise RenderCVInternalError("Date is not provided for this entry.")


def process_url(entry: Entry) -> str:
    """Format entry URL as Markdown link with cleaned display text.

    Example:
        ```py
        # Entry with url="https://www.example.com/project"
        result = process_url(entry)
        # Returns: "[example.com/project](https://www.example.com/project)"
        ```

    Args:
        entry: Entry with url or doi field.

    Returns:
        Markdown link with cleaned URL as display text.
    """
    if isinstance(entry, PublicationEntry) and entry.doi:
        return process_doi(entry)
    if hasattr(entry, "url") and entry.url:
        url = entry.url
        return f"[{clean_url(url)}]({url})"  # ty: ignore[invalid-argument-type]
    raise RenderCVInternalError("URL is not provided for this entry.")


def process_doi(entry: Entry) -> str:
    """Format publication DOI as Markdown link to DOI URL.

    Example:
        ```py
        # Entry with doi="10.1000/xyz123"
        result = process_doi(entry)
        # Returns: "[10.1000/xyz123](https://doi.org/10.1000/xyz123)"
        ```

    Args:
        entry: Publication entry with DOI.

    Returns:
        Markdown link with DOI as display text and DOI URL as target.
    """
    if isinstance(entry, PublicationEntry) and entry.doi:
        return f"[{entry.doi}]({entry.doi_url})"
    raise RenderCVInternalError("DOI is not provided for this entry.")


def process_citations(citations: int) -> str:
    """Format citation count for display.
    
    Args:
        citations: Number of citations (-1 = no data, 0 = no citations yet, >0 = citation count)
        
    Returns:
        Formatted string like \"Cited by 450\" or \"Citations: no data\"
    """
    if citations < 0:
        return "Citations: no data"
    elif citations == 0:
        return "Citations: 0"
    else:
        return f"Cited by {citations}"
    return ""


def process_summary(summary: str) -> str:
    """Wrap summary text in Markdown admonition syntax for special rendering in Typst.

    Example:
        ```py
        result = process_summary("Key project achievements\\nand outcomes")
        # Returns:
        # !!! summary
        #     Key project achievements
        #     and outcomes
        ```

    Args:
        summary: Summary text to wrap.

    Returns:
        Markdown admonition block with indented summary.
    """
    return f"!!! summary\n{textwrap.indent(summary, '    ')}"


def remove_not_provided_placeholders(
    entry_templates: dict[str, str], entry_fields: dict[str, str]
) -> dict[str, str]:
    """Remove template placeholders for missing optional fields and surrounding punctuation.

    Why:
        Optional entry fields like location or URL should disappear cleanly from
        templates when not provided. Regex removal eliminates placeholders plus
        adjacent punctuation to prevent "Position at " or trailing commas.

    Example:
        ```py
        templates = {"title": "POSITION at COMPANY, LOCATION"}
        fields = {"POSITION": "Engineer", "COMPANY": "Acme"}  # LOCATION missing
        result = remove_not_provided_placeholders(templates, fields)
        # Returns: {"title": "POSITION at COMPANY"}
        ```

    Args:
        entry_templates: Template strings with uppercase placeholders.
        entry_fields: Available field values with uppercase keys.

    Returns:
        Templates with missing placeholders and surrounding characters removed.
    """
    # Remove the not provided placeholders from the templates, including characters
    # around them:
    used_placeholders_in_templates = set(
        uppercase_word_pattern.findall(" ".join(entry_templates.values()))
    )
    not_provided_placeholders = used_placeholders_in_templates - set(
        entry_fields.keys()
    )
    if not_provided_placeholders:
        not_provided_placeholders_pattern = re.compile(
            r"\S*(?:" + "|".join(not_provided_placeholders) + r")\S*"
        )
        entry_templates = {
            key: clean_trailing_parts(not_provided_placeholders_pattern.sub("", value))
            for key, value in entry_templates.items()
        }

    return entry_templates


unwanted_trailing_parts_pattern = re.compile(r"[^A-Za-z0-9.!?\[\]\(\)\*_%]+$")


def clean_trailing_parts(text: str) -> str:
    """Remove trailing characters except alphanumeric and markdown formatting chars.

    Why:
        Placeholder removal can leave trailing separators like commas, colons,
        or dashes. Regex preserves markdown formatting (brackets, asterisks)
        while removing unwanted trailing characters.

    Example:
        ```py
        result = clean_trailing_parts("Position at Company, \\nLink: ")
        # Returns: "Position at Company\\nLink"
        # Removes ", " and ": "
        ```

    Args:
        text: Text with potential trailing characters.

    Returns:
        Text with only allowed trailing characters (A-Z, a-z, 0-9, .!?[]())*_%).
    """
    new_lines = []
    for line in text.splitlines():
        new_line = line.rstrip()
        if new_line == "":
            continue
        new_lines.append(unwanted_trailing_parts_pattern.sub("", new_line).rstrip())
    return "\n".join(new_lines)

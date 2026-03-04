"""BibTeX parser for academic CV publications.

This module parses BibTeX files and converts them to RenderCV publication format.
It supports:
- Group member tagging (marking co-authors with asterisks)
- Media coverage linking
- Automatic formatting of author lists
- DOI and URL extraction
"""

import re
from typing import Dict, List, Optional
import bibtexparser
from pathlib import Path


def parse_bibtex_file(bib_file: str) -> List[Dict]:
    """Parse a BibTeX file and return list of publication dictionaries.
    
    Args:
        bib_file: Path to the .bib file
        
    Returns:
        List of dictionaries containing publication data
    """
    with open(bib_file, 'r', encoding='utf-8') as f:
        bib_database = bibtexparser.load(f)
    
    publications = []
    for entry in bib_database.entries:
        pub = {
            'citation_key': entry.get('ID', ''),
            'title': clean_bibtex_string(entry.get('title', '')),
            'authors': entry.get('author', '').split(' and '),
            'year': entry.get('year', ''),
            'journal': clean_bibtex_string(entry.get('journal', '')),
            'volume': entry.get('volume', ''),
            'pages': entry.get('pages', ''),
            'doi': entry.get('doi', ''),
            'url': entry.get('url', ''),
            'note': entry.get('note') or entry.get('notes', ''),  # handle both 'note' and 'notes' fields
            'entry_type': entry.get('ENTRYTYPE', 'article')
        }
        publications.append(pub)
    
    # Sort by year (descending)
    publications.sort(key=lambda x: int(x['year']) if x['year'].isdigit() else 0, reverse=True)
    
    return publications


def clean_bibtex_string(s: str) -> str:
    """Remove BibTeX formatting from strings (curly braces, LaTeX commands).
    
    Args:
        s: BibTeX string to clean
        
    Returns:
        Cleaned string
    """
    # Remove outer curly braces
    s = re.sub(r'^\{(.*)\}$', r'\1', s)
    # Handle accented characters with curly-brace notation {\"X} before other cleanup
    umlaut_map = {'a': 'ä', 'e': 'ë', 'i': 'ï', 'o': 'ö', 'u': 'ü',
                  'A': 'Ä', 'E': 'Ë', 'I': 'Ï', 'O': 'Ö', 'U': 'Ü'}
    s = re.sub(r'\{\\\"(?:\\)?([aeiouAEIOUi])\}', lambda m: umlaut_map.get(m.group(1), m.group(0)), s)
    acute_map = {'a': 'á', 'e': 'é', 'i': 'í', 'o': 'ó', 'u': 'ú', 'y': 'ý',
                 'A': 'Á', 'E': 'É', 'I': 'Í', 'O': 'Ó', 'U': 'Ú', 'Y': 'Ý'}
    s = re.sub(r"\{\\'([aeiouyAEIOUY])\}", lambda m: acute_map.get(m.group(1), m.group(0)), s)
    # Remove LaTeX commands like \textit, \textbf, etc.
    s = re.sub(r'\\text[a-z]+\{([^}]*)\}', r'\1', s)
    # Remove other common LaTeX commands
    s = re.sub(r'\\[a-z]+\{([^}]*)\}', r'\1', s)
    # Handle special characters
    # bibtexparser returns \\' sequences, but Python literals use \'    
    s = s.replace("\\'e", 'é').replace("\\'\'e", 'é').replace("\\'a", 'á').replace("\\'E", 'É')
    s = s.replace('\\"o', 'ö').replace('\\"u', 'ü').replace('\\"O', 'Ö').replace('\\"U', 'Ü')
    s = s.replace('\\"i', 'ï').replace('\\"e', 'ë').replace('\\"I', 'Ï').replace('\\"E', 'Ë')
    s = s.replace('\\~n', 'ñ').replace('\\~N', 'Ñ')
    s = s.replace('\\"a', 'ä').replace('\\"A', 'Ä')
    s = s.replace("\\'`e", 'è').replace("\\'`a", 'à')
    s = s.replace('\\^e', 'ê').replace('\\^a', 'â')
    s = s.replace('\\c{c}', 'ç').replace('\\c{C}', 'Ç')
    # Remove remaining curly braces left over from LaTeX grouping
    s = s.replace('{', '').replace('}', '')
    # Remove any remaining single backslashes before letters (but keep escaped quotes)
    s = re.sub(r'\\([a-zA-Z])', r'\1', s)
    return s.strip()


def format_authors_as_list(authors: List[str], group_members: Optional[List[str]] = None) -> List[str]:
    """Format author list with Markdown bold/italic highlighting, returning a list.

    Formatting rules:
        - Marine Denolle (PI) → **First Last** (bold)
        - Group members / mentees → *First Last* (italic)
        - All other co-authors → First Last (plain)

    Args:
        authors: List of author strings from BibTeX (in "Last, First" format)
        group_members: List of mentee full names for italic tagging

    Returns:
        List of formatted author names with Markdown bold/italic applied
    """
    if not authors:
        return []

    formatted = []
    for author in authors:
        # Clean up author name
        author = clean_bibtex_string(author.strip())

        # Skip empty authors
        if not author:
            continue

        # Parse "Last, First" format to "First Last"
        if ', ' in author:
            parts = author.split(', ', 1)
            if len(parts) == 2:
                author = f"{parts[1]} {parts[0]}"

        author_lower = author.lower()

        # PI: always bold
        if 'denolle' in author_lower:
            formatted.append(f'**{author}**')
            continue

        # Mentees: italic — use word-boundary matching to avoid short names like
        # "Ni" or "Ma" matching inside words like "veronica" or "ilma".
        is_group_member = False
        if group_members:
            for member in group_members:
                last = re.escape(member.split()[-1].lower())
                if re.search(r'\b' + last + r'\b', author_lower):
                    is_group_member = True
                    break

        if is_group_member:
            formatted.append(f'*{author}*')
        else:
            formatted.append(author)

    return formatted


def format_authors(authors: List[str], group_members: Optional[List[str]] = None) -> str:
    """Format author list with group member tagging as a string.
    
    Args:
        authors: List of author strings from BibTeX
        group_members: List of group member last names to mark with asterisk
        
    Returns:
        Formatted author string with group members marked
    """
    formatted = format_authors_as_list(authors, group_members)
    
    # Join with commas
    if len(formatted) <= 2:
        return ' and '.join(formatted)
    else:
        return ', '.join(formatted[:-1]) + f', and {formatted[-1]}'


def extract_urls_from_note(note: str) -> List[str]:
    """Extract URLs from BibTeX note field.
    
    Handles:
    - LaTeX \\url{...} commands
    - Standalone URLs (http/https)
    - Multiple URLs separated by whitespace/commas
    
    Args:
        note: BibTeX note field content
        
    Returns:
        List of extracted URLs
    """
    if not note:
        return []

    # Two capturing groups: (1) inside \url{...}, (2) bare https?://... URL.
    # re.findall with groups returns (group1, group2) tuples for each match.
    pattern = r'\\url\{([^}]+)\}|(https?://[^\s,;\}\]]+)'

    matches = re.findall(pattern, note)

    urls = []
    for match in matches:
        if isinstance(match, tuple):
            # match = (\url{} captured content, bare URL captured content)
            url = match[0] if match[0] else match[1]
        else:
            url = match
        if url.strip():
            urls.append(url.strip())

    return urls


def bibtex_to_rendercv(
    bib_file: str,
    group_members: Optional[List[str]] = None,
    media_coverage: Optional[Dict[str, List[str]]] = None
) -> List[Dict]:
    """Convert BibTeX file to RenderCV publication format.
    
    Args:
        bib_file: Path to BibTeX file
        group_members: List of group member names to tag with asterisk
        media_coverage: Dictionary mapping citation keys to lists of media URLs
        
    Returns:
        List of publication dictionaries in RenderCV format
    """
    publications = parse_bibtex_file(bib_file)
    
    rendercv_pubs = []
    for pub in publications:
        # Format publication entry
        entry = {
            'title': pub['title'],
            'authors': format_authors_as_list(pub['authors'], group_members),
            'date': f"{pub['year']}-01" if pub['year'] else '',
            'journal': pub['journal'],
            'citation_key': pub['citation_key']  # Keep citation key for citation matching
        }
        
        # Add optional fields
        if pub['doi']:
            entry['doi'] = pub['doi']
            if not pub['url']:
                entry['url'] = f"https://doi.org/{pub['doi']}"
        elif pub['url']:
            entry['url'] = pub['url']
        
        if pub['volume']:
            entry['journal'] += f", {pub['volume']}"
        
        # Add media coverage from manual dict or auto-extract from note field
        if media_coverage and pub['citation_key'] in media_coverage:
            # Manual media_coverage dict takes precedence
            entry['media_coverage'] = media_coverage[pub['citation_key']]
        elif pub.get('note'):
            # Auto-extract URLs from note field
            urls = extract_urls_from_note(pub['note'])
            if urls:
                entry['media_coverage'] = urls
        
        rendercv_pubs.append(entry)
    
    return rendercv_pubs


def add_citations_to_publications(
    publications: list[dict],
    citation_cache_file: str = 'marine-cv-docs/citation_cache.json'
) -> list[dict]:
    """Add citation counts from cache to publication entries.
    
    Args:
        publications: List of publication dicts from parse_bibtex_file()
        citation_cache_file: Path to JSON cache file
        
    Returns:
        Publications list with 'citations' field added (0 if no data)
    """
    import json
    from pathlib import Path
    
    cache_path = Path(citation_cache_file)
    if not cache_path.exists():
        # Don't add citation field if no cache exists
        return publications
    
    try:
        with open(cache_path) as f:
            cache = json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: Could not read citation cache: {e}", file=sys.stderr)
        return publications
    
    # Add citations to publications
    for pub in publications:
        citation_key = pub.get('citation_key')
        if citation_key:
            if citation_key in cache.get('citations', {}):
                count = cache['citations'][citation_key]
                pub['citations'] = count  # Add count even if 0
            else:
                # Mark as -1 to indicate no data available
                pub['citations'] = -1
    
    return publications


def extract_group_member_publications(
    bib_file: str,
    group_members: List[str],
    output_format: str = 'yaml'
) -> str:
    """Extract publications co-authored with group members.
    
    Args:
        bib_file: Path to BibTeX file
        group_members: List of group member names
        output_format: Output format ('yaml' or 'json')
        
    Returns:
        Formatted string of publications with group members
    """
    publications = parse_bibtex_file(bib_file)
    
    group_pubs = []
    for pub in publications:
        # Check if any group member is in author list
        has_group_member = False
        for member in group_members:
            member_last = member.split()[-1].lower()
            for author in pub['authors']:
                if member_last in author.lower():
                    has_group_member = True
                    break
            if has_group_member:
                break
        
        if has_group_member:
            group_pubs.append(pub)
    
    if output_format == 'yaml':
        output = []
        for pub in group_pubs:
            authors_str = format_authors(pub['authors'], group_members)
            output.append(f"  - title: '{pub['title']}'")
            output.append(f"    authors: [{authors_str}]")
            output.append(f"    journal: '{pub['journal']}'")
            output.append(f"    date: {pub['year']}-01")
            if pub['doi']:
                output.append(f"    doi: {pub['doi']}")
                output.append(f"    url: https://doi.org/{pub['doi']}")
            output.append("")
        return '\n'.join(output)
    else:
        import json
        return json.dumps(group_pubs, indent=2)


# Default group members (mentees) for Marine Denolle's CV.
# Names are sourced from phd_advisees.yaml, postdocs.yaml,
# undergraduate_students.yaml, and other_graduate_student_supervision.yaml.
# Both accented and ASCII variants are included where bib entries vary.
DEFAULT_GROUP_MEMBERS = [
    # PhD Advisees — UW (current)
    'Michael Hemmett',
    'Manuela Koepfli',
    'Manuela Köpfli',    # accent variant used in bib entries
    'Akash Kharita',
    'Yiyu Ni',
    # PhD Advisees — Harvard (graduated)
    'Congcong Yuan',
    'Stephanie Olinger',
    'Tim Clements',
    'Jiuxun Yin',
    # Postdoctoral researchers
    'Qibin Shi',
    'Kuan-Fu Feng',
    'Ethan Williams',
    'Laura Ermert',
    'Xiaotao Yang',
    'Kurama Okubo',
    'Zhitu Ma',
    'Chengxin Jiang',
    'Chris Van Houtte',
    'Loïc Viens',
    # Undergraduate students (those with publications)
    'Jared Bryan',
    'Julian Schmitt',
    'Albert Aguilar',
    'Francesca Skene',
    # Other graduate student supervision
    'Natasha Toghramadjian',
    'Zhuo Yang',
    'Thibault Pérol',
    'Thibault Perol',    # ASCII variant
    'Philippe Danré',
    'Pierre Danré',      # alternative first-name variant
    'Maleen Kidiwela',
    'Zoe Krauss',
    'Parker Sprinkle',
    'Manuel Florez',
    'William Flanagan',
]


if __name__ == '__main__':
    # Example usage
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python bibtex_parser.py <bibtex_file>")
        sys.exit(1)
    
    bib_file = sys.argv[1]
    
    # Parse and display publications
    publications = bibtex_to_rendercv(
        bib_file,
        group_members=DEFAULT_GROUP_MEMBERS
    )
    
    print(f"Found {len(publications)} publications")
    print("\nFirst 3 publications:")
    for i, pub in enumerate(publications[:3], 1):
        print(f"\n{i}. {pub['title']}")
        print(f"   Authors: {pub['authors']}")
        print(f"   {pub['journal']} ({pub['date']})")

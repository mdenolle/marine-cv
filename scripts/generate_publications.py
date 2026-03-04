#!/usr/bin/env python3
"""Generate publications section entries from BibTeX file.

This script parses denolle-pub.bib and generates a YAML-formatted publications
section with group member tagging and media coverage links.

Usage:
    python scripts/generate_publications.py > marine-cv-docs/publications_section.yaml
"""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from rendercv.bibtex_parser import bibtex_to_rendercv, DEFAULT_GROUP_MEMBERS


# Media coverage mapping (citation key -> list of URLs)
MEDIA_COVERAGE = {
    'Denolle2014': [
        'https://news.stanford.edu/2014/01/23/earthquake-prediction-012314/',
        'https://www.science.org/doi/10.1126/science.1245678'
    ],
    'Perol2018': [
        'https://news.harvard.edu/gazette/story/2018/02/harvard-scientists-use-deep-learning-to-detect-earthquakes/',
        'https://www.sciencemag.org/news/2018/02/artificial-intelligence-earthquake-detection'
    ],
    'Denolle2020': [
        'https://www.science.org/doi/10.1126/science.abd8358',
        'https://www.sciencedaily.com/releases/2020/09/200917141734.htm'
    ],
    'Clements2018': [
        'https://eos.org/research-spotlights/tracking-groundwater-with-seismic-noise'
    ],
    'Olinger2023': [
        'https://www.washington.edu/news/2023/12/04/ice-shelf-rift-propagation/'
    ]
}


def _yaml_quote(s: str) -> str:
    """Wrap a string in double-quotes for YAML, escaping backslashes and double-quotes."""
    escaped = s.replace('\\', '\\\\').replace('"', '\\"')
    return f'"{escaped}"'


def _needs_quoting(s: str) -> bool:
    """Return True if the string requires YAML double-quoting."""
    return any(c in s for c in ["'", '"', ":", "#", "[", "]", "{", "}", "|", ">", "!", "&", "*", "@", "`"])


def main():
    """Generate publications YAML section."""
    import traceback

    try:
        _generate()
    except Exception as exc:
        print(f"Error in generate_publications.py: {exc}", file=sys.stderr)
        traceback.print_exc()
        sys.exit(1)


def _generate():
    """Inner logic — separated so try/except in main() catches all errors."""
    # Path to BibTeX file
    bib_file = Path(__file__).parent.parent / 'marine-cv-docs' / 'denolle-pub.bib'

    if not bib_file.exists():
        raise FileNotFoundError(f"BibTeX file not found: {bib_file}")

    # Convert BibTeX to RenderCV format
    publications = bibtex_to_rendercv(
        str(bib_file),
        group_members=DEFAULT_GROUP_MEMBERS,
        media_coverage=MEDIA_COVERAGE
    )

    # Add citation counts from cache
    from rendercv.bibtex_parser import add_citations_to_publications
    publications = add_citations_to_publications(publications)

    # Generate YAML array entries for direct section include
    print("# AUTO-GENERATED from denolle-pub.bib using scripts/generate_publications.py")
    print(f"# {len(publications)} publications")
    print("# Author formatting: **Bold** = Marine A. Denolle (PI); *Italic* = mentored students/postdocs")
    print("# See publications_legend section in Marine_Denolle_CV.yaml for the rendered legend.")
    print("# Citations marked with -1 indicate 'no data available'")
    print()

    for pub in publications:
        title = pub['title']
        journal = pub['journal']

        # Double-quote strings that contain special YAML characters.
        # _yaml_quote also escapes any embedded double-quotes and backslashes.
        if _needs_quoting(title):
            title = _yaml_quote(title)
        if _needs_quoting(journal):
            journal = _yaml_quote(journal)

        print(f'- title: {title}')
        print("  authors:")
        for author in pub['authors']:
            # Authors starting with * (Markdown bold/italic) must be double-quoted.
            if author.startswith('*') or _needs_quoting(author):
                print(f'    - {_yaml_quote(author)}')
            else:
                print(f"    - {author}")

        if 'summary' in pub and pub['summary']:
            print(f"  summary: {pub['summary']}")
        else:
            print("  summary:")

        if 'doi' in pub and isinstance(pub['doi'], str) and pub['doi'].startswith('10.'):
            print(f"  doi: {pub['doi']}")

        # Only print url if it is a real URL (not a placeholder like https://doi.org/XX)
        url = pub.get('url', '')
        if url and (not url.startswith('https://doi.org/') or url.startswith('https://doi.org/10.')):
            print(f"  url: {url}")

        print(f'  journal: {journal}')
        print(f"  date: {pub['date']}")

        # Citations — always show if available (even if 0 or -1 for 'no data')
        if 'citations' in pub:
            print(f"  citations: {pub['citations']}")

        if 'media_coverage' in pub:
            print("  media_coverage:")
            for murl in pub['media_coverage']:
                print(f"    - '{murl}'")

        print()


if __name__ == '__main__':
    main()

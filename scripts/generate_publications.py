#!/usr/bin/env python3
"""Generate publications section for Marine_Denolle_CV.yaml from BibTeX file.

This script parses denolle-pub.bib and generates a YAML-formatted publications
section with group member tagging and media coverage links.

Usage:
    python scripts/generate_publications.py > publications.yaml
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


def main():
    """Generate publications YAML section."""
    # Path to BibTeX file
    bib_file = Path(__file__).parent.parent / 'marine-cv-docs' / 'denolle-pub.bib'
    
    if not bib_file.exists():
        print(f"Error: BibTeX file not found: {bib_file}", file=sys.stderr)
        sys.exit(1)
    
    # Convert BibTeX to RenderCV format
    publications = bibtex_to_rendercv(
        str(bib_file),
        group_members=DEFAULT_GROUP_MEMBERS,
        media_coverage=MEDIA_COVERAGE
    )
    
    # Add citation counts from cache
    from rendercv.bibtex_parser import add_citations_to_publications
    publications = add_citations_to_publications(publications)
    
    # Generate YAML
    print("    publications:")
    print("      # AUTO-GENERATED from denolle-pub.bib using scripts/generate_publications.py")
    print(f"      # {len(publications)} publications with group member tagging (*)")
    print("      # Citations marked with -1 indicate 'no data available'")
    print()
    
    for pub in publications:
        # Manually handle YAML string escaping
        # For single-line strings in YAML, just need to handle special chars
        title = pub['title']
        journal = pub['journal']
        
        # Quote strings if they contain: apostrophes, colons, or special YAML chars
        needs_quotes_title = any(c in title for c in ["'", ":", "#", "[", "]", "{", "}", "|", ">", "!", "&", "*", "@", "`"])
        needs_quotes_journal = any(c in journal for c in ["'", ":", "#", "[", "]", "{", "}", "|", ">", "!", "&", "*", "@", "`"])
        
        if needs_quotes_title:
            title = f'"{title}"'
        if needs_quotes_journal:
            journal = f'"{journal}"'
        
        print(f'      - title: {title}')
        print("        authors:")
        for author in pub['authors']:
            print(f"          - {author}")
        
        if 'summary' in pub and pub['summary']:
            print(f"        summary: {pub['summary']}")
        else:
            print("        summary:")
        
        if 'doi' in pub:
            print(f"        doi: {pub['doi']}")
        
        if 'url' in pub:
            print(f"        url: {pub['url']}")
        
        print(f'        journal: {journal}')
        print(f"        date: {pub['date']}")
        
        # Citations - always show if available (even if 0 or -1 for 'no data')
        if 'citations' in pub:
            print(f"        citations: {pub['citations']}")
        
        if 'media_coverage' in pub:
            print("        media_coverage:")
            for url in pub['media_coverage']:
                print(f"          - '{url}'")
        
        print()


if __name__ == '__main__':
    main()

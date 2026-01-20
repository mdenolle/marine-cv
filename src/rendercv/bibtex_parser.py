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
            'note': entry.get('note', ''),
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
    # Remove LaTeX commands like \textit, \textbf, etc.
    s = re.sub(r'\\text[a-z]+\{([^}]*)\}', r'\1', s)
    # Remove other common LaTeX commands
    s = re.sub(r'\\[a-z]+\{([^}]*)\}', r'\1', s)
    # Handle special characters
    # bibtexparser returns \\' sequences, but Python literals use \'
    s = s.replace("\\'e", 'é').replace('\\\'e', 'é').replace("\\'a", 'á').replace("\\'E", 'É')
    s = s.replace('\\"o', 'ö').replace('\\"u', 'ü').replace('\\"O', 'Ö').replace('\\"U', 'Ü')
    s = s.replace('\\~n', 'ñ').replace('\\~N', 'Ñ')
    s = s.replace('\\"a', 'ä').replace('\\"A', 'Ä')
    s = s.replace("\\`e", 'è').replace('\\`a', 'à')
    s = s.replace('\\^e', 'ê').replace('\\^a', 'â')
    s = s.replace('\\c{c}', 'ç').replace('\\c{C}', 'Ç')
    # Remove any remaining single backslashes before letters (but keep escaped quotes)
    s = re.sub(r'\\([a-zA-Z])', r'\1', s)
    return s.strip()


def format_authors(authors: List[str], group_members: Optional[List[str]] = None) -> str:
    """Format author list with group member tagging.
    
    Args:
        authors: List of author strings from BibTeX
        group_members: List of group member last names to mark with asterisk
        
    Returns:
        Formatted author string with group members marked
    """
    if not authors:
        return ''
    
    formatted = []
    for author in authors:
        # Clean up author name
        author = clean_bibtex_string(author.strip())
        
        # Check if this is a group member
        is_group_member = False
        if group_members:
            for member in group_members:
                # Match last name (simple heuristic)
                if member.split()[-1].lower() in author.lower():
                    is_group_member = True
                    break
        
        # Add asterisk for group members
        if is_group_member:
            formatted.append(f'{author}*')
        else:
            formatted.append(author)
    
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
    
    # Match \url{URL} or standalone http(s)://URL
    # Pattern captures URLs inside \url{} and standalone URLs
    pattern = r'\\url\{([^}]+)\}|https?://[^\s,;\}\]]+'
    
    matches = re.findall(pattern, note)
    
    # Flatten tuples from alternation groups
    # re.findall with groups returns tuples when using |,
    # so we need to extract the non-empty match
    urls = []
    for match in matches:
        if isinstance(match, tuple):
            # Get the non-empty group from the alternation
            url = (
                match[0] if match[0]
                else match[1] if len(match) > 1
                else ''
            )
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
            'authors': format_authors(pub['authors'], group_members).split(', '),
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


# Default group members for Marine Denolle's CV
DEFAULT_GROUP_MEMBERS = [
    'Yiyu Ni',
    'Manuela Kopefli', 
    'Akash Kharita',
    'Michael Hemmett',
    'Congcong Yuan',
    'Stephanie Olinger',
    'Tim Clements',
    'Jiuxun Yin',
    'Qibin Shi',
    'Kuan-Fu Feng',
    'Ethan Williams',
    'Laura Ermert',
    'Xiaotao Yang',
    'Kurama Okubo',
    'Zhitu Ma',
    'Chengxin Jiang',
    'Loïc Viens',
    'Chengxin Jiang',
    'Pierre Danré',
    'Jared Bryan',
    'Julian Schmitt',
    'Francesca Skene',
    'Albert Aguilar',
    'Chris Van Houtte',
    'Thibaud Perol'
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

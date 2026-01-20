#!/usr/bin/env python3
"""Fetch Google Scholar citation counts for publications.

This script queries Google Scholar to get citation counts for all publications
in the BibTeX file and saves them to a cache file.

Usage:
    python scripts/fetch_citations.py [--force-refresh]

The citation cache is saved to marine-cv-docs/citation_cache.json and is 
automatically used by generate_publications.py when rendering the CV.
"""

import argparse
import json
import sys
import time
from datetime import datetime
from pathlib import Path

# Try importing scholarly
try:
    from scholarly import scholarly
except ImportError:
    print("Error: scholarly not installed. Run: pip install scholarly", file=sys.stderr)
    sys.exit(1)

# Try importing fuzzywuzzy for title matching
try:
    from fuzzywuzzy import fuzz
except ImportError:
    print("Warning: fuzzywuzzy not installed. Using exact title matching only.")
    print("For better matching, run: pip install fuzzywuzzy python-Levenshtein", file=sys.stderr)
    fuzz = None

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))
from rendercv.bibtex_parser import parse_bibtex_file

# ==============================================================================
# CONFIGURATION
# ==============================================================================

# Default CV YAML file (to read Google Scholar ID from social_networks)
CV_YAML_FILE = Path(__file__).parent.parent / 'marine-cv-docs' / 'Marine_Denolle_CV.yaml'

# Cache settings
CACHE_FILE = Path(__file__).parent.parent / 'marine-cv-docs' / 'citation_cache.json'
BIB_FILE = Path(__file__).parent.parent / 'marine-cv-docs' / 'denolle-pub.bib'
CACHE_EXPIRY_DAYS = 30  # Refresh if cache is older than this

# Fuzzy matching threshold (0-100, higher = stricter)
TITLE_MATCH_THRESHOLD = 85

# Rate limiting (seconds between requests)
REQUEST_DELAY = 2

# ==============================================================================


def get_google_scholar_id_from_yaml(yaml_file: Path) -> str | None:
    """Extract Google Scholar ID from CV YAML file's social_networks section.
    
    Args:
        yaml_file: Path to CV YAML file
        
    Returns:
        Google Scholar author ID or None if not found
    """
    try:
        from ruamel.yaml import YAML
        yaml = YAML()
        
        with open(yaml_file) as f:
            data = yaml.load(f)
        
        # Look for GoogleScholar in social_networks
        social_networks = data.get('cv', {}).get('social_networks', [])
        for network in social_networks:
            network_name = network.get('network', '').lower().replace(' ', '')
            if network_name in ['googlescholar']:
                return network.get('username')
        
        return None
    except Exception as e:
        print(f"Warning: Could not read Google Scholar ID from YAML: {e}", file=sys.stderr)
        return None


def load_cache():
    """Load citation cache from JSON file."""
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE) as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Warning: Corrupted cache file, starting fresh", file=sys.stderr)
    return {"last_updated": None, "author_id": None, "citations": {}}


def save_cache(cache):
    """Save citation cache to JSON file."""
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)
    print(f"\n✓ Saved citation cache to {CACHE_FILE}")


def is_cache_fresh(cache, force_refresh=False):
    """Check if cache is fresh enough to use."""
    if force_refresh:
        return False
    
    if not cache['last_updated']:
        return False
    
    try:
        last_update = datetime.fromisoformat(cache['last_updated'])
        age_days = (datetime.now() - last_update).days
        return age_days < CACHE_EXPIRY_DAYS
    except (ValueError, KeyError):
        return False


def fetch_scholar_citations(author_id):
    """Fetch all publications and citation counts from Google Scholar.
    
    Returns:
        tuple: (publications_dict, metrics_dict)
            publications_dict: Maps publication titles to citation data
            metrics_dict: Author-level metrics (h-index, i10-index, etc.)
    """
    print(f"Fetching publications for Google Scholar ID: {author_id}")
    
    try:
        # Search for author by ID
        author = scholarly.search_author_id(author_id)
        print(f"Found author: {author.get('name', 'Unknown')}")
        
        # Fill author details with publications and metrics
        print("Fetching publication list and metrics...")
        author_filled = scholarly.fill(author, sections=['basics', 'indices', 'publications'])
        
        # Extract author-level metrics
        metrics = {
            'total_citations': author_filled.get('citedby', 0),
            'total_citations_5y': author_filled.get('citedby5y', 0),
            'h_index': author_filled.get('hindex', 0),
            'h_index_5y': author_filled.get('hindex5y', 0),
            'i10_index': author_filled.get('i10index', 0),
            'i10_index_5y': author_filled.get('i10index5y', 0),
            'cites_per_year': author_filled.get('cites_per_year', {}),
        }
        
        total_pubs = len(author_filled.get('publications', []))
        print(f"Found {total_pubs} publications on Google Scholar")
        print(f"Total citations: {metrics['total_citations']:,}")
        print(f"h-index: {metrics['h_index']}, i10-index: {metrics['i10_index']}\n")
        
    except Exception as e:
        print(f"Error fetching author data: {e}", file=sys.stderr)
        return {}, {}
    
    # Process each publication
    citations = {}
    for i, pub in enumerate(author_filled['publications'], 1):
        try:
            # Rate limiting
            if i > 1:
                time.sleep(REQUEST_DELAY)
            
            # Fill publication details
            pub_filled = scholarly.fill(pub)
            
            title = pub_filled['bib'].get('title', 'Unknown')
            count = pub_filled.get('num_citations', 0)
            year = pub_filled['bib'].get('pub_year', '')
            
            print(f"  [{i}/{total_pubs}] {title[:60]}... → {count} citations")
            
            citations[title] = {
                'count': count,
                'year': year,
                'fetched_at': datetime.now().isoformat()
            }
            
        except Exception as e:
            print(f"  [{i}/{total_pubs}] Error processing publication: {e}", file=sys.stderr)
            continue
    
    return citations, metrics


def match_titles(bib_title, scholar_title):
    """Match BibTeX title to Scholar title with fuzzy matching.
    
    Returns:
        int: Match score (0-100), or -1 if fuzzy matching not available
    """
    # Normalize titles
    bib_clean = bib_title.lower().strip()
    scholar_clean = scholar_title.lower().strip()
    
    # Exact match
    if bib_clean == scholar_clean:
        return 100
    
    # Fuzzy match if available
    if fuzz:
        return fuzz.ratio(bib_clean, scholar_clean)
    
    # Simple contains check as fallback
    if bib_clean in scholar_clean or scholar_clean in bib_clean:
        return 80
    
    return 0


def match_bibtex_to_scholar(bib_pubs, scholar_citations):
    """Match BibTeX entries to Google Scholar data.
    
    Args:
        bib_pubs: List of publication dicts from parse_bibtex_file()
        scholar_citations: Dict of Scholar data from fetch_scholar_citations()
    
    Returns:
        dict: Maps BibTeX citation keys to citation counts
              {"Denolle2014": 450, "Perol2018": 320, ...}
    """
    matched = {}
    unmatched_bib = []
    
    print(f"\nMatching {len(bib_pubs)} BibTeX entries to {len(scholar_citations)} Scholar entries...")
    print(f"Using match threshold: {TITLE_MATCH_THRESHOLD}%\n")
    
    for pub in bib_pubs:
        bib_title = pub.get('title', '')
        citation_key = pub.get('citation_key', '')
        
        if not bib_title or not citation_key:
            continue
        
        # Find best match
        best_match = None
        best_score = 0
        
        for scholar_title, data in scholar_citations.items():
            score = match_titles(bib_title, scholar_title)
            if score > best_score:
                best_score = score
                best_match = (scholar_title, data)
        
        # Accept match if above threshold
        if best_score >= TITLE_MATCH_THRESHOLD:
            matched[citation_key] = best_match[1]['count']
            print(f"  ✓ {citation_key}: {best_match[1]['count']} citations (match: {best_score}%)")
        else:
            unmatched_bib.append(f"{citation_key}: {bib_title[:50]}...")
            print(f"  ✗ {citation_key}: No match (best: {best_score}%)")
    
    # Summary
    print(f"\n--- Matching Summary ---")
    print(f"Matched: {len(matched)}/{len(bib_pubs)} publications")
    print(f"Unmatched: {len(unmatched_bib)}")
    
    if unmatched_bib:
        print(f"\nUnmatched BibTeX entries:")
        for entry in unmatched_bib[:10]:  # Show first 10
            print(f"  - {entry}")
        if len(unmatched_bib) > 10:
            print(f"  ... and {len(unmatched_bib) - 10} more")
    
    total_citations = sum(matched.values())
    print(f"\nTotal citations: {total_citations}")
    
    return matched


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Fetch Google Scholar citation counts')
    parser.add_argument('--force-refresh', action='store_true',
                        help='Force refresh even if cache is recent')
    args = parser.parse_args()
    
    print("=" * 70)
    print("Google Scholar Citation Fetcher")
    print("=" * 70)
    
    # Get Google Scholar ID from YAML
    scholar_id = get_google_scholar_id_from_yaml(CV_YAML_FILE)
    if not scholar_id:
        print(f"Error: Google Scholar ID not found in {CV_YAML_FILE}", file=sys.stderr)
        print("Add it to social_networks with network: GoogleScholar", file=sys.stderr)
        sys.exit(1)
    
    print(f"\nGoogle Scholar ID: {scholar_id}")
    
    # Check BibTeX file exists
    if not BIB_FILE.exists():
        print(f"Error: BibTeX file not found: {BIB_FILE}", file=sys.stderr)
        sys.exit(1)
    
    # Load cache
    cache = load_cache()
    
    # Check if cache is fresh
    if is_cache_fresh(cache, args.force_refresh):
        last_update = cache['last_updated']
        print(f"\nCache is fresh (updated {last_update})")
        print(f"Cached citations: {len(cache.get('citations', {}))}")
        print(f"Total citations: {sum(cache.get('citations', {}).values())}")
        print(f"\nUse --force-refresh to fetch new data")
        return
    
    print(f"\nFetching fresh citation data...")
    if cache.get('last_updated'):
        print(f"(Previous update: {cache['last_updated']})")
    
    # Parse BibTeX
    print(f"\nParsing BibTeX file: {BIB_FILE}")
    try:
        bib_pubs = parse_bibtex_file(str(BIB_FILE))
        print(f"Loaded {len(bib_pubs)} publications from BibTeX\n")
    except Exception as e:
        print(f"Error parsing BibTeX: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Fetch from Google Scholar
    scholar_citations, author_metrics = fetch_scholar_citations(scholar_id)
    
    if not scholar_citations:
        print("\nError: No citations fetched from Google Scholar", file=sys.stderr)
        sys.exit(1)
    
    # Match titles
    matched = match_bibtex_to_scholar(bib_pubs, scholar_citations)
    
    # Update cache
    cache['citations'] = matched
    cache['metrics'] = author_metrics
    cache['last_updated'] = datetime.now().isoformat()
    cache['author_id'] = scholar_id
    
    # Save cache
    save_cache(cache)
    
    print(f"\n{'=' * 70}")
    print("✓ Citation fetch complete!")
    print(f"{'=' * 70}")


if __name__ == '__main__':
    main()

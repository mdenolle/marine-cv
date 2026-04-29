#!/usr/bin/env python3
"""Fetch citation counts for publications via the OpenAlex API.

Replaces the previous scholarly-based fetcher which was blocked by Google
in CI environments. OpenAlex is a free, open bibliographic API that does
not require authentication and is not blocked from GitHub Actions.

Usage:
    python scripts/fetch_citations.py [--force-refresh]

The citation cache is saved to marine-cv-docs/citation_cache.json and is
automatically used by generate_publications.py when rendering the CV.

Cache structure:
    {
        "last_updated": "<ISO datetime>",
        "author_id": "<ORCID>",
        "citations": {"CitationKey": <count>, ...},
        "metrics": {
            "total_citations": <int>,       # OpenAlex
            "h_index": <int>,               # OpenAlex
            "i10_index": <int>,             # OpenAlex
            "cites_per_year": {<year>: <int>, ...},  # OpenAlex
            "openalex_total_citations": <int>,
            "openalex_h_index": <int>,
            "gs_h_index": <int>,            # Google Scholar (last known, archival)
            "gs_total_citations": <int>     # Google Scholar (last known, archival)
        }
    }
"""

import argparse
import json
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

# Try importing requests (preferred for cleaner error handling)
try:
    import requests as _requests
    _HAS_REQUESTS = True
except ImportError:
    _HAS_REQUESTS = False

# Try importing fuzzywuzzy for title matching (optional)
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

# Default CV YAML file (to read ORCID and Google Scholar ID from social_networks)
CV_YAML_FILE = Path(__file__).parent.parent / 'marine-cv-docs' / 'Marine_Denolle_CV.yaml'

# Cache settings
CACHE_FILE = Path(__file__).parent.parent / 'marine-cv-docs' / 'citation_cache.json'
BIB_FILE = Path(__file__).parent.parent / 'marine-cv-docs' / 'denolle-pub.bib'
CACHE_EXPIRY_DAYS = 30  # Refresh if cache is older than this

# Fuzzy matching threshold (0-100, higher = stricter)
TITLE_MATCH_THRESHOLD = 85

# OpenAlex API base URL and polite email (improves rate limits)
OPENALEX_BASE = "https://api.openalex.org"
OPENALEX_EMAIL = "mdenolle@uw.edu"  # Used in mailto= param for the polite pool

# Rate limiting (seconds between requests)
REQUEST_DELAY = 0.5  # OpenAlex is generous; 0.5s is plenty

# ==============================================================================


def get_social_network_ids(yaml_file: Path) -> dict:
    """Extract ORCID and Google Scholar ID from CV YAML social_networks.

    Returns:
        dict with keys 'orcid' and 'google_scholar' (either may be None)
    """
    result = {'orcid': None, 'google_scholar': None}
    try:
        from ruamel.yaml import YAML
        yaml = YAML()
        with open(yaml_file) as f:
            data = yaml.load(f)
        social_networks = data.get('cv', {}).get('social_networks', [])
        for network in social_networks:
            name = network.get('network', '').lower().replace(' ', '')
            if name == 'orcid':
                result['orcid'] = network.get('username')
            elif name in ('googlescholar', 'google_scholar'):
                result['google_scholar'] = network.get('username')
    except Exception as e:
        print(f"Warning: Could not read social networks from YAML: {e}", file=sys.stderr)
    return result


def _api_get(url: str) -> dict:
    """Simple HTTP GET that works with or without the requests library."""
    if _HAS_REQUESTS:
        resp = _requests.get(url, timeout=30)
        resp.raise_for_status()
        return resp.json()
    req = urllib.request.Request(url, headers={"User-Agent": "marine-cv/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


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


def fetch_author_metrics_openalex(orcid: str) -> dict:
    """Fetch author-level metrics from OpenAlex.

    Args:
        orcid: ORCID identifier (e.g. "0000-0002-1610-2250")

    Returns:
        dict with keys: total_citations, h_index, i10_index, cites_per_year
        Returns empty dict on failure.
    """
    url = f"{OPENALEX_BASE}/authors/https://orcid.org/{orcid}?mailto={OPENALEX_EMAIL}"
    print(f"Fetching author metrics from OpenAlex for ORCID {orcid}...")
    try:
        data = _api_get(url)
        stats = data.get('summary_stats', {})
        # OpenAlex cites_per_year is a list of {year, cited_by_count}
        raw_cpy = data.get('counts_by_year', [])
        cites_per_year = {str(item['year']): item['cited_by_count'] for item in raw_cpy}
        metrics = {
            'total_citations': data.get('cited_by_count', 0),
            'h_index': stats.get('h_index', 0),
            'i10_index': stats.get('i10_index', 0),
            'cites_per_year': cites_per_year,
            'openalex_total_citations': data.get('cited_by_count', 0),
            'openalex_h_index': stats.get('h_index', 0),
        }
        print(f"  Total citations: {metrics['total_citations']:,}")
        print(f"  h-index (OpenAlex): {metrics['h_index']}")
        print(f"  i10-index (OpenAlex): {metrics['i10_index']}")
        return metrics
    except Exception as e:
        print(f"Error fetching author metrics from OpenAlex: {e}", file=sys.stderr)
        return {}


def fetch_paper_citations_openalex(orcid: str) -> dict:
    """Fetch per-paper citation counts from OpenAlex.

    Paginates through all works for the given ORCID and returns a lookup
    dict keyed by normalised DOI and normalised title.

    Args:
        orcid: ORCID identifier

    Returns:
        dict: {normalised_doi: count, normalised_title: count}
    """
    print(f"\nFetching per-paper citations from OpenAlex...")
    lookup = {}  # key → citation count
    cursor = "*"
    page = 0
    total_fetched = 0

    while cursor:
        url = (
            f"{OPENALEX_BASE}/works"
            f"?filter=author.orcid:{orcid}"
            f"&select=doi,title,cited_by_count"
            f"&per_page=200&cursor={cursor}"
            f"&mailto={OPENALEX_EMAIL}"
        )
        try:
            data = _api_get(url)
        except Exception as e:
            print(f"Error fetching works page {page + 1}: {e}", file=sys.stderr)
            break

        results = data.get('results', [])
        if not results:
            break

        for work in results:
            count = work.get('cited_by_count', 0)
            # Index by normalised DOI
            doi = work.get('doi', '') or ''
            doi = doi.replace('https://doi.org/', '').lower().strip()
            if doi:
                lookup[doi] = count
            # Also index by normalised title as fallback
            title = work.get('title', '') or ''
            title_norm = title.lower().strip()
            if title_norm:
                lookup[title_norm] = count

        total_fetched += len(results)
        page += 1

        meta = data.get('meta', {})
        next_cursor = meta.get('next_cursor')
        # Stop if no next page or we got fewer results than requested
        if not next_cursor or len(results) < 200:
            break
        cursor = next_cursor
        time.sleep(REQUEST_DELAY)

    print(f"  Fetched {total_fetched} works from OpenAlex")
    return lookup


def _norm_doi(doi: str) -> str:
    """Normalise a DOI string to bare lowercase form."""
    return doi.replace('https://doi.org/', '').replace('http://doi.org/', '').lower().strip()


def match_bibtex_to_openalex(bib_pubs: list, openalex_lookup: dict) -> dict:
    """Match BibTeX entries to OpenAlex citation counts.

    Tries DOI matching first; falls back to fuzzy title matching.

    Args:
        bib_pubs: List of publication dicts from parse_bibtex_file()
        openalex_lookup: Dict from fetch_paper_citations_openalex()

    Returns:
        dict: {"CitationKey": <count>, ...}
    """
    matched = {}
    unmatched = []

    total = len(bib_pubs)
    print(f"\nMatching {total} BibTeX entries to OpenAlex data...")
    print(f"Fuzzy threshold: {TITLE_MATCH_THRESHOLD}%\n")

    for pub in bib_pubs:
        citation_key = pub.get('citation_key', '')
        bib_doi = _norm_doi(pub.get('doi', '') or '')
        bib_title = (pub.get('title', '') or '').lower().strip()

        if not citation_key:
            continue

        count = None

        # --- Primary: DOI match ---
        if bib_doi and bib_doi not in ('xx', ''):
            count = openalex_lookup.get(bib_doi)
            if count is not None:
                print(f"  ✓ {citation_key}: {count} citations (DOI match)")

        # --- Fallback: title fuzzy match ---
        if count is None and bib_title:
            best_score = 0
            best_count = None
            for key, val in openalex_lookup.items():
                # Only compare against title keys (not DOIs - they don't contain spaces)
                if ' ' not in key:
                    continue
                if fuzz:
                    score = fuzz.ratio(bib_title, key)
                else:
                    # simple substring fallback
                    score = 100 if bib_title == key else (80 if bib_title in key or key in bib_title else 0)
                if score > best_score:
                    best_score = score
                    best_count = val
            if best_score >= TITLE_MATCH_THRESHOLD and best_count is not None:
                count = best_count
                print(f"  ✓ {citation_key}: {count} citations (title match {best_score}%)")

        if count is not None:
            matched[citation_key] = count
        else:
            unmatched.append(citation_key)
            print(f"  ✗ {citation_key}: No match")

    print(f"\n--- Matching Summary ---")
    print(f"Matched: {len(matched)}/{total}")
    print(f"Unmatched: {len(unmatched)}")
    if unmatched[:10]:
        print("Unmatched keys:", unmatched[:10])
        if len(unmatched) > 10:
            print(f"  ... and {len(unmatched) - 10} more")
    print(f"Total citations (matched): {sum(matched.values())}")
    return matched


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Fetch citation counts via OpenAlex')
    parser.add_argument('--force-refresh', action='store_true',
                        help='Force refresh even if cache is recent')
    args = parser.parse_args()

    print("=" * 70)
    print("Citation Fetcher (OpenAlex)")
    print("=" * 70)

    # Get ORCID (and optionally Google Scholar ID) from YAML
    ids = get_social_network_ids(CV_YAML_FILE)
    orcid = ids.get('orcid')
    gs_id = ids.get('google_scholar')

    if not orcid:
        print(f"Error: ORCID not found in {CV_YAML_FILE}", file=sys.stderr)
        print("Add it to social_networks with network: ORCID", file=sys.stderr)
        sys.exit(1)

    print(f"\nORCID: {orcid}")
    if gs_id:
        print(f"Google Scholar ID: {gs_id} (archival reference only)")

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

    print(f"\nFetching fresh citation data from OpenAlex...")
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

    # Fetch author-level metrics
    author_metrics = fetch_author_metrics_openalex(orcid)
    if not author_metrics:
        print("\nWarning: Could not fetch author metrics from OpenAlex.", file=sys.stderr)
        print("Falling back to existing cached metrics.", file=sys.stderr)
        author_metrics = cache.get('metrics', {})

    # Preserve last-known Google Scholar metrics in cache for reference
    existing_metrics = cache.get('metrics', {})
    if 'h_index' in existing_metrics and 'gs_h_index' not in existing_metrics:
        # First migration: copy old GS h-index as archival
        author_metrics['gs_h_index'] = existing_metrics.get('h_index', 0)
        author_metrics['gs_total_citations'] = existing_metrics.get('total_citations', 0)
    else:
        # Carry forward archival GS values if they exist
        author_metrics['gs_h_index'] = existing_metrics.get('gs_h_index', 0)
        author_metrics['gs_total_citations'] = existing_metrics.get('gs_total_citations', 0)

    # Fetch per-paper citations
    openalex_lookup = fetch_paper_citations_openalex(orcid)
    if not openalex_lookup:
        print("\nWarning: Could not fetch per-paper data from OpenAlex.", file=sys.stderr)
        print("Falling back to existing cached citations.", file=sys.stderr)
        matched = cache.get('citations', {})
    else:
        # Match BibTeX entries to OpenAlex data
        matched = match_bibtex_to_openalex(bib_pubs, openalex_lookup)

    # Update and save cache
    cache['citations'] = matched
    cache['metrics'] = author_metrics
    cache['last_updated'] = datetime.now().isoformat()
    cache['author_id'] = orcid

    save_cache(cache)

    print(f"\n{'=' * 70}")
    print("✓ Citation fetch complete!")
    print(f"{'=' * 70}")




if __name__ == '__main__':
    main()

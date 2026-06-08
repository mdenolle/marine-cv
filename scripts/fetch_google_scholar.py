#!/usr/bin/env python3
"""Fetch Google Scholar metrics and update citation cache locally.

This script fetches h-index and citation count from Google Scholar for the 
configured scholar ID. Results are stored in citation_cache.json as archival 
reference data (not replacing OpenAlex, which is the primary source in CI).

Google Scholar is intentionally NOT in the automated workflow because:
- Google blocks automated requests from CI/cloud services
- This allows you to update manually when needed
- Run this locally on your machine where Google Scholar works

Usage:
    python scripts/fetch_google_scholar.py [--scholar-id YOUR_SCHOLAR_ID]

If no scholar ID is provided, reads from CV YAML social_networks.
"""

import argparse
import json
import sys
import time
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any

# Try importing scholarly
try:
    from scholarly import scholarly, ProxyGenerator
except ImportError:
    print("Error: scholarly package is required for Google Scholar fetching")
    print("Install with: pip install scholarly", file=sys.stderr)
    sys.exit(1)

# Configuration
SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
CV_YAML_FILE = PROJECT_DIR / 'marine-cv-docs' / 'Marine_Denolle_CV.yaml'
CACHE_FILE = PROJECT_DIR / 'marine-cv-docs' / 'citation_cache.json'


def get_google_scholar_id(yaml_file: Path, override_id: Optional[str] = None) -> Optional[str]:
    """Extract Google Scholar ID from CV YAML or use provided override."""
    if override_id:
        return override_id
    
    try:
        from ruamel.yaml import YAML
        yaml = YAML()
        with open(yaml_file) as f:
            data = yaml.load(f)
        social_networks = data.get('cv', {}).get('social_networks', [])
        for network in social_networks:
            name = network.get('network', '').lower().replace(' ', '')
            if name in ('googlescholar', 'google_scholar'):
                return network.get('username')
    except Exception as e:
        print(f"Warning: Could not read Google Scholar ID from YAML: {e}", file=sys.stderr)
    return None


def fetch_google_scholar_metrics(scholar_id: str) -> Dict[str, Any]:
    """Fetch h-index and citation count from Google Scholar.
    
    Args:
        scholar_id: Google Scholar ID
        
    Returns:
        dict with keys: h_index, total_citations, or empty dict on failure
    """
    print(f"\nFetching Google Scholar metrics for ID: {scholar_id}")
    
    try:
        # Set up scholarly (optional: use proxy if needed for reliability)
        # pg = ProxyGenerator()
        # pg.FreeProxies()
        # scholarly.use_proxy(pg)
        
        # Get author profile
        author = next(scholarly.search_author(scholar_id))
        author_filled = scholarly.fill(author)
        
        h_index = author_filled.get('h_index', 0)
        citations = author_filled.get('citedby', 0)
        
        print(f"  ✓ Total citations: {citations:,}")
        print(f"  ✓ h-index: {h_index}")
        
        return {
            'h_index': h_index,
            'total_citations': citations
        }
    except StopIteration:
        print(f"  ✗ Could not find author with ID: {scholar_id}", file=sys.stderr)
        return {}
    except Exception as e:
        print(f"  ✗ Error fetching from Google Scholar: {e}", file=sys.stderr)
        print(f"     (This is normal if you're behind a firewall or Google is blocking)", file=sys.stderr)
        return {}


def update_cache_with_gs_metrics(metrics: Dict[str, Any]) -> bool:
    """Update citation cache with Google Scholar metrics.
    
    Args:
        metrics: dict from fetch_google_scholar_metrics()
        
    Returns:
        True if successful
    """
    if not metrics:
        return False
    
    # Load existing cache
    if not CACHE_FILE.exists():
        print(f"Warning: Cache file not found: {CACHE_FILE}", file=sys.stderr)
        print(f"Run 'python scripts/fetch_citations.py' first to create cache", file=sys.stderr)
        return False
    
    try:
        with open(CACHE_FILE, 'r') as f:
            cache = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Could not parse cache file: {CACHE_FILE}", file=sys.stderr)
        return False
    
    # Ensure metrics dict exists
    if 'metrics' not in cache:
        cache['metrics'] = {}
    
    # Update with Google Scholar data (marked as archival)
    cache['metrics']['gs_h_index'] = metrics.get('h_index', 0)
    cache['metrics']['gs_total_citations'] = metrics.get('total_citations', 0)
    cache['metrics']['gs_last_updated'] = datetime.now().isoformat()
    
    # Save updated cache
    try:
        with open(CACHE_FILE, 'w') as f:
            json.dump(cache, f, indent=2, ensure_ascii=False)
        print(f"\n✓ Updated cache at {CACHE_FILE}")
        return True
    except Exception as e:
        print(f"Error saving cache: {e}", file=sys.stderr)
        return False


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Fetch Google Scholar metrics and update citation cache'
    )
    parser.add_argument('--scholar-id', help='Override Google Scholar ID from YAML')
    args = parser.parse_args()
    
    print("=" * 70)
    print("Google Scholar Fetcher (Local/Manual)")
    print("=" * 70)
    
    # Get Scholar ID
    scholar_id = get_google_scholar_id(CV_YAML_FILE, args.scholar_id)
    if not scholar_id:
        print("Error: Could not find Google Scholar ID", file=sys.stderr)
        print("Provide it with: --scholar-id YOUR_ID", file=sys.stderr)
        print("Or add it to CV YAML social_networks: {network: Google Scholar, username: YOUR_ID}", file=sys.stderr)
        sys.exit(1)
    
    # Fetch metrics
    metrics = fetch_google_scholar_metrics(scholar_id)
    if not metrics:
        sys.exit(1)
    
    # Update cache
    if update_cache_with_gs_metrics(metrics):
        print("\n" + "=" * 70)
        print("✓ Google Scholar metrics added to cache!")
        print("=" * 70)
        print("\nNext steps:")
        print("  1. Run: python scripts/update_cv_citations.py")
        print("  2. Review changes in research_impact_summary.yaml")
        print("  3. Commit and push if satisfied")
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()

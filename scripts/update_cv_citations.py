#!/usr/bin/env python3
"""
Update CV with citation metrics from cache.

This script reads citation metrics from citation_cache.json and updates
the research_impact_summary section in Marine_Denolle_CV.yaml with:
- Total citations
- h-index
- i10-index
- Year-over-year citation growth

Usage:
    python scripts/update_cv_citations.py
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional

try:
    from ruamel.yaml import YAML
except ImportError:
    print("Error: ruamel.yaml is required. Install it with: pip install ruamel.yaml")
    sys.exit(1)

# File paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
CV_DIR = PROJECT_DIR / 'marine-cv-docs'
CV_FILE = CV_DIR / 'Marine_Denolle_CV.yaml'
CACHE_FILE = CV_DIR / 'citation_cache.json'


def load_citation_cache() -> Dict[str, Any]:
    """Load citation cache from JSON file."""
    if not CACHE_FILE.exists():
        print(f"Error: Cache file not found: {CACHE_FILE}")
        sys.exit(1)
    
    with open(CACHE_FILE, 'r') as f:
        return json.load(f)


def calculate_yoy_growth(cites_per_year: Dict[str, int]) -> Optional[str]:
    """Calculate year-over-year citation growth.
    
    Args:
        cites_per_year: Dictionary of {year: citation_count}
        
    Returns:
        String describing the growth, or None if insufficient data
    """
    if not cites_per_year or len(cites_per_year) < 2:
        return None
    
    # Use only fully completed years (exclude the current calendar year)
    current_calendar_year = datetime.now().year
    completed_years = sorted(
        [int(y) for y in cites_per_year.keys() if int(y) < current_calendar_year]
    )
    if len(completed_years) < 2:
        return None
    
    current_year = completed_years[-1]
    previous_year = completed_years[-2]
    
    current_citations = cites_per_year.get(str(current_year), 0)
    previous_citations = cites_per_year.get(str(previous_year), 0)
    
    if previous_citations == 0:
        return None
    
    growth_pct = ((current_citations - previous_citations) / previous_citations) * 100
    
    return f"{growth_pct:+.1f}% from {previous_year} to {current_year}"


def update_cv_with_metrics(cache: Dict[str, Any]) -> bool:
    """Update CV YAML file with citation metrics.
    
    Args:
        cache: Citation cache dictionary
        
    Returns:
        True if update was successful, False otherwise
    """
    if 'metrics' not in cache:
        print("Warning: No metrics found in citation cache")
        print("Run 'python scripts/fetch_citations.py --force-refresh' to fetch metrics")
        return False
    
    metrics = cache['metrics']

    # Extract OpenAlex metrics (primary, live source)
    oa_total = metrics.get('openalex_total_citations', metrics.get('total_citations', 0))
    oa_h = metrics.get('openalex_h_index', metrics.get('h_index', 0))
    i10_index = metrics.get('i10_index', 0)
    cites_per_year = metrics.get('cites_per_year', {})

    # Extract archival Google Scholar metrics (last known)
    gs_h = metrics.get('gs_h_index', 0)
    gs_total = metrics.get('gs_total_citations', 0)

    # Calculate year-over-year growth
    yoy_growth = calculate_yoy_growth(cites_per_year)

    # Format the citation details — show both sources
    oa_part = f"{oa_total:,} total (h-index: {oa_h}, i10: {i10_index})"
    if yoy_growth:
        oa_part += f" {yoy_growth}"
    oa_part += " (OpenAlex)"

    if gs_h:
        gs_part = f"h-index: {gs_h}"
        if gs_total:
            gs_part = f"{gs_total:,} total, " + gs_part
        gs_part += " (Google Scholar, last known)"
        citation_details = f"{oa_part} | {gs_part}"
    else:
        citation_details = oa_part

    print(f"\nCitation Metrics:")
    print(f"  Total citations (OpenAlex): {oa_total:,}")
    print(f"  h-index (OpenAlex): {oa_h}")
    print(f"  i10-index (OpenAlex): {i10_index}")
    if gs_h:
        print(f"  h-index (Google Scholar, last known): {gs_h}")
    if yoy_growth:
        print(f"  Year-over-year growth: {yoy_growth}")

    # Load research_impact_summary.yaml directly
    # (Marine_Denolle_CV.yaml uses !include which ruamel.yaml does not resolve)
    impact_file = CV_DIR / 'research_impact_summary.yaml'
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.default_flow_style = False
    yaml.width = 4096  # Prevent line wrapping

    try:
        with open(impact_file, 'r') as f:
            impact_summary = yaml.load(f)
    except Exception as e:
        print(f"Error loading {impact_file}: {e}")
        return False

    if not isinstance(impact_summary, list):
        print(f"Error: {impact_file} does not contain a YAML list")
        return False

    # Find or create the Research Citations entry
    citation_entry = None
    for entry in impact_summary:
        if isinstance(entry, dict) and entry.get('label') == 'Research Citations':
            citation_entry = entry
            break

    if citation_entry:
        citation_entry['details'] = citation_details
        print(f"\n✓ Updated 'Research Citations' entry")
    else:
        import ruamel.yaml.comments as _ryc
        new_entry = _ryc.CommentedMap({'label': 'Research Citations', 'details': citation_details})
        impact_summary.insert(0, new_entry)
        print(f"\n✓ Added 'Research Citations' entry")

    # Save updated research_impact_summary.yaml
    try:
        # Clear any accumulated document-level comments (prevent duplicate headers)
        if hasattr(impact_summary, 'ca') and impact_summary.ca.items:
            impact_summary.ca.items.clear()
        if hasattr(impact_summary, 'ca') and impact_summary.ca.comment:
            impact_summary.ca.comment = None
        with open(impact_file, 'w') as f:
            f.write("# AUTO-GENERATED by scripts/update_cv_citations.py — do not edit manually\n")
            yaml.dump(impact_summary, f)
        print(f"✓ Saved updated {impact_file}\n")
        return True
    except Exception as e:
        print(f"Error saving {impact_file}: {e}")
        return False


def main():
    """Main function."""
    print("=" * 70)
    print("Citation Metrics CV Updater")
    print("=" * 70)
    
    # Load cache
    print(f"\nLoading citation cache from {CACHE_FILE}...")
    cache = load_citation_cache()
    
    last_updated = cache.get('last_updated', 'unknown')
    print(f"Cache last updated: {last_updated}")
    
    # Update CV
    success = update_cv_with_metrics(cache)
    
    if success:
        print("=" * 70)
        print("✓ CV update complete!")
        print("=" * 70)
    else:
        print("\n" + "=" * 70)
        print("✗ CV update failed")
        print("=" * 70)
        sys.exit(1)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Update CV YAML with GitHub and PyPI statistics from cache.

This script reads the github_stats_cache.json file and updates the CV YAML
with current statistics for the research impact summary and software entries.

Usage:
    python scripts/update_cv_stats.py
"""

import json
import sys
from datetime import datetime
from pathlib import Path

try:
    from ruamel.yaml import YAML
except ImportError:
    print("Error: ruamel.yaml not installed. Run: pip install ruamel.yaml", file=sys.stderr)
    sys.exit(1)

# ==============================================================================
# CONFIGURATION
# ==============================================================================

CV_YAML_FILE = Path(__file__).parent.parent / 'marine-cv-docs' / 'Marine_Denolle_CV.yaml'
CACHE_FILE = Path(__file__).parent.parent / 'marine-cv-docs' / 'github_stats_cache.json'

# Map of YAML entry names to GitHub repo full names
REPO_MAP = {
    'NoisePy': 'noisepy/NoisePy',
    'Machine Learning in the Geosciences Textbook': 'geo-smart/mlgeo-book',
}

# ==============================================================================


def load_cache():
    """Load GitHub stats cache."""
    if not CACHE_FILE.exists():
        print(f"Error: Cache file not found: {CACHE_FILE}", file=sys.stderr)
        sys.exit(1)
    
    with open(CACHE_FILE) as f:
        return json.load(f)


def format_month_year(iso_timestamp):
    """Format ISO timestamp to 'Mon YYYY' format."""
    try:
        dt = datetime.fromisoformat(iso_timestamp)
        return dt.strftime('%b %Y')
    except (ValueError, TypeError):
        return datetime.now().strftime('%b %Y')


def update_cv_yaml(cache):
    """Update CV YAML file with statistics from cache."""
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096  # Prevent line wrapping
    
    # Load CV YAML
    with open(CV_YAML_FILE) as f:
        cv_data = yaml.load(f)
    
    # Extract stats
    github_stats = cache['github']
    pypi_stats = cache['pypi']
    last_updated = format_month_year(cache['last_updated'])
    
    agg = github_stats['aggregate']
    featured = github_stats['featured_repos']
    
    # Update research impact summary section
    if 'research_impact_summary' in cv_data['cv']['sections']:
        summary_section = cv_data['cv']['sections']['research_impact_summary']
        
        # Calculate total PyPI downloads (annual estimate)
        total_pypi_monthly = sum(stats['last_month'] for stats in pypi_stats.values())
        total_pypi_annual = total_pypi_monthly * 12
        
        # Count unique contributors across all repos
        all_contributors = set()
        for repo_data in featured.values():
            # This is an approximation - we don't have unique contributor count
            # across all repos, so we just report the aggregate
            pass
        
        # Update each summary item
        for item in summary_section:
            if item['label'] == 'Open-Source Software':
                item['details'] = f"{agg['total_stars']} GitHub stars across {agg['active_repos']} active repositories"
            elif item['label'] == 'Software Downloads':
                if total_pypi_annual > 0:
                    item['details'] = f"{total_pypi_annual:,}+ PyPI downloads annually (NoisePy package)"
                else:
                    item['details'] = 'PyPI package available (NoisePy)'
            elif item['label'] == 'Development Community':
                # Get contributor count from top repos
                top_contributors = sum(repo['contributors'] for repo in list(featured.values())[:5])
                item['details'] = f"{top_contributors}+ contributors across lab and collaborative projects"
        
        print(f"✓ Updated research impact summary")
    
    # Update software section entries
    if 'software' in cv_data['cv']['sections']:
        software_section = cv_data['cv']['sections']['software']
        
        for entry in software_section:
            entry_name = entry.get('name', '')
            
            if entry_name in REPO_MAP:
                repo_full_name = REPO_MAP[entry_name]
                
                if repo_full_name in featured:
                    repo = featured[repo_full_name]
                    
                    # Update the first highlight with stats
                    if entry.get('highlights'):
                        stats_line = f"{repo['stars']} GitHub stars, {repo['forks']} forks, {repo['contributors']} contributors ({last_updated})"
                        
                        # Check if first highlight is a stats line (contains 'stars' or 'forks')
                        if entry['highlights'] and ('stars' in entry['highlights'][0] or 'forks' in entry['highlights'][0]):
                            entry['highlights'][0] = stats_line
                        else:
                            # Insert as first highlight
                            entry['highlights'].insert(0, stats_line)
                        
                        # Add PyPI downloads if applicable
                        if entry_name == 'NoisePy' and 'noisepy' in pypi_stats:
                            pypi_line = f"{pypi_stats['noisepy']['last_month']} PyPI downloads/month"
                            
                            # Check if second highlight is PyPI line
                            if len(entry['highlights']) > 1 and 'PyPI downloads' in entry['highlights'][1]:
                                entry['highlights'][1] = pypi_line
                            else:
                                entry['highlights'].insert(1, pypi_line)
                        
                        print(f"✓ Updated stats for {entry_name}")
    
    # Save updated YAML
    with open(CV_YAML_FILE, 'w') as f:
        yaml.dump(cv_data, f)
    
    print(f"✓ Saved updated CV to {CV_YAML_FILE}")


def main():
    """Main entry point."""
    print("Updating CV with GitHub/PyPI statistics...")
    
    cache = load_cache()
    update_cv_yaml(cache)
    
    print("\n✓ CV successfully updated")
    return 0


if __name__ == '__main__':
    sys.exit(main())

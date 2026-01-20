#!/usr/bin/env python3
"""Fetch GitHub repository statistics and PyPI download metrics.

This script queries GitHub API to get comprehensive statistics across all
repositories for specified users and organizations, plus PyPI download counts.
It tracks temporal trends in CSV and caches latest snapshot in JSON.

Usage:
    python scripts/fetch_github_stats.py [--force-refresh]

The stats cache is saved to:
- marine-cv-docs/github_stats_cache.json (latest snapshot)
- marine-cv-docs/github_stats_history.csv (temporal trends)

Configuration:
    Edit GITHUB_ACCOUNTS and PYPI_PACKAGES below to track additional
    users, organizations, or Python packages.
"""

import argparse
import csv
import json
import sys
import time
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Dict, List, Any

try:
    import requests
except ImportError:
    print("Error: requests not installed. Run: pip install requests", file=sys.stderr)
    sys.exit(1)

# ==============================================================================
# CONFIGURATION
# ==============================================================================

# GitHub accounts to track (users and organizations)
GITHUB_ACCOUNTS = {
    'users': ['mdenolle'],
    'orgs': ['Denolle-Lab', 'noisepy', 'geo-smart', 'EarthML4PNW'],
    # Add more organizations here as needed
}

# PyPI packages to track downloads
PYPI_PACKAGES = [
    'noisepy',
    # Add more packages here as needed
]

# Cache settings
CACHE_FILE = Path(__file__).parent.parent / 'marine-cv-docs' / 'github_stats_cache.json'
HISTORY_FILE = Path(__file__).parent.parent / 'marine-cv-docs' / 'github_stats_history.csv'
CACHE_EXPIRY_DAYS = 7  # Refresh weekly (more frequent than citations)

# GitHub API settings
GITHUB_API_BASE = 'https://api.github.com'
PYPISTATS_API_BASE = 'https://pypistats.org/api'

# Rate limiting
REQUEST_DELAY = 0.5  # Seconds between requests

# ==============================================================================


def get_github_token() -> Optional[str]:
    """Get GitHub token from environment variable."""
    import os
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print("Warning: GITHUB_TOKEN not set. Using unauthenticated API (60 req/hour limit)", 
              file=sys.stderr)
    return token


def make_github_request(endpoint: str, token: Optional[str] = None) -> Optional[Any]:
    """Make a request to GitHub API with rate limiting."""
    url = f"{GITHUB_API_BASE}{endpoint}"
    headers = {'Accept': 'application/vnd.github.v3+json'}
    
    if token:
        headers['Authorization'] = f'token {token}'
    
    try:
        time.sleep(REQUEST_DELAY)
        response = requests.get(url, headers=headers)
        
        if response.status_code == 403 and 'rate limit' in response.text.lower():
            print(f"Warning: GitHub API rate limit exceeded", file=sys.stderr)
            return None
        
        response.raise_for_status()
        return response.json()
    
    except requests.RequestException as e:
        print(f"Warning: GitHub API request failed for {endpoint}: {e}", file=sys.stderr)
        return None


def fetch_repos_for_account(account: str, account_type: str, token: Optional[str]) -> List[Dict]:
    """Fetch all repositories for a user or organization."""
    endpoint = f"/{account_type}s/{account}/repos?per_page=100"
    repos = []
    
    page = 1
    while True:
        data = make_github_request(f"{endpoint}&page={page}", token)
        if not data or len(data) == 0:
            break
        
        repos.extend(data)
        page += 1
        
        # Safety limit: stop at 500 repos
        if len(repos) >= 500:
            break
    
    return repos


def fetch_contributor_count(owner: str, repo: str, token: Optional[str]) -> int:
    """Fetch number of unique contributors for a repository."""
    # Note: This endpoint is paginated, we're approximating with first 100
    all_contributors = make_github_request(f"/repos/{owner}/{repo}/contributors?per_page=100", token)
    return len(all_contributors) if all_contributors else 0


def fetch_pypi_stats(package: str) -> Dict[str, int]:
    """Fetch download statistics for a PyPI package."""
    try:
        url = f"{PYPISTATS_API_BASE}/packages/{package}/recent"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        return {
            'last_day': data.get('data', {}).get('last_day', 0),
            'last_week': data.get('data', {}).get('last_week', 0),
            'last_month': data.get('data', {}).get('last_month', 0),
        }
    
    except requests.RequestException as e:
        print(f"Warning: PyPI stats request failed for {package}: {e}", file=sys.stderr)
        return {'last_day': 0, 'last_week': 0, 'last_month': 0}


def aggregate_repo_stats(repos: List[Dict]) -> Dict[str, Any]:
    """Aggregate statistics across multiple repositories."""
    total_stars = 0
    total_forks = 0
    total_watchers = 0
    total_open_issues = 0
    languages = defaultdict(int)
    active_repos = 0
    
    six_months_ago = datetime.now() - timedelta(days=180)
    
    for repo in repos:
        if repo.get('fork', False):
            continue
        
        total_stars += repo.get('stargazers_count', 0)
        total_forks += repo.get('forks_count', 0)
        total_watchers += repo.get('watchers_count', 0)
        total_open_issues += repo.get('open_issues_count', 0)
        
        lang = repo.get('language')
        if lang:
            languages[lang] += 1
        
        pushed_at = repo.get('pushed_at')
        if pushed_at:
            try:
                pushed_date = datetime.fromisoformat(pushed_at.replace('Z', '+00:00'))
                if pushed_date.replace(tzinfo=None) > six_months_ago:
                    active_repos += 1
            except ValueError:
                pass
    
    return {
        'total_repos': len(repos),
        'total_stars': total_stars,
        'total_forks': total_forks,
        'total_watchers': total_watchers,
        'total_open_issues': total_open_issues,
        'active_repos': active_repos,
        'languages': dict(languages),
    }


def fetch_all_github_stats(token: Optional[str] = None) -> Dict[str, Any]:
    """Fetch comprehensive GitHub statistics for all configured accounts."""
    print("Fetching GitHub statistics...")
    all_repos = []
    per_account_stats = {}
    featured_repos = {}
    
    for user in GITHUB_ACCOUNTS['users']:
        print(f"  Fetching repos for user: {user}")
        repos = fetch_repos_for_account(user, 'user', token)
        all_repos.extend(repos)
        per_account_stats[user] = aggregate_repo_stats(repos)
        print(f"    Found {len(repos)} repos")
    
    for org in GITHUB_ACCOUNTS['orgs']:
        print(f"  Fetching repos for org: {org}")
        repos = fetch_repos_for_account(org, 'org', token)
        all_repos.extend(repos)
        per_account_stats[org] = aggregate_repo_stats(repos)
        print(f"    Found {len(repos)} repos")
    
    aggregate_stats = aggregate_repo_stats(all_repos)
    
    print("  Fetching details for top repositories...")
    sorted_repos = sorted(all_repos, key=lambda r: r.get('stargazers_count', 0), reverse=True)
    
    for repo in sorted_repos[:20]:
        if repo.get('fork', False):
            continue
        
        owner = repo['owner']['login']
        name = repo['name']
        full_name = f"{owner}/{name}"
        
        print(f"    {full_name}: {repo.get('stargazers_count', 0)} stars")
        
        contributor_count = fetch_contributor_count(owner, name, token)
        
        featured_repos[full_name] = {
            'name': name,
            'owner': owner,
            'url': repo.get('html_url', ''),
            'description': repo.get('description', ''),
            'stars': repo.get('stargazers_count', 0),
            'forks': repo.get('forks_count', 0),
            'watchers': repo.get('watchers_count', 0),
            'open_issues': repo.get('open_issues_count', 0),
            'contributors': contributor_count,
            'language': repo.get('language', ''),
            'created_at': repo.get('created_at', ''),
            'updated_at': repo.get('updated_at', ''),
            'pushed_at': repo.get('pushed_at', ''),
        }
    
    return {
        'aggregate': aggregate_stats,
        'per_account': per_account_stats,
        'featured_repos': featured_repos,
    }


def fetch_all_pypi_stats() -> Dict[str, Dict[str, int]]:
    """Fetch PyPI download statistics for all configured packages."""
    print("Fetching PyPI statistics...")
    pypi_stats = {}
    
    for package in PYPI_PACKAGES:
        print(f"  Fetching stats for: {package}")
        stats = fetch_pypi_stats(package)
        pypi_stats[package] = stats
        print(f"    Last month: {stats['last_month']:,} downloads")
    
    return pypi_stats


def load_cache() -> Dict[str, Any]:
    """Load stats cache from JSON file."""
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE) as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Warning: Corrupted cache file, starting fresh", file=sys.stderr)
    
    return {
        'last_updated': None,
        'github': {},
        'pypi': {},
    }


def save_cache(data: Dict[str, Any]) -> None:
    """Save stats cache to JSON file."""
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    with open(CACHE_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✓ Saved cache to {CACHE_FILE}")


def append_to_history(github_stats: Dict[str, Any], pypi_stats: Dict[str, Dict[str, int]]) -> None:
    """Append current stats to CSV history file."""
    timestamp = datetime.now().isoformat()
    
    row = {
        'timestamp': timestamp,
        'total_repos': github_stats['aggregate']['total_repos'],
        'total_stars': github_stats['aggregate']['total_stars'],
        'total_forks': github_stats['aggregate']['total_forks'],
        'total_watchers': github_stats['aggregate']['total_watchers'],
        'active_repos': github_stats['aggregate']['active_repos'],
        'total_open_issues': github_stats['aggregate']['total_open_issues'],
    }
    
    for package, stats in pypi_stats.items():
        row[f'pypi_{package}_last_month'] = stats['last_month']
    
    file_exists = HISTORY_FILE.exists()
    HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    with open(HISTORY_FILE, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(row)
    
    print(f"✓ Appended history to {HISTORY_FILE}")


def is_cache_valid(cache: Dict[str, Any]) -> bool:
    """Check if cache is still valid based on expiry time."""
    if not cache.get('last_updated'):
        return False
    
    try:
        last_updated = datetime.fromisoformat(cache['last_updated'])
        age = datetime.now() - last_updated
        return age.days < CACHE_EXPIRY_DAYS
    except (ValueError, TypeError):
        return False


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Fetch GitHub and PyPI statistics')
    parser.add_argument('--force-refresh', action='store_true',
                        help='Force refresh even if cache is valid')
    args = parser.parse_args()
    
    cache = load_cache()
    
    if not args.force_refresh and is_cache_valid(cache):
        print(f"Cache is still valid (refreshed {cache['last_updated']})")
        print("Use --force-refresh to update anyway")
        return 0
    
    token = get_github_token()
    
    try:
        github_stats = fetch_all_github_stats(token)
        pypi_stats = fetch_all_pypi_stats()
    except Exception as e:
        print(f"Error fetching statistics: {e}", file=sys.stderr)
        return 1
    
    cache['last_updated'] = datetime.now().isoformat()
    cache['github'] = github_stats
    cache['pypi'] = pypi_stats
    
    save_cache(cache)
    append_to_history(github_stats, pypi_stats)
    
    print("\n" + "="*60)
    print("GitHub Statistics Summary")
    print("="*60)
    agg = github_stats['aggregate']
    print(f"Total repositories: {agg['total_repos']}")
    print(f"Total stars: {agg['total_stars']:,}")
    print(f"Total forks: {agg['total_forks']:,}")
    print(f"Active repositories (last 6 months): {agg['active_repos']}")
    print(f"Top languages: {', '.join(list(agg['languages'].keys())[:5])}")
    
    if pypi_stats:
        print("\n" + "="*60)
        print("PyPI Download Statistics")
        print("="*60)
        for package, stats in pypi_stats.items():
            print(f"{package}: {stats['last_month']:,} downloads/month")
    
    print("\n✓ Statistics updated successfully")
    return 0


if __name__ == '__main__':
    sys.exit(main())

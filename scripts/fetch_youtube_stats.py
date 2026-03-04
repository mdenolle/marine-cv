#!/usr/bin/env python3
"""Fetch YouTube channel statistics for Marine Denolle's channels.

Calls the YouTube Data API v3 to retrieve viewCount, subscriberCount, and
videoCount for each channel listed in CHANNEL_HANDLES. Results are cached
in youtube_stats_cache.json for CACHE_DAYS days.

Usage:
    # With API key:
    YOUTUBE_API_KEY=... python scripts/fetch_youtube_stats.py

    # Force refresh even if cache is fresh:
    YOUTUBE_API_KEY=... python scripts/fetch_youtube_stats.py --force-refresh

Requirements:
    pip install requests
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

import requests

# ==============================================================================
# CONFIGURATION
# ==============================================================================

CACHE_FILE = Path(__file__).parent.parent / "marine-cv-docs" / "youtube_stats_cache.json"
CACHE_DAYS = 7  # refresh weekly

# Handles to track (the @ part after youtube.com/@)
CHANNEL_HANDLES = [
    "scoped6259",       # @scoped6259  – SCOPED workshop channel
    "uwgeophysics6888", # @uwgeophysics6888 – UW Geophysics channel
]

YT_API_BASE = "https://www.googleapis.com/youtube/v3"

# ==============================================================================


def load_cache() -> dict:
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE) as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {}


def save_cache(data: dict) -> None:
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print(f"  Saved cache → {CACHE_FILE}")


def is_cache_fresh(cache: dict) -> bool:
    last = cache.get("last_updated")
    if not last:
        return False
    try:
        age = datetime.now() - datetime.fromisoformat(last)
        return age < timedelta(days=CACHE_DAYS)
    except ValueError:
        return False


def fetch_channel_stats(handle: str, api_key: str) -> dict | None:
    """Fetch statistics for a single channel by handle (without leading @)."""
    url = f"{YT_API_BASE}/channels"
    params = {
        "part": "statistics,snippet",
        "forHandle": f"@{handle}",
        "key": api_key,
    }
    try:
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        items = data.get("items", [])
        if not items:
            print(f"  ⚠ No channel found for handle @{handle}", file=sys.stderr)
            return None
        item = items[0]
        stats = item.get("statistics", {})
        snippet = item.get("snippet", {})
        return {
            "handle": handle,
            "channel_id": item.get("id", ""),
            "title": snippet.get("title", handle),
            "view_count": int(stats.get("viewCount", 0)),
            "subscriber_count": int(stats.get("subscriberCount", 0)),
            "video_count": int(stats.get("videoCount", 0)),
            "fetched_at": datetime.now().isoformat(),
        }
    except requests.RequestException as e:
        print(f"  ⚠ Failed to fetch @{handle}: {e}", file=sys.stderr)
        return None


def aggregate_channels(channels: list[dict]) -> dict:
    return {
        "total_views": sum(c["view_count"] for c in channels),
        "total_subscribers": sum(c["subscriber_count"] for c in channels),
        "total_videos": sum(c["video_count"] for c in channels),
        "channel_count": len(channels),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force-refresh", action="store_true", help="Bypass cache")
    args = parser.parse_args()

    api_key = os.environ.get("YOUTUBE_API_KEY", "")

    # Load existing cache
    cache = load_cache()

    if not args.force_refresh and is_cache_fresh(cache):
        print("YouTube stats cache is fresh — skipping fetch.")
        return 0

    if not api_key:
        print(
            "⚠  YOUTUBE_API_KEY not set. "
            "Keeping existing cached data (if any).",
            file=sys.stderr,
        )
        if not cache:
            # Write empty placeholder so update_cv_stats.py doesn't crash
            save_cache({
                "last_updated": datetime.now().isoformat(),
                "channels": [],
                "aggregate": {
                    "total_views": 0,
                    "total_subscribers": 0,
                    "total_videos": 0,
                    "channel_count": 0,
                },
                "note": "No API key provided — placeholder data",
            })
        return 0

    print(f"Fetching YouTube stats for {len(CHANNEL_HANDLES)} channels...")
    channels = []
    for handle in CHANNEL_HANDLES:
        print(f"  Querying @{handle}...")
        stats = fetch_channel_stats(handle, api_key)
        if stats:
            channels.append(stats)
            print(
                f"    {stats['title']}: "
                f"{stats['view_count']:,} views, "
                f"{stats['subscriber_count']:,} subscribers, "
                f"{stats['video_count']} videos"
            )

    agg = aggregate_channels(channels)
    print(
        f"\nAggregate: {agg['total_views']:,} total views, "
        f"{agg['total_subscribers']:,} subscribers across {agg['channel_count']} channels"
    )

    new_cache = {
        "last_updated": datetime.now().isoformat(),
        "channels": channels,
        "aggregate": agg,
    }
    save_cache(new_cache)
    return 0


if __name__ == "__main__":
    sys.exit(main())

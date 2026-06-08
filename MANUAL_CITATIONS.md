# Manual Google Scholar Citation Updates

## Overview

This project uses **two citation sources**:

1. **OpenAlex** — Automatically fetched via GitHub Actions (monthly)
   - Primary/live source
   - Reliable and works in CI environments
   - Updated automatically at 2am UTC on the 1st of each month

2. **Google Scholar** — Manually fetched locally (this document)
   - Reference/archival source
   - Blocked from automated CI/cloud services by Google
   - Updated manually when needed
   - Stored in cache as "last known" values

## Why Two Sources?

Google Scholar actively blocks automated requests from GitHub Actions and similar CI environments. Rather than add unreliable proxying or fail silently, we use:
- **OpenAlex** as the primary automated source
- **Google Scholar** as manually-updated archival reference

The CV displays both: *"X citations (OpenAlex) | Y citations, h-index: Z (Google Scholar, last known)"*

## Safe Manual Update Process

### Step 1: Fetch Google Scholar Locally

Run this on your machine (where Google Scholar allows requests):

```bash
# Basic usage (reads Scholar ID from CV YAML)
python scripts/fetch_google_scholar.py

# Or specify Scholar ID directly
python scripts/fetch_google_scholar.py --scholar-id YOUR_SCHOLAR_ID
```

**Output:** Fetched metrics are added to `marine-cv-docs/citation_cache.json` as archival data.

### Step 2: Update CV with New Metrics

```bash
python scripts/update_cv_citations.py
```

This reads the cache and updates `marine-cv-docs/research_impact_summary.yaml` with both OpenAlex and Google Scholar data.

### Step 3: Review & Commit

```bash
# Check what changed
git diff marine-cv-docs/

# Stage the changes
git add marine-cv-docs/citation_cache.json marine-cv-docs/research_impact_summary.yaml

# Commit (the auto-updating workflow won't touch these if they're recent)
git commit -m "Update Google Scholar citation metrics [manual]"
git push
```

## Cache Structure

The `citation_cache.json` file structure:

```json
{
  "last_updated": "ISO datetime",
  "author_id": "ORCID",
  "metrics": {
    "openalex_total_citations": <int>,      // Auto-updated by CI
    "openalex_h_index": <int>,              // Auto-updated by CI
    "i10_index": <int>,                     // Auto-updated by CI
    "gs_total_citations": <int>,            // Manually updated (this script)
    "gs_h_index": <int>,                    // Manually updated (this script)
    "gs_last_updated": "ISO datetime"       // When you last ran fetch_google_scholar.py
  }
}
```

## Safe to Manually Edit

You can safely hand-edit `marine-cv-docs/citation_cache.json` to add Google Scholar metrics:

```json
{
  "metrics": {
    "gs_h_index": 42,
    "gs_total_citations": 8000,
    "gs_last_updated": "2026-06-08T14:30:00"
  }
}
```

Then run `python scripts/update_cv_citations.py` to regenerate the CV.

## Troubleshooting

### "Error: scholarly package is required"
Install it:
```bash
pip install scholarly
```

### "Could not find author..."
Make sure your Google Scholar ID is correct. Check your profile URL:
- URL: `https://scholar.google.com/citations?user=ABC123XYZ`
- ID: `ABC123XYZ`

### "Google is blocking requests"
This is expected from some networks/VPNs. Try:
- Running from home network (not VPN)
- Running at a different time
- Manually entering your metrics (see "Safe to Manually Edit" above)

## Automation (Future)

If you want to add Google Scholar to the CI workflow later, you have options:

1. **Proxy service** — Use a commercial proxy pool (ScraperAPI, Bright Data)
2. **Local runner** — Set up a personal GitHub runner with trusted network
3. **Scheduled local fetch** — Cron job on your machine that commits updates

For now, the manual process keeps things simple and reliable.

## References

- **OpenAlex API**: https://docs.openalex.org/
- **Scholarly GitHub**: https://github.com/scholarly-python-package/scholarly
- **Google Scholar**: https://scholar.google.com/

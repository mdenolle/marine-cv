# Scripts Directory

This directory contains automation scripts for maintaining the CV and calculating metrics.

## Grant Analysis

### `calculate_grant_totals.py`

Calculates total grant funding amounts from `grant_support.yaml`, categorized by role.

**Usage:**
```bash
python scripts/calculate_grant_totals.py
```

**Output:**
- Lead PI grants total and count
- Co-PI/Co-I grants total and count (includes both lead PI on multi-institution grants and co-PI on collaborative grants)
- Grand total across all grants
- Detailed breakdown by year and institution

**Automation:**
This script runs automatically via GitHub Actions (`.github/workflows/calculate-grants.yml`) whenever `marine-cv-docs/grant_support.yaml` is modified. The results are:
- Posted as a comment on pull requests
- Available in the workflow summary for push events
- Can be manually triggered via workflow dispatch

## Publications & Citations

### `generate_publications.py`
Generates publication entries from BibTeX files.

### `fetch_citations.py`
Fetches citation counts from Google Scholar.

### `update_cv_citations.py`
Updates CV with latest citation information.

## GitHub Statistics

### `fetch_github_stats.py`
Fetches repository statistics from GitHub and PyPI.

### `update_cv_stats.py`
Updates CV with latest GitHub/PyPI statistics.

**Automation:**
Runs monthly via GitHub Actions (`.github/workflows/update-stats.yml`).

## Development Tools

### `create_executable.py`
Creates standalone executables for RenderCV.

### `update_entry_figures.py`
Updates entry type figures in documentation.

### `update_examples.py`
Updates example CV files.

### `update_schema.py`
Updates the JSON schema file.

## Requirements

Most scripts require:
- Python 3.12+
- PyYAML (`pip install pyyaml`)
- Requests (`pip install requests`)
- ruamel.yaml (`pip install ruamel.yaml`)

For the full development environment, use:
```bash
pixi install
```

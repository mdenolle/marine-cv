<div align="center">
<h1>Marine Denolle's Academic CV</h1>

_Automated BibTeX-based CV system built with RenderCV_

**Based on [RenderCV](https://github.com/rendercv/rendercv) v2.6** — A powerful CV/resume generator for academics and engineers

[![Original RenderCV](https://img.shields.io/badge/based%20on-RenderCV-blue)](https://github.com/rendercv/rendercv)
[![RenderCV docs](https://img.shields.io/badge/docs-RenderCV-rgb(0%2C79%2C144))](https://docs.rendercv.com)

</div>

## About This Repository

This repository contains an **adapted version** of [RenderCV](https://github.com/rendercv/rendercv) with custom enhancements for academic CVs, specifically:

- **BibTeX integration** for automated publication management
- **Group member tagging** to track co-authored papers
- **Custom parser** for academic bibliography formatting
- **Academic-specific sections** (datasets, software, invited talks)

### Original RenderCV

RenderCV is an excellent open-source CV generator that converts YAML to beautifully formatted PDFs. It was created and is maintained by [Sina Atalay](https://github.com/sinaatalay).

**Original repository**: https://github.com/rendercv/rendercv  
**Documentation**: https://docs.rendercv.com  
**License**: MIT

Write your CV as YAML, then run RenderCV,

```bash
rendercv render Marine_Denolle_CV.yaml
```

and get a 10-page PDF with perfect typography, automated publications from BibTeX, and group member tagging.

## What's Different from Original RenderCV?

This repository adds the following enhancements:

### 1. **BibTeX Parser** (`src/rendercv/bibtex_parser.py`)
Automatically parse `.bib` files and convert to RenderCV publication format:
- Cleans LaTeX formatting
- Extracts DOIs and generates URLs
- Supports 62+ publications from a single source file
- Handles special characters (ö, é, ñ, etc.)

### 2. **Group Member Tagging**
Automatically marks co-authored publications with asterisk (*):
```python
# Publications with group members get marked
'Ni, Yiyu*', 'Denolle, Marine*', 'Shi, Qibin*'  # Automatically tagged
```
Tracks 19 group members (PhD students, postdocs, mentees) across 62 publications.

### 3. **Publication Generator Script** (`scripts/generate_publications.py`)
One-command publication updates:
```bash
python scripts/generate_publications.py > temp_publications.yaml
# Copy output into your CV YAML
```

### 4. **Media Coverage Linking**
Link news articles and press releases to publications:
```python
MEDIA_COVERAGE = {
    'Denolle2014': [
        'https://news.stanford.edu/2014/01/23/earthquake-prediction/',
    ],
}
```

### 5. **Academic Sections**
Extended sections for:
- **Datasets** with DOIs and GitHub links
- **Software** with GitHub statistics
- **Invited Talks** (65+ talks over 14 years)
- **Teaching** with course URLs

## Quick Start

### 1. Install Dependencies

Using pixi (recommended):
```bash
pixi install
```

Or using conda:
```bash
conda env create -f environment.yml
conda activate marine-cv
pip install -e .
```

### 2. Prepare Your BibTeX File

Create or export your publications as a `.bib` file in the `marine-cv-docs/` directory. Most reference managers support BibTeX export:

**From Zotero:**
1. Select publications → Right-click → Export Items
2. Choose "BibTeX" format
3. Save as `your_publications.bib`

**From Mendeley:**
1. File → Export → BibTeX (.bib)

**Example BibTeX entry:**
```bibtex
@article{Denolle2014,
  author = {Denolle, Marine A. and Dunham, Eric M. and Prieto, Germ\'an A. and Beroza, Gregory C.},
  title = {Strong Ground Motion Prediction using Virtual Earthquakes},
  journal = {Science},
  volume = {343},
  number = {6169},
  pages = {399--403},
  year = {2014},
  doi = {10.1126/science.1245678},
  url = {https://doi.org/10.1126/science.1245678}
}
```

**Tips for BibTeX:**
- Include `doi` field for automatic URL generation
- Add media coverage URLs in `note` field using `\url{https://...}` format for automatic extraction
- Use standard LaTeX escapes: `\'e` for é, `\"o` for ö, `\~n` for ñ
- Use `and` to separate multiple authors
- Keep citation keys consistent (e.g., `LastName2024`, `LastNameEtAl2024a`)

**Media Coverage Feature:**
Add news articles and press coverage directly in BibTeX note fields:
```bibtex
@article{Denolle2025,
  author = {Denolle, Marine A. and Others},
  title = {Important Paper},
  journal = {Science},
  year = {2025},
  doi = {10.1126/science.xxxxx},
  note = {\url{https://news.university.edu/article} \url{https://science.org/news}}
}
```
These URLs will automatically appear as "Featured in: [Link 1](url1), [Link 2](url2)" in your CV.

### 3. Configure Group Members (Optional)

To automatically tag co-authored publications with asterisks, edit `src/rendercv/bibtex_parser.py`:

```python
DEFAULT_GROUP_MEMBERS = [
    'Your Name',           # Your name
    'PhD Student 1',       # Current/former PhD students
    'Postdoc Name',        # Current/former postdocs
    'Collaborator Name',   # Other group members you want tagged
]
```

Publications with these authors will automatically show asterisks: `*Your Name*`, `*PhD Student 1*`

**Configure Google Scholar ID for Citation Fetching:**

Add your Google Scholar author ID to your CV YAML file:

1. Find your Google Scholar ID:
   - Go to https://scholar.google.com/citations
   - Your ID is in the URL: `?user=YOUR_ID_HERE`

2. Add to `social_networks` in your CV YAML:
   ```yaml
   social_networks:
     - network: Google Scholar
       username: YOUR_SCHOLAR_ID  # The ID from your profile URL
   ```

The citation fetcher will automatically read this ID from your YAML file.

### 4. Fill Out Your CV YAML

Create `Your_Name_CV.yaml`:

```yaml

With RenderCV, you can:

- Version-control your CV — it's just text.
- Focus on content — don't worry about the formatting.
- Get perfect typography — pixel-perfect alignment and spacing, handled for you.

### 3. Fill Out Your CV YAML

Create `Your_Name_CV.yaml`:

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/rendercv/rendercv/refs/tags/v2.5/schema.json

# Design Configuration (optional but recommended at top)
design:
  theme: moderncv  # Options: classic, moderncv, sb2nov, engineeringresumes
  page:
    size: us-letter  # or a4
    top_margin: 0.7in
    bottom_margin: 0.7in
    left_margin: 0.7in
    right_margin: 0.7in
  colors:
    name: rgb(128, 0, 0)          # Your name color
    section_titles: rgb(69, 128, 179)  # Section headers
  typography:
    font_family:
      body: 'IBM Plex Serif'      # Main text font
      section_titles: 'IBM Plex Sans'  # Header font

# CV Content
cv:
  name: Your Full Name
  headline: Your Title/Position
  location: City, State
  email: your.email@university.edu
  website: https://yourwebsite.edu/
  social_networks:
    - network: LinkedIn
      username: yourprofile
    - network: GitHub
      username: yourusername
    - network: ORCID
      username: 0000-0000-0000-0000
    - network: Google Scholar
      username: YOUR_SCHOLAR_ID  # For automatic citation fetching

  sections:
    # Employment Section
    employment:
      - company: University Name
        position: Associate Professor
        start_date: 2024-01
        end_date: present
        location: City, State
        summary: Department of Your Field
        highlights:
          - Key achievement or responsibility
          - Another achievement

    # Education Section
    education:
      - institution: University Name
        area: Your Field
        degree: PhD
        start_date: 2008-09
        end_date: 2014-06
        location: City, State
        highlights:
          - 'Supervisor: Dr. Name'
          - Notable achievements

    # Teaching Section (with URLs)
    teaching:
      - name: 'Course Name'
        url: https://your-course-website.edu/
        date: 'COURSE 101'
        location: 'University Name'
        summary: 'Course description'
        highlights:
          - 'Taught Fall 2021, 2022, 2023'
          - 'Course adoption by other institutions'

    # Software Section (with GitHub stats)
    software:
      - name: 'Your Software Package'
        url: https://github.com/yourusername/yourpackage
        date: '2020-present'
        summary: 'Brief description of the software'
        highlights:
          - 'X stars, Y forks, Z contributors'
          - 'Used by researchers worldwide'

    # Datasets Section (with DOIs)
    datasets:
      - name: 'Your Dataset Name'
        url: https://doi.org/10.xxxxx/xxxxx
        date: '2023'
        summary: 'Dataset description and significance'
        highlights:
          - 'Published in Journal Name'
          - 'DOI: 10.xxxxx/xxxxx'

    # Publications Section (manually entered, or use script)
    selected_publications:
      # See "Generate Publications from BibTeX" below
      - title: 'Your Publication Title'
        authors:
          - LastName, FirstName
          - '*YourName*'  # Use asterisk for group members
          - OtherAuthor, Name
        journal: 'Journal Name, Volume(Issue), Pages'
        date: 2024-01
        doi: 10.xxxx/xxxxx
        url: https://doi.org/10.xxxx/xxxxx

# Locale (optional)
locale:
  language: english

# Settings (optional)
settings:
  current_date: '2026-01-16'
```

**YAML Tips:**
- Use 2-space indentation (not tabs)
- Dates: `YYYY-MM` format or `YYYY-MM-DD`, or just `YYYY`
- For `end_date`, use string `'present'` for ongoing positions
- URLs: Include `https://` prefix
- Lists: Use `- item` format
- Strings with special characters or colons: Use quotes `'text: description'`
- For bullet entries: `- bullet: 'Year -- Type -- Institution -- Description'`
- For one-line entries: Use `label` and `details` fields

See [Marine_Denolle_CV.yaml](marine-cv-docs/Marine_Denolle_CV.yaml) for a complete example.

**Customizing Publication Template:**
In your YAML, you can customize how publications are displayed:

```yaml
design:
  templates:
    publication_entry:
      main_column: |-
        **TITLE**
        AUTHORS
        JOURNAL
        URL
        MEDIA_COVERAGE
```

The template supports these special placeholders:
- `TITLE`, `AUTHORS`, `JOURNAL`, `DOI`, `URL` - Standard publication fields
- `MEDIA_COVERAGE` - Automatically populated from BibTeX `note` field URLs

### 5. Generate Publications from BibTeX

**Option A: Automatic Generation (Recommended)**

1. Edit group members in `src/rendercv/bibtex_parser.py`:
```python
DEFAULT_GROUP_MEMBERS = [
    'Your Name',
    'PhD Student 1',
    'Postdoc 1',
    # Add all group members
]
```

2. Edit media coverage in `scripts/generate_publications.py`:
```python
MEDIA_COVERAGE = {
    'CitationKey2024': [
        'https://news.university.edu/article',
    ],
}
```

3. Generate publications YAML:
```bash
python scripts/generate_publications.py > temp_publications.yaml
```

4. Copy the output into your CV YAML (replace `selected_publications` section)

**Option B: Manual Entry**

Write publications directly in YAML (see example above). Use asterisk (*) to mark group members.

### 5. Generate Publications from BibTeX

**Automatic Generation (Recommended):**

Run the publication generator script to convert your BibTeX file to RenderCV YAML format:

```bash
python scripts/generate_publications.py marine-cv-docs/your-publications.bib > temp_publications.yaml
```

This script:
- Converts all BibTeX entries to YAML format
- Automatically tags group members with asterisks
- Extracts DOIs and generates URLs
- Extracts media coverage URLs from `note` fields
- Adds citation counts from cache (if available)
- Cleans LaTeX formatting and special characters

**Fetching Citation Counts:**

Before generating publications, you can fetch Google Scholar citation counts:

```bash
# First time setup: fetch citations (takes 2-3 minutes for ~60 papers)
python scripts/fetch_citations.py

# This creates marine-cv-docs/citation_cache.json with citation counts
# The cache is used automatically by generate_publications.py
```

The citation fetcher:
- Queries Google Scholar using your author ID
- Matches BibTeX titles to Scholar publications (fuzzy matching)
- Saves citation counts to `citation_cache.json`
- Cache expires after 30 days
- Use `--force-refresh` to update immediately

**Citation Cache Management:**
```bash
# Check if cache is fresh (shows last update date)
python scripts/fetch_citations.py

# Force refresh even if cache is recent
python scripts/fetch_citations.py --force-refresh
```

**Note:** The GitHub Actions workflow will automatically refresh citations monthly.

**Manual media coverage override (optional):**
If you need to manually add media coverage URLs for specific publications, edit `scripts/generate_publications.py`:
```python
MEDIA_COVERAGE = {
    'CitationKey2024': [
        'https://news.university.edu/article1',
        'https://magazine.com/article2',
    ],
    'AnotherKey2023': [
        'https://press.release.edu/story',
    ],
}
```

Then copy the generated YAML output into your CV YAML file under the `selected_publications` section.

### 6. Render Your CV to PDF

Navigate to your CV directory and run:

```bash
pixi run python -m rendercv render marine-cv-docs/Your_Name_CV.yaml
```

Or if using conda environment:
```bash
rendercv render marine-cv-docs/Your_Name_CV.yaml
```

The command will:
1. Validate your YAML file
2. Generate Typst source code
3. Compile to PDF using Typst
4. Generate additional formats (Markdown, HTML, PNG)
5. Save all outputs to `marine-cv-docs/rendercv_output/`

### 7. View Your Generated CV

Find your CV in `marine-cv-docs/rendercv_output/`:
- `Your_Name_CV.pdf` — **Main PDF output** (publication-ready)
- `Your_Name_CV.html` — Web version (for online hosting)
- `Your_Name_CV.md` — Markdown format
- `Your_Name_CV.typ` — Typst source (for advanced editing)
- `Your_Name_CV_*.png` — Page images (for previews)

Open the PDF:
```bash
open marine-cv-docs/rendercv_output/Your_Name_CV.pdf  # macOS
xdg-open marine-cv-docs/rendercv_output/Your_Name_CV.pdf  # Linux
start marine-cv-docs\rendercv_output\Your_Name_CV.pdf  # Windows
```

## Complete Workflow Example

### From BibTeX to PDF (Step-by-Step)

```bash
# 1. Clone this repository
git clone https://github.com/yourusername/marine-cv.git
cd marine-cv

# 2. Install dependencies
pixi install

# 3. Add your BibTeX file
cp ~/my_publications.bib marine-cv-docs/my-publications.bib

# 4. (Optional) Configure group members
vim src/rendercv/bibtex_parser.py
# Edit DEFAULT_GROUP_MEMBERS list

# Add your Google Scholar ID to CV YAML
vim marine-cv-docs/my-publications.yaml
# Add GoogleScholar to social_networks (see step 3 above)

# 5. Fetch citation counts from Google Scholar
python scripts/fetch_citations.py

# 6. Generate publications YAML from BibTeX (with citations)
python scripts/generate_publications.py marine-cv-docs/my-publications.bib > temp_publications.yaml

# 7. Create your CV YAML (or copy the example)
cp marine-cv-docs/Marine_Denolle_CV.yaml marine-cv-docs/My_Name_CV.yaml
vim marine-cv-docs/My_Name_CV.yaml
# Edit personal info and paste publications from temp_publications.yaml

# 7. Render to PDF
pixi run python -m rendercv render marine-cv-docs/My_Name_CV.yaml

# 8. View your CV
open marine-cv-docs/rendercv_output/My_Name_CV.pdf
```

### Updating Your CV

**When adding new publications:**
```bash
# 1. Add new entries to your .bib file
vim marine-cv-docs/my-publications.bib

# 2. (Optional) Refresh citation counts
python scripts/fetch_citations.py --force-refresh

# 3. Regenerate publications YAML
python scripts/generate_publications.py marine-cv-docs/my-publications.bib > temp_publications.yaml

# 4. Copy updated publications section into your CV YAML
vim marine-cv-docs/My_Name_CV.yaml
# Replace the selected_publications section with content from temp_publications.yaml

# 5. Re-render CV
pixi run python -m rendercv render marine-cv-docs/My_Name_CV.yaml
```

**When updating other CV sections (employment, teaching, etc.):**
```bash
# 1. Edit YAML file directly
vim marine-cv-docs/My_Name_CV.yaml

# 2. Re-render CV
pixi run python -m rendercv render marine-cv-docs/My_Name_CV.yaml
```

**Adding media coverage to existing publications:**
```bash
# Option 1: Add to BibTeX note field
vim marine-cv-docs/my-publications.bib
# Add: note = {\url{https://news.article.url}}

# Option 2: Override in generate_publications.py
vim scripts/generate_publications.py
# Add URL to MEDIA_COVERAGE dict

# Then regenerate
python scripts/generate_publications.py marine-cv-docs/my-publications.bib > temp_publications.yaml
```

## Features

### Automatic Publication Management

- **Single source of truth**: All publications in one `.bib` file
- **Group member tracking**: Co-authors automatically tagged with asterisks (*)
- **Citation counts**: Automatic fetching from Google Scholar with monthly updates
- **DOI extraction**: Automatic URL generation from DOI field
- **Clean formatting**: LaTeX commands removed, special characters handled
- **Media coverage**: Automatically extract news article URLs from BibTeX `note` fields
- **Manual override**: Optional MEDIA_COVERAGE dict for custom links
- **Automated updates**: GitHub Actions workflow refreshes citations monthly

### Citation Count Features

- **Google Scholar integration**: Fetches citation counts using the `scholarly` library
- **Fuzzy title matching**: Automatically matches BibTeX entries to Scholar publications (85% threshold)
- **Caching system**: 30-day cache to minimize API requests
- **GitHub Actions**: Monthly automated updates via scheduled workflow
- **Non-invasive**: Only shows citations when data is available (no zeros)
- **Display format**: "Cited by 450" appears below publication URL

### GitHub & PyPI Statistics Tracking

- **Comprehensive metrics**: Tracks stars, forks, contributors across all repositories
- **Multi-account support**: Personal account + lab organizations (Denolle-Lab, noisepy, geo-smart, EarthML4PNW)
- **PyPI downloads**: Automatic download statistics for Python packages
- **Temporal trends**: CSV history file tracks growth over time
- **Auto-update CV**: Script automatically updates statistics in YAML file
- **Research impact summary**: Aggregate metrics displayed in CV header
- **Per-repository stats**: Individual software entries show current statistics
- **GitHub Actions**: Monthly automated refresh with built-in token (no setup required)

**Configuration:**
Edit `GITHUB_ACCOUNTS` in `scripts/fetch_github_stats.py` to add organizations:
```python
GITHUB_ACCOUNTS = {
    'users': ['your-username'],
    'orgs': ['your-lab', 'your-organization'],
}
```

Add PyPI packages to track:
```python
PYPI_PACKAGES = [
    'your-package',
    'another-package',
]
```

**Manual refresh:**
```bash
python scripts/fetch_github_stats.py --force-refresh
python scripts/update_cv_stats.py
```

**Files created:**
- `marine-cv-docs/github_stats_cache.json` - Latest snapshot (7-day cache)
- `marine-cv-docs/github_stats_history.csv` - Historical trends for analysis

## Troubleshooting

### Common Issues

**"There are errors in the input file"**
- Check YAML indentation (must use 2 spaces, not tabs)
- Ensure all section entries use valid field names:
  - BulletEntry: requires `bullet` field
  - OneLineEntry: requires `label` and `details` fields
  - See [Marine_Denolle_CV.yaml](marine-cv-docs/Marine_Denolle_CV.yaml) for examples

**Citation fetching issues:**
- Add Google Scholar ID to `social_networks` in your CV YAML file with `network: Google Scholar`
- Find your ID at: https://scholar.google.com/citations?user=YOUR_ID
- Check internet connection for API access
- Google Scholar may rate-limit: wait a few minutes and retry
- Install dependencies: `pip install scholarly fuzzywuzzy python-Levenshtein`
- Citations won't appear if cache doesn't exist or entry has 0 citations

**"No such file or directory"**
- Use correct relative paths from repository root
- BibTeX file: `marine-cv-docs/your-file.bib`
- CV YAML: `marine-cv-docs/Your_Name_CV.yaml`

**Publications not showing up**
- Ensure BibTeX entries have required fields: `author`, `title`, `year`, `journal`
- Check that citation keys are unique
- Verify you've copied the generated YAML into your CV file

**Media coverage not appearing**
- URLs in BibTeX must use `\url{https://...}` format in `note` field
- Check publication template includes `MEDIA_COVERAGE` placeholder
- Verify URLs are properly formatted (start with `http://` or `https://`)

**Group member asterisks not working**
- Edit `DEFAULT_GROUP_MEMBERS` in `src/rendercv/bibtex_parser.py`
- Names must match exactly as they appear in BibTeX author field
- Re-run `generate_publications.py` after editing group members

### RenderCV Core Features

From the [original RenderCV](https://github.com/rendercv/rendercv):

With RenderCV, you can:

### RenderCV Core Features

From the [original RenderCV](https://github.com/rendercv/rendercv):

- ✅ **Version-control your CV** — it's just text
- ✅ **Focus on content** — don't worry about the formatting
- ✅ **Get perfect typography** — pixel-perfect alignment and spacing, handled for you
- ✅ **JSON Schema support** — autocompletion and validation in VS Code
- ✅ **Multiple themes** — classic, moderncv, sb2nov, engineeringresumes, engineeringclassic
- ✅ **Extensive design options** — control every detail
- ✅ **Strict validation** — know exactly what's wrong and where
- ✅ **Multi-language support** — any language with locale settings

See example CVs from different themes:

| Classic | Moderncv | Sb2nov |
|---------|----------|---------|
| [![Classic](https://raw.githubusercontent.com/rendercv/rendercv/main/docs/assets/images/classic.png)](https://github.com/rendercv/rendercv/blob/main/examples/John_Doe_ClassicTheme_CV.pdf) | [![Moderncv](https://raw.githubusercontent.com/rendercv/rendercv/main/docs/assets/images/moderncv.png)](https://github.com/rendercv/rendercv/blob/main/examples/John_Doe_ModerncvTheme_CV.pdf) | [![Sb2nov](https://raw.githubusercontent.com/rendercv/rendercv/main/docs/assets/images/sb2nov.png)](https://github.com/rendercv/rendercv/blob/main/examples/John_Doe_Sb2novTheme_CV.pdf) |

## Documentation

- **[BIBTEX_INTEGRATION.md](BIBTEX_INTEGRATION.md)** — Complete guide to BibTeX workflow
- **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)** — Technical details of adaptations
- **[Original RenderCV Docs](https://docs.rendercv.com)** — Full RenderCV documentation
- **Example CV**: [Marine_Denolle_CV.yaml](marine-cv-docs/Marine_Denolle_CV.yaml) — 10-page academic CV

## File Structure

```
marine-cv/
├── README.md                       # This file
├── BIBTEX_INTEGRATION.md          # BibTeX workflow guide
├── IMPLEMENTATION_SUMMARY.md      # Technical documentation
├── pixi.toml                      # Environment configuration
├── environment.yml                # Conda environment
├── pyproject.toml                 # Python package metadata
├── marine-cv-docs/
│   ├── Marine_Denolle_CV.yaml    # Example CV (complete)
│   ├── denolle-pub.bib           # BibTeX publications (62 papers)
│   └── rendercv_output/          # Generated PDFs, PNGs, HTML
├── src/rendercv/
│   ├── bibtex_parser.py          # BibTeX parsing module (NEW)
│   └── [other rendercv modules]
└── scripts/
    └── generate_publications.py  # Publication YAML generator (NEW)
```

## Customization

### Change Colors and Fonts

Edit the `design` section at the top of your YAML:

```yaml
design:
  colors:
    name: rgb(128, 0, 0)          # Dark red
    section_titles: rgb(69, 128, 179)  # Blue
  typography:
    font_family:
      body: 'IBM Plex Serif'      # Serif font for body
      section_titles: 'IBM Plex Sans'  # Sans for headers
```

Available fonts: IBM Plex, Source Sans, Roboto, Latin Modern, and more (see [RenderCV font docs](https://docs.rendercv.com)).

### Add Group Members

Edit `src/rendercv/bibtex_parser.py`:

```python
DEFAULT_GROUP_MEMBERS = [
    'Your Name',
    'PhD Student 1',
    'PhD Student 2',
    'Postdoc Name',
    # Add all current and former group members
]
```

Publications co-authored with these people will be tagged with (*).

### Add Media Coverage

Edit `scripts/generate_publications.py`:

```python
MEDIA_COVERAGE = {
    'YourCitationKey2024': [
        'https://news.university.edu/your-research',
        'https://www.sciencemag.org/news/your-article',
    ],
}
```

## Dependencies

All dependencies managed by pixi or conda:

- **Python** ≥3.12
- **bibtexparser** ≥1.4.1 — BibTeX parsing
- **pydantic** ≥2.10.6 — Data validation
- **ruamel.yaml** ≥0.18 — YAML processing
- **jinja2** ≥3.1.6 — Templating
- **typst** ≥0.14.4 — PDF generation
- **rendercv** ≥2.6 — CV generation

## Troubleshooting

### "rendercv: command not found"
```bash
# Use pixi run
pixi run rendercv render Your_CV.yaml

# Or activate environment first
pixi shell
rendercv render Your_CV.yaml
```

### "BibTeX file not found"
Make sure to run scripts from repository root:
```bash
cd /path/to/marine-cv
python scripts/generate_publications.py
```

### "Group members not tagged"
Check that names in `DEFAULT_GROUP_MEMBERS` match BibTeX author names (case-insensitive last name matching).

### "YAML validation errors"
- Check indentation (2 spaces, not tabs)
- Ensure all required fields present (see schema)
- Use quotes for strings with special characters
- Verify date formats: `YYYY-MM` or `YYYY-MM-DD`

### "Design section duplicate"
Only include `design:` section once (at the top, before `cv:`).

## Contributing

This is a personal CV repository adapted from RenderCV. If you'd like to use this for your own CV:

1. Fork this repository
2. Update `marine-cv-docs/Marine_Denolle_CV.yaml` with your information
3. Update group members in `src/rendercv/bibtex_parser.py`
4. Add your `.bib` file
5. Render your CV!

For improvements to the core RenderCV engine, contribute to the [original repository](https://github.com/rendercv/rendercv).

## Credits and License

### Original RenderCV

This repository is based on [RenderCV](https://github.com/rendercv/rendercv) v2.6:

- **Author**: Sina Atalay ([@sinaatalay](https://github.com/sinaatalay))
- **Repository**: https://github.com/rendercv/rendercv
- **Documentation**: https://docs.rendercv.com
- **License**: MIT

RenderCV is an excellent open-source project. Please support the original author and star the [original repository](https://github.com/rendercv/rendercv)!

### Adaptations

BibTeX integration and academic enhancements by Marine Denolle.

**Additions**:
- `src/rendercv/bibtex_parser.py` — BibTeX parser with group member tagging
- `scripts/generate_publications.py` — Publication YAML generator
- Academic CV example with datasets, software, invited talks sections
- Integration documentation

### License

**RenderCV Core**: MIT License (see original repository)

**BibTeX Adaptations**: MIT License

```
Copyright (c) 2025 Marine Denolle (adaptations)
Copyright (c) 2024 Sina Atalay (original RenderCV)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Related Resources

- **Original RenderCV**: https://github.com/rendercv/rendercv
- **RenderCV Documentation**: https://docs.rendercv.com
- **Typst**: https://typst.app/ (the typesetting system used by RenderCV)
- **BibTeX**: https://www.bibtex.org/

## Support

For issues with:
- **RenderCV core features**: See [RenderCV issues](https://github.com/rendercv/rendercv/issues)
- **BibTeX integration**: Open an issue in this repository
- **General CV formatting**: See [RenderCV documentation](https://docs.rendercv.com)

---

**Example Output**: See [Marine_Denolle_CV.pdf](marine-cv-docs/rendercv_output/Marine_Denolle_CV.pdf) for a 10-page academic CV with 62 publications, teaching, datasets, software, and service sections.

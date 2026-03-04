# Academic CV Template — auto-updating, BibTeX-powered, open-science ready

Self-updating academic CV built with [RenderCV](https://github.com/rendercv/rendercv).
Write one YAML file per section, keep publications in a `.bib` file, and let GitHub
Actions render a fresh PDF every time you push.

**Live example:** Marine Denolle's CV ([PDF](marine-cv-docs/rendercv_output/Marine_Denolle_CV.pdf)) —
a 16-page academic CV maintained entirely through this system.

[![based on RenderCV](https://img.shields.io/badge/based%20on-RenderCV-blue)](https://github.com/rendercv/rendercv)
[![license MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## Why put your CV on GitHub?

For researchers who value open science and technical transparency, a versioned CV in a public repo will most efficiently save you time to adapt your CV for various requests. It will gather your research impact stats pulling Google Scholar citation and github metrics automatically. Each section in the CV is a separate YAML file for modular writing. This template was modified from render-cv and entirely vibe coded after with Claude Opus 4.6 and Sonnet 4.6 using VsCode CoPilot agentic tools.

---

## Quickstart

### Prerequisites

```bash
# Install pixi (cross-platform package manager)
curl -fsSL https://pixi.sh/install.sh | bash
```

(Or use the [Dockerfile](Dockerfile) for a pre-built environment.)

### 1. Fork and clone

```bash
git clone https://github.com/your-username/marine-cv.git
cd marine-cv
pixi install
```

Rename the repository!

### 2. Copy the template

```bash
cp -r template/ my-cv-docs/
mv my-cv-docs/Your_Name_CV.yaml my-cv-docs/Jane_Doe_CV.yaml
```

### 3. Edit your data

Each section is a separate YAML file — edit only what you need:

| File | What to put in it |
|---|---|
| `Your_Name_CV.yaml` | name, email, website, social links, section list |
| `employment.yaml` | positions, institutions, dates |
| `education.yaml` | degrees, advisor names |
| `your-publications.bib` | all publications (BibTeX) |

See [`marine-cv-docs/`](marine-cv-docs/) for a complete working example across
all section types (grants, talks, datasets, mentoring, etc.).

### 4. Configure group members and Google Scholar ID

**Author formatting** — edit `DEFAULT_GROUP_MEMBERS` in
`src/rendercv/bibtex_parser.py` so your mentees appear *italic* in author lists and your own name appears **bold**.

**Citation counts** — add your Scholar ID to `social_networks` in your CV YAML:

```yaml
social_networks:
  - network: Google Scholar
    username: YOUR_SCHOLAR_ID   # from scholar.google.com URL: ?user=YOUR_ID
```

### 5. Render

```bash
pixi run -- rendercv render my-cv-docs/Jane_Doe_CV.yaml
```

Your PDF is at `my-cv-docs/rendercv_output/Jane_Doe_CV.pdf`. Push to GitHub and
the `deploy-cv.yaml` workflow commits a fresh render automatically.

---

## Repository structure

```
marine-cv/
├── template/                   ← START HERE — copy and edit these files
│   ├── Your_Name_CV.yaml       ← main config (!include for each section)
│   ├── employment.yaml         ← employment section stub
│   ├── education.yaml          ← education section stub
│   └── your-publications.bib  ← example BibTeX entries
│
├── marine-cv-docs/             ← live working example (Marine Denolle's CV)
│   ├── Marine_Denolle_CV.yaml  ← main config
│   ├── *.yaml                  ← one file per CV section
│   ├── denolle-pub.bib         ← 66 publications
│   └── rendercv_output/        ← rendered PDF/HTML (auto-committed by CI)
│
├── scripts/                    ← automation (run by GitHub Actions)
│   ├── generate_publications.py     ← BibTeX → publications_section.yaml
│   ├── fetch_citations.py           ← Google Scholar h-index + citation counts
│   ├── fetch_github_stats.py        ← GitHub/PyPI metrics
│   ├── fetch_youtube_stats.py       ← YouTube channel stats
│   ├── update_cv_stats.py           ← writes research_impact_summary.yaml
│   └── calculate_grant_totals.py    ← Lead PI vs Co-PI totals
│
├── src/rendercv/               ← RenderCV library + custom BibTeX parser
│   └── bibtex_parser.py        ← edit DEFAULT_GROUP_MEMBERS here
│
├── .github/workflows/          ← 5 targeted GitHub Actions (see below)
├── tests/                      ← CI tests for publication generation
└── Dockerfile                  ← known-working build environment
```

---

## Publications from BibTeX

Keep all publications in a `.bib` file and generate the formatted section:

```bash
python scripts/generate_publications.py > my-cv-docs/publications_section.yaml
```

Then reference it in your CV YAML:

```yaml
sections:
  publications: !include publications_section.yaml
```

**What the generator does:**

- APA-style author lists with **bold PI** and *italic mentees*
- Extracts DOIs → `https://doi.org/` links
- Pulls media coverage URLs from BibTeX `note` fields (`\url{https://...}`)
- Adds Google Scholar citation counts from cache
- Skips placeholder `doi: XX` for in-review papers

**Media coverage in BibTeX:**

```bibtex
@article{Your2024,
  ...
  note = {\url{https://news.university.edu/press-release}},
}
```

---

## Research impact summary

The first section of the CV auto-computes 6 metrics from local data files:

| Row | Source |
|---|---|
| Research Citations | `citation_cache.json` (Google Scholar) |
| Publications | `publications_section.yaml` (T1/T2/T3 tier counts) |
| Research Funding | `grant_support.yaml` (Lead PI vs Co-PI totals) |
| Open-Source Software | `github_stats_cache.json` + PyPI |
| Mentoring | `phd_advisees.yaml`, `postdocs.yaml`, `undergraduate_students.yaml` |
| Broader Impact | `training_schools.yaml` + YouTube stats |

Regenerate at any time:

```bash
python scripts/update_cv_stats.py
```

---

## GitHub Actions (5 workflows)

No library tests, no PyPI publishing, no executable builds.

| Workflow | Trigger | What it does |
|---|---|---|
| `deploy-cv.yaml` | push to `marine-cv-docs/**` or manual | Renders CV, commits PDF/HTML |
| `validate-publications.yml` | push to `.bib` or scripts | Regenerates + validates YAML, auto-commits |
| `update-citations.yml` | 1st of month @ 2:00 UTC | Fetches Google Scholar metrics |
| `update-stats.yml` | 1st of month @ 3:00 UTC | Fetches GitHub/PyPI/YouTube stats |
| `calculate-grants.yml` | push to `grant_support.yaml` | Computes grant totals |

**One optional secret:** add `YOUTUBE_API_KEY` in Settings → Secrets → Actions
to enable YouTube stats. Everything else uses the built-in `GITHUB_TOKEN`.

The automated chain each month:

```
1st @ 2:00 UTC  →  citation_cache.json updated
1st @ 3:00 UTC  →  research_impact_summary.yaml updated
                   (triggers deploy-cv.yaml)
                →  rendercv_output/ updated with fresh PDF
```

---

## Customization reference

**Theme and colors** — edit the `design:` block in your CV YAML:

```yaml
design:
  theme: moderncv   # classic | moderncv | sb2nov | engineeringresumes
  colors:
    name: rgb(128, 0, 0)
    section_titles: rgb(69, 128, 179)
```

**Add or remove sections** — each `!include` line in your CV YAML is one
section; delete or reorder to taste.

**Publication display template** — customize the layout per-entry:

```yaml
design:
  templates:
    publication_entry:
      main_column: "AUTHORS (DATE). **TITLE**. JOURNAL_WITH_DOI\nMEDIA_COVERAGE"
```

**BibTeX author bold/italic** — edit `DEFAULT_GROUP_MEMBERS` in
`src/rendercv/bibtex_parser.py`. Your PI name is matched automatically.

---

## Troubleshooting

**`rendercv: command not found`**
→ Use `pixi run -- rendercv render ...`

**YAML indentation errors**
→ Use 2 spaces, never tabs. Quote strings containing `:` or `#`.

**Citations not appearing**
→ Run `python scripts/fetch_citations.py` first.
Scholar may rate-limit — wait a few minutes and retry with `--force-refresh`.

**Publications YAML invalid**
→ Run `python scripts/generate_publications.py` locally and check stderr for
the full traceback.

**`url: https://doi.org/XX` appears for in-review papers**
→ This is filtered automatically. Re-run `generate_publications.py` if you see
placeholder URLs in the output.

---

## Acknowledgements

Built on [RenderCV](https://github.com/rendercv/rendercv) by
[Sina Atalay](https://github.com/sinaatalay) (MIT license).
RenderCV handles YAML → Typst → PDF; this repository adds BibTeX integration,
automated data pipelines, and a personal-CV-ready GitHub Actions setup.

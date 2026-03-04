#!/usr/bin/env python3
"""Update research_impact_summary.yaml and software highlights from all data caches.

Computes all impact metrics from YAML files and cache JSONs:
  - Citation metrics from citation_cache.json
  - Publication tier counts from publications_section.yaml
  - Grant totals from grant_support.yaml
  - GitHub/PyPI stats from github_stats_cache.json
  - YouTube stats from youtube_stats_cache.json
  - Mentoring metrics from phd_advisees.yaml / postdocs.yaml / undergrad yaml
  - Workshop reach from training_schools.yaml

Usage:
    python scripts/update_cv_stats.py
"""

import json
import re
import sys
from pathlib import Path

try:
    from ruamel.yaml import YAML
except ImportError:
    print("Error: ruamel.yaml not installed. Run: pip install ruamel.yaml", file=sys.stderr)
    sys.exit(1)

# ==============================================================================
# PATHS
# ==============================================================================

BASE = Path(__file__).parent.parent / "marine-cv-docs"
SCRIPTS_DIR = Path(__file__).parent

SUMMARY_YAML = BASE / "research_impact_summary.yaml"
CV_YAML_FILE = BASE / "Marine_Denolle_CV.yaml"
CITATION_CACHE = BASE / "citation_cache.json"
GITHUB_CACHE = BASE / "github_stats_cache.json"
YOUTUBE_CACHE = BASE / "youtube_stats_cache.json"
PUBS_YAML = BASE / "publications_section.yaml"
GRANTS_YAML = BASE / "grant_support.yaml"
PHD_YAML = BASE / "phd_advisees.yaml"
POSTDOCS_YAML = BASE / "postdocs.yaml"
UNDERGRAD_YAML = BASE / "undergraduate_students.yaml"
OTHER_GRAD_YAML = BASE / "other_graduate_student_supervision.yaml"
TRAINING_YAML = BASE / "training_schools.yaml"
SOFTWARE_YAML = BASE / "software.yaml"

# Journal tier classification
T1_JOURNALS = {
    "nature", "science", "pnas", "proceedings of the national academy",
    "nature communications", "nature geoscience", "science advances",
    "nature physics", "nature methods", "communications earth",
    "communications earth & environment",
}
T2_JOURNALS = {
    "geophysical research letters", "grl",
    "journal of geophysical research", "jgr",
    "agu advances",
    "bulletin of the seismological society", "bssa",
    "seismological research letters", "srl",
    "earth and planetary science letters", "epsl",
    "journal of geophysical research: solid earth",
    "journal of geophysical research: oceans",
    "journal of geophysical research: earth surface",
    "reviews of geophysics",
}
REVIEW_KEYWORDS = {"review", "progress", "annual review"}
PREPRINT_KEYWORDS = {"arxiv", "essoar", "eartharxiv", "preprint", "biorxiv"}

# GitHub repo map for software highlights
REPO_MAP = {
    "NoisePy": "noisepy/NoisePy",
    "Machine Learning in the Geosciences Textbook": "geo-smart/mlgeo-book",
}


# ==============================================================================
# HELPERS
# ==============================================================================

def _load_yaml(path: Path):
    yaml = YAML()
    yaml.preserve_quotes = True
    with open(path) as f:
        return yaml.load(f)


def _load_json(path: Path):
    if not path.exists():
        return {}
    with open(path) as f:
        return json.load(f)


# ==============================================================================
# METRIC FUNCTIONS
# ==============================================================================

def load_citation_metrics():
    """Read total/h/i10 from citation_cache.json."""
    data = _load_json(CITATION_CACHE)
    m = data.get("metrics", {})
    return {
        "total": m.get("total_citations", 0),
        "h": m.get("h_index", 0),
        "i10": m.get("i10_index", 0),
        "total_5y": m.get("total_citations_5y", 0),
        "h_5y": m.get("h_index_5y", 0),
        "i10_5y": m.get("i10_index_5y", 0),
    }


def load_publication_tiers():
    """Count T1/T2/T3/review/preprint publications from publications_section.yaml."""
    if not PUBS_YAML.exists():
        return {"t1": 0, "t2": 0, "t3": 0, "review": 0, "preprint": 0, "total": 0}

    entries = _load_yaml(PUBS_YAML)
    counts = {"t1": 0, "t2": 0, "t3": 0, "review": 0, "preprint": 0}
    total = 0

    for entry in entries:
        # Each publication_entry has a 'journal' or embedded in the main_column
        # We look at the 'journal' field or fall back to parsing the entry text
        journal_raw = ""
        if isinstance(entry, dict):
            journal_raw = str(entry.get("journal", "")).lower()
            if not journal_raw:
                # Try to extract from highlights or other fields
                journal_raw = str(entry.get("highlights", "")).lower()
        if not journal_raw:
            continue

        total += 1
        is_preprint = any(kw in journal_raw for kw in PREPRINT_KEYWORDS)
        is_review = any(kw in journal_raw for kw in REVIEW_KEYWORDS)
        is_t1 = any(kw in journal_raw for kw in T1_JOURNALS)
        is_t2 = any(kw in journal_raw for kw in T2_JOURNALS)

        if is_preprint:
            counts["preprint"] += 1
        elif is_review:
            counts["review"] += 1
        elif is_t1:
            counts["t1"] += 1
        elif is_t2:
            counts["t2"] += 1
        else:
            counts["t3"] += 1

    # If journal field not present, fall back to header comment count
    if total == 0:
        # Read comment line count from YAML header
        with open(PUBS_YAML) as f:
            first_lines = "".join(f.readline() for _ in range(5))
        m = re.search(r"(\d+)\s+publications", first_lines)
        if m:
            total = int(m.group(1))
            counts["t3"] = total  # conservative fallback

    counts["total"] = total
    return counts


def parse_grant_totals():
    """Parse grant_support.yaml into lead_pi / co_pi / fellowship buckets."""
    if not GRANTS_YAML.exists():
        return {
            "lead_pi": {"total": 0, "count": 0},
            "co_pi": {"total": 0, "count": 0},
            "fellowship": {"total": 0, "count": 0},
        }

    entries = _load_yaml(GRANTS_YAML)
    buckets = {
        "lead_pi": {"total": 0, "count": 0},
        "co_pi": {"total": 0, "count": 0},
        "fellowship": {"total": 0, "count": 0},
    }

    for entry in entries:
        if not isinstance(entry, dict):
            continue
        area = str(entry.get("area", "")).lower()
        # Skip returned/no-cost grants
        if "returned" in area or "no-cost" in area:
            continue
        # Extract dollar amount
        matches = re.findall(r"\$([\d,]+)", area)
        if not matches:
            continue
        amount = int(matches[0].replace(",", ""))

        # Determine role
        if "fellowship" in area:
            bucket = "fellowship"
        elif "co-pi" in area or "co-i" in area or "co_pi" in area:
            # Only count Denolle's share if specified: "to uw" or "denolle co-pi"
            uw_match = re.search(r"\$([\d,]+)\s+to\s+uw", area)
            if uw_match:
                amount = int(uw_match.group(1).replace(",", ""))
            bucket = "co_pi"
        else:
            bucket = "lead_pi"

        buckets[bucket]["total"] += amount
        buckets[bucket]["count"] += 1

    return buckets


def load_github_stats():
    """Read aggregate + featured repo stats from github_stats_cache.json."""
    data = _load_json(GITHUB_CACHE)
    gh = data.get("github", {})
    pypi = data.get("pypi", {})
    agg = gh.get("aggregate", {})
    featured = gh.get("featured_repos", {})
    return {
        "stars": agg.get("total_stars", 0),
        "forks": agg.get("total_forks", 0),
        "active_repos": agg.get("active_repos", 0),
        "featured": featured,
        "pypi_monthly": pypi.get("noisepy", {}).get("last_month", 0),
    }


def load_youtube_stats():
    """Read aggregated YouTube stats from youtube_stats_cache.json."""
    data = _load_json(YOUTUBE_CACHE)
    if "aggregate" in data:
        agg = data["aggregate"]
        return {
            "views": agg.get("total_view_count", 0),
            "subscribers": agg.get("total_subscriber_count", 0),
            "videos": agg.get("total_video_count", 0),
        }
    # Sum across channels if no aggregate key
    total_views = 0
    total_subs = 0
    total_vids = 0
    for key, val in data.items():
        if isinstance(val, dict) and "view_count" in val:
            total_views += int(val.get("view_count", 0))
            total_subs += int(val.get("subscriber_count", 0))
            total_vids += int(val.get("video_count", 0))
    return {"views": total_views, "subscribers": total_subs, "videos": total_vids}


def _count_entries(path: Path, skip_labels=None):
    """Count list entries in a YAML file, skipping label-only entries."""
    if not path.exists():
        return 0
    entries = _load_yaml(path)
    count = 0
    for e in entries:
        if not isinstance(e, dict):
            continue
        # Skip header/note entries that have only a label field
        if "label" in e and len(e) <= 2 and skip_labels:
            label_lower = str(e.get("label", "")).lower()
            if any(s in label_lower for s in skip_labels):
                continue
        # For experience-like entries, count those with a position/name field
        if "position" in e or "name" in e or "label" in e:
            count += 1
    return count


def _count_faculty_placements(path: Path):
    """Count people who went on to faculty positions from their highlights/summary."""
    if not path.exists():
        return 0
    entries = _load_yaml(path)
    faculty_keywords = ["professor", "faculty", "asst. prof", "assistant prof",
                        "associate prof", "lecturer", "research scientist"]
    count = 0
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        text_parts = [
            str(entry.get("summary", "")),
            str(entry.get("highlights", "")),
        ]
        combined = " ".join(text_parts).lower()
        if any(kw in combined for kw in faculty_keywords):
            count += 1
    return count


def count_phd_metrics():
    """Count PhD advisees (total, current, graduated) and faculty placements."""
    if not PHD_YAML.exists():
        return {"total": 0, "current": 0, "graduated": 0, "faculty": 0}
    entries = _load_yaml(PHD_YAML)
    total, current, graduated, faculty = 0, 0, 0, 0
    faculty_keywords = ["professor", "faculty", "asst. prof", "assistant prof",
                        "associate prof", "lecturer", "research scientist",
                        "postdoctoral fellow at", "postdoc at"]
    for entry in entries:
        if not isinstance(entry, dict) or "position" not in entry:
            continue
        total += 1
        company = str(entry.get("company", "")).lower()
        date = str(entry.get("date", ""))
        summary = str(entry.get("summary", "")).lower()
        highlights_raw = entry.get("highlights", [])
        highlights = " ".join(str(h) for h in highlights_raw).lower() if highlights_raw else ""
        combined = company + " " + summary + " " + highlights

        if "present" in date.lower() or "candidate" in company or "pre-candidate" in company:
            current += 1
        else:
            graduated += 1

        if any(kw in combined for kw in faculty_keywords):
            faculty += 1

    return {"total": total, "current": current, "graduated": graduated, "faculty": faculty}


def count_postdoc_metrics():
    """Count postdoctoral researchers and faculty placements."""
    if not POSTDOCS_YAML.exists():
        return {"total": 0, "faculty": 0}
    entries = _load_yaml(POSTDOCS_YAML)
    total, faculty = 0, 0
    faculty_keywords = ["professor", "faculty", "asst. prof", "assistant prof",
                        "associate prof", "lecturer", "research scientist"]
    for entry in entries:
        if not isinstance(entry, dict) or "position" not in entry:
            continue
        total += 1
        combined = (
            str(entry.get("summary", ""))
            + " "
            + " ".join(str(h) for h in entry.get("highlights", []))
        ).lower()
        if any(kw in combined for kw in faculty_keywords):
            faculty += 1
    return {"total": total, "faculty": faculty}


def count_undergrad_metrics():
    """Count undergraduate advisees (skip note/header entries)."""
    skip = ["note", "advising context", "legend", "current", "graduated", "alumni"]
    return _count_entries(UNDERGRAD_YAML, skip_labels=skip)


def count_other_grad_metrics():
    """Count co-supervised graduate students."""
    if not OTHER_GRAD_YAML.exists():
        return 0
    entries = _load_yaml(OTHER_GRAD_YAML)
    count = 0
    for e in entries:
        if isinstance(e, dict) and ("position" in e or ("label" in e and "note" not in str(e.get("label", "")).lower())):
            count += 1
    return count


def count_workshop_metrics():
    """Count workshops and total participants from training_schools.yaml."""
    if not TRAINING_YAML.exists():
        return {"workshops": 0, "participants": 0}
    entries = _load_yaml(TRAINING_YAML)
    workshops = 0
    participants = 0
    for entry in entries:
        if not isinstance(entry, dict) or "name" not in entry:
            continue
        workshops += 1
        summary = str(entry.get("summary", ""))
        m = re.search(r"(\d+)\s+participants", summary, re.IGNORECASE)
        if m:
            participants += int(m.group(1))
    return {"workshops": workshops, "participants": participants}


# ==============================================================================
# SUMMARY BUILDER
# ==============================================================================

def build_summary():
    """Compute all metrics and return list of OneLineEntry dicts."""
    print("Loading citation metrics...", flush=True)
    cit = load_citation_metrics()

    print("Loading publication tiers...", flush=True)
    pubs = load_publication_tiers()

    print("Parsing grant totals...", flush=True)
    grants = parse_grant_totals()

    print("Loading GitHub/PyPI stats...", flush=True)
    gh = load_github_stats()

    print("Loading YouTube stats...", flush=True)
    yt = load_youtube_stats()

    print("Counting mentoring metrics...", flush=True)
    phd = count_phd_metrics()
    postdoc = count_postdoc_metrics()
    undergrad = count_undergrad_metrics()
    other_grad = count_other_grad_metrics()
    workshops = count_workshop_metrics()

    # 1. Research Citations
    cit_line = (
        f"{cit['total']:,} total (h-index: {cit['h']}, i10: {cit['i10']}) | "
        f"{cit['total_5y']:,} last-5y (h\u2085: {cit['h_5y']}, i10\u2085: {cit['i10_5y']}) | "
        f"Google Scholar"
    )

    # 2. Publications
    pub_total = pubs.get("total", 0)
    t1 = pubs.get("t1", 0)
    t2 = pubs.get("t2", 0)
    t3 = pubs.get("t3", 0)
    rev = pubs.get("review", 0)
    pre = pubs.get("preprint", 0)
    if pub_total == 0:
        pub_line = "Publications data unavailable"
    else:
        pub_parts = [f"{pub_total} peer-reviewed"]
        if t1:
            pub_parts.append(f"{t1} Nature/Science-family (T1)")
        if t2:
            pub_parts.append(f"{t2} AGU-flagship (T2)")
        if t3:
            pub_parts.append(f"{t3} domain journals (T3)")
        if rev:
            pub_parts.append(f"{rev} reviews/perspectives")
        if pre:
            pub_parts.append(f"{pre} preprints")
        pub_line = " | ".join(pub_parts)

    # 3. Research Funding
    lp_total = grants["lead_pi"]["total"]
    lp_count = grants["lead_pi"]["count"]
    cp_total = grants["co_pi"]["total"]
    cp_count = grants["co_pi"]["count"]
    fl_total = grants["fellowship"]["total"]
    fl_count = grants["fellowship"]["count"]

    def fmt_dollars(v):
        if v >= 1_000_000:
            return f"${v / 1_000_000:.1f}M"
        elif v >= 1000:
            return f"${v / 1000:.0f}K"
        return f"${v:,}"

    grant_parts = []
    if lp_count:
        grant_parts.append(f"Lead PI: {fmt_dollars(lp_total)} ({lp_count} grants)")
    if cp_count:
        grant_parts.append(f"Co-PI/Co-I: {fmt_dollars(cp_total)} ({cp_count} grants)")
    if fl_count:
        grant_parts.append(f"Fellowships: {fmt_dollars(fl_total)} ({fl_count})")
    grant_line = " | ".join(grant_parts) if grant_parts else "See grant list"

    # 4. Open-Source Software
    stars = gh["stars"]
    forks = gh["forks"]
    active = gh["active_repos"]
    featured = gh["featured"]
    pypi_mo = gh["pypi_monthly"]
    np_repo = featured.get("noisepy/NoisePy", {})
    np_stars = np_repo.get("stars", 207)
    np_forks = np_repo.get("forks", 83)
    np_contrib = np_repo.get("contributors", 19)
    pypi_annual = pypi_mo * 12

    oss_parts = [
        f"{stars} GitHub stars | {forks} forks | {active} active repos",
        f"NoisePy: {np_stars} stars, {np_forks} forks, {np_contrib} contributors",
    ]
    if pypi_annual:
        oss_parts.append(f"{pypi_annual:,}+ PyPI downloads/yr")
    oss_line = " | ".join(oss_parts)

    # 5. Mentoring
    total_faculty = phd["faculty"] + postdoc["faculty"]
    mentoring_parts = [
        f"{phd['total']} PhD ({phd['current']} current, {phd['graduated']} graduated)",
        f"{postdoc['total']} postdocs",
        f"{undergrad}+ undergrads",
    ]
    if other_grad:
        mentoring_parts.append(f"{other_grad} co-supervised grad students")
    if total_faculty:
        mentoring_parts.append(f"{total_faculty} became faculty")
    mentoring_line = " | ".join(mentoring_parts)

    # 6. Mentoring Reach / Broader Impact
    reach_parts = []
    wk = workshops["workshops"]
    part = workshops["participants"]
    if wk:
        reach_parts.append(f"{wk} workshops, {part}+ seismologists trained")
    mlgeo = featured.get("geo-smart/mlgeo-book", {})
    mlgeo_stars = mlgeo.get("stars", 0)
    if mlgeo_stars:
        reach_parts.append(f"mlgeo-book: {mlgeo_stars} GitHub stars")
    if yt["views"]:
        reach_parts.append(f"YouTube: {yt['views']:,} views ({yt['videos']} videos)")
    elif yt["videos"]:
        reach_parts.append(f"YouTube: {yt['videos']} videos")
    reach_line = " | ".join(reach_parts) if reach_parts else "Workshops and outreach"

    return [
        {"label": "Research Citations", "details": cit_line},
        {"label": "Publications", "details": pub_line},
        {"label": "Research Funding", "details": grant_line},
        {"label": "Open-Source Software", "details": oss_line},
        {"label": "Mentoring", "details": mentoring_line},
        {"label": "Broader Impact", "details": reach_line},
    ]


# ==============================================================================
# SOFTWARE HIGHLIGHTS UPDATE (preserved from original script)
# ==============================================================================

def update_software_highlights(gh):
    """Update software.yaml highlights with live GitHub/PyPI stats."""
    if not SOFTWARE_YAML.exists():
        return
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096

    with open(SOFTWARE_YAML) as f:
        software = yaml.load(f)

    if not isinstance(software, list):
        return

    featured = gh["featured"]
    changed = False
    for entry in software:
        entry_name = entry.get("name", "")
        if entry_name not in REPO_MAP:
            continue
        repo_key = REPO_MAP[entry_name]
        if repo_key not in featured:
            continue
        repo = featured[repo_key]

        pypi_monthly = gh["pypi_monthly"] if entry_name == "NoisePy" else 0
        stats_line = (
            f"{repo['stars']} GitHub stars, {repo['forks']} forks, "
            f"{repo['contributors']} contributors"
        )

        highlights = entry.get("highlights", [])
        if not highlights:
            continue

        if "stars" in str(highlights[0]) or "forks" in str(highlights[0]):
            highlights[0] = stats_line
        else:
            highlights.insert(0, stats_line)

        if pypi_monthly and len(highlights) > 1:
            pypi_line = f"{pypi_monthly} PyPI downloads/month"
            if "PyPI downloads" in str(highlights[1]):
                highlights[1] = pypi_line
            else:
                highlights.insert(1, pypi_line)

        changed = True
        print(f"  ✓ Updated highlights for {entry_name}")

    if changed:
        with open(SOFTWARE_YAML, "w") as f:
            yaml.dump(software, f)
        print(f"✓ Saved {SOFTWARE_YAML.name}")


# ==============================================================================
# MAIN
# ==============================================================================

def main():
    """Compute all metrics and write research_impact_summary.yaml."""
    print("=" * 60)
    print("update_cv_stats.py — computing research impact metrics")
    print("=" * 60)

    rows = build_summary()

    # Write YAML (plain array, no section key — required for !include)
    yaml = YAML()
    yaml.default_flow_style = False
    yaml.width = 200

    with open(SUMMARY_YAML, "w") as f:
        f.write("# AUTO-GENERATED by scripts/update_cv_stats.py — do not edit manually\n")
        yaml.dump(rows, f)

    print(f"\n✓ Wrote {len(rows)} rows to {SUMMARY_YAML.name}")

    # Also update software highlights
    print("\nUpdating software highlights...")
    gh = load_github_stats()
    update_software_highlights(gh)

    print("\n✓ Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

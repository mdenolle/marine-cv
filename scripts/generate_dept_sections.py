#!/usr/bin/env python3
"""Generate department CV sections: reverse-chron sorted, with [RECENT] markers.

The UW College of Environment requires CV items to be listed in reverse
chronological order (most recent first) with items active or completed
in the last 3 years highlighted.  This script:

  1. Reads each source YAML section file from marine-cv-docs/
  2. Sorts entries in strict reverse chronological order (by start year)
  3. Prepends [RECENT] to the primary display field of entries that are
     active (end_date: present) or completed on/after --since-year
  4. Writes processed copies to marine-cv-docs/dept_cv_sections/

Usage:
    python scripts/generate_dept_sections.py
    python scripts/generate_dept_sections.py --since-year 2023
    python scripts/generate_dept_sections.py --cv-dir /path/to/dir
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Optional

import yaml


# ---------------------------------------------------------------------------
# Paths / constants
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).parent
CV_DIR = SCRIPT_DIR.parent / "marine-cv-docs"
DEFAULT_SINCE_YEAR = 2023
MARKER = "[RECENT]"

# (filename, copy_verbatim)
# copy_verbatim=True → file is written unchanged (no sort, no markers)
SECTIONS: list[tuple[str, bool]] = [
    ("research_impact_summary.yaml",             True),  # aggregate summary
    ("education.yaml",                           False),
    ("employment.yaml",                          False),
    ("awards.yaml",                              False),
    ("teaching.yaml",                            False),
    ("phd_advisees.yaml",                        False),
    ("postdocs.yaml",                            False),
    ("other_graduate_student_supervision.yaml",  False),
    ("graduate_student_committees.yaml",         False),
    ("international_phd_dissertation_readers.yaml", False),
    ("undergraduate_students.yaml",              False),
    ("training_schools.yaml",                    False),
    ("university_service.yaml",                  False),
    ("committee_service.yaml",                   False),
    ("review_panels.yaml",                       False),
    ("editorial_service.yaml",                   False),
    ("publications_section.yaml",                False),
    ("grant_support.yaml",                       False),
    ("research_products.yaml",                   False),
    ("invited_talks.yaml",                       False),
]


# ---------------------------------------------------------------------------
# Date helpers
# ---------------------------------------------------------------------------

def _years_in(s: str) -> list[int]:
    """Return all 4-digit years (1900–2099) found in a string."""
    return [int(y) for y in re.findall(r'\b((?:19|20)\d{2})\b', str(s))]


def _sort_key(entry: dict) -> int:
    """Return a year-based sort key used for descending (reverse-chron) sort.

    Strategy: use the START year of the entry so that a position spanning
    2021–present sorts after a position spanning 2024–present.  Current
    positions naturally have recent start years and will appear near the top.
    """
    # Explicit start_date (ExperienceEntry / some EducationEntry)
    if "start_date" in entry:
        years = _years_in(str(entry["start_date"]))
        if years:
            return years[0]

    # Bare date field: "2026", "2022 - 2024", "2020,2024", "2026-01"
    if "date" in entry:
        years = _years_in(str(entry["date"]))
        if years:
            return years[0]

    # OneLineEntry: date embedded in details text ("2021-present", "2023-2026")
    if "details" in entry:
        years = _years_in(str(entry["details"]))
        if years:
            return years[0]

    return 0  # unknown date → sort to end


def _is_recent(entry: dict, since_year: int) -> bool:
    """Return True if the entry is active or completed on/after since_year."""
    # Explicit "present" in end_date or date → always recent
    for field in ("end_date", "date"):
        if "present" in str(entry.get(field, "")).lower():
            return True

    # Any year >= since_year in numeric date fields
    for field in ("start_date", "end_date", "date"):
        val = entry.get(field)
        if val is not None:
            if any(y >= since_year for y in _years_in(str(val))):
                return True

    # OneLineEntry: check details text
    details = str(entry.get("details", ""))
    if "present" in details.lower():
        return True
    if any(y >= since_year for y in _years_in(details)):
        return True

    return False


# ---------------------------------------------------------------------------
# Entry introspection
# ---------------------------------------------------------------------------

def _primary_field(entry: dict) -> Optional[str]:
    """Return the key of the primary human-visible display field.

    Field priority mirrors RenderCV entry type detection:
      PublicationEntry → title (unless '__HIDDEN__' hack used by training_schools)
      ExperienceEntry  → position
      EducationEntry   → institution
      OneLineEntry     → label
      training_schools hack → name (when title == '__HIDDEN__')
      BulletEntry      → bullet
    """
    title = str(entry.get("title", ""))
    if "title" in entry and title not in ("__HIDDEN__", ""):
        return "title"
    if "position" in entry:
        return "position"
    if "institution" in entry:
        return "institution"
    if "label" in entry:
        return "label"
    if "name" in entry:
        return "name"   # training_schools with title == '__HIDDEN__'
    if "bullet" in entry:
        return "bullet"
    return None


def _is_header_note(entry: dict) -> bool:
    """Return True for informational header entries (label: Note / Notes).

    These are kept at the top of their section regardless of sort order
    and never receive the [RECENT] marker.
    """
    return str(entry.get("label", "")).strip().lower() in ("note", "notes")


def _mark_recent(entry: dict) -> dict:
    """Return entry unchanged for recent items.

    Department format now relies on left-sidebar dates for recency context,
    so no text prefix or extra metadata fields are injected.
    """
    return dict(entry)


# ---------------------------------------------------------------------------
# Core processing
# ---------------------------------------------------------------------------

def _drop_nulls(entry: dict) -> dict:
    """Return a copy of entry with None-valued keys removed."""
    return {k: v for k, v in entry.items() if v is not None}


def process_section(entries: list[dict], since_year: int) -> list[dict]:
    """Sort entries in reverse chronological order and add [RECENT] markers."""
    # Separate sticky header notes from sortable items
    headers = [e for e in entries if _is_header_note(e)]
    items   = [e for e in entries if not _is_header_note(e)]

    # Stable sort: equal-year entries preserve original relative order
    items_sorted = sorted(items, key=_sort_key, reverse=True)

    annotated = []
    for entry in items_sorted:
        e = _drop_nulls(dict(entry))
        if _is_recent(e, since_year):
            e = _mark_recent(e)
        annotated.append(e)

    return [_drop_nulls(h) for h in headers] + annotated


# ---------------------------------------------------------------------------
# YAML I/O
# ---------------------------------------------------------------------------

class _NoAliasDumper(yaml.Dumper):
    """Dumper that never emits YAML anchors/aliases."""
    def ignore_aliases(self, data: object) -> bool:
        return True


def _load_yaml(path: Path) -> list[dict]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or []


def _dump_yaml(data: list[dict], path: Path, since_year: int) -> None:
    header_comment = (
        "# AUTO-GENERATED by scripts/generate_dept_sections.py — do not edit manually\n"
        f"# Sorted reverse-chronologically; active/completed since {since_year} are not text-labeled\n"
    )
    body = yaml.dump(
        data,
        Dumper=_NoAliasDumper,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=10000,
    )
    path.write_text(header_comment + body, encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate dept CV sections (reverse-chron + [RECENT] markers)."
    )
    parser.add_argument(
        "--since-year", type=int, default=DEFAULT_SINCE_YEAR,
        help=f"Mark items active or completed since this year (default: {DEFAULT_SINCE_YEAR})",
    )
    parser.add_argument(
        "--cv-dir", type=Path, default=CV_DIR,
        help="Directory containing source YAML section files",
    )
    args = parser.parse_args()

    src_dir: Path = args.cv_dir
    out_dir: Path = src_dir / "dept_cv_sections"
    since: int = args.since_year

    out_dir.mkdir(exist_ok=True)
    print(f"Source : {src_dir}")
    print(f"Output : {out_dir}")
    print(f"[RECENT] threshold: {since}+\n")

    errors = 0
    for filename, copy_only in SECTIONS:
        src = src_dir / filename
        if not src.exists():
            print(f"  SKIP  {filename}  (file not found)")
            continue

        entries = _load_yaml(src)
        if not isinstance(entries, list):
            print(f"  SKIP  {filename}  (not a YAML list)")
            continue

        if copy_only:
            processed = entries
            tag = "copied verbatim"
        else:
            processed = process_section(entries, since)
            n_recent = sum(
                1 for e in processed
                if any(
                    str(e.get(f, "")).startswith(MARKER)
                    for f in ("title", "position", "institution", "label", "name", "bullet")
                )
            )
            tag = f"{n_recent}/{len(processed)} marked {MARKER}"

        try:
            _dump_yaml(processed, out_dir / filename, since)
            print(f"  OK    {filename}  ({tag})")
        except Exception as exc:
            print(f"  ERROR {filename}  {exc}", file=sys.stderr)
            errors += 1

    print(f"\nDone — {len(SECTIONS)} sections processed, {errors} errors.")
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

pytest.importorskip("ruamel.yaml")

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = REPO_ROOT / "scripts" / "update_cv_citations.py"

_spec = importlib.util.spec_from_file_location("update_cv_citations", SCRIPT_PATH)
update_cv_citations = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(update_cv_citations)
format_citation_details = update_cv_citations.format_citation_details

OPENALEX = {
    "openalex_total_citations": 3394,
    "openalex_h_index": 26,
    "i10_index": 52,
}


def test_openalex_only_when_no_google_scholar() -> None:
    assert format_citation_details(OPENALEX) == (
        "3,394 total (h-index: 26, i10: 52) (OpenAlex)"
    )


def test_google_scholar_with_i10_and_date() -> None:
    metrics = {
        **OPENALEX,
        "gs_total_citations": 4036,
        "gs_h_index": 30,
        "gs_i10_index": 54,
        "gs_last_updated": "2026-11-14",
    }
    assert format_citation_details(metrics) == (
        "3,394 total (h-index: 26, i10: 52) (OpenAlex) | "
        "4,036 total (h-index: 30, i10: 54) (Google Scholar, Nov 2026)"
    )


def test_google_scholar_without_date_or_i10_is_last_known() -> None:
    metrics = {**OPENALEX, "gs_total_citations": 3678, "gs_h_index": 26}
    assert format_citation_details(metrics) == (
        "3,394 total (h-index: 26, i10: 52) (OpenAlex) | "
        "3,678 total (h-index: 26) (Google Scholar, last known)"
    )


def test_unparseable_date_falls_back_to_last_known() -> None:
    metrics = {**OPENALEX, "gs_h_index": 30, "gs_last_updated": "sometime"}
    assert format_citation_details(metrics).endswith(
        "| h-index: 30 (Google Scholar, last known)"
    )

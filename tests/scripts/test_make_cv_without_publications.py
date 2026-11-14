from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = REPO_ROOT / "scripts" / "make_cv_without_publications.py"

_spec = importlib.util.spec_from_file_location("make_cv_without_publications", SCRIPT_PATH)
make_cv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(make_cv)

FULL_CV = (REPO_ROOT / "marine-cv-docs" / "Marine_Denolle_CV.yaml").read_text(encoding="utf-8")


def test_removes_only_publications_sections() -> None:
    out = make_cv.build(FULL_CV)

    assert "publications: !include" not in out
    assert "publications_legend:" not in out
    for kept in ("grants: !include", "review_panels: !include", "research_products: !include"):
        assert kept in out
    assert "rendercv_output/Marine_Denolle_CV_no_publications.pdf" in out


def test_committed_copy_matches_full_cv() -> None:
    committed = make_cv.TARGET.read_text(encoding="utf-8")
    assert committed == make_cv.build(FULL_CV)


def test_fails_when_block_missing() -> None:
    with pytest.raises(ValueError):
        make_cv.build("cv:\n  sections:\n    grants: !include grant_support.yaml\n")

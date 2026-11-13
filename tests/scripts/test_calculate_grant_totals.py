from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = REPO_ROOT / "scripts" / "calculate_grant_totals.py"

_spec = importlib.util.spec_from_file_location("calculate_grant_totals", SCRIPT_PATH)
calculate_grant_totals = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(calculate_grant_totals)
parse_amount = calculate_grant_totals.parse_amount


@pytest.mark.parametrize(
    ("area", "expected_amount", "expected_role"),
    [
        # Sole PI
        ("URG Program: $50,000 (PI)", 50_000, "lead-PI"),
        ("Monitoring at Mt Rainier: $750,000 (lead PI)", 750_000, "lead-PI"),
        # Unclosed "(lead PI" at the end of the line
        ("Climate-Compounded Geohazards: $300,000 (lead PI", 300_000, "lead-PI"),
        # PI on the UW award of a collaborative project led elsewhere
        (
            "SCOPED: $717,441.00 to UW (PI), collaborative with UAF "
            "(lead PI Carl Tape), Columbia, UT Austin and Colorado School of Mines, "
            "OAC-2103701",
            717_441,
            "lead-PI",
        ),
        (
            "PREEVENTS: $324,495.00 to UW (PI), collaborative with lead PI "
            "Yihe Huang and Amanda Thomas, EAR-1739712",
            324_495,
            "lead-PI",
        ),
        # Someone else is lead PI
        (
            "Fiber sensing: $880,490 (lead PI Wilcock, Denolle co-PI), OCE-2526198",
            880_490,
            "co-PI",
        ),
        (
            "UW FiberLab equipment: $950,000 (co-PI, lead PI Brad Lipovsky).",
            950_000,
            "co-PI",
        ),
        ("GeoSMART: $995,817 (co-PI). Build a course MLGEO.", 995_817, "co-PI"),
        # UW share listed first, so it is the amount counted
        (
            "CS4All: $62,000 to UW (Denolle co-PI, lead PI Lore), "
            "$889,766 total across institutions, DRL-2524060",
            62_000,
            "co-PI",
        ),
        # Returned grant written "(Denolle PI)" stays out of the totals
        ("Ridgecrest: $33,307 (Denolle PI) - returned", 33_307, "unknown"),
    ],
)
def test_parse_amount_role(area: str, expected_amount: int, expected_role: str) -> None:
    amount, role = parse_amount(area)

    assert amount == expected_amount
    assert role == expected_role


def test_parse_amount_without_dollar_figure() -> None:
    assert parse_amount("Recommended for funding, agreement in negotiation") == (
        0.0,
        "unknown",
    )

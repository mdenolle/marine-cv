from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from ruamel.yaml import YAML


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = REPO_ROOT / "scripts" / "generate_publications.py"


def run_generator() -> str:
    result = subprocess.run(
        [sys.executable, str(SCRIPT_PATH)],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def test_generate_publications_outputs_yaml_array() -> None:
    output = run_generator()

    assert "publications:" not in output
    assert "- title:" in output

    yaml = YAML(typ="safe")
    parsed = yaml.load(output)
    assert isinstance(parsed, list)
    assert len(parsed) > 0

    # All items are PublicationEntry dicts (legend is in the CV YAML, not here)
    pub = parsed[0]
    assert isinstance(pub, dict), "First entry should be a PublicationEntry dict, not a string"
    assert "title" in pub
    assert "authors" in pub


def test_generate_publications_filters_invalid_doi_placeholders() -> None:
    output = run_generator()

    assert "doi: XX" not in output


def test_generate_publications_bold_pi_italic_mentees() -> None:
    """PI name is bold (**...**) and mentee names are italic (*...*) in author lists."""
    output = run_generator()

    yaml = YAML(typ="safe")
    parsed = yaml.load(output)

    all_authors: list[str] = []
    for entry in parsed:
        if isinstance(entry, dict) and "authors" in entry:
            all_authors.extend(entry["authors"])

    # Denolle must appear as bold somewhere
    denolle_names = [a for a in all_authors if "Denolle" in a]
    assert denolle_names, "Expected Denolle to appear in at least one author list"
    for name in denolle_names:
        assert name.startswith("**") and name.endswith("**"), (
            f"Denolle name not bold: {name!r}"
        )

    # A known mentee (Tim Clements) must appear as italic where present
    mentee_names = [a for a in all_authors if "Clements" in a]
    for name in mentee_names:
        assert name.startswith("*") and name.endswith("*") and not name.startswith("**"), (
            f"Mentee name not italic: {name!r}"
        )

    # No author should have the old asterisk-suffix style (plain trailing *)
    for name in all_authors:
        assert not (name.endswith("*") and not name.endswith("**") and not name.startswith("*")), (
            f"Old asterisk-suffix style detected: {name!r}"
        )

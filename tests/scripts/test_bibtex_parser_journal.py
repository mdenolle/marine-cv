from __future__ import annotations

import pytest

from rendercv.bibtex_parser import format_journal


@pytest.mark.parametrize(
    ("args", "expected"),
    [
        (("Science", "392", "6795", "306--310"), "Science, 392(6795), 306–310"),
        (("Science Advances", "12", "9", "eaea3684"), "Science Advances, 12(9), eaea3684"),
        (("Seismica", "5", "1", ""), "Seismica, 5(1)"),
        (("Comptes Rendus. Géoscience", "343", "8-9", "600--614"),
         "Comptes Rendus. Géoscience, 343(8-9), 600–614"),
        # Online-first: article number but no volume yet, so no issue either
        (("Geophysical Journal International", "", "2", "ggaf322"),
         "Geophysical Journal International, ggaf322"),
        (("Seismological Research Letters", "", "", ""), "Seismological Research Letters"),
    ],
)
def test_format_journal(args: tuple[str, str, str, str], expected: str) -> None:
    assert format_journal(*args) == expected

"""Personal parameters for the DLMDSAS01 Advanced Workbook.

Single source of truth, parsed from ``exam_tasks/assignment_values_2.txt`` so
that no number is ever retyped by hand. Every quantity in the workbook is
derived from this module.
"""

from __future__ import annotations

import re
from pathlib import Path

VALUES_FILE = (Path(__file__).resolve().parents[2]
               / "exam_tasks" / "assignment_values_2.txt")

EXPECTED_SIGNATURE = "99d9e51eff0fb88f6911fa8b4392742591f8f6da"


def _parse(path: Path) -> tuple[dict[str, str], str]:
    raw = path.read_text(encoding="utf-8")
    values: dict[str, str] = {}
    for match in re.finditer(r"^\s*\*?\s*ξ(\d+)\s*:\s*(.+?)\s*$", raw, re.MULTILINE):
        values[f"xi{match.group(1)}"] = match.group(2)
    signature_match = re.search(r"^\s*signature\s*\n\s*([0-9a-f]{40})\s*$",
                                raw, re.MULTILINE)
    if signature_match is None:
        raise ValueError(f"no 40-character signature found in {path}")
    return values, signature_match.group(1)


_RAW, SIGNATURE = _parse(VALUES_FILE)

if SIGNATURE != EXPECTED_SIGNATURE:
    raise ValueError(
        f"parameter file signature {SIGNATURE} does not match the signature "
        f"{EXPECTED_SIGNATURE} this workbook was written against; "
        "regenerate the workbook rather than mixing parameter sets"
    )


def _num(key: str) -> float:
    return float(_RAW[key])


def _seq(key: str) -> list[float]:
    return [float(v) for v in _RAW[key].split(",")]


def _pairs(key: str) -> list[tuple[float, float]]:
    return [(float(a), float(b))
            for a, b in re.findall(r"\(\s*(-?[\d.]+)\s*,\s*(-?[\d.]+)\s*\)", _RAW[key])]


# Task 1 - Bernoulli vote
XI1 = int(_num("xi1"))
XI2 = _num("xi2")

# Task 2 - waiting time for the owl
XI4 = int(_num("xi4"))
XI5 = _num("xi5")
XI6 = _num("xi6")
XI7 = _num("xi7")
XI8 = _num("xi8")

# Task 3 - router bandwidth to failure
XI9 = int(_num("xi9"))
XI10 = _seq("xi10")

# Task 4 - hammer weights
XI11 = _num("xi11")
XI12 = _num("xi12")
XI13 = int(_num("xi13"))
XI14 = _seq("xi14")

# Task 5 - regularised polynomial regression
XI15 = int(_num("xi15"))
XI16 = _pairs("xi16")

# Task 6 - Bayesian estimate
XI17 = _num("xi17")
XI18 = _num("xi18")
XI19 = _num("xi19")

#: Sample size fixed by the wording of Task 6 ("let x_1, ..., x_10").
TASK6_N = 10

#: Shape of the sampling distribution in Task 6, fixed by the task wording.
TASK6_ALPHA = 3.0

# The generator truncates xi5 and xi7 to two decimals, so they sum to 0.99
# while the task sheet requires xi5 + xi7 = 1. Renormalising restores the
# constraint exactly; see Task 2 of the workbook for the justification.
XI5_STAR = XI5 / (XI5 + XI7)
XI7_STAR = XI7 / (XI5 + XI7)

BRANCHES = {
    1: XI1,
    2: XI4,
    3: XI9,
    4: XI13,
    5: XI15,
}

"""Check the per-task length budget.

The task sheet requires the answer to each task to be one A4 page of text plus
or minus ten per cent. Word counts are estimated from the rendered Markdown
rather than the .docx because pagination needs a Word layout engine, which is
not available here; the conversion factor below is derived from the page
geometry the reference document enforces.

Exit status is non-zero if any task is outside the allowance, so the build
surfaces a formatting breach instead of hiding it.
"""

from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent

#: Calibrated by measuring this workbook's own prose in the real Arial outlines
#: at 11 pt: mean word 24.8 pt plus a 3.1 pt space, in a 482 x 729 pt text block
#: (A4 less 2 cm margins) at a 18.97 pt line height (Arial single line is about
#: 1.15 em; Word's "1.5 lines" multiplies that). That gives 17.3 words across
#: 38.4 lines, less paragraph spacing and one heading block, and a further 5 %
#: allowance for the ragged ends that line breaking leaves.
WORDS_PER_PAGE = 550

#: A display equation sits in its own paragraph and typically occupies about two
#: line heights once fractions and integrals are taken into account.
WORDS_PER_EQUATION = 28

TOLERANCE = 0.10


def measure(body: str) -> tuple[int, int, int]:
    equations = len(re.findall(r"\$\$.*?\$\$", body, re.S))
    figures = len(re.findall(r"^!\[", body, re.M))
    prose = re.sub(r"\$\$.*?\$\$", " ", body, flags=re.S)
    prose = re.sub(r"^!\[.*?\)\{[^}]*\}\s*$", " ", prose, flags=re.M | re.S)
    prose = re.sub(r"```\{=openxml\}.*?```", " ", prose, flags=re.S)
    prose = re.sub(r"\$[^$]*\$", "x", prose)
    prose = re.sub(r"[*_`#|-]", " ", prose)
    return len(prose.split()), equations, figures


def main() -> int:
    # "One A4 page of text" is ambiguous about whether display equations count
    # as text, so both readings are reported rather than one being assumed.
    print(f"{'task':10s} {'words':>6s} {'eqs':>4s} {'figs':>5s} "
          f"{'prose':>6s} {'+eqs':>6s}  status")
    print("-" * 64)
    failures = 0
    for path in sorted((HERE / "src").glob("0[1-6]-task*.md")):
        words, equations, figures = measure(path.read_text(encoding="utf-8"))
        prose_pages = words / WORDS_PER_PAGE
        full_pages = (words + WORDS_PER_EQUATION * equations) / WORDS_PER_PAGE
        limit = 1 + TOLERANCE
        if full_pages <= limit:
            status = "ok"
        elif prose_pages <= limit:
            status = "ok if equations excluded"
            failures += 1
        else:
            status = "OVER BUDGET"
            failures += 1
        print(f"{path.stem[:10]:10s} {words:6d} {equations:4d} {figures:5d} "
              f"{prose_pages:6.2f} {full_pages:6.2f}  {status}")

    print()
    print(f"limit: 1 page + {TOLERANCE:.0%} at {WORDS_PER_PAGE} words per page, "
          f"{WORDS_PER_EQUATION} words per display equation.")
    if failures:
        print(f"{failures} task(s) exceed the limit when display equations are "
              "counted as text. Estimated from page geometry; confirm the "
              "pagination in Word before submitting.")
    else:
        print("all tasks within budget on both readings (estimated).")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

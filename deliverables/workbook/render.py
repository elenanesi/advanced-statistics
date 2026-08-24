"""Substitute computed results into the workbook prose.

The Markdown sources contain no literal numeric results. Every figure quoted in
the text is written as a token ``{{key}}`` or ``{{key:spec}}`` whose value comes
from ``build/results.json``. An unknown key is a hard error, so a renamed or
deleted result can never leave a stale number in the prose.

Format specifiers:
  ``{{task4.z:.3f}}``    ordinary Python format specification
  ``{{task2.p_2_4:sci3}}`` LaTeX scientific notation, e.g. ``8.443 \\times 10^{-15}``
  ``{{task5.lam_star:sci2}}``
"""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "src"
BUILD = HERE / "build"

TOKEN = re.compile(r"\{\{([a-z0-9_]+\.[a-z0-9_]+)(?::([^}]+))?\}\}", re.IGNORECASE)

#: ``<!-- CODE: compute.py -->`` is replaced by a listing of that file, so the
#: appendix always shows the code that actually produced the results.
CODE = re.compile(r"^<!--\s*CODE:\s*(\S+)\s*-->\s*$", re.MULTILINE)


def inline_code(text: str) -> str:
    def replace(match: re.Match) -> str:
        path = HERE / match.group(1)
        if not path.exists():
            raise FileNotFoundError(f"appendix listing refers to missing {path}")
        body = path.read_text(encoding="utf-8").rstrip()
        return f"```python\n{body}\n```"

    return CODE.sub(replace, text)


def latex_scientific(value: float, digits: int) -> str:
    """Render a number as ``m \\times 10^{e}`` for use inside LaTeX math."""
    if value == 0:
        return "0"
    exponent = math.floor(math.log10(abs(value)))
    mantissa = value / (10 ** exponent)
    # Guard against 9.999... rounding up to 10.000 at the requested precision.
    if round(abs(mantissa), digits) >= 10:
        mantissa /= 10
        exponent += 1
    return rf"{mantissa:.{digits}f} \times 10^{{{exponent}}}"


def format_value(value, spec: str | None) -> str:
    if spec is None:
        if isinstance(value, float) and value.is_integer():
            return str(int(value))
        return str(value)
    if spec.startswith("sci"):
        return latex_scientific(float(value), int(spec[3:] or 2))
    return format(value, spec)


def render(text: str, results: dict, source: str, missing: set[str]) -> str:
    def replace(match: re.Match) -> str:
        key, spec = match.group(1), match.group(2)
        if key not in results:
            missing.add(f"{key}  (in {source})")
            return match.group(0)
        return format_value(results[key], spec)

    return TOKEN.sub(replace, text)


def main() -> int:
    results_path = BUILD / "results.json"
    if not results_path.exists():
        print("build/results.json is missing; run compute.py first", file=sys.stderr)
        return 1
    results = json.loads(results_path.read_text(encoding="utf-8"))

    sources = sorted(SRC.glob("*.md"))
    if not sources:
        print(f"no Markdown sources found in {SRC}", file=sys.stderr)
        return 1

    missing: set[str] = set()
    chunks = [inline_code(render(path.read_text(encoding="utf-8"),
                                 results, path.name, missing))
              for path in sources]

    if missing:
        print("unresolved result keys:", file=sys.stderr)
        for item in sorted(missing):
            print(f"  {item}", file=sys.stderr)
        return 1

    out = BUILD / "workbook.md"
    out.write_text("\n\n".join(chunks) + "\n", encoding="utf-8")

    used = {m.group(1) for chunk in sources
            for m in TOKEN.finditer(chunk.read_text(encoding="utf-8"))}
    print(f"rendered {len(sources)} sources -> {out.name} "
          f"({len(used)} distinct result keys substituted)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

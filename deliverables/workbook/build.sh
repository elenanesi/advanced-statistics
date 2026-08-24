#!/usr/bin/env bash
# Build the Advanced Workbook .docx from source.
#
#   compute.py     -> build/results.json + figures/*.png
#   render.py      -> build/workbook.md   (results substituted into the prose)
#   pandoc         -> the .docx, with native Word equations
#   postprocess.py -> Roman/Arabic page numbering via section breaks
#
# Run from anywhere; paths are resolved relative to this script.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/../.." && pwd)"
PY="$REPO/.venv/bin/python"
OUT="$HERE/Advanced_Workbook_DLMDSAS01_DRAFT.docx"

cd "$HERE"

for tool in "$PY" "$(command -v pandoc || true)"; do
  if [ ! -x "$tool" ]; then
    echo "missing required tool: $tool" >&2
    echo "run: brew install pandoc && python3 -m venv .venv && .venv/bin/pip install matplotlib scipy numpy python-docx pypdf" >&2
    exit 1
  fi
done

echo "1/4  computing results and figures"
"$PY" compute.py

echo "2/4  rendering prose"
"$PY" render.py

echo "3/4  converting to .docx"
pandoc build/workbook.md \
  --from=markdown+tex_math_dollars+pipe_tables+raw_attribute+bracketed_spans \
  --to=docx \
  --reference-doc=assets/reference.docx \
  --number-sections \
  --resource-path=. \
  --output="$OUT"

echo "4/4  applying page numbering"
"$PY" postprocess.py "$OUT"

echo
echo "built: ${OUT#"$REPO"/}"
echo
# Advisory only: the length estimate cannot be exact without a Word layout
# engine, so a breach is reported rather than failing the build.
"$PY" check_length.py || true

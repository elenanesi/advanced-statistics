"""Execute ``workbook_analysis.ipynb`` and save it with its outputs.

The notebook is the single source of every number and every figure in the
workbook, so the build has to run it rather than read it. Execution happens in
place: the stored outputs are the ones that produced ``build/results.json``, so
opening the notebook afterwards shows exactly what the document was built from.

A failing cell aborts the build with the traceback that caused it; a notebook
that runs but does not write ``build/results.json`` is treated as a failure too,
since a silent no-op there would leave stale numbers in the document.
"""

from __future__ import annotations

import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE / "workbook_analysis.ipynb"
RESULTS = HERE / "build" / "results.json"

#: Generous, but bounded: the whole notebook runs in a couple of seconds, so a
#: cell still running after this has hung rather than slowed down.
CELL_TIMEOUT_SECONDS = 300


def main() -> int:
    if not NOTEBOOK.exists():
        print(f"missing {NOTEBOOK.name}", file=sys.stderr)
        return 1

    before = RESULTS.stat().st_mtime if RESULTS.exists() else None

    notebook = nbformat.read(NOTEBOOK, as_version=4)
    client = NotebookClient(
        notebook,
        timeout=CELL_TIMEOUT_SECONDS,
        kernel_name="python3",
        # Run as if the notebook had been opened from its own directory, so
        # that ``import params`` and the relative output paths resolve.
        resources={"metadata": {"path": str(HERE)}},
    )

    try:
        client.execute()
    except CellExecutionError as error:
        nbformat.write(notebook, NOTEBOOK)
        print(f"\n{NOTEBOOK.name} failed; the traceback is stored in the "
              f"notebook and repeated here:\n", file=sys.stderr)
        print(error, file=sys.stderr)
        return 1

    nbformat.write(notebook, NOTEBOOK)

    if not RESULTS.exists() or RESULTS.stat().st_mtime == before:
        print(f"{NOTEBOOK.name} ran but did not write "
              f"{RESULTS.relative_to(HERE)}", file=sys.stderr)
        return 1

    executed = sum(cell.cell_type == "code" for cell in notebook.cells)
    print(f"executed {executed} code cells in {NOTEBOOK.name}")
    for cell in notebook.cells[-1:]:
        for output in cell.get("outputs", []):
            if output.get("output_type") == "stream":
                print("  " + output["text"].strip().replace("\n", "\n  "))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

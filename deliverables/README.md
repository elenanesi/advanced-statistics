# Deliverables

Final exports for IU submission and personal archives.

| Artifact | Status | Source |
|----------|--------|--------|
| `workbook/workbook_analysis.ipynb` | All six tasks, current parameter set | The computational source of truth — owns every number and figure |
| `workbook/Advanced_Workbook_DLMDSAS01_DRAFT.docx` | Draft builds clean | `workbook/build.sh` — executes the notebook, substitutes `{{task.key}}` tokens into `workbook/src/*.md` |

`exam_tasks/user_notebook.ipynb` is Elena's scratch notebook (Task 1 only, superseded
parameter values) and is not a deliverable.

## `.docx` workbook

Build it with `cd workbook && ./build.sh`. The pipeline:

1. Mirrors PDF task order (Tasks 1–6).
2. **Executes** `workbook_analysis.ipynb` via `run_notebook.py` and harvests its results — it does not read the notebook as text.
3. Substitutes `{{task.key}}` tokens into `src/*.md`, so prose files must carry no literal results. To change a number, change the notebook.
4. Emits the `.docx` with title page, course code DLMDSAS01, figures, and tool-trust paragraphs, plus the notebook as copyable text in Appendix B.

Do not commit personal `assignment_values*.txt` to public remotes if the user plans to open-source the repo.

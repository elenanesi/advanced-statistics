# Appendix A: personal parameters and signature {-}

The values below are the output of the IU parameter generator and are reproduced
verbatim. They are referenced throughout the workbook and are the sole source of
every number in it.

| Task | Parameter | Value |
|---|---|---|
| 1 | $\xi_1$ | {{meta.xi1}} |
| 1 | $\xi_2$ | {{meta.xi2:.2f}} |
| 2 | $\xi_4$ | {{meta.xi4}} |
| 2 | $\xi_5$ | {{meta.xi5:.2f}} |
| 2 | $\xi_6$ | {{meta.xi6:.0f}} |
| 2 | $\xi_7$ | {{meta.xi7:.2f}} |
| 2 | $\xi_8$ | {{meta.xi8:.0f}} |
| 3 | $\xi_9$ | {{meta.xi9}} |
| 3 | $\xi_{10}$ | {{meta.xi10}} |
| 4 | $\xi_{11}$ | {{meta.xi11:.0f}} |
| 4 | $\xi_{12}$ | {{meta.xi12:.1f}} |
| 4 | $\xi_{13}$ | {{meta.xi13}} |
| 4 | $\xi_{14}$ | {{meta.xi14}} |
| 5 | $\xi_{15}$ | {{meta.xi15}} |
| 5 | $\xi_{16}$ | {{meta.xi16_n}} coordinate pairs, listed in Table A.1 |
| 6 | $\xi_{17}$ | {{meta.xi17:.0f}} |
| 6 | $\xi_{18}$ | {{meta.xi18:.0f}} |
| 6 | $\xi_{19}$ | {{meta.xi19:.2f}} |

Signature string: `{{meta.signature}}`

**Table A.1** The {{meta.xi16_n}} pairs $(x, y)$ of $\xi_{16}$ used in Task 5,
sorted by $x$.

| $x$ | $y$ | $x$ | $y$ |
|---|---|---|---|
{{task5.pairs_rows}}

# Appendix B: source code {-}

The listings below are the complete code that produced every number and every
figure in this workbook. They are included as text, not as images, so that they
can be copied from the PDF and re-run.

The calculations live in a Jupyter notebook, `workbook_analysis.ipynb`, which is
reproduced in section B.2 with its commentary and its code cells in the order in
which they run. A notebook was chosen over a plain script because the reasoning
that motivates each calculation can then sit immediately above the code that
performs it, which is what a colleague taking the work over needs. Cell outputs
are omitted here: every number and figure the notebook produces already appears
in the body of the workbook, and repeating them would bury the code.

The notebook writes a file of results that the workbook text draws on directly;
no numeric result in the main text is typed by hand. Running the notebook from
top to bottom reproduces the whole document, and the build script does exactly
that before rendering it, so the two cannot disagree.

**B.1 `params.py`** — parses the generator output and verifies the signature.
It is a separate module rather than a cell because it is file parsing rather
than statistics, and because the signature check must fail before any
calculation begins.

<!-- CODE: params.py -->

**B.2 `workbook_analysis.ipynb`** — all six tasks.

<!-- NOTEBOOK: workbook_analysis.ipynb -->

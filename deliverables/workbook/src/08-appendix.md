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
figure in this workbook. They are included as text so that they can be copied
from the PDF and re-run. The entry point is `compute.py`, which writes a file of
results that the workbook text draws on directly; no numeric result in the main
text is typed by hand.

**B.1 `params.py`** — parses the generator output and verifies the signature.

<!-- CODE: params.py -->

**B.2 `compute.py`** — all six tasks.

<!-- CODE: compute.py -->

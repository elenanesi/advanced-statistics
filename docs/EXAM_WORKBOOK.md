# Exam workbook — Task specification & personal branches

Official document: `exam_tasks/Task_Advanced_Workbook_DLMDSAS011.pdf` (IU DLMDSAS01 Advanced Statistics).

**Rule from the PDF:** If a task says “If \(\xi_k\) is …”, **only perform that sub-task** when your personal value matches. Otherwise skip and state that the branch does not apply.

**Implementation home:** `exam_tasks/bernoulli_vote_analysis.ipynb` (single notebook for all tasks unless user requests split).

---

## Parameter file

`exam_tasks/assignment_values.txt` lists \(\xi_1\ldots\xi_{20}\) plus a `signature` hash. Parse lines like `* ξ2: 0.58`.

When the generator output changes, recompute the **Personal path** table below before coding.

---

## Personal path (current assignment)

| Task | Condition | Applies? | Personal setup |
|------|-----------|----------|----------------|
| **1** | \(\xi_1=0\) Bernoulli | **Yes** | \(P(\text{for})=\xi_2=0.58\) |
| 1 | \(\xi_1\in\{1,2,3\}\) meteorites | No | — |
| **2** | \(\xi_4=0\) linear exponents in \(y\) | No | — |
| 2 | \(\xi_4=1\) | No | — |
| 2 | \(\xi_4=2\) | No | — |
| **2** | \(\xi_4=3\) | **Yes** | \(\bar F_Y(y)=P(Y>y)=\xi_5 e^{-\xi_6 y^2}+\xi_7 e^{-\xi_8 y^2}\) |
| **3** | \(\xi_9=0\) Exp(1) | No | — |
| 3 | \(\xi_9=1\) | No | — |
| **3** | \(\xi_9=2\) | **Yes** | \(f_S(s)=\frac{1}{120\theta^7}s^6 e^{-s/\theta}\) (Gamma/Erlang shape 7) |
| **4** | \(\xi_{13}=0\) more constant | No | — |
| 4 | \(\xi_{13}=1\) lower | No | — |
| **4** | \(\xi_{13}=2\) higher | **Yes** | Test whether new system → higher weights |
| 4 | \(\xi_{13}=3\) less constant | No | — |
| **5** | \(\xi_{15}=0\) degree 12 poly | No | — |
| **5** | \(\xi_{15}=2\) degree 10 poly | **Yes** | \(f(x)=\sum_{i=0}^{10}\alpha_i x^i\) |
| **6** | — | **Yes** | Hogg 11.2.2 style; \(\xi_{17},\xi_{18},\xi_{19}\) |

### Task 2 numeric survival (personal)

\[
\bar F_Y(y) = 0.79\, e^{-4 y^2} + 0.20\, e^{-6 y^2},\quad y\ge 0 \text{ (hours)}.
\]

Check: \(\xi_5+\xi_7=0.79+0.20=0.99\) — PDF says parameters should satisfy \(\xi_5+\xi_7=1\); **flag 0.01 gap** in notebook and discuss (rounding vs generator).

Required outputs:

- \(P(2<Y<4)\)
- PDF plot \(f_Y(y)\)
- Minute-level histogram (convert units carefully: hours → minutes)
- Mean, variance, quartiles on plots

**Theory pointers:** survival → PDF via derivative; Unit 3 (Gamma/Exponential) for mixture intuition; transformed variables Unit 3.5.

### Task 3 personal

- Single router \(S\): Erlang/Gamma with shape 7, scale \(\theta\).
- Dual system \(T = S_1+S_2\) with i.i.d. routers, automatic failover → sum of independent times.
- Sample for MLE: \(\xi_{10} = (37, 58, 8, 176, 10)\) (TB).
- Log-likelihood transform (e.g. log-likelihood) for easy maximization.
- Report \(\hat\theta\), \(\mathbb{E}[T]\) under fitted model.

**Theory pointers:** Unit 3.3 (Gamma/Exponential), Unit 3.5 (sums), Unit 6.1 (MLE).

### Task 4 personal

- Historical: \(\mu_0=\xi_{11}=956\) g, \(\sigma_0=\xi_{12}=17.2\) g (from 1000 hammers).
- Question: **higher weights** under new system?
- Sample \(\xi_{14}\): 966, 957, 1036, 902, 1014, 968, 1002, 973, 949, 946 (n=10).

Deliver: model + assumptions, \(H_0,H_1\), test choice, critical-region logic, \(\alpha\)/error discussion, computation, conclusion.

**Theory pointers:** Unit 3.2 Normal, Unit 7 Hypothesis Testing (esp. 7.1–7.2).

### Task 5 personal

- Model: polynomial degree 10.
- Data: 22 points in \(\xi_{16}\) (pairs \((x,y)\)).
- OLS + ridge; justify penalty weight(s); compare solution qualities (bias/variance, norm of \(\alpha\), fit).

**Theory pointers:** Unit 6.2 OLS, Unit 6.4 Ridge.

### Task 6 personal

Gamma sample with \(\alpha=3\), \(\beta=1/\theta\); prior \(\theta\sim\text{Gamma}(\xi_{17},\xi_{18})=\text{Gamma}(35,51)\); observed \(\bar x=\xi_{19}=90.37\).

Parts (a) posterior, (b) Bayes estimate squared error loss, (c) posterior mode.

**Theory pointers:** Unit 4 Bayesian, 4.3 Conjugate priors; Hogg et al. (2020) as cited in PDF.

---

## Task 1 — full branch text (reference)

### If \(\xi_1=0\) (personal)

Bernoulli trial: \(P(\text{vote}=\text{for})=\xi_2\). Graphic + percentages; can expectation be calculated? State hypotheses for integrability/measurability.

### If \(\xi_1=1\)

Poisson(\(\lambda=\xi_2\)): PMF plot until tail \(<0.5\%\); prove truncation; expectation and median on plot.

### If \(\xi_1=2\)

Negative binomial with expectation \(k=\xi_2\), \(p=\xi_3\).

### If \(\xi_1=3\)

Geometric(\(p=\xi_2\)) counting trials until success.

---

## Task 2 — survival branches (reference)

Let \(Y\) = hours until owl is heard. \(\bar F_Y(y)=P(Y>y)\):

| \(\xi_4\) | \(\bar F_Y(y)\) |
|----------|-----------------|
| 0 | \(\xi_5 e^{-\xi_6 y}+\xi_7 e^{-\xi_8 y}\) |
| 1 | \(\xi_5 e^{-\xi_6 y^2}+\xi_7 e^{-\xi_8 y^8}\) |
| 2 | \(\xi_5 e^{-\xi_6\sqrt{y}}+\xi_7 e^{-\xi_8\sqrt{y^3}}\) |
| 3 | \(\xi_5 e^{-\xi_6 y^2}+\xi_7 e^{-\xi_8 y^2}\) |

---

## Task 3 — density branches (reference)

| \(\xi_9\) | \(f_S(s)\) |
|----------|------------|
| 0 | \(\frac{1}{\theta}e^{-s/\theta}\) |
| 1 | \(\frac{1}{24\theta^5}s^4 e^{-s/\theta}\) |
| 2 | \(\frac{1}{120\theta^7}s^6 e^{-s/\theta}\) |

---

## Acceptance criteria (grading-style)

| Criterion | Required |
|-----------|----------|
| Correct branch | Only personal sub-task executed |
| Proof/citation | Steps or reference for non-trivial claims |
| Graphics scale | Axes labeled with units; reader can read values |
| Tool trust | Libraries named; spot checks included |
| Computation steps | Especially Tasks 5–6 — math path matches code |
| Task 6 | Parts (a), (b), (c) clearly labeled |

---

## Notebook section naming convention

Use markdown headers:

```text
# Task N: <short title>
## Branch resolution
## Model and assumptions
## Derivation
## Numerical results
## Visualization
## Tool trust and checks
```

Cross-link to slide: `learning/concepts.json` entry if a deck exists.

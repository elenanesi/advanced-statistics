# Exam workbook — Task specification & personal branches

Official document: `exam_tasks/Task_Advanced_Workbook_DLMDSAS011.pdf` (IU DLMDSAS01 Advanced Statistics).

**Rule from the PDF:** If a task says “If \(\xi_k\) is …”, **only perform that sub-task** when your personal value matches. Otherwise skip and state that the branch does not apply.

**Implementation home:** `deliverables/workbook/` — `compute.py` produces every number and figure, `src/*.md` holds the prose, `build.sh` emits the .docx. `exam_tasks/bernoulli_vote_analysis.ipynb` predates this and is built on the superseded parameter set.

---

## Parameter file

**Source of truth: `exam_tasks/assignment_values_2.txt`**, signature `99d9e51eff0fb88f6911fa8b4392742591f8f6da`. It lists \(\xi_1\ldots\xi_{20}\) plus a `signature` hash; parse lines like `* ξ2: 0.65`.

`exam_tasks/assignment_values.txt` is the **superseded** first generator run (signature `1bd4e9ec…`) and is kept only for provenance. Anything quoting \(\xi_2=0.58\), \(\xi_4=3\), \(\xi_9=2\), \(\mu_0=956\) or \(\text{Gamma}(35,51)\) is from that old set.

`deliverables/workbook/params.py` parses the file and **raises if the signature does not match**, so a mixed parameter set cannot silently produce a workbook.

When the generator output changes, recompute the **Personal path** table below before coding.

---

## Personal path (current assignment, signature `99d9e51e`)

| Task | Condition | Applies? | Personal setup |
|------|-----------|----------|----------------|
| **1** | \(\xi_1=0\) Bernoulli | **Yes** | \(P(\text{for})=\xi_2=0.65\) |
| 1 | \(\xi_1\in\{1,2,3\}\) meteorites | No | — |
| 2 | \(\xi_4=0\) linear exponents in \(y\) | No | — |
| **2** | \(\xi_4=1\) | **Yes** | \(\bar F_Y(y)=\xi_5 e^{-\xi_6 y^2}+\xi_7 e^{-\xi_8 y^8}\) |
| 2 | \(\xi_4\in\{2,3\}\) | No | — |
| **3** | \(\xi_9=0\) exponential | **Yes** | \(f_S(s)=\frac{1}{\theta}e^{-s/\theta}\) |
| 3 | \(\xi_9\in\{1,2\}\) | No | — |
| 4 | \(\xi_{13}=0\) more constant | No | — |
| 4 | \(\xi_{13}=1\) lower | No | — |
| **4** | \(\xi_{13}=2\) higher | **Yes** | Test whether new system → higher weights |
| 4 | \(\xi_{13}=3\) less constant | No | — |
| 5 | \(\xi_{15}=0\) degree 12 poly | No | — |
| **5** | \(\xi_{15}=2\) degree 10 poly | **Yes** | \(f(x)=\sum_{i=0}^{10}\alpha_i x^i\) |
| **6** | — | **Yes** | Hogg 11.2.2 style; \(\xi_{17}=23,\xi_{18}=63,\xi_{19}=95.48\) |

### Task 1 personal

\(p=\xi_2=0.65\); \(\mathbb{E}[X]=0.65\), \(\operatorname{Var}(X)=0.2275\), sd \(=0.47697\).

### Task 2 numeric survival (personal)

\[
\bar F_Y(y) = \tfrac{2}{3}\, e^{-8 y^2} + \tfrac{1}{3}\, e^{-5 y^8},\quad y\ge 0 \text{ (hours)}.
\]

**Parameter correction (decided, documented in the workbook):** the generator returned \(\xi_5=0.66\), \(\xi_7=0.33\), summing to 0.99, but the task sheet requires \(\xi_5+\xi_7=1\). Since \(0.66/0.99=2/3\) and \(0.33/0.99=1/3\) exactly, the generator truncated to two decimals. **Renormalise to \(\xi_5^*=2/3\), \(\xi_7^*=1/3\)** and state the correction explicitly. Verified \(\bar F_Y(0)=1\) and \(\int f_Y = 1\).

Both components are Weibull survival functions: shape 2 (Rayleigh), scale 0.35355 h, weight 2/3; and shape 8, scale 0.81777 h, weight 1/3. The density is **bimodal** (peaks near 15.0 and 47.9 min).

Verified results: \(\mathbb{E}[Y]=0.465594\) h \(=27.94\) min; \(\operatorname{Var}=0.068605\) h²; \(Q_1/\text{median}/Q_3 = 14.54/24.90/42.79\) min; \(P(2<Y<4)=8.443\times10^{-15}\); \(P(Y<1\text{ h})=99.753\%\). Closed forms: \(\mathbb{E}[Y]=\frac{\xi_5^*}{2}\sqrt{\pi/\xi_6}+\xi_7^*\Gamma(9/8)\xi_8^{-1/8}\), \(\mathbb{E}[Y^2]=\frac{\xi_5^*}{\xi_6}+\frac{\xi_7^*\Gamma(1/4)}{4\xi_8^{1/4}}\).

Required outputs: \(P(2<Y<4)\); PDF plot; minute-level histogram (hours → minutes); mean, variance, quartiles on plots.

**Theory pointers:** survival → PDF via \(f=-\bar F'\); \(\mathbb{E}[Y]=\int_0^\infty\bar F\) for \(Y\ge0\); Unit 3 for mixture intuition; Unit 3.5 transformed variables.

### Task 3 personal

- Single router \(S\sim\text{Exponential}(\text{mean }\theta)\) — **the \(\xi_9=2\) branch and its 120-vs-720 typo no longer apply.**
- Dual system \(T=S_1+S_2\) i.i.d. with automatic failover → \(T\sim\text{Gamma}(2,\theta)\), \(f_T(t)=t e^{-t/\theta}/\theta^2\), by convolution.
- Sample \(\xi_{10}=(33, 29, 6, 37, 1)\) TB, \(n=5\), \(\sum t_i=106\).
- MLE via log-likelihood: \(\hat\theta=\bar T/2=10.6\) TB; \(\mathbb{E}[T]=2\hat\theta=21.2\) TB.
- Fisher information \(2n/\theta^2\) → se 3.352, approximate 95% interval [4.03, 17.17] (very wide at \(n=5\)).
- Fit check: observed CV 0.778 vs \(1/\sqrt2=0.707\).

**Theory pointers:** Unit 3.3 (Gamma/Exponential), Unit 3.5 (sums), Unit 6.1 (MLE).

### Task 4 personal

- Historical: \(\mu_0=\xi_{11}=842\) g, \(\sigma_0=\xi_{12}=55.3\) g (from 1000 hammers).
- Question: **higher weights** under new system? One-sided, upper tail.
- Sample \(\xi_{14}\): 719, 743, 803, 814, 925, 1051, 776, 806, 802, 1083 (n=10).
- \(\bar x=852.2\), \(s=125.65\), se \(=17.4874\), \(z=0.5833\), \(z_{0.95}=1.6449\), \(p=0.2799\), critical \(\bar x>870.76\) g.
- **Conclusion FLIPS versus the old parameter set: fail to reject \(H_0\).** The old deck concluded "reject" and is wrong for this data.
- \(t\) alternative: \(t=0.2567\), \(t_{0.95,9}=1.8331\), \(p=0.4016\) — same conclusion.
- Errors: Type I = 5% by construction; power at the observed effect only 14.42% (β = 85.58%); minimum detectable difference at 80% power is 43.48 g against an observed 10.2 g.
- **Red flag worth writing up:** \(s=125.65\) vs \(\sigma_0=55.3\) is a variance ratio of 5.16, so "σ unchanged" is doubtful.

**Theory pointers:** Unit 3.2 Normal, Unit 7 Hypothesis Testing (esp. 7.1–7.2).

### Task 5 personal

- Model: polynomial degree 10 (11 coefficients). Data: 22 \((x,y)\) pairs in \(\xi_{16}\); \(x=0\) **is** in the sample with \(y=-0.98\), so \(\alpha_0\) is directly observable.
- **Conditioning is the headline:** raw Vandermonde condition number \(1.02\times10^{13}\); after rescaling \(x\) to \([-1,1]\) it is \(3.74\times10^{3}\). Rescaling is mandatory. Scale \(y\) too so \(\lambda\) is meaningful.
- Solve by **SVD**, not by inverting \(X^\top X\) (which squares the condition number). Intercept unpenalised.
- \(\lambda^*=4.5\times10^{-4}\) by leave-one-out cross-validation.
- RMSE (original units): OLS \(1.63\times10^{11}\), ridge \(2.98\times10^{11}\), heavy ridge \(5.54\times10^{11}\). Coefficient norm 6.63 → 1.007 (−84.8%).
- **Quality answer:** least squares is dominated by the largest \(|y|\approx6\times10^{13}\); for \(|x|\le7\) both fits are worthless (fitted intercept \(1.90\times10^{11}\) OLS, \(-3.89\times10^{9}\) ridge, against an observed \(-0.98\)).

**Theory pointers:** Unit 6.2 OLS, Unit 6.4 Ridge; Hastie et al. (2009) §3.4.1.

### Task 6 personal

Gamma sample with \(\alpha=3\), \(\beta=1/\theta\); prior \(\theta\sim\text{Gamma}(\xi_{17},\xi_{18})=\text{Gamma}(23,63)\); observed \(\bar x=\xi_{19}=95.48\), \(n=10\), \(\sum x_i=954.8\).

**Convention (declare it in the paper): Hogg writes \(\beta\) as a SCALE.** So the prior rate is \(1/63=0.015873\).

- (a) Posterior \(=\text{Gamma}(\text{shape }53,\ \text{rate }954.8159)\).
- (b) Bayes estimate (squared-error loss) = posterior mean = **0.0555081**.
- (c) Posterior mode \(=(a-1)/r=\) **0.0544608**.
- Alternative reading (\(\xi_{18}\) as a rate): rate 1017.8, mean 0.0520731, mode 0.0510906 — a 6.19% difference. Report in a footnote.
- Prior influence: MLE \(\alpha/\bar x=0.03142\) lies **outside** the 95% credible interval [0.0416, 0.0714]; the prior supplies 23 of 53 shape units but only 0.0159 of 954.82 rate units.

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

---

## Workbook deliverable (`deliverables/workbook/`)

| File | Role |
|------|------|
| `params.py` | Parses `assignment_values_2.txt`; **fails loudly if the signature changes** |
| `compute.py` | Every number and figure; writes `build/results.json` and `figures/*.png` |
| `src/*.md` | Prose. Contains **no literal numeric results** — only `{{task4.z:.3f}}` tokens |
| `render.py` | Substitutes tokens; unknown key = hard error. Also inlines code into the appendix |
| `make_reference.py` | Builds `assets/reference.docx` with the IU formatting rules |
| `postprocess.py` | Section breaks for Roman front matter / Arabic body page numbers |
| `check_length.py` | Per-task A4 page budget estimate |
| `build.sh` | Runs the whole chain |

**Why the token indirection:** the task sheet is graded on the calculation matching the text, and the parameter set has already been regenerated once. Tokens make it impossible for a stale number to survive a recompute.

**Formatting decisions baked into `reference.docx`:** A4, 2.00 cm margins on all sides (the IU template ships 2.54 cm — the guidelines win), Arial 11 pt, 1.5 line spacing, justified body, headings 16/14/11 pt bold left-aligned, captions and footnotes 10 pt, hyphenation on, centred page number in the footer.

**Known open points:** title-page fields are `[[PLACEHOLDER]]` tokens; the final submission must be a **PDF**, not the .docx; the affidavit is submitted separately via myCampus **before** the assignment.

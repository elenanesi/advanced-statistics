# Sources — course book map & external authorities

Primary reference: `knowledge/Advanced_statistics_Course_Book.pdf` (DLMDSAS01, IU, 2025).

Use this file to cite **where** to look before searching the web.

---

## Course book units ↔ exam tasks

| Exam task | Topics | Course book (Unit — section) |
|-----------|--------|------------------------------|
| 1 Bernoulli / counts | PMF, expectation, discrete distributions | Unit 1 — 1.3; Unit 3 — 3.1 (binomial/negbin), 3.3 (Poisson) |
| 2 Owl waiting time | Survival, PDF, continuous distributions | Unit 3 — 3.3–3.4; Unit 2 — quantiles |
| 3 Routers | Gamma/Erlang, sums, MLE | Unit 3 — 3.3, 3.5; Unit 6 — 6.1 |
| 4 Hammers | Normal model, hypothesis tests | Unit 3 — 3.2; Unit 7 — 7.1–7.2 |
| 5 Regression | OLS, ridge | Unit 6 — 6.2, 6.4 |
| 6 Bayesian | Conjugate priors, posterior | Unit 4 — 4.1, 4.3; Hogg et al. (2020) per exam PDF |

### Visualization norms

Unit 5 — histograms, bar plots, scales (Tasks 1–2 plots).

---

## External references (when book is insufficient)

Prefer standard texts / docs; cite in notebook markdown.

| Topic | Suggested source |
|-------|------------------|
| Distributions | Casella & Berger, *Statistical Inference*; scipy.stats docs |
| Survival → PDF | Ross, *Introduction to Probability Models*; any reliability notes on \(f=-\bar F'\) |
| MLE | Casella & Berger; scipy.optimize notes |
| Hypothesis tests | Rice, *Mathematical Statistics*; scipy.stats test docs |
| Ridge regression | Hastie et al., *Elements of Statistical Learning* §3.4; sklearn Ridge |
| Bayesian conjugacy | Gelman et al., *Bayesian Data Analysis*; Hogg, McKean, Craig (2020) |

**Wikipedia:** OK for reminders, not as sole citation for graded workbook.

**LLM-generated math:** Verify every identity with book or sympy before submission.

---

## PDF extraction (agents)

If `pdftotext` is unavailable:

```bash
pip install pypdf
python3 -c "from pypdf import PdfReader; print(PdfReader('knowledge/Advanced_statistics_Course_Book.pdf').pages[NN].extract_text())"
```

Page numbers in citations: use **printed page** from PDF footer if visible, else PDF page index + 1.

---

## Copyright reminder

Do not redistribute IU PDFs or full worked solutions publicly. This repo is for private study.

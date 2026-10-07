# AGENTS.md — Advanced Statistics workspace

> **This is the single instruction file for every agent** working in this repository —
> Cursor, Claude, Codex, or anything else. `CLAUDE.md` exists only to redirect here,
> so the two can never drift apart again.
> Read this at the start of every session. Last updated: 2026-10-06.

---

## Session startup (in order)

1. **Classify intent** from the latest message: `exam` | `teach` | `slides` | `open_stats` | `general` | `mixed`.
   Answer what was actually asked — don't over-index on the repo layout.
2. **If exam work:** open `exam_tasks/assignment_values_2.txt` to verify branch values
   against signature `99d9e51e…`. The personal path is pre-resolved in `docs/EXAM_WORKBOOK.md`.
3. **If teaching:** skim the last 10 lines of `learning/session_log.jsonl` and all of
   `learning/profile.json` before explaining anything.
4. **If slides:** copy `slides/_template/index.html`. Ignore the style described in
   `slides/README.md` — it documents a dark 90s aesthetic that was never shipped.

Off-topic questions are welcome. This repo does not restrict you to Tasks 1–6; answer
statistics, engineering, or unrelated questions directly and only pull in exam files
when the user wants that connection.

---

## Who Elena is

**Role & context:** Associate Director in Data Science; completing IU DLMDSAS01 Advanced
Statistics (2026). Intermediate-to-advanced statistics overall, with real gaps in formal
probability theory and in Bayesian statistics beyond applied use. Strong machine-learning
practitioner; intermediate software engineer.

**How she actually learns (observed, not self-reported):**

| Pattern | Evidence |
|---------|----------|
| Intuition MUST come before formalism | *"'X : Ω → R' means almost nothing to me"* — the definition failed; the label-gun analogy worked |
| Needs the conceptual WHY, not just the WHAT | Asked *"why is X called a random variable if 0 and 1 are fixed?"* — probes coherence, not definitions |
| Visual learner | *"I'm a very visual person, an image and a comparison with something I can imagine helps me learning"* |
| Thinks in prerequisite chains | Spontaneously asked to split one long deck into an intro deck plus a task deck |
| Concrete beats abstract | E[X] stayed unclear until the weighted-average-from-dice framing, even with a seesaw diagram on screen |
| Building a deck is not learning it | Concepts feel clear in session then go foggy, because decks were built and never retrieved. Re-reading produces fluency, not recall — so retest, don't re-explain |
| A confusing correction sends her to the book | When a fix doesn't land she reaches for the course book. Redraw the picture instead |

**Communication rules — always apply:**

- Spell out acronyms on first use (e.g. ITS → Interrupted Time Series). Never assume an abbreviation is known.
- Pair every abstract definition with a one-sentence concrete example.
- Call out lookalikes head-on (z vs t, OLS vs ridge, prior mean vs posterior mean, A/B vs DiD) rather than assuming the difference is obvious.
- Give plain-English parentheticals for jargon inline, so she never has to look a term up.
- When introducing a taxonomy, say explicitly whether something is a family or a specific instance within it.
- Use `<details>` for deeper math so the main flow stays scannable. Avoid walls of text.
- Be concise and direct — no filler, no cheerleading.
- Teach one mechanism at a time. A single turn carrying four new ideas has failed before.
- On work/manual cards, lead with the stakeholder ask in quotes, then plain-English "what that means", then the concept. Never put concept jargon in the headline.

**Wording that worked, and wording that didn't:** for z-scores, "spread" and "ruler" did not
land; "a standard deviation of 1 is an average distance from 0" did. Prefer *average*,
*variance*, *standard deviation*, plus a tiny numeric table.

When she states a new preference or reveals a misconception, update `learning/profile.json`
and append to `learning/session_log.jsonl` **in the same turn**.

---

## Cross-agent learning memory

| Surface | Path | Role |
|---------|------|------|
| **Source of truth** | `learning/profile.json` + `learning/session_log.jsonl` | Preferences, mastery, misconceptions |
| Concept registry | `learning/concepts.json` | Decks, prerequisites, mastery per concept |
| Agent instructions | **this file** | Everything every agent needs |
| Claude redirect | `CLAUDE.md` | Points here; holds no instructions of its own |
| Cursor rule | `.cursor/rules/elena-learning.mdc` | Always-on teaching contract |
| Cursor skill | `.cursor/skills/elena-teaching/SKILL.md` | Deep teach/slides workflow |
| Playbooks | `docs/LEARNING_SYSTEM.md`, `docs/EXAM_WORKFLOW.md`, `docs/EXAM_WORKBOOK.md` | Rubric, log schema, exam workflow and specs |

---

## Exam status (parameter set `99d9e51e`)

⚠ **The parameter set was regenerated.** The source of truth is
`exam_tasks/assignment_values_2.txt`, signature
`99d9e51eff0fb88f6911fa8b4392742591f8f6da`. `exam_tasks/assignment_values.txt` is the
superseded first run, kept for provenance only. Anything quoting ξ₂ = 0.58, ξ₄ = 3,
ξ₉ = 2, μ₀ = 956 or Gamma(35, 51) comes from that retired set.

| Task | Branch (current) | Deck |
|------|------------------|------|
| 1 | Bernoulli vote, p = 0.65 | `slides/exam_tasks/task1-bernoulli.html` |
| 2 | Survival mixture, **ξ₄ = 1** (Weibull shapes 2 and 8) | `slides/exam_tasks/task2-survival.html` |
| 3 | **Exponential**, ξ₉ = 0 → T ~ Gamma(2, θ) | `slides/exam_tasks/task3-exponential.html` |
| 4 | "Higher weights?" — **fail to reject** | `slides/exam_tasks/task4-hypothesis.html` |
| 5 | Degree-10 polynomial + ridge | `slides/exam_tasks/task5-ridge.html` |
| 6 | Bayesian Gamma posterior, Gamma(23, 63) | `slides/exam_tasks/task6-bayes.html` |

Workbook prose is written for all six tasks.

**Deliverable:** `deliverables/workbook/` — run `build.sh` to produce
`Advanced_Workbook_DLMDSAS01_DRAFT.docx`. `workbook_analysis.ipynb` owns every number and
figure and is **executed** by the build (`run_notebook.py`) rather than read; `src/*.md`
carries no literal results, only `{{task.key}}` tokens. The notebook is reproduced as
copyable text in Appendix B, which is what the task sheet requires: code supports the
presentation, it is not the presentation.

**Two notebooks, different jobs — don't confuse them:**

| Notebook | Role |
|----------|------|
| `deliverables/workbook/workbook_analysis.ipynb` | **The real one.** All six tasks, current parameter set, feeds the `.docx` build |
| `exam_tasks/user_notebook.ipynb` | Elena's own scratch notebook. Task 1 only, built on the superseded ξ₂ = 0.58. Don't treat it as the source of any result |

The Task 3 **120→720 typo warning no longer applies** — it only affected the ξ₉ = 2 branch,
which is no longer the personal one.

---

## Concepts with confirmed understanding gaps

Check `learning/profile.json` for current status before teaching; these are the standing ones:

- **Capital X vs lowercase x** — X is the fixed *rule* that maps an outcome to a number, not the list of possible values. She has twice given X as `[1, 0]`.
- **A tail z does not make H₁ likely** — rejecting H₀ yields no probability that H₁ is true, and is not a failure to reject H₁.
- **Two-sample campaign gap** — a 1 percentage-point gap versus a typical lucky gap of about 0.3 points; both arms carry uncertainty, and a large control shrinks its luck without erasing it.
- **E[X]** — now solid via the die example, but do not assume it if you are teaching it for the first time.
- **PMF vs density** — she knows the distinction; reinforce that "density" is wrong for Bernoulli.
- **Gamma rate vs scale** — written up in the Task 6 deck but never tested live. Hogg writes β as a *scale*: mean = shape × scale = shape ÷ rate.

---

## Slide system

**Template:** `slides/_template/index.html` is the ground truth. Copy it; everything below
comes for free.

**Style:**

- Background warm parchment `#f0ebe0` with a dot-grid overlay; cards near-white `#fffef8`, `border: 2px solid #ccc4e0`, `box-shadow: 4px 4px 0 rgba(80,60,140,.18)`
- Fonts: **DotGothic16** (Google Fonts) for `h1`, the counter and buttons only — **Consolas / Courier New** for everything else: body, formulas, code, side nav
- Palette: `--accent #1a5ca8` sapphire (h1, checkpoints), `--rose #c42848` crimson (speech bubbles), `--honey #b86800` amber (h2, formulas), `--teal #0d7a6e` positive signals, `--mist #6a5888` secondary, `--slate #3a4d7a` methodology callouts, `--text #1c1a30`
- Effects: laser-dot cursor, fairydust trail, click explosion — all already in the template JS
- Side nav: slides numbered; sub-chapters via `data-nav-tier="sub"` plus a `data-nav-section` label
- All visuals are hand-coded inline SVG with a `viewBox` and `max-width:100%` — no external image dependencies
- Buddy sprites are pixel-art 16×16 `shape-rendering="crispEdges"` SVG `<rect>` blocks; the catalog is in the template

**KaTeX:** already wired into the template (CSS + `katex.min.js` + `auto-render.min.js`
with `onload`). Delimiters are `$$…$$` for display and `$…$` for inline. Always keep
`throwOnError: false` so a bad expression degrades instead of breaking the slide. When
retrofitting an old deck, copy the three `<head>` tags and add `.formula .katex` and
`.formula .katex-display` rules.

**Hover tooltips:** `<span class="tip" data-tip-title="Term" data-tip="explanation">term</span>`,
styled with an amber dashed underline. The tooltip JS renders KaTeX inside `data-tip` if you
include `$math$`.

**Buddy assignment** (full sprite catalog is a comment block in the template):

| `buddy_id` | Character | Use for |
|------------|-----------|---------|
| `coin-sprite` | Penny the Cat | Bernoulli, coins, discrete outcomes |
| `owl-sprite` | Hootsworth the Owl | Foundations, survival functions |
| `router-sprite` | Packet the Bunny | Gamma, routers, MLE |
| `hammer-sprite` | Forge the Bear | Hypothesis tests |
| `ridge-sprite` | Ridge the Penguin | OLS, ridge, regularization |
| `prior-sprite` | Bayes the Fox | Priors, conjugate Bayes |

**Decks that exist:**

| Path | Content | Slides |
|------|---------|--------|
| `slides/intro-stats-probability/index.html` | Stats vs probability, distributions, E[X] from scratch, variance, PMF/PDF, Bernoulli, roadmap for all six tasks, Task 2 prep | 15 |
| `slides/ch3-distributions/index.html` | Unit 3 distribution field guide | 19 |
| `slides/exam_tasks/task1-bernoulli.html` | Task 1 Bernoulli vote, p = 0.65 — assumes the intro deck first | 16 |
| `slides/exam_tasks/task2-survival.html` | Task 2 survival: F̄(y), Weibull-2/Weibull-8 mixture, PDF, Jacobian, quartiles | 19 |
| `slides/exam_tasks/task3-exponential.html` | Task 3 routers: S ~ Exp(θ), T = S₁+S₂ ~ Gamma(2, θ), MLE | 21 |
| `slides/exam_tasks/task4-hypothesis.html` | Task 4 hammer z-test — **fail to reject**; z-vs-t trap, power | 18 |
| `slides/exam_tasks/task5-ridge.html` | Task 5 degree-10 OLS + ridge, conditioning and SVD | 18 |
| `slides/exam_tasks/task6-bayes.html` | Task 6 Gamma conjugate Bayes, Gamma(23, 63), rate-vs-scale | 17 |
| `slides/mmm/index.html` | Marketing Mix Modeling, media-plan first | 19 |
| `slides/mmm/ols.html` | OLS as a measurement instrument (A/B tests) | 16 |
| `slides/monks-ds-manual/index.html` | Monks problem→concept field manual | 10 |
| `slides/marketing-ds-solutions/index.html` | Marketing data-science solutions overview | 5 |
| `slides/xgboost/index.html` | XGBoost | 15 |
| `slides/causal-inference/*.html` | Causal inference: overview, ITS, specification curve | 16 / 14 / 11 |
| `slides/vbb/*.html` | VBB client and options decks (separate design system) | 15 / 11 |

**Conventions:** exam task decks are flat files, `slides/exam_tasks/taskN-<topic>.html`, one
per task — no parameter-set suffixes. Register every new deck in `learning/concepts.json`
with its `slide_path` and `related_exam_tasks`. Lead with intuition before formalism and a
visual before a formula.

---

## Causal impact — ITS method distinctions

Interrupted Time Series (ITS) splits into two paradigms that answer different questions.

**Segmented regression ITS** (ordinary least squares, or CausalPy for the Bayesian version):

- Model: `Y = β₀ + β₁t + β₂D + β₃(t−T₀)D`
- β₂ is the immediate level jump at T₀; β₃ is the change in growth rate afterwards
- Answers: did the metric jump, and did the growth rate permanently accelerate?
- Assumes a permanent linear structural break. Best for permanent interventions: site redesigns, pricing changes.

**Counterfactual ITS / BSTS** (Bayesian Structural Time Series, e.g. `tfcausalimpact`):

- Learns trend and seasonality from the pre-period with a state-space model
- Projects a counterfactual ŷ(t) for every post-period day
- α(t) = y(t) − ŷ(t) is the pointwise daily effect; Σα(t) is cumulative lift
- Answers: what was the total lift, how did the daily effect evolve, did it fade?
- Handles non-linear trend and complex seasonality natively; better for temporary effects

**Decision rule:**

- Temporary, bounded effect (promo, campaign) → BSTS cumulative Σα(t). Regression ITS β₃ ≈ 0 and only adds noise.
- Permanent, structural change (UX redesign, pricing) → regression ITS β₂ + β₃. BSTS can confirm direction, but its cumulative grows without bound.
- Unsure → run both and plot BSTS α(t): if it stabilises the change is permanent; if it decays, the BSTS cumulative is the metric.
- "Regression gives the rate of growth" means β₃ — correct but incomplete, since regression also gives β₂. The deeper difference is paradigm: regression fits a formula, BSTS builds a daily counterfactual.

**Regression variants beyond the simple form:** autoregressive / ARIMA-ITS adds lagged Y and
is the most practically important, since plain ITS ignores autocorrelation and inflates the
false-positive rate. Controlled ITS subtracts a concurrent untreated series. Nonlinear-trend
ITS replaces β₁t with a polynomial or spline. Multiple-breakpoint ITS adds a D/slope pair per
intervention. Hierarchical ITS shares priors across units. BSTS absorbs autocorrelation and
nonlinear trend automatically, which is a practical reason to prefer it for messy data.

---

## Reference index

| Need | Document |
|------|----------|
| Exam workflow, output contract, file permissions | `docs/EXAM_WORKFLOW.md` |
| Task branch specs, acceptance criteria | `docs/EXAM_WORKBOOK.md` |
| Teaching rubric, assessment, log schema | `docs/LEARNING_SYSTEM.md` |
| Course book units ↔ topics, external sources | `docs/SOURCES.md` |
| Personal assignment values | `exam_tasks/assignment_values_2.txt` |

---

## What NOT to do

- Don't let `CLAUDE.md` accumulate instructions — it is a pointer to this file, nothing more.
- Don't lead with formalism; anchor with intuition and a concrete example first.
- Don't apply the dark-indigo 90s style from `slides/README.md` — use the actual template.
- Don't forget `show(0);` immediately after the keydown binding in any deck's JS — without it the counter stays blank on load. This bug has recurred repeatedly.
- Don't add KaTeX CDN tags by hand to a new deck; they are already in the template.
- Don't quote the retired parameter set (ξ₂ = 0.58, ξ₄ = 3, ξ₉ = 2, μ₀ = 956, Gamma(35, 51)).
- Don't treat `exam_tasks/user_notebook.ipynb` as authoritative; it is scratch work on old values.
- Don't commit or push unless Elena explicitly asks.
- Don't publish exam solutions to external platforms (IU copyright, plagiarism checks).
- Don't edit `exam_tasks/*.pdf` or `knowledge/*.pdf` — read-only.
- Don't apply the retro slide aesthetic to the workbook `.docx`, notebooks, or exam prose; those stay sober and academic.

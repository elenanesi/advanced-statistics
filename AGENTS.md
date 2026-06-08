## Learned User Preferences

- Always spell out acronyms on first use before using them (e.g. ITS → Interrupted Time Series). Never assume the abbreviation is already known.
- When introducing a taxonomy, make the hierarchy explicit: state whether something is a category/family or a specific model/instance within it.
- When two concepts look similar (e.g. A/B test vs. DiD), call out the distinguishing difference head-on rather than assuming it's obvious.
- Provide brief plain-English definitions for jargon inline where it appears (parenthetical or expandable info-point) — don't require prior stats knowledge.
- Pair abstract/terse definitions with a one-sentence concrete example; Elena prefers concrete over abstract.
- Use expandable `<details>` info-points to keep the main flow scannable while making deeper definitions available on click; avoid walls of text.
- These teaching/communication preferences apply to all slide decks, concept explanations, and teaching materials.

## Learned Workspace Facts

- This repository contains advanced-statistics learning materials including HTML slide decks (in `slides/`) and concept reference files (in `learning/`).
- Slide decks use a retro-cute 90s videogame aesthetic (pixel-art mascots, starfield backgrounds) per the `retro-cute-slides` skill. Typography matches `slides/causal-impact/index.html`: **Press Start 2P** for `h1` and nav buttons only; **Consolas** (with Courier New fallback) for all body text, tables, formulas, and side nav — do not use VT323.
- A `slides/_template/index.html` exists as the base template for new slide decks.
- Slide side nav: main path slides numbered 1–N (`data-nav-tier="core"`); detail slides are sub-chapters under their parent (`data-nav-tier="sub-control"`, `sub-its`, etc.) numbered parent.subindex (e.g. 4.1, 5.2). No separate “deep dive” section — optional detail = sub-chapters. Reference: `slides/causal-models/index.html`.

## Causal Impact — ITS Method Distinctions

Interrupted Time Series (ITS) splits into two paradigms that answer different questions:

**Segmented Regression ITS** (OLS or CausalPy Bayesian):
- Model: `Y = β₀ + β₁t + β₂D + β₃(t−T₀)D`
- β₂ = immediate level jump at T₀; β₃ = change in growth rate (slope change) after T₀
- Directly answers: "Did the metric jump? Did the growth rate permanently accelerate?"
- Assumes a permanent linear structural break. CausalPy is the Bayesian version (same formula, posterior distributions on β₂ and β₃ instead of point estimates + frequentist CIs).
- Best for permanent interventions: website redesigns, pricing changes that permanently alter behaviour.

**Counterfactual ITS / BSTS** (tfcausalimpact):
- Learns the time series dynamics (trend + seasonality) in the pre-period via a state-space model.
- Projects a counterfactual ŷ(t) forward for every post-period day.
- α(t) = y(t) − ŷ(t) = pointwise daily effect; Σα(t) = cumulative total lift (e.g. £300K over 4 days).
- Directly answers: "What was the total cumulative lift? How did the daily effect evolve? Did it fade?"
- Handles non-linear trends and complex seasonality natively. Better for temporary or time-varying effects.

**Decision rule — choose or run both:**
- Temporary/bounded effect (promo, campaign) → BSTS cumulative Σα(t) is the right output; regression ITS β₃ ≈ 0 and adds noise. Run BSTS primarily.
- Permanent/structural change (UX redesign, pricing) → Regression ITS β₂ + β₃ is the right question; BSTS can validate direction but cumulative grows indefinitely.
- Unsure temporary vs permanent → run both and plot BSTS α(t) over time: if α(t) stabilises → permanent (regression interpretation); if it decays → temporary (BSTS cumulative is the metric).
- When an agent says "regression gives the rate of growth" they mean β₃ — correct but incomplete (regression also gives β₂). The deeper difference is paradigm: regression fits a formula; BSTS builds a daily counterfactual.

**ITS regression variants (beyond simple segmented regression):**
- Simple: `Y = β₀ + β₁t + β₂D + β₃(t−T₀)D`
- Autoregressive / ARIMA-ITS: adds lagged Y terms — most practically important, handles autocorrelation that plain ITS ignores (inflates FPR if skipped).
- Controlled ITS: subtracts a concurrent non-treated comparison series before fitting — strongest non-experimental ITS design.
- Nonlinear trend ITS: replaces β₁t with polynomial or natural spline — use when pre-period trend curves.
- Multiple breakpoint ITS: adds D/slope-change pairs for each intervention — use for sequential changes on the same series.
- Hierarchical ITS: multiple units sharing priors — panel-data version.
- BSTS absorbs autocorrelation and nonlinear trend automatically via its state-space components, which is a practical reason to prefer it over plain regression ITS for messy real-world data.

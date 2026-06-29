# CLAUDE.md — Advanced Statistics workspace
> Read this at the start of every session. Last updated: 2026-06-24.
> Detailed playbooks live in `docs/`. This file is the fast-path session bootstrap.

---

## Session startup (do these first, in order)

1. **Classify intent** from the latest message: `exam` | `teach` | `slides` | `open_stats` | `general` | `mixed`. Don't over-index on repo layout — answer what was actually asked.
2. **If exam work**: open `exam_tasks/assignment_values.txt` to verify branch values. Task 1 notebook cells exist; Tasks 2–6 are not done. Personal path is pre-resolved in `docs/EXAM_WORKBOOK.md`.
3. **If teaching**: skim `learning/session_log.jsonl` (last 10 lines) and `learning/profile.json` before explaining anything.
4. **If slides**: the real template is `slides/_template/index.html` — use it, not the style described in `slides/README.md` (those docs describe an older style that was never shipped).

---

## Who Elena is (working profile)

**Role & context:** Associate Director in Data Science; completing IU DLMDSAS01 Advanced Statistics exam (2026). Intermediate-to-advanced statistics overall but real gaps in formal probability theory and Bayesian stats beyond applied use. Strong ML practitioner; intermediate software engineer.

**How she actually learns (observed, not self-reported):**

| Pattern | Evidence from session |
|---------|----------------------|
| Intuition MUST come before formalism | Direct quote: *"'X : Ω → R' means almost nothing to me"* — the definition failed; the label-gun analogy worked |
| Needs the conceptual WHY, not just the WHAT | Asked *"why is X called a random variable if 0 and 1 are fixed?"* — probes coherence, not just definition |
| Visual learner | Direct quote: *"I'm a very visual person, an image and a comparison with something I can imagine helps me learning"* — said this explicitly after first draft lacked visuals |
| Thinks in prerequisite chains | Spontaneously asked to split one long deck into intro deck + task deck — she naturally organizes by dependency |
| E[X] was genuinely unclear until made concrete | Said *"I'm actually still not 100% clear on this"* after a seesaw diagram existed — needed the weighted-average-from-dice framing, not just the formula |

**Communication rules (cross-session, always apply):**
- Spell out acronyms on first use; never assume abbreviations are known
- Pair every abstract definition with a one-sentence concrete example
- Call out distinctions head-on when two things look similar (don't assume the difference is obvious)
- Provide plain-English parenthetical definitions inline — don't force her to look them up
- Use `<details>` for deeper definitions to keep main flow scannable
- Be concise and direct; she explicitly prefers no filler

---

## Slide system — what actually exists

**Current template:** `slides/_template/index.html` is the ground truth. Ignore `slides/README.md` for style — it describes a dark 90s aesthetic that was never used in practice.

**Actual style (as of 2026-06-24):**
- Background: warm parchment `#f0ebe0`, dot-grid overlay
- Cards: near-white `#fffef8`, `border: 2px solid #ccc4e0`, `box-shadow: 4px 4px 0 rgba(80,60,140,.18)`
- Fonts: **DotGothic16** (Google Fonts) for `h1`, counter, buttons only — **Consolas/Courier New** for everything else (body, formulas, code, side nav)
- Palette: `--accent #1a5ca8` (sapphire), `--rose #c42848` (crimson), `--honey #b86800` (amber), `--teal #0d7a6e`, `--mist #6a5888`, `--text #1c1a30`
- Effects: laser-dot cursor + fairydust trail + click explosion (all in the template JS)
- Side nav: slides numbered; sub-chapters via `data-nav-tier="sub"` + `data-nav-section` label
- All visuals: hand-coded inline SVG with `viewBox` and `max-width:100%` — no external image deps
- Buddy sprites: pixel-art 16×16 `shape-rendering="crispEdges"` SVG `<rect>` blocks — catalog in `_template/index.html`

**Decks that exist:**

| Path | Content | Status |
|------|---------|--------|
| `slides/intro-stats-probability/` | Stats vs probability, distributions, E[X] from scratch (die analogy), variance, PMF/PDF, Bernoulli, distribution roadmap for all 6 tasks | Created 2026-06-24 |
| `slides/task1-bernoulli/` | Full Task 1 proof deck — assumes intro deck done first | Extended 2026-06-24 |
| `slides/causal-inference/` | Causal inference methods (ITS, DiD, SCA) | Exists, separate domain |
| `slides/task2-survival/` | Task 2 survival analysis | Status unknown — check |
| `slides/vbb/` | VBB (separate design system) | Not part of stats quest template |

**When creating a new deck:** copy `_template/`, use DotGothic16 + Consolas, pick the right buddy from the sprite catalog (Penny=Bernoulli, Hootsworth=Owl/survival, Packet=Gamma/router, Forge=hypothesis tests, Ridge=OLS/ridge, Bayes=conjugate priors), put intro-before-formalism, visual-before-formula.

---

## Exam task status (as of 2026-06-24)

| Task | Branch | Status |
|------|--------|--------|
| 1 | Bernoulli, p=0.58 | Notebook started; slides complete |
| 2 | Survival mixture, ξ4=3 | Not started |
| 3 | Gamma(7,θ) router MLE | Not started |
| 4 | "Higher weights?" hypothesis test | Not started |
| 5 | Degree-10 polynomial + ridge | Not started |
| 6 | Bayesian Gamma posterior | Not started |

Notebook: `exam_tasks/bernoulli_vote_analysis.ipynb`

---

## Key concepts with confirmed understanding gaps

These came up this session; update `learning/profile.json` when gaps close:

- **E[X]** — struggled with *what it is* until concrete die example (values × probabilities → weighted average → long-run average). Now solid after intro deck. Do not assume it's understood if this is the first time you're teaching it.
- **"Why random variable"** — needed the "deterministic function, random input" framing + capital X vs lowercase x distinction. Fixed in task1-bernoulli slide.
- **PMF vs density** — she knows the distinction; reinforce that "density" is wrong for Bernoulli.

---

## Detailed workflow references

| Need | Document |
|------|----------|
| Full exam workflow + output contract | `docs/AGENTS.md` |
| Task branch specs, acceptance criteria | `docs/EXAM_WORKBOOK.md` |
| Teaching rubric, assessment, log schema | `docs/LEARNING_SYSTEM.md` |
| Causal inference domain knowledge | Root `AGENTS.md` (still exists; has ITS/BSTS decision rules) |
| Personal assignment values | `exam_tasks/assignment_values.txt` |

---

## What NOT to do

- Don't apply the dark-indigo 90s style from `slides/README.md` — use the actual template
- Don't lead with formalism for Elena — always anchor with intuition and a concrete example first
- Don't commit unless explicitly asked
- Don't publish exam solutions to external platforms (IU copyright)
- Don't edit `exam_tasks/*.pdf` or `knowledge/*.pdf` (read-only)

# CLAUDE.md — Advanced Statistics workspace
> Read this at the start of every session. Last updated: 2026-08-06.
> Detailed playbooks live in `docs/`. This file is the fast-path session bootstrap.

---

## Cross-agent learning memory (Cursor / Claude / Codex)

| Surface | Path | Role |
|---------|------|------|
| **Source of truth** | `learning/profile.json` + `learning/session_log.jsonl` | Preferences, mastery, misconceptions |
| Cursor rule | `.cursor/rules/elena-learning.mdc` | Always-on teach contract |
| Cursor skill | `.cursor/skills/elena-teaching/SKILL.md` (+ `~/.cursor/skills/elena-teaching/`) | Deep teach/slides workflow |
| Claude bootstrap | this file | Session checklist |
| Codex bootstrap | `AGENTS.md` | Same prefs + causal-impact notes |
| Playbooks | `docs/LEARNING_SYSTEM.md`, `docs/AGENTS.md` | Rubric, log schema, exam workflow |

When Elena states a new preference or misconception: update `profile.json` and append `session_log.jsonl` in the same turn.

---

## Session startup (do these first, in order)

1. **Classify intent** from the latest message: `exam` | `teach` | `slides` | `open_stats` | `general` | `mixed`. Don't over-index on repo layout — answer what was actually asked.
2. **If exam work**: open `exam_tasks/assignment_values.txt` to verify branch values. Task 1 notebook cells exist; Tasks 2–6 notebook not done. Personal path is pre-resolved in `docs/EXAM_WORKBOOK.md`.
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

**Actual style (as of 2026-07-02):**
- Background: warm parchment `#f0ebe0`, dot-grid overlay
- Cards: near-white `#fffef8`, `border: 2px solid #ccc4e0`, `box-shadow: 4px 4px 0 rgba(80,60,140,.18)`
- Fonts: **DotGothic16** (Google Fonts) for `h1`, counter, buttons only — **Consolas/Courier New** for everything else (body, formulas, code, side nav)
- Palette: `--accent #1a5ca8` (sapphire), `--rose #c42848` (crimson), `--honey #b86800` (amber), `--teal #0d7a6e`, `--mist #6a5888`, `--text #1c1a30`
- Effects: laser-dot cursor + fairydust trail + click explosion (all in the template JS)
- Side nav: slides numbered; sub-chapters via `data-nav-tier="sub"` + `data-nav-section` label
- All visuals: hand-coded inline SVG with `viewBox` and `max-width:100%` — no external image deps
- Buddy sprites: pixel-art 16×16 `shape-rendering="crispEdges"` SVG `<rect>` blocks — catalog in `_template/index.html`

**KaTeX math rendering (added 2026-07-02 — now in template and all decks):**
- CDN: KaTeX v0.16.11 via `cdn.jsdelivr.net` (3 tags: CSS + katex.min.js + auto-render.min.js with `onload`)
- Delimiters: `$...$` = display block, `\(...\)` = inline
- Always set `throwOnError: false` — silently degrades rather than breaking the slide
- `.formula` CSS: keeps Consolas for plain text; KaTeX auto-overrides font for math elements inside `$...$`
- If adding KaTeX to an existing deck: copy the 3 `<link>`/`<script>` tags from the template `<head>`, add `.formula .katex` and `.formula .katex-display` rules to the `<style>` block

**Hover tooltips (added 2026-07-02 — now in template and all decks):**
- Markup: `<span class="tip" data-tip-title="Term name" data-tip="explanation text">term</span>`
- Style: amber dashed underline (`border-bottom: 2px dashed var(--honey); cursor: help`)
- The tooltip JS block renders KaTeX inside tooltip content if you include `$math$` in `data-tip`
- Copy the full `.tip` / `#tip-box` / `.tip-label` CSS + tooltip IIFE JS from the template

**Decks that exist:**

| Path | Content | Status |
|------|---------|--------|
| `slides/intro-stats-probability/` | Stats vs probability, distributions, E[X] from scratch (die analogy), variance, PMF/PDF, Bernoulli, distribution roadmap for all 6 tasks; Task 2 prep slides (survival function, mixture) | KaTeX + tooltips added 2026-07-02; 15 slides |
| `slides/exam_tasks/task1-bernoulli.html` | Full Task 1 proof deck — assumes intro deck done first | KaTeX + tooltips |
| `slides/exam_tasks/task2-survival.html` | Task 2 survival — F̄(y), mixture, PDF, Jacobian, quartiles | KaTeX + tooltips; 16 slides |
| `slides/exam_tasks/task3-gamma-mle.html` | Task 3 Gamma routers + MLE (120→720 flag) | KaTeX + tooltips; 18 slides |
| `slides/exam_tasks/task4-hypothesis.html` | Task 4 hammer z-test (higher weights); z-vs-t trap | Created 2026-08-06; Forge |
| `slides/exam_tasks/task5-ridge.html` | Task 5 degree-10 OLS + ridge | Created 2026-08-06; Ridge |
| `slides/exam_tasks/task6-bayes.html` | Task 6 Gamma conjugate Bayes (Hogg rate form) | Created 2026-08-06; Bayes |
| `slides/exam_tasks/task*-99d9e51.html` | **Current** decks for parameter set `99d9e51e` — the six above are superseded | Created 2026-08-22 |
| `slides/ch3-distributions/` | Unit 3 distribution field guide | 19 slides |
| `slides/monks-ds-manual/` | Monks problem→concept field manual (marketing/creative/ecom) | Created 2026-08-06 |
| `slides/causal-inference/` | Causal inference methods (ITS, DiD, SCA) | Separate domain |
| `slides/vbb/` | VBB (separate design system) | Not part of stats quest template |

**Convention:** all exam task decks are flat files: `slides/exam_tasks/taskN-<topic>.html`.

**When creating a new deck:** copy `_template/`, use DotGothic16 + Consolas, pick the right buddy from the sprite catalog (Penny=Bernoulli, Hootsworth=Owl/survival, Packet=Gamma/router, Forge=hypothesis tests, Ridge=OLS/ridge, Bayes=conjugate priors), put intro-before-formalism, visual-before-formula.

KaTeX and tooltips are already wired into the template — they come for free when you copy it. After writing the keydown event binding in the JS, **always add `show(0);` immediately after it** — omitting this leaves the counter blank on load (recurring bug fixed in all existing decks 2026-07-02).

---

## Exam task status (as of 2026-08-22)

⚠ **The parameter set was regenerated.** Source of truth is now
`exam_tasks/assignment_values_2.txt`, signature `99d9e51eff0fb88f6911fa8b4392742591f8f6da`.
`assignment_values.txt` is the superseded first run, kept for provenance only.
Two branches changed (Task 2: ξ4 3→1; Task 3: ξ9 2→0) and Task 4's conclusion
flipped from reject to fail-to-reject. Full detail in `docs/EXAM_WORKBOOK.md`.

| Task | Branch (current) | Status |
|------|------------------|--------|
| 1 | Bernoulli, p=0.65 | Workbook prose done; deck `task1-bernoulli-99d9e51.html` |
| 2 | Survival mixture, **ξ4=1** (Weibull shapes 2 and 8) | Workbook prose done; deck `task2-survival-99d9e51.html` |
| 3 | **Exponential**, ξ9=0 → T~Gamma(2,θ) | Workbook prose done; deck `task3-exponential-99d9e51.html` |
| 4 | "Higher weights?" — **fail to reject** | Workbook prose done; deck `task4-hypothesis-99d9e51.html` |
| 5 | Degree-10 polynomial + ridge | Workbook prose done; deck `task5-ridge-99d9e51.html` |
| 6 | Bayesian Gamma posterior, Gamma(23,63) | Workbook prose done; deck `task6-bayes-99d9e51.html` |

**Deliverable:** `deliverables/workbook/` — run `build.sh` to produce
`Advanced_Workbook_DLMDSAS01_DRAFT.docx`. `compute.py` owns every number;
`src/*.md` carries no literal results, only `{{task.key}}` tokens.

The old `exam_tasks/bernoulli_vote_analysis.ipynb` predates the regeneration and
is built on superseded values. The original slide decks (without the `-99d9e51`
suffix) are likewise on the old parameter set and are kept only for comparison.

The Task 3 **120→720 typo warning no longer applies** — it only affected the
ξ9=2 branch, which is no longer the personal one.

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
- Don't forget `show(0)` after the keydown binding in any deck's JS — the counter stays blank without it
- Don't add KaTeX CDN tags manually to new decks — they're already in the template; just copy the template

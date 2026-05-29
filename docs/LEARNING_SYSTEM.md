# Learning system — teach, assess, remember, visualize

How agents (and human tutors) adapt teaching for Elena and maintain shared state across tools/models.

---

## Principles

1. **Assess before lecture** — short diagnostics beat long monologues.
2. **Spaced reuse** — tie explanations to exam tasks **only when relevant**; many questions need no exam link.
3. **Shared memory** — `learning/profile.json` + `learning/session_log.jsonl` are the cross-agent source of truth (optional for one-off `general` chat).
4. **Multimodal preference** — HTML slides (90s game aesthetic) complement notebook math.
5. **Honest uncertainty** — distinguish “can compute” vs “understands why.”
6. **Open scope** — Statistics beyond the IU book, other courses, and non-stats questions are in scope; see [AGENTS.md](AGENTS.md) § Open questions.

---

## Off-exam and off-syllabus statistics

When the question is **not** one of Tasks 1–6:

- Use the same rubric and teaching modes; do **not** open or edit `bernoulli_vote_analysis.ipynb` unless the user asks to connect or practice there.
- Prefer `knowledge/Advanced_statistics_Course_Book.pdf` when the topic exists in the TOC; otherwise use [SOURCES.md](SOURCES.md) or standard references.
- Log with `"intent": "open_stats"` and `"related_exam_tasks": []` when you append to `session_log.jsonl`.
- Register new concepts in `learning/concepts.json` with optional `"tags": ["off-syllabus"]` so slides can be built later without implying an exam task exists.

**Unrelated (non-stats) questions:** Answer normally. Skip profile/log unless the user wants preferences captured (e.g. “I learn better with diagrams” still belongs in `profile.json`).

---

## Understanding rubric

After diagnostics, assign one level per concept:

| Level | Signals | Teaching strategy |
|-------|---------|-------------------|
| `novice` | Cannot define terms; random guesses | Story + intuition, one formula, visual slide, tiny numeric example |
| `developing` | Partial definition; arithmetic errors | Step-by-step derivation, check understanding mid-way |
| `solid` | Correct definitions; can do standard problem | Edge cases, exam-style question, link to next concept |
| `expert` | Explains assumptions; spots traps | Skip basics; challenge problems or proof sketches |

Update `learning/profile.json` → `concepts.<id>.mastery` when level changes.

---

## Diagnostic question bank (templates)

Use 1–3 per session before teaching:

- **Define:** “In one sentence, what is a conjugate prior?”
- **Compute:** “If \(X\sim\mathrm{Bernoulli}(0.58)\), what is \(\mathbb{E}[X]\)?”
- **Conceptual:** “Why do we need \(\xi_5+\xi_7=1\) in Task 2?”
- **Transfer:** “When would a t-test be wrong for the hammer task?”
- **Meta:** “What part of that explanation felt unclear — formula, graph, or words?”

Record prompts and summarized answers in the session log.

---

## Teaching modes (`preferences.preferred_modes`)

Rank modes the learner likes (update from reactions in log):

| Mode ID | When to use |
|---------|-------------|
| `visual` | Plots, slides, color-coded distributions |
| `narrative` | Stories (owls, routers, hammers) |
| `algebra` | Full symbolic derivation first |
| `computational` | Code-forward, inspect numbers |
| `exam_drill` | IU task format, timed feel |
| `socratic` | Agent asks, user derives |

If unknown, start with **`visual` + `narrative`**, then ask which helped.

---

## Strengths / weaknesses tracking

**`profile.json` fields:**

- `strengths[]` — e.g. “comfortable with Python plots”
- `weaknesses[]` — e.g. “hypothesis test tail confusion”
- `misconceptions[]` — objects with `concept`, `belief`, `correction`, `last_seen`

When the user says “I don’t get X” or fails a diagnostic, add or refresh a misconception entry.

---

## Session log schema (`learning/session_log.jsonl`)

**Append one JSON object per line** (JSONL). Never rewrite the whole file.

**`intent` values:** `teach` | `open_stats` | `exam_help` | `slides` | `general`

```json
{
  "ts": "2026-05-29T14:30:00Z",
  "agent": "cursor-composer",
  "concept_id": "bernoulli-expectation",
  "intent": "teach",
  "diagnostic": {
    "questions": ["Can expectation be computed for one Bernoulli trial outcome?"],
    "user_responses_summary": "Confused outcome vs expectation",
    "assessed_level": "developing"
  },
  "explanation_mode": ["visual", "narrative"],
  "summary": "Clarified E[X] vs single realized vote",
  "user_reaction": "helpful",
  "user_reaction_notes": "Wanted more on measurability hypotheses",
  "follow_ups": ["kolmogorov-axioms-light"],
  "related_exam_tasks": [1],
  "artifacts_updated": ["learning/profile.json", "exam_tasks/bernoulli_vote_analysis.ipynb"]
}
```

**`user_reaction` enum:** `helpful` | `neutral` | `confused` | `too_long` | `too_shallow` | `wants_practice` | `wants_slide`

Other agents: **read the last 10–20 lines** before teaching the same concept.

---

## Concept registry (`learning/concepts.json`)

Each concept:

```json
{
  "id": "bernoulli-expectation",
  "title": "Expectation of a Bernoulli trial",
  "mastery": "solid",
  "prerequisites": ["probability-space-basics"],
  "related_exam_tasks": [1],
  "course_book": ["Unit 1 — 1.3 Probability Distributions"],
  "slide_path": "slides/bernoulli-expectation/index.html",
  "slide_status": "draft",
  "buddy_id": "coin-sprite"
}
```

`slide_status`: `none` | `queued` | `draft` | `ready`

When mastery ≥ `solid` and user enjoyed visuals → set `slide_status` to `queued` or refresh slide.

---

## When to create or update slides

Create `slides/<concept-id>/` when any of:

- User asks for slides on a concept
- Concept is `developing` or below after two confused reactions
- Concept is exam-critical (linked task incomplete) and visual mode is preferred
- User says a slide would help

**Do not** block exam work solely for slides unless user prioritizes learning track.

---

## Cross-agent handoff

Exportable summary for a new model (paste or point to files):

1. `learning/profile.json` — preferences + mastery map
2. Last 5 log entries for the active `concept_id`
3. Relevant notebook headings (exam)
4. `slides/<concept-id>/` if exists

---

## Discovering “how Elena learns best”

Run a **lightweight calibration** early (can span multiple sessions):

| Session | Focus |
|---------|--------|
| 1 | One diagnostic per major unit (probability, distributions, estimation, testing, Bayesian) |
| 2 | Try two modes on the weakest unit; log `user_reaction` |
| 3 | Set `profile.json` → `preferences` ranks from evidence |

Revise every ~5 sessions or when user says teaching style isn’t working.

**Success metric:** User can solve a parallel mini-problem without hints, and rates explanation `helpful` or asks for harder practice—not just “got the exam answer.”

---

## Concepts beyond the course book

Allowed and encouraged when they deepen understanding:

- Measure-theoretic intuition (light touch)
- LLN/CLT connections to hammer test
- Conjugate prior catalog (Beta-Gamma, etc.)
- Ridge as prior / MAP view (Task 5)

Always label **“beyond Unit X”** so exam write-ups stay aligned with IU expectations unless user wants enrichment sections.

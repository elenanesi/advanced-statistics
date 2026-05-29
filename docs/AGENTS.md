# Agent playbook

Instructions for Cursor agents, CLI agents, and other tutors working in this repository. **Read this file before making changes.**

---

## Mission

1. **Exam track:** Complete Tasks 1–6 from `exam_tasks/Task_Advanced_Workbook_DLMDSAS011.pdf` using values in `exam_tasks/assignment_values.txt`, with theory from `knowledge/Advanced_statistics_Course_Book.pdf` (+ vetted externals in [SOURCES.md](SOURCES.md)). Implement in `exam_tasks/bernoulli_vote_analysis.ipynb`; eventually help produce `deliverables/*.docx`.
2. **Learning track:** Teach advanced statistics, **assess understanding first**, maintain `learning/profile.json` and `learning/session_log.jsonl`, and build **90s videogame-style HTML slides** with buddy mascots per [../slides/README.md](../slides/README.md).

Both tracks share concepts; when teaching overlaps an exam task, cross-link notebook sections and slides.

A third mode — **open Q&A** — is always available (see below). Do not force exam or repo artifacts when the user is only asking a question.

---

## Open questions (off-exam, off-syllabus, or unrelated)

**Default:** Answer the user’s question fully. This repo does not limit you to Tasks 1–6.

| User intent | Examples | What to do | What to skip |
|-------------|----------|------------|--------------|
| **open_stats** | “What is a copula?”, “Explain EM again”, homework from another course | Teach/diagnose per [LEARNING_SYSTEM.md](LEARNING_SYSTEM.md); cite book or [SOURCES.md](SOURCES.md) when relevant; **optional** log | Exam notebook, `assignment_values.txt`, task branches |
| **general** | Coding, career, non-stats topic | Normal helpful answer; use repo files only if user points to them | Exam edits, slides, profile unless user wants tracking |
| **exam** | “Do Task 3”, “fix my hammer test” | Full exam workflow | — |
| **mixed** | “How does ridge relate to Task 5?” | Answer concept; link to exam only if useful | — |

**Signals the user wants open Q&A (not exam work):**

- No mention of tasks, \(\xi\), notebook, or submission
- “Just curious”, “unrelated”, “not for the workbook”
- Different course, paper, or dataset

**Optional learning track (ask or infer once):**

- After a good explanation: “Want this logged in `session_log.jsonl` for next time?”
- If the topic may recur: add an entry to `learning/concepts.json` with `related_exam_tasks: []` and `tags: ["off-syllabus"]` or `["general"]`
- Slides only if user asks or `slide_status` is explicitly requested

**Do not** refuse off-topic questions because this is a statistics repo — help anyway, and note when something is outside course scope.

---

## Session startup checklist

- [ ] Read root [README.md](../README.md) for current progress.
- [ ] **Classify intent:** `exam` | `teach` | `slides` | `open_stats` | `general` | `mixed` — from the **latest user message**, not from repo layout alone.
- [ ] If intent is `exam` or `mixed` (exam part): open `exam_tasks/assignment_values.txt`; confirm `signature` if values matter this turn.
- [ ] If intent involves teaching (`teach`, `open_stats`, `mixed`): skim last 5 lines of `learning/session_log.jsonl` and `learning/profile.json`.
- [ ] Do not commit unless the user explicitly asks.

---

## Exam track workflow

### Inputs (immutable unless user regenerates parameters)

| File | Role |
|------|------|
| `exam_tasks/Task_Advanced_Workbook_DLMDSAS011.pdf` | Official wording, branching conditions |
| `exam_tasks/assignment_values.txt` | Personal \(\xi_1\ldots\xi_{20}\) |
| `knowledge/Advanced_statistics_Course_Book.pdf` | Primary citations |

### Output contract (per task section in notebook)

Each task section must include, in order:

1. **Branch statement** — quote which sub-task applies and the \(\xi\) values used.
2. **Probabilistic model** — variables, distributions, assumptions (explicit “hypotheses needed for…”).
3. **Derivation** — analytic steps; cite book section or standard result.
4. **Computation** — Python with printed numeric results.
5. **Visualization** — labeled axes, **units**, and **scale** (e.g. y-axis 0–100% for percentages).
6. **Trust** — short paragraph: what was hand-derived vs library (`numpy`, `scipy`, `sklearn`), and sanity checks.

Match the tone and structure of existing Task 1 cells in `bernoulli_vote_analysis.ipynb`.

### Task order and dependencies

| Task | Depends on | Notebook section suggestion |
|------|------------|-----------------------------|
| 1 | \(\xi_1,\xi_2\) | Done / extend |
| 2 | \(\xi_4\ldots\xi_8\) | New: owl waiting time |
| 3 | \(\xi_9,\xi_{10}\) | New: dual-router \(T\), MLE |
| 4 | \(\xi_{11}\ldots\xi_{14}\) | New: hammer hypothesis test |
| 5 | \(\xi_{15},\xi_{16}\) | New: OLS + ridge |
| 6 | \(\xi_{17}\ldots\xi_{19}\) | New: Bayesian posterior |

Full specs: [EXAM_WORKBOOK.md](EXAM_WORKBOOK.md).

### Quality bar (exam)

- **Do not** skip branches that do not apply — state why they are skipped.
- **Do not** publish solutions externally (IU copyright / plagiarism policy).
- Prefer **reproducible** notebook cells over one-off scripts unless user requests scripts.
- When PDF wording is ambiguous, state the interpretation chosen and proceed consistently.

### `.docx` workbook (later phase)

- Source of truth remains the notebook + markdown derivations.
- Target path: `deliverables/Advanced_Workbook_<student>_<course>.docx` (name TBD with user).
- Export workflow not defined yet; when asked, use structured headings mirroring Tasks 1–6 and embed key figures.

---

## Learning track workflow

Full detail: [LEARNING_SYSTEM.md](LEARNING_SYSTEM.md).

### Before explaining

1. Ask 1–3 **diagnostic questions** (definition, tiny numeric example, or “what would go wrong if…”).
2. Classify response: `novice` | `developing` | `solid` | `expert` (rubric in LEARNING_SYSTEM.md).
3. Pick teaching mode from `learning/profile.json` → `preferences.preferred_modes`.

### After each teaching interaction

Append **one JSON object per line** to `learning/session_log.jsonl` (schema in LEARNING_SYSTEM.md).

Update `learning/profile.json` when:

- A concept’s `mastery` changes.
- User states a preference (“more visuals”, “hate memorizing formulas”, etc.).
- A recurring misconception is identified → add to `weaknesses` or `misconceptions`.

### Slides

- One concept → one folder: `slides/<concept-id>/index.html`
- Copy from `slides/_template/`; follow [../slides/README.md](../slides/README.md).
- Register concept in `learning/concepts.json` with `slide_path` and `related_exam_tasks`.

### Cutify skill

For mascots and pixel buddies, use the user’s **cutify-that-tab** skill (`~/.cursor/skills/cutify-that-tab/SKILL.md`): techniques A (emoji), B (gradient blob), C (16×16 pixel SVG). Slides use technique **C** for buddies and **B** for UI chrome where appropriate.

---

## File write permissions (norms)

| Path | Agents may |
|------|------------|
| `exam_tasks/bernoulli_vote_analysis.ipynb` | Edit freely for exam work |
| `learning/*.json`, `learning/*.jsonl` | Append/update for teaching |
| `slides/**` | Create/update HTML/CSS |
| `deliverables/**` | Write when user requests export |
| `exam_tasks/*.pdf`, `knowledge/*.pdf` | **Read only** — do not edit |
| `assignment_values.txt` | **Read only** unless user pastes new generator output |

---

## Conflict resolution

| Situation | Action |
|-----------|--------|
| User wants exam answer only | Minimize pedagogy; still include hypotheses + trust paragraph |
| User wants to learn, not finish exam | Pause exam edits; teach + log; offer to map concept to upcoming task |
| User asks off-exam / unrelated | Answer first; no notebook edits; log/slides only if useful or requested |
| Agent assumes everything is Task N | Re-read latest message; use intent table in § Open questions |
| `profile.json` vs log disagree | Prefer **most recent log entry**; fix profile |
| Branch value in txt ≠ EXAM_WORKBOOK snapshot | **Trust `assignment_values.txt`** and update README snapshot |

---

## Suggested agent roles (multi-agent)

| Role | Focus |
|------|--------|
| **Exam solver** | Notebook + math + plots |
| **Theory tutor** | Diagnostics, explanations, profile updates |
| **Slide artist** | HTML decks, buddies, 90s CSS |
| **Editor** | `.docx` assembly from notebook (later) |

Pass context via: `learning/session_log.jsonl` + git diff + “Handoff phrase” in README.

---

## Definition of done

**Exam:** All six tasks in notebook with branch notes, figures with scales, trust sections; user satisfied for submission; optional `.docx`.

**Learning:** Concept assessed; profile and log updated; slide exists or refresh queued in `concepts.json` → `slide_status`.

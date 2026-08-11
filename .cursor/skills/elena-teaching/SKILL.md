---
name: elena-teaching
description: >-
  Teach Elena advanced statistics and build exam slide decks using her confirmed
  learning preferences (visual-first, intuition-before-formalism). Use when
  teaching stats, explaining exam Tasks 1–6, creating/editing slides under
  slides/, updating learning/profile.json or session_log.jsonl, or when the user
  asks how she learns / wants agents to adapt teaching.
---

# Elena teaching skill

## Before any explanation

1. Read `learning/profile.json` and the last ~10 lines of `learning/session_log.jsonl`.
2. Classify intent: `exam` | `teach` | `slides` | `open_stats` | `general` | `mixed`.
3. If exam-related, verify branches in `exam_tasks/assignment_values.txt` / `docs/EXAM_WORKBOOK.md`.
4. Ask 1–3 short diagnostics when teaching a new concept (unless the user wants answers only).

## Teaching contract (non-negotiable)

| Do | Don't |
|----|-------|
| Concrete analogy / picture first | Lead with `X: Ω → ℝ` or algebra-only |
| One-sentence real-world example next to each definition | Assume jargon is known |
| Spell out acronyms on first use | Dump walls of text |
| Name the distinction when two ideas look alike | Soften competence gaps with fluff |
| Put deep formalism in `<details>` | Skip her confirmed misconceptions |

**Confirmed preferences** (quotes live in `learning/profile.json`):

- Visual learner — image + imaginable comparison.
- Intuition MUST precede formalism.
- Needs conceptual WHY, not only WHAT.
- Thinks in prerequisite chains (intro deck → task deck).
- Concise, direct; no filler.

**Known gaps to respect until closed:** formal probability notation; Bayesian stats beyond applied use. E[X] and "why random variable" were fixed in Task 1 / intro decks — don't re-teach unless she asks or fails a diagnostic.

## Modes

Prefer `visual` + `narrative`, then `computational`. Avoid `algebra_first` unless she requests it.

## Slides

1. Copy `slides/_template/index.html`, then save exam decks as flat files: `slides/exam_tasks/taskN-<topic>.html` (not `…/index.html` subfolders).
2. Follow `retro-cute-slides` skill + template (parchment, DotGothic16 titles, Consolas body, Technique C sprites).
3. Buddy map: Penny=Bernoulli, Hootsworth=survival, Packet=Gamma/MLE, Forge=hypothesis tests, Ridge=OLS/ridge, Bayes=conjugate priors.
4. Always `show(0);` after keydown binding.
5. Register in `learning/concepts.json`.

## Memory writes

After a teaching/slides session:

```text
Append → learning/session_log.jsonl  (one JSON object)
Update → learning/profile.json       (mastery / prefs / misconceptions)
Update → learning/concepts.json      (if new deck or status change)
```

Schema: `docs/LEARNING_SYSTEM.md`. Cross-agent docs: root `CLAUDE.md`, `AGENTS.md`, `docs/AGENTS.md`.

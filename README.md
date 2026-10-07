# Advanced Statistics — Exam Workbook & Personalized Learning

Dual-purpose repository for **(1)** completing the IU Advanced Statistics workbook exam (`DLMDSAS01`) with personal parameter values, and **(2)** teaching advanced statistics concepts in a way that adapts to the learner’s understanding, preferences, and progress.

**Primary human:** Elena  
**Course:** DLMDSAS01 — Advanced Statistics (IU Internationale Hochschule)

---

## Goals (read this first)

| Goal | Deliverables | Where to work |
|------|----------------|---------------|
| **1. Exam workbook** | Solutions with proofs/citations, a reproducible notebook, and the formal `.docx` workbook | [`deliverables/workbook/`](deliverables/workbook/) |
| **2. Concept teaching** | Understanding checks, learner profile, session log, cute HTML concept slides | [`learning/`](learning/), [`slides/`](slides/) |
| **3. Open Q&A** | Answers, intuition, optional log/slides — **no exam notebook edits required** | Chat in Cursor; see [docs/EXAM_WORKFLOW.md](docs/EXAM_WORKFLOW.md) § Open questions |

You can ask about **any** statistics topic (even outside the course book) or **unrelated** subjects in this workspace. Agents should answer directly and only pull in exam files when you want that connection.

Agents and tutors: start with **[AGENTS.md](AGENTS.md)** — the single instruction file for every agent, Claude included. It links every workflow, file, and rule.

---

## Repository layout

```
advanced_statistics/
├── README.md                 ← you are here
├── AGENTS.md                 ← single instruction file for ALL agents (start here)
├── CLAUDE.md                 ← redirect: "read AGENTS.md"
├── docs/
│   ├── EXAM_WORKFLOW.md      ← checklists, output contract, file permissions
│   ├── EXAM_WORKBOOK.md      ← tasks 1–6, branching, grading criteria
│   ├── LEARNING_SYSTEM.md    ← tutoring, assessment, slide production
│   └── SOURCES.md            ← course book map + external references
├── exam_tasks/
│   ├── Task_Advanced_Workbook_DLMDSAS011.pdf   ← official task sheet (IU copyright)
│   ├── assignment_values_2.txt                 ← CURRENT personal ξ₁…ξ₂₀ (do not share)
│   ├── assignment_values.txt                   ← superseded first run, provenance only
│   └── user_notebook.ipynb                     ← Elena's scratch notebook (Task 1, old values)
├── knowledge/
│   └── Advanced_statistics_Course_Book.pdf     ← primary theory reference
├── learning/
│   ├── profile.json            ← strengths, weaknesses, preferences, mastery
│   ├── concepts.json           ← concept registry and links to slides
│   └── session_log.jsonl       ← append-only teaching interactions
├── slides/                     ← HTML decks
│   ├── _template/              ← starter deck — copy this
│   └── exam_tasks/             ← taskN-<topic>.html, one per exam task
└── deliverables/
    └── workbook/               ← the submission
        ├── workbook_analysis.ipynb  ← owns every number and figure
        ├── src/*.md                 ← prose with {{task.key}} tokens, no literals
        └── build.sh                 ← emits Advanced_Workbook_DLMDSAS01_DRAFT.docx
```

---

## Quick start

### Solve the next exam task

1. Read [`exam_tasks/assignment_values_2.txt`](exam_tasks/assignment_values_2.txt) and resolve branches in **[docs/EXAM_WORKBOOK.md](docs/EXAM_WORKBOOK.md)** (personal path is pre-computed there).
2. Open **[`deliverables/workbook/workbook_analysis.ipynb`](deliverables/workbook/workbook_analysis.ipynb)** — one notebook holds all six tasks. Edit the values cell at the top to change parameters.
3. Ground theory in **`knowledge/Advanced_statistics_Course_Book.pdf`** (see **[docs/SOURCES.md](docs/SOURCES.md)** for unit ↔ topic map).
4. For each task: formal model → math → code → plots with **explicit scales** → trust/justification paragraph (see Task 1 cells for the pattern).

### Teach or assess a concept

1. Follow **[docs/LEARNING_SYSTEM.md](docs/LEARNING_SYSTEM.md)** — probe understanding before lecturing.
2. Append a line to **`learning/session_log.jsonl`** after each teaching exchange.
3. Update **`learning/profile.json`** when mastery or preferences change.
4. Create or refresh slides by copying **`slides/_template/`**, following **[AGENTS.md](AGENTS.md) § Slide system** (exam decks are flat files under `slides/exam_tasks/`).

---

## Personal assignment snapshot

Current parameter set, signature `99d9e51eff0fb88f6911fa8b4392742591f8f6da`
(`exam_tasks/assignment_values_2.txt`). Verify the signature before trusting any number —
an earlier set was regenerated, so anything quoting ξ₂ = 0.58, ξ₄ = 3, ξ₉ = 2, μ₀ = 956 g
or Gamma(35, 51) comes from the retired run.

| Parameter | Value | Effect |
|-----------|-------|--------|
| ξ₁ | 0 | Task 1: Bernoulli vote, \(P(\text{for}) = \xi_2\) |
| ξ₂ | 0.65 | Task 1 success probability |
| ξ₄ | 1 | Task 2: survival mixture of Weibull shapes 2 and 8 |
| ξ₅…ξ₈ | 0.66, 8, 0.33, 5 | Task 2 weights and rates (weights rescaled so \(\xi_5 + \xi_7 = 1\)) |
| ξ₉ | 0 | Task 3: one router is \(\text{Exp}(\theta)\), so \(T = S_1 + S_2 \sim \Gamma(2, \theta)\) |
| ξ₁₀ | 33, 29, 6, 37, 1 | Task 3 MLE sample |
| ξ₁₁, ξ₁₂ | 842 g, 55.3 g | Task 4 baseline mean and standard deviation |
| ξ₁₃ | 2 | Task 4: "higher weights?" — conclusion is **fail to reject** |
| ξ₁₄ | 10 hammer weights | Task 4 sample |
| ξ₁₅ | 2 | Task 5: degree-10 polynomial + ridge |
| ξ₁₆ | 22 \((x, y)\) points | Task 5 data |
| ξ₁₇…ξ₁₉ | 23, 63, 95.48 | Task 6 Bayesian gamma → posterior Gamma(23, 63) |

**Progress:** all six tasks are derived and computed in
`deliverables/workbook/workbook_analysis.ipynb`, the prose lives in
`deliverables/workbook/src/`, and `build.sh` produces the draft `.docx`. Six slide decks
exist under `slides/exam_tasks/`.

---

## Copyright & academic integrity

- IU holds copyright on **`exam_tasks/Task_Advanced_Workbook_DLMDSAS011.pdf`**. Do not publish full solutions on third-party platforms.
- **`assignment_values*.txt`** is personal; treat it like credentials-adjacent data in git remotes.
- Submissions are plagiarism-checked; this repo is for **learning and private completion**, not public answer keys.

---

## Tooling (suggested)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install jupyter numpy scipy matplotlib pandas pypdf
jupyter lab deliverables/workbook/workbook_analysis.ipynb
```

To build the submission document: `cd deliverables/workbook && ./build.sh`.

---

## Documentation index

| Document | Purpose |
|----------|---------|
| [AGENTS.md](AGENTS.md) | **Start here.** Single instruction file for all agents: session startup, learning profile, exam status, slide system |
| [docs/EXAM_WORKFLOW.md](docs/EXAM_WORKFLOW.md) | Checklists, output contract, file write permissions, agent roles |
| [docs/EXAM_WORKBOOK.md](docs/EXAM_WORKBOOK.md) | Full task specs, branching logic, acceptance criteria |
| [docs/LEARNING_SYSTEM.md](docs/LEARNING_SYSTEM.md) | How to teach, assess, log, and build slides |
| [docs/SOURCES.md](docs/SOURCES.md) | Course book units + external authority list |
| [slides/README.md](slides/README.md) | ⚠ Stale — describes a dark 90s style never shipped. Use [AGENTS.md](AGENTS.md) § Slide system |

---

## Handoff phrase for new agents

> Read `AGENTS.md`, verify the `assignment_values_2.txt` signature, work the exam in `deliverables/workbook/workbook_analysis.ipynb`, and log any teaching in `learning/session_log.jsonl`.

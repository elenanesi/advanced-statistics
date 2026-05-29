# Advanced Statistics — Exam Workbook & Personalized Learning

Dual-purpose repository for **(1)** completing the IU Advanced Statistics workbook exam (`DLMDSAS01`) with personal parameter values, and **(2)** teaching advanced statistics concepts in a way that adapts to the learner’s understanding, preferences, and progress.

**Primary human:** Elena  
**Course:** DLMDSAS01 — Advanced Statistics (IU Internationale Hochschule)

---

## Goals (read this first)

| Goal | Deliverables | Where to work |
|------|----------------|---------------|
| **1. Exam workbook** | Solutions with proofs/citations, reproducible notebook, later a formal `.docx` workbook | [`exam_tasks/`](exam_tasks/) |
| **2. Concept teaching** | Understanding checks, learner profile, session log, cute HTML concept slides | [`learning/`](learning/), [`slides/`](slides/) |
| **3. Open Q&A** | Answers, intuition, optional log/slides — **no exam notebook edits required** | Chat in Cursor; see [docs/AGENTS.md](docs/AGENTS.md) § Open questions |

You can ask about **any** statistics topic (even outside the course book) or **unrelated** subjects in this workspace. Agents should answer directly and only pull in exam files when you want that connection.

Agents and tutors: start with **[docs/AGENTS.md](docs/AGENTS.md)** — it links every workflow, file, and rule.

---

## Repository layout

```
advanced_statistics/
├── README.md                 ← you are here
├── docs/
│   ├── AGENTS.md             ← master playbook for AI agents
│   ├── EXAM_WORKBOOK.md      ← tasks 1–6, branching, grading criteria
│   ├── LEARNING_SYSTEM.md    ← tutoring, assessment, slide production
│   └── SOURCES.md            ← course book map + external references
├── exam_tasks/
│   ├── Task_Advanced_Workbook_DLMDSAS011.pdf   ← official task sheet (IU copyright)
│   ├── assignment_values.txt                   ← personal ξ₁…ξ₂₀ (do not share publicly)
│   └── bernoulli_vote_analysis.ipynb           ← main computation notebook (all tasks)
├── knowledge/
│   └── Advanced_statistics_Course_Book.pdf     ← primary theory reference
├── learning/
│   ├── profile.json            ← strengths, weaknesses, preferences, mastery
│   ├── concepts.json           ← concept registry and links to slides
│   └── session_log.jsonl       ← append-only teaching interactions
├── slides/                     ← one HTML deck per main concept
│   ├── README.md               ← 90s aesthetic + “buddy” characters
│   └── _template/              ← starter deck for new concepts
└── deliverables/               ← final exports (.docx workbook when ready)
```

---

## Quick start

### Solve the next exam task

1. Read [`exam_tasks/assignment_values.txt`](exam_tasks/assignment_values.txt) and resolve branches in **[docs/EXAM_WORKBOOK.md](docs/EXAM_WORKBOOK.md)** (personal path is pre-computed there).
2. Open **[`exam_tasks/bernoulli_vote_analysis.ipynb`](exam_tasks/bernoulli_vote_analysis.ipynb)** — add sections per task; keep one notebook unless the user asks to split.
3. Ground theory in **`knowledge/Advanced_statistics_Course_Book.pdf`** (see **[docs/SOURCES.md](docs/SOURCES.md)** for unit ↔ topic map).
4. For each task: formal model → math → code → plots with **explicit scales** → trust/justification paragraph (see Task 1 cells for the pattern).

### Teach or assess a concept

1. Follow **[docs/LEARNING_SYSTEM.md](docs/LEARNING_SYSTEM.md)** — probe understanding before lecturing.
2. Append a line to **`learning/session_log.jsonl`** after each teaching exchange.
3. Update **`learning/profile.json`** when mastery or preferences change.
4. Create or refresh slides under **`slides/<concept-id>/`** using **`slides/README.md`** and the cutify skill (pixel mascots / buddies).

---

## Personal assignment snapshot

Resolved branches for the current `assignment_values.txt` (verify signature before trusting):

| Parameter | Value | Effect |
|-----------|-------|--------|
| ξ₁ | 0 | Task 1: Bernoulli vote, \(P(\text{for})=\xi_2\) |
| ξ₂ | 0.58 | Used in Task 1 |
| ξ₄ | 3 | Task 2: survival \( \xi_5 e^{-\xi_6 y^2} + \xi_7 e^{-\xi_8 y^2} \) |
| ξ₅…ξ₈ | 0.79, 4, 0.20, 6 | Task 2 (check \(\xi_5+\xi_7=1\)) |
| ξ₉ | 2 | Task 3: Gamma/Erlang order 7 for \(S\) |
| ξ₁₀ | 9 sample TB values | Task 3 MLE |
| ξ₁₁, ξ₁₂ | 956 g, 17.2 g | Task 4 baseline |
| ξ₁₃ | 2 | Task 4: “higher weights?” |
| ξ₁₄ | 10 hammer weights | Task 4 sample |
| ξ₁₅ | 2 | Task 5: degree-10 polynomial + ridge |
| ξ₁₆ | 22 \((x,y)\) points | Task 5 data |
| ξ₁₇…ξ₁₉ | 35, 51, 90.37 | Task 6 Bayesian gamma |

**Progress:** Task 1 is started in the notebook; Tasks 2–6 and the `.docx` workbook are not done.

---

## Copyright & academic integrity

- IU holds copyright on **`exam_tasks/Task_Advanced_Workbook_DLMDSAS011.pdf`**. Do not publish full solutions on third-party platforms.
- **`assignment_values.txt`** is personal; treat it like credentials-adjacent data in git remotes.
- Submissions are plagiarism-checked; this repo is for **learning and private completion**, not public answer keys.

---

## Tooling (suggested)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install jupyter numpy scipy matplotlib pandas pypdf
jupyter lab exam_tasks/bernoulli_vote_analysis.ipynb
```

Optional later: `python-docx` when building **`deliverables/workbook.docx`**.

---

## Documentation index

| Document | Purpose |
|----------|---------|
| [docs/AGENTS.md](docs/AGENTS.md) | Checklists, file contracts, handoffs between agents |
| [docs/EXAM_WORKBOOK.md](docs/EXAM_WORKBOOK.md) | Full task specs, branching logic, acceptance criteria |
| [docs/LEARNING_SYSTEM.md](docs/LEARNING_SYSTEM.md) | How to teach, assess, log, and build slides |
| [docs/SOURCES.md](docs/SOURCES.md) | Course book units + external authority list |
| [slides/README.md](slides/README.md) | Visual style guide for HTML decks |

---

## Handoff phrase for new agents

> Read `docs/AGENTS.md`, verify `assignment_values.txt` signature, continue the exam in `exam_tasks/bernoulli_vote_analysis.ipynb` from the next incomplete task, and log any teaching in `learning/session_log.jsonl`.

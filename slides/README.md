# HTML concept slides — style guide

One **main concept** → one folder `slides/<concept-id>/index.html`.

Slides are study companions (Goal 2), not exam submission files. They should feel like a **90s SNES/GBA title screen**: chunky pixels, starfield, scanlines optional, upbeat copy.

---

## Buddy system

Buddies are defined in `learning/concepts.json` → `buddies`. Each concept has a `buddy_id`.

| Buddy | Concept areas |
|-------|----------------|
| Penny (`coin-sprite`) | Bernoulli, discrete PMF |
| Hootsworth (`owl-sprite`) | Survival, PDF, waiting times |
| Packet (`router-sprite`) | Gamma, Erlang, MLE |
| Forge (`hammer-sprite`) | Hypothesis tests |
| Ridge (`ridge-sprite`) | OLS / ridge |
| Bayes (`prior-sprite`) | Conjugate priors |

**Buddy rules:**

- Buddy appears on **title** and **recap** slides (corner sprite or speech bubble).
- Buddy dialogue is 1–2 short sentences per slide — encouraging, slightly cheesy 90s RPG tone.
- Use **pixel SVG** (16×16 grid, `shape-rendering="crispEdges"`) — see cutify skill technique C.

---

## Visual spec (90s videogame)

| Element | Guideline |
|---------|-----------|
| Font | `'Press Start 2P', monospace` from Google Fonts, or system `monospace` fallback |
| Background | Dark `#1a1a2e` + CSS starfield or slow parallax gradient |
| Accents | Neon `#00ff88`, `#ff6b9d`, `#ffd700` sparingly |
| Cards | `border: 4px solid #fff`; `box-shadow: 4px 4px 0 #000` |
| Motion | `@keyframes` blink caret, subtle float on buddy — **no** seizure-flash |
| Math | KaTeX CDN optional; keep formulas few per slide |

---

## Slide deck structure (5–9 slides typical)

1. **Title** — concept name + buddy intro  
2. **Why care** — link to exam task or real life  
3. **Core idea** — one key formula or diagram  
4. **Worked micro-example** — tiny numbers  
5. **Common mistake** — call out misconception from `profile.json` if any  
6. **Quiz slide** — one question, answer in `<details>`  
7. **Recap** — 3 bullet checkpoints + buddy sign-off  

Navigation: keyboard `←` `→` or on-screen chunky buttons.

---

## Cutify skill integration

Path: `~/.cursor/skills/cutify-that-tab/SKILL.md`

| Technique | Use on slides |
|-----------|-----------------|
| A — emoji favicon | `index.html` `<link rel="icon">` for tab cuteness |
| B — gradient blob | Decorative borders / mascot variant |
| C — 16×16 pixel art | **Primary** for buddy sprites (inline SVG) |

Author sprites by hand in SVG `<rect>` — do not rely on external image hosts for core buddies.

---

## File template

Copy `slides/_template/` when creating a new concept:

```bash
cp -r slides/_template slides/my-concept-id
# Edit index.html title, buddy, and concept copy
# Register in learning/concepts.json → slide_status: draft
```

---

## Accessibility & practicality

- Minimum body text ~14px equivalent (Press Start 2P is small — use 12–14px with generous line-height).
- Works offline after first load (avoid required live APIs except optional KaTeX CDN).
- Single `index.html` per concept preferred (+ embedded CSS); no build step required.

---

## Quality checklist before `slide_status: ready`

- [ ] Matches `concept_id` folder name  
- [ ] Buddy on title + recap  
- [ ] At least one interactive or `<details>` quiz  
- [ ] Linked from `learning/concepts.json`  
- [ ] Session log notes user reaction if slide was requested  

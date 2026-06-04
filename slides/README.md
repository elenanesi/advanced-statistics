# HTML concept slides — style guide

One **main concept** → one folder `slides/<concept-id>/index.html`.

Slides are study companions (Goal 2), not exam submission files. They should feel like a **90s SNES/GBA title screen**: chunky pixels, starfield, scanlines optional, upbeat copy.

---

## Buddy system

Buddies are defined in `learning/concepts.json` → `buddies`. Each concept has a `buddy_id`.

| Buddy | Animal | Concept areas |
|-------|--------|----------------|
| Penny (`coin-sprite`) | Cat — warm cream, dusty-rose ears | Bernoulli, discrete PMF |
| Hootsworth (`owl-sprite`) | Owl — plum body, big 3×3 eye discs | Survival, PDF, waiting times |
| Packet (`router-sprite`) | Bunny — mint, very tall ears | Gamma, Erlang, MLE |
| Forge (`hammer-sprite`) | Bear — warm grey, cream snout | Hypothesis tests |
| Ridge (`ridge-sprite`) | Penguin — slate blue, white belly | OLS / ridge |
| Bayes (`prior-sprite`) | Fox — amber, cream muzzle | Conjugate priors |

**Buddy rules:**

- Buddy appears on **title** and **recap** slides (corner sprite or speech bubble).
- Buddy dialogue is 1–2 short sentences per slide — encouraging, slightly cheesy 90s RPG tone.
- Use **pixel SVG** (16×16 grid, `shape-rendering="crispEdges"`) — full SVG source for all 6 buddies is in `_template/index.html` as commented blocks.
- See the retro-cute-slides skill for the complete buddy catalog and color specs.

---

## Visual spec (90s videogame)

| Element | Guideline |
|---------|-----------|
| Font | `'Press Start 2P', monospace` from Google Fonts, or system `monospace` fallback |
| Background | Deep indigo `#1b1b2f` + warm-tinted CSS starfield (dimmer than pure white) |
| Accents | Sage `#82c4a0`, dusty rose `#c4919e`, warm amber `#d4a76a` — all muted, no pure neons |
| Cards | `border: 3px solid #9890a0`; `box-shadow: 5px 5px 0 #0a0a18` |
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

## Retro cute slides skill

Path: `~/.cursor/skills/retro-cute-slides/SKILL.md`

The combined skill covers the full 90s videogame visual spec (colors, typography,
card styling, animations) **and** pixel-art authoring. It mandates **Technique C
(16×16 pixel-art SVG)** as the only approach for buddy sprites, icons, and
decorative elements — emoji favicons and gradient blobs are not used.

Author all sprites by hand in SVG `<rect>` with `shape-rendering="crispEdges"` —
do not rely on external image hosts or raster assets for core buddies.

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

# The Five Aspect Ratios

The same line in a different ratio is **a recomposition, not a resize**. Copy volume, subject position, and line breaks all change.

---

## The Layout-Skeleton Library (pick the skeleton first, then fit the ratio)

⚠️ **The diagrams in each ratio section below show only the most common skeleton for that ratio — not the only option.**
What actually determines how an image looks is the skeleton; the ratio only decides how it's arranged.

| Skeleton | Structure | Pairs with |
|---|---|---|
| **Copy left, image right** | Copy in the left 55–62%, subject on the right | Prop / product |
| **Copy top, image bottom** | Copy pinned to the top, subject sunk to the bottom, big gap between | Prop / product |
| **Centered type-only** | Big type is the image, no still life, negative space all around | Type-only |
| **Type embedded in the subject** | The copy grows out of the object itself | Prop |
| **Tear-off calendar** | One side tiled with identical icons, the other side down to a single one, one almanac line at the bottom | Graphic array |
| **UI mimicry** | System dialog / chat bubble / code / calendar page / dictionary page | Type-only |

**"Type embedded in the subject" is the most overlooked and has the strongest double meaning.** Put the words exactly where the object would normally display information — the readout on a bathroom scale, a phone screen, a price tag, a calendar cell, a shipping label, an elevator floor indicator.
The fact that the object is speaking is established by the position alone, **so you can even drop the "X says:" lead-in** — and dropping it is exactly what "explain it and it dies" asks for.

**When producing several images in a row, change the skeleton before you change the palette.** Same skeleton with a new palette is a reskin, not a different layout.

---

## Quick Reference

| Ratio | Primary placement | Copy limit | Subject position | Line breaks |
|---|---|---|---|---|
| **3:4** | Microblog / social feed / newsletter body | 4 lines × 12 chars | Center, slightly low | By sense unit |
| **1:1** | Lifestyle-app posts / video-channel covers / avatar slots | 2 lines × 10 chars | Dead center | 2 lines maximum |
| **4:3** | Slides / video-site thumbnails / horizontal banners | 2 lines × 14 chars | Copy left, image right | Left-aligned |
| **9:16** | Short video / vertical feed posts / splash screens | 3 lines × 10 chars | Copy top, image bottom | Stacked short lines |
| **16:9** | YouTube / slides / website hero | 1 line × 16 chars | Copy left, image right | One line preferred |

---

## 3:4 (the workhorse — Durex's native format)

```
┌──────────────┐  1200 × 1600
│  ↕ 130        │
│  copy, 4 lines │  Copy zone: top 30%, left-aligned or centered
│  keyword scaled│  Body 40px, keyword 88px
│               │
│    ┌────┐     │  Subject zone: middle 40%,
│    │ subj │    │  subject width ≤ 45% of frame
│    └────┘     │
│               │
│               │  Negative space: bottom 30%
│   (durex)     │  Logo 8% up from the bottom
└──────────────┘
```
- **The most forgiving ratio**, carries the most information; 80% of Durex posters are this
- Vertical calligraphy and Chinese-classical styling are only done in this ratio

---

## 1:1 (lifestyle-app posts / video-channel covers)

```
┌──────────────┐  1200 × 1200
│              │
│  big type,    │  Copy compressed to 2 lines or fewer,
│  2 lines      │  and the size goes UP: body 64px (bigger than 3:4!)
│    ┌───┐     │
│    │subj│    │  Subject dead center, 30–40%
│    └───┘     │
│   (durex)    │
└──────────────┘
```
- **The copy must be cut to 2 lines.** 1:1 has no depth; one extra line crowds it
- Prefer a **type-only subject** or a **single prop**; avoid complex scenes
- It has to be readable as a thumbnail → keywords 50% larger than in 3:4

---

## 4:3 (landscape — slides / video sites)

```
┌─────────────────────────┐  1600 × 1200
│                         │
│  copy, 2 lines   ┌────┐ │  Left 45% copy, right 55% subject
│  keyword scaled   │subj│ │  Copy left-aligned, vertically centered
│                  └────┘ │
│  (durex)                │
└─────────────────────────┘
```
- **Copy left, image right** is the default landscape skeleton; the reverse works too but be consistent
- Copy is vertically centered — don't pin it to the top

---

## 9:16 (short video / splash screens / vertical video covers)

```
┌────────┐  1080 × 1920
│        │  ← top 15% safe zone (clear of the status bar)
│ line 1 │
│ line 2 │  Copy zone: top 30%, stacked short lines
│ line 3 │  ≤ 10 chars per line, 72px
│        │
│ ┌────┐ │
│ │subj│ │  Subject zone: middle 35%
│ └────┘ │
│        │
│(durex) │  ← bottom 20% safe zone (clear of platform UI)
└────────┘
```
- **Safe zones top and bottom**: keep key information out of the top 15% and bottom 20% (platform UI covers them)
- Copy is **stacked short lines**, each line complete in itself, like subtitles
- This is the only vertical ratio where **centered copy is allowed**

---

## 16:9 (website hero / YouTube / slide covers)

```
┌───────────────────────────────┐  1920 × 1080
│                               │
│   one-line copy         subject │  Copy on one line, left 40%
│   ────────                    │  96px+
│                               │
│  (durex)                      │
└───────────────────────────────┘
```
- **One line, done.** 16:9 is the worst ratio for long copy
- The subject can be a **full-bleed background darkened on the left**, with the copy over the dark area
- A subhead is one line at most, at 40% of the headline size

---

## Cross-Ratio Rewrite Example

The same line — "A hundred AI newsletters won't beat one workflow you shipped":

| Ratio | Rendering |
|---|---|
| 3:4 | A hundred AI newsletters<br>won't beat<br>**one** workflow you shipped.<br><sub>(image: a screen full of news cards vs a single process node)</sub> |
| 1:1 | A hundred newsletters.<br>**One** shipped workflow. |
| 4:3 | A hundred AI newsletters　｜　won't beat **one** you shipped |
| 9:16 | A hundred<br>AI newsletters<br>won't beat **one** |
| 16:9 | A hundred AI newsletters won't beat **one** workflow you shipped. |

**The pattern: the squarer or narrower the ratio, the shorter the copy; the wider the ratio, the more it has to compress into one line.**

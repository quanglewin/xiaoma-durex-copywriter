# Image Pipeline: AI Makes the Layers, Code Does the Typesetting

**English** · [Tiếng Việt](production.vi.md)

## Why Not Let AI Write the Text into the Image

Tested conclusion: image models still render Chinese with **wrong characters, missing strokes, broken glyph forms, and garbled punctuation**, and do it unpredictably.

And the whole point of this visual system is **precise typesetting**:
- Keywords scaled 1.8–2.5× and tinted brand color → needs exact size ratios
- Manual line breaks by sense unit → needs exact control over where lines break
- Logo at a fixed position, never enlarged → needs pixel-level placement
- Negative space ≥ 50% → needs exact margins

All of that is **a typesetting engine's job, not a generative model's**.

## The Layered Pipeline

```
① AI image model → produces ONLY the background texture / prop / graphic elements
   The prompt must explicitly say: NO text, NO letters, NO numbers, NO logos
   Recommended: GPT Image 2 (cheap, fast) or Nano Banana Pro (better texture)

② Code typesetting → carries all text
   Following the size / palette / negative-space spec in visual-system.md

③ Precise screenshot → export the five formats per ratios.md
```

**Bonus**: changing the copy is a one-line code change, with no money burned regenerating images; all five ratios reuse the same set of variables.

---

## Choosing a Typesetting Approach

| Approach | Strengths | Weaknesses | When to use |
|---|---|---|---|
| **HTML/CSS + Playwright** ⭐ | The full CSS toolkit; easiest CJK line-breaking and tracking; WYSIWYG; fastest iteration | Depends on a browser binary | **Default choice** |
| **Satori + resvg** | JSX→SVG→PNG, **no browser needed**, deterministic, fast (the Vercel OG image approach) | Supports only a CSS subset (flex, no grid); CJK needs fonts mounted manually | Server-side batch integration |
| **Canvas** (skia-canvas / node-canvas) | Strong programmatic drawing, no browser, good performance | **You write your own line-wrapping and text measurement**; no layout engine | **Icon arrays** (the screen-filling cars/shopping bags of the tear-off-calendar format), data-driven graphics |
| **SVG template + resvg** | Vector, scales infinitely, deterministic | Line breaks require hand-written `tspan`; font embedding is fiddly | When vector deliverables are required |
| **Pillow / ImageMagick** | Zero dependencies | Poor typesetting quality, no tracking control | Watermarks and batch stamping only |
| **Figma API** | Designer collaboration, deliverable source files | Needs a token + an existing design file | When there's a design team |

**The pattern**: text-driven → HTML; **graphic-array-driven → Canvas**. Durex's tear-off-calendar format (a screen of icons contrasted against a single one) is far better generated programmatically with Canvas than placed by hand.

---

## HTML/CSS Reference Implementation

The key points are in the comments. A complete runnable version is at `assets/compose_example.py` one level up (if missing, build from the skeleton below).

```python
from playwright.sync_api import sync_playwright
import base64, pathlib

RED = "#E2001A"      # brand accent, the only one in the image
INK = "#E8ECF2"      # body
# (format, width, height, body px, highlight px) — body ≈ 2.5%–3.5% of frame height
SPECS = [("3x4",1200,1600,44,92), ("1x1",1200,1200,74,118),
         ("4x3",1600,1200,52,96), ("9x16",1080,1920,62,104),
         ("16x9",1920,1080,60,104)]

def plate(tag):  # the AI-generated background layer, inlined as base64 to avoid path issues
    b = pathlib.Path(f"plates/{tag}.png").read_bytes()
    return "data:image/png;base64," + base64.b64encode(b).decode()

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{
  width:%(w)spx;height:%(h)spx;overflow:hidden;
  background:#0E1A2E url('%(plate)s') center/cover no-repeat;
  font-family:"PingFang SC","Source Han Sans SC",sans-serif;
  color:%(ink)s;-webkit-font-smoothing:antialiased;
}
.copy{line-height:1.62;letter-spacing:.02em;font-size:%(body)spx}
.hl{color:%(red)s;font-weight:600;font-size:%(hl)spx;letter-spacing:0}
/* Prop subject: a text caret. Pure CSS = pixel-exact, more reliable than generating it */
.caret{width:%(cw)spx;height:%(ch)spx;background:%(red)s;
       box-shadow:0 0 24px rgba(226,0,26,.45),0 0 72px rgba(226,0,26,.18)}
.sig{position:absolute;bottom:5.8%%;left:0;right:0;text-align:center;
     font-size:%(sig)spx;letter-spacing:.42em;color:rgba(232,236,242,.34)}
"""

with sync_playwright() as p:
    br = p.chromium.launch()
    for tag, w, h, body, hl in SPECS:
        page = br.new_page(viewport={"width": w, "height": h},
                           device_scale_factor=2)   # 2x = crisp text
        page.set_content(build_html(tag, w, h, body, hl))
        page.wait_for_timeout(400)                   # let fonts load
        page.screenshot(path=f"final/{tag}.png")
        page.close()
    br.close()
```

### Layout branches for the five formats (skeletons)

```
vertical (3:4)  ── copy top / subject middle / space bottom; copy within 4 lines
square   (1:1)  ── big centered type is the subject; copy cut to 2 lines, size goes up
split    (4:3)  ── left 46% copy (vertically centered) / right 54% subject
stack    (9:16) ── safe zones top and bottom (15% / 20%), stacked short lines
hero     (16:9) ── left 62% one-line headline + subhead / right 38% subject
```

---

## AI Background-Layer Prompt Template

```
An abstract minimalist background plate for a premium graphic poster.
Absolutely NO text, NO letters, NO numbers, NO characters, NO logos, NO objects, NO people.
Pure atmospheric field only.
<palette description, e.g. Deep midnight navy gradient from #16233F to #0A1220>
A very soft diffuse light falloff from the upper area, fading into darkness at the edges.
Fine cinematic film grain and delicate paper-like texture.
Subtle vignette on all four corners.
Calm, restrained, expensive, editorial.
Completely empty and clean — this is only a background texture,
the entire surface must remain unobstructed with nothing placed on it.
```

**Three negatives are mandatory**: `NO text` / `NO objects` (unless the prop is exactly what you want generated) / `NO people`.

For AI-themed work, add one more negation:
```
No sci-fi blue glow, no circuit boards, no robots, no brains, no globes, no neural network graphics.
```
— these are the visual clichés of the AI subject; the moment they appear, the work is downgraded.

---

## QA

After exporting, go through the checklist in `visual-system.md`, plus two more:

- [ ] Any wrong or malformed Chinese characters? (Should be zero under the HTML pipeline; if any appear, the font is missing glyphs — switch fonts)
- [ ] Is the keyword scale multiplier between 1.8 and 2.5? (Outside that it goes off balance)

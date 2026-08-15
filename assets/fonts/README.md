# Commercially Usable Font Library

This directory holds **only fonts that are free for commercial use**, for direct reference when this skill typesets images.
Each family ships the original `.ttf` (some also `.otf`) plus a `.woff2` (for web use, roughly 40% the size of the ttf).

Families marked `[wght]` are **variable fonts** — one file covers the full weight range; call them from CSS with `font-variation-settings` or `font-weight: 100~900`.

## Chinese (`cjk/`)

| Font | File | License | Use |
|---|---|---|---|
| Source Han Sans / Noto Sans SC | `NotoSansSC[wght].ttf` | SIL OFL 1.1 | First choice for body text and UI, weights 100–900 |
| Source Han Serif / Noto Serif SC | `NotoSerifSC[wght].ttf` | SIL OFL 1.1 | Headlines, Chinese-classical styling, still-life posters |
| Smiley Sans (得意黑) | `SmileySans-Oblique.ttf/.otf` | SIL OFL 1.1 | Headline punch, oblique by design, **large headlines only** |
| LXGW WenKai (霞鹜文楷) | `LXGWWenKai-Regular.ttf` | SIL OFL 1.1 | Handwritten-feeling body text, long copy, letter format |
| ZCOOL KuaiLe (站酷快乐体) | `ZCOOLKuaiLe-Regular.ttf` | SIL OFL 1.1 | Playful, children's, promotional |
| ZCOOL XiaoWei (站酷小薇 LOGO 体) | `ZCOOLXiaoWei-Regular.ttf` | SIL OFL 1.1 | Literary light Song, for logos and short headlines |
| ZCOOL QingKe HuangYou (站酷庆科黄油体) | `ZCOOLQingKeHuangYou-Regular.ttf` | SIL OFL 1.1 | Round and heavy, for food and lifestyle headlines |
| Ma Shan Zheng brush kai (马善政毛笔楷书) | `MaShanZheng-Regular.ttf` | SIL OFL 1.1 | Vertical calligraphy, seasonal markers, the rice-paper warm white palette |

## Latin / monospace (`latin/`)

| Font | File | License |
|---|---|---|
| Inter | `Inter[opsz,wght].ttf` | SIL OFL 1.1 |
| JetBrains Mono | `JetBrainsMono[wght].ttf` | SIL OFL 1.1 |
| Playfair Display | `PlayfairDisplay[wght].ttf` | SIL OFL 1.1 |
| Space Mono | `SpaceMono-Regular/Bold.ttf` | SIL OFL 1.1 |

## ⚠️ Not Included (fetch these yourself)

The following are **free for commercial use but do not permit third-party redistribution**, so they aren't vendored here. Download them from the official sites when needed:

- **Alibaba PuHuiTi** — https://fonts.alibabagroup.com/
- **OPPO Sans** — https://open.oppomobile.com/new/developmentDoc/info?id=13223
- **HarmonyOS Sans** — Huawei Developer Alliance, HarmonyOS design resources

## ❌ Never Use (paid license required)

Microsoft YaHei, PingFang, the Founder (方正) families, the Hanyi (汉仪) families, the Hakka / Arphic families.
**"It's installed on my system" ≠ "I can use it commercially."** Chinese font infringement is the single most common legal risk in Chinese marketing collateral.

## Web Usage Example

```css
@font-face {
  font-family: 'Noto Sans SC';
  src: url('assets/fonts/cjk/NotoSansSC[wght].woff2') format('woff2-variations');
  font-weight: 100 900;
  font-display: swap;
}
```

## License Text

All fonts here are under the SIL Open Font License 1.1; full terms at https://openfontlicense.org/ .
The OFL permits commercial use, modification, and redistribution; the one restriction is that **the fonts may not be sold on their own**, and derivative fonts must stay under the OFL.

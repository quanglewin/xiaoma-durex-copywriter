# Pipeline ra hình: AI dựng lớp, code dàn chữ

**Tiếng Việt** · [English](production.md)

## Vì sao không để AI viết chữ thẳng vào hình

Kết luận thực chứng: các mô hình sinh ảnh vẫn render chữ Hán **sai chữ, thiếu nét, méo tự dạng, loạn dấu câu**, và hỏng một cách khó lường.

Trong khi toàn bộ tinh thần của hệ thống thị giác này lại là **dàn chữ chính xác**:
- Từ khoá phóng 1,8–2,5× và nhuộm màu thương hiệu → cần tỷ lệ cỡ chữ chính xác
- Ngắt dòng thủ công theo cụm nghĩa → cần kiểm soát chính xác điểm xuống dòng
- Logo vị trí cố định, không bao giờ phóng to → cần định vị chuẩn từng pixel
- Khoảng trắng ≥ 50% → cần lề chính xác

Tất cả những thứ đó là **việc của một engine dàn trang, không phải của một mô hình sinh ảnh**.

## Pipeline phân lớp

```
① Mô hình sinh ảnh → CHỈ tạo chất nền / đạo cụ / yếu tố đồ hoạ
   Prompt bắt buộc ghi rõ: NO text, NO letters, NO numbers, NO logos
   Gợi ý: GPT Image 2 (rẻ, nhanh) hoặc Nano Banana Pro (chất liệu đẹp hơn)

② Code dàn chữ → gánh toàn bộ phần chữ
   Theo quy chuẩn cỡ chữ / bảng màu / khoảng trắng trong visual-system.vi.md

③ Chụp màn hình chính xác → xuất năm khổ theo ratios.vi.md
```

**Lợi ích kèm theo**: sửa copy chỉ là sửa một dòng code, không đốt tiền sinh lại ảnh; cả năm tỷ lệ tái sử dụng cùng một bộ biến.

---

## Chọn hướng dàn chữ

| Hướng | Mạnh | Yếu | Khi nào dùng |
|---|---|---|---|
| **HTML/CSS + Playwright** ⭐ | Trọn bộ đồ nghề CSS; ngắt dòng và giãn chữ CJK nhàn nhất; thấy sao được vậy; lặp nhanh nhất | Phụ thuộc binary trình duyệt | **Lựa chọn mặc định** |
| **Satori + resvg** | JSX→SVG→PNG, **không cần trình duyệt**, kết quả tất định, nhanh (cách Vercel làm ảnh OG) | Chỉ hỗ trợ tập con CSS (flex, không grid); font CJK phải gắn tay | Tích hợp chạy hàng loạt phía server |
| **Canvas** (skia-canvas / node-canvas) | Vẽ lập trình mạnh, không trình duyệt, hiệu năng tốt | **Tự viết wrap dòng và đo chữ**; không có layout engine | **Mảng icon** (ô tô / túi mua sắm phủ kín màn của thể lịch bóc), đồ hoạ chạy theo dữ liệu |
| **Template SVG + resvg** | Vector phóng vô hạn, tất định | Xuống dòng phải viết tay `tspan`; nhúng font lằng nhằng | Khi cần bàn giao vector |
| **Pillow / ImageMagick** | Không phụ thuộc gì | Chất lượng dàn chữ kém, không kiểm soát giãn chữ | Chỉ hợp đóng watermark, dán hàng loạt |
| **Figma API** | Cộng tác với designer, bàn giao được file nguồn | Cần token + file thiết kế có sẵn | Khi có team thiết kế |

**Quy luật**: chữ là chính → HTML; **mảng đồ hoạ là chính → Canvas**. Thể lịch bóc của Durex (cả màn icon đối lập với một icon đơn lẻ) sinh bằng Canvas lập trình hơn đứt xếp tay.

---

## Bản tham chiếu HTML/CSS

Ý chính nằm trong comment. Bản chạy được hoàn chỉnh ở `assets/compose_example.py` cùng cấp (không có thì tự dựng theo sườn bên dưới).

```python
from playwright.sync_api import sync_playwright
import base64, pathlib

RED = "#E2001A"      # màu nhấn thương hiệu, duy nhất trong hình
INK = "#E8ECF2"      # chữ nội dung
# (khổ, rộng, cao, nội dung px, nhấn px) — nội dung ≈ 2,5%–3,5% chiều cao khung
SPECS = [("3x4",1200,1600,44,92), ("1x1",1200,1200,74,118),
         ("4x3",1600,1200,52,96), ("9x16",1080,1920,62,104),
         ("16x9",1920,1080,60,104)]

def plate(tag):  # lớp nền do AI sinh, nhúng base64 để khỏi lo đường dẫn
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
/* Chủ thể đạo cụ: con trỏ văn bản. CSS thuần = chuẩn pixel, tin cậy hơn nhờ AI vẽ */
.caret{width:%(cw)spx;height:%(ch)spx;background:%(red)s;
       box-shadow:0 0 24px rgba(226,0,26,.45),0 0 72px rgba(226,0,26,.18)}
.sig{position:absolute;bottom:5.8%%;left:0;right:0;text-align:center;
     font-size:%(sig)spx;letter-spacing:.42em;color:rgba(232,236,242,.34)}
"""

with sync_playwright() as p:
    br = p.chromium.launch()
    for tag, w, h, body, hl in SPECS:
        page = br.new_page(viewport={"width": w, "height": h},
                           device_scale_factor=2)   # 2x = chữ sắc nét
        page.set_content(build_html(tag, w, h, body, hl))
        page.wait_for_timeout(400)                   # chờ font tải xong
        page.screenshot(path=f"final/{tag}.png")
        page.close()
    br.close()
```

### Nhánh bố cục cho năm khổ (sườn)

```
vertical (3:4)  ── chữ trên / chủ thể giữa / trống dưới; copy trong 4 dòng
square   (1:1)  ── chữ lớn căn giữa chính là chủ thể; copy cắt còn 2 dòng, cỡ chữ tăng
split    (4:3)  ── trái 46% copy (canh giữa dọc) / phải 54% chủ thể
stack    (9:16) ── vùng an toàn trên dưới (15% / 20%), câu ngắn xếp chồng
hero     (16:9) ── trái 62% tiêu đề một dòng + phụ đề / phải 38% chủ thể
```

---

## Mẫu prompt cho lớp nền AI

```
An abstract minimalist background plate for a premium graphic poster.
Absolutely NO text, NO letters, NO numbers, NO characters, NO logos, NO objects, NO people.
Pure atmospheric field only.
<mô tả bảng màu, ví dụ: Deep midnight navy gradient from #16233F to #0A1220>
A very soft diffuse light falloff from the upper area, fading into darkness at the edges.
Fine cinematic film grain and delicate paper-like texture.
Subtle vignette on all four corners.
Calm, restrained, expensive, editorial.
Completely empty and clean — this is only a background texture,
the entire surface must remain unobstructed with nothing placed on it.
```

**Ba câu phủ định bắt buộc**: `NO text` / `NO objects` (trừ khi đạo cụ chính là thứ bạn muốn AI vẽ) / `NO people`.

Làm chủ đề AI thì thêm một câu phủ định nữa:
```
No sci-fi blue glow, no circuit boards, no robots, no brains, no globes, no neural network graphics.
```
— đây là những sáo mòn thị giác của đề tài AI; xuất hiện là hình bị hạ cấp ngay.

---

## Kiểm hình

Xuất xong rà checklist trong `visual-system.vi.md`, cộng thêm hai mục:

- [ ] Chữ Hán có sai / thiếu nét không? (Với pipeline HTML phải là zero; nếu có nghĩa là font thiếu glyph — đổi font)
- [ ] Hệ số phóng từ khoá có nằm trong 1,8–2,5 không? (Ra ngoài là mất cân bằng)

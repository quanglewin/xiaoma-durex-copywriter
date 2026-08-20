#!/usr/bin/env python3
"""Tải và chuẩn hoá ảnh tư liệu Durex Việt Nam.

Chạy trên máy có mạng bình thường (môi trường tạo repo này bị chặn egress
nên ảnh không được commit sẵn).

    pip install requests pillow

    python fetch_images.py              # tải ảnh ứng viên -> _candidates/<id>/
    # ... tự duyệt, copy ảnh đúng vào folder này thành vn-01.jpg ... vn-12.jpg
    python fetch_images.py --normalize  # nén vn-*.jpg về <=800px, JPEG q82, xoá EXIF

_candidates/ chỉ là thư mục tạm — xoá trước khi commit (rm -rf _candidates).
"""

import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

HERE = Path(__file__).parent
CANDIDATES = HERE / "_candidates"
MAX_SIDE = 800          # cùng chuẩn với examples/durex-reference/
JPEG_QUALITY = 82
MIN_BYTES = 15_000      # bỏ icon, logo, ảnh trang trí nhỏ
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

# Quét mọi chuỗi trong trang trông như URL ảnh (src, data-src, og:image, css url()...)
# — thà thừa ứng viên còn hơn sót, vì bước duyệt là thủ công.
IMG_SRC_RE = re.compile(
    r"""["'(]([^"'()\s]+\.(?:jpe?g|png|webp)(?:\?[^"'()\s]*)?)["')]""",
    re.IGNORECASE,
)
IMG_EXT_RE = re.compile(r"\.(jpe?g|png|webp)(\?|$)", re.IGNORECASE)


def fetch(sources_path: Path) -> None:
    import requests

    data = json.loads(sources_path.read_text(encoding="utf-8"))
    (CANDIDATES / ".gitignore").parent.mkdir(exist_ok=True)
    (CANDIDATES / ".gitignore").write_text("*\n")  # không bao giờ commit ảnh chưa duyệt

    session = requests.Session()
    session.headers["User-Agent"] = UA

    for src in data["sources"]:
        out_dir = CANDIDATES / src["id"]
        out_dir.mkdir(parents=True, exist_ok=True)
        print(f"\n== {src['id']}  (cho mục: {', '.join(src['items'])})")
        try:
            page = session.get(src["url"], timeout=30)
            page.raise_for_status()
        except Exception as exc:
            print(f"   !! không tải được trang: {exc}")
            continue

        urls, seen = [], set()
        for m in IMG_SRC_RE.finditer(page.text):
            url = urljoin(src["url"], m.group(1).strip())
            if url in seen or not IMG_EXT_RE.search(url):
                continue
            seen.add(url)
            urls.append(url)

        print(f"   {len(urls)} ảnh ứng viên")
        for i, url in enumerate(urls, 1):
            name = f"{i:02d}_{Path(urlparse(url).path).name[:60]}"
            dest = out_dir / name
            if dest.exists():
                continue
            try:
                r = session.get(url, timeout=30)
                r.raise_for_status()
                if len(r.content) < MIN_BYTES:
                    continue
                dest.write_bytes(r.content)
                print(f"   + {name} ({len(r.content) // 1024} KB)")
            except Exception as exc:
                print(f"   - bỏ qua {url[:70]}: {exc}")
            time.sleep(1)  # lịch sự với server

    print("\nXong. Duyệt _candidates/, copy ảnh đúng vào folder này thành vn-XX.jpg,")
    print("rồi chạy: python fetch_images.py --normalize")


def normalize() -> None:
    from PIL import Image

    files = sorted(HERE.glob("vn-*.jpg")) + sorted(HERE.glob("vn-*.png")) + sorted(HERE.glob("vn-*.webp"))
    if not files:
        print("Chưa có file vn-*.jpg nào trong folder để chuẩn hoá.")
        return
    for f in files:
        img = Image.open(f)
        img = img.convert("RGB")  # bỏ alpha + EXIF
        w, h = img.size
        scale = MAX_SIDE / max(w, h)
        if scale < 1:
            img = img.resize((round(w * scale), round(h * scale)), Image.LANCZOS)
        out = f.with_suffix(".jpg")
        img.save(out, "JPEG", quality=JPEG_QUALITY, optimize=True)
        if out != f:
            f.unlink()
        kb = out.stat().st_size // 1024
        print(f"{out.name}: {img.size[0]}x{img.size[1]}, {kb} KB")
    print("\nXong. Kiểm tra lại từng ảnh rồi commit.")


if __name__ == "__main__":
    if "--normalize" in sys.argv:
        normalize()
    else:
        fetch(HERE / "sources.json")

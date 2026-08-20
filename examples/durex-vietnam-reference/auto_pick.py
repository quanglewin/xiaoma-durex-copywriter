import os
import shutil
from PIL import Image

mapping = {
    "vn-01": "ngaocontent",
    "vn-02": "adsplus-worldcup-2018",
    "vn-03": "vietnammoi-worldcup",
    "vn-04": "iptime-worldcup",
    "vn-05": "quantrimang-tong-hop",
    "vn-06": "ngaocontent",
    "vn-07": "cafef-mang-tien-ve-cho-me",
    "vn-08": "kootoro",
    "vn-09": "cafebiz-ever-given",
    "vn-10": "2dep-thoi-su",
    "vn-11": "cafebiz-doi-ngu-content",
    "vn-12": "vietads-halloween",
}

for item, folder in mapping.items():
    candidate_dir = os.path.join("_candidates", folder)
    if not os.path.isdir(candidate_dir):
        continue
    files = os.listdir(candidate_dir)
    images = [f for f in files if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpeg")]
    
    valid_images = []
    for img in images:
        path = os.path.join(candidate_dir, img)
        try:
            with Image.open(path) as im:
                im.verify()
            valid_images.append(img)
        except Exception:
            pass
            
    if not valid_images:
        print(f"No valid images for {item}")
        continue
        
    largest = max(valid_images, key=lambda f: os.path.getsize(os.path.join(candidate_dir, f)))
    src = os.path.join(candidate_dir, largest)
    dst = f"{item}.jpg"
    shutil.copy(src, dst)
    print(f"Copied {src} to {dst}")

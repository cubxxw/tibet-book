#!/usr/bin/env python3
"""
Rebuild docs/public/images/ from chengdu-tibet-318/ source photos.
Uses photo_analysis.json as authoritative source-of-truth mapping.

For HEIC files: sips → JPEG temp → ffmpeg → webp (gets full resolution)
For JPG files: ffmpeg → webp directly
"""

import json
import subprocess
import os
import tempfile
from pathlib import Path
from collections import defaultdict

BASE = Path("/Users/xiongxinwei/Documents/Obsidian/tibet-book")
SRC_DIR = BASE / "chengdu-tibet-318"
DST_DIR = BASE / "docs/public/images"
JSON_FILE = SRC_DIR / "photo_analysis.json"

with open(JSON_FILE) as f:
    photos = json.load(f)

def convert(src: Path, dst: Path, quality: int = 85) -> bool:
    """Convert any image to webp. HEIC uses sips→jpeg→webp pipeline."""
    if dst.exists():
        dst.unlink()

    ext = src.suffix.lower()

    if ext in ('.heic',):
        # sips can't write webp but can convert HEIC → JPEG at full resolution
        tmp = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
        tmp_path = tmp.name
        tmp.close()

        # Step 1: HEIC → JPEG via sips
        r1 = subprocess.run(
            ["sips", "-s", "format", "jpeg", str(src), "--out", tmp_path],
            capture_output=True, text=True
        )
        if r1.returncode != 0 or not Path(tmp_path).exists():
            print(f"  ERROR sips {src.name}: {r1.stderr[-100:]}")
            return False

        # Step 2: JPEG → webp via ffmpeg
        r2 = subprocess.run(
            ["ffmpeg", "-y", "-i", tmp_path, "-c:v", "libwebp", "-quality", str(quality), str(dst)],
            capture_output=True, text=True
        )
        os.unlink(tmp_path)

        if r2.returncode != 0:
            print(f"  ERROR ffmpeg {src.name}: {r2.stderr[-100:]}")
            return False
    else:
        # JPG → webp directly
        r = subprocess.run(
            ["ffmpeg", "-y", "-i", str(src), "-c:v", "libwebp", "-quality", str(quality), str(dst)],
            capture_output=True, text=True
        )
        if r.returncode != 0:
            print(f"  ERROR {src.name}: {r.stderr[-100:]}")
            return False

    size = dst.stat().st_size // 1024
    print(f"  ✓ {src.name} → {dst.name} ({size}KB)")
    return True

def get_src(original_file: str) -> Path:
    p = SRC_DIR / original_file
    if p.exists():
        return p
    for f in SRC_DIR.iterdir():
        if f.name.lower() == original_file.lower():
            return f
    return None

# ─── Group photos ─────────────────────────────────────────────────────────────
groups = defaultdict(list)
for p in photos:
    groups[(p["scene"], p["location_estimated"])].append(p)

# ─── Build assignment list ────────────────────────────────────────────────────
assignments = []

def add(src_file, dst_name, desc=""):
    src = get_src(src_file)
    if src is None:
        print(f"  MISSING: {src_file}")
        return
    assignments.append((src, DST_DIR / dst_name, desc or src_file))

def add_group(scene, loc, prefix, count):
    items = groups.get((scene, loc), [])
    for i, p in enumerate(items[:count], 1):
        add(p["original_file"], f"{prefix}-{i}.webp", p["description_cn"])

# Sanxingdui (11 photos)
add_group("museum", "Sanxingdui", "sanxingdui", 12)

# Lhasa museum (6 photos from 5N0A JPGs + HEIC)
for i, p in enumerate(groups.get(("museum", "Lhasa City"), [])[:6], 1):
    add(p["original_file"], f"lhasa-museum-{i}.webp", p["description_cn"])

# Pandas (4)
add_group("panda", "Chengdu Panda Base", "panda", 4)

# Chengdu city
add("IMG_1161.HEIC", "chengdu-city.webp", "成都IFS")

# Litang (18)
add_group("city", "Litang", "litang", 18)

# Chongqing
add("IMG_7547.HEIC", "chongqing-city.webp", "重庆中央公园")
add("IMG_7547.HEIC", "lhasa-memory-final-2.webp", "旅程的终点，重庆")

# Lhasa city life
add("IMG_7423.HEIC", "lhasa-city-final.webp", "拉萨市区生活")
add("IMG_7423.HEIC", "teahouse-1.webp", "拉萨甜茶馆")
add("IMG_7423.HEIC", "milk-tea.webp", "甜茶")

# Lhasa cityview (nanshan overlook)
add("IMG_6277.HEIC", "lhasa-cityview-1.webp", "拉萨南山全景")
add("IMG_6279.HEIC", "lhasa-cityview-2.webp", "拉萨南山全景2")

# Chengdu cafe
add("IMG_1876.HEIC", "chengdu-cafe.webp", "成都咖啡馆")

# Jiuzhaigou (11)
add_group("lake", "Jiuzhaigou", "jiuzhaigou", 11)
add("IMG_2328.heic", "jiuzhaigou-extra.webp", "九寨沟")

# Shannan lake 羊卓雍错 (6 from 5N0A JPGs + HEIC)
shannan = groups.get(("lake", "Shannan"), [])
for i, p in enumerate(shannan[:6], 1):
    add(p["original_file"], f"shannan-lake-{i}.webp", p["description_cn"])

# Namtso (8)
add_group("lake", "Namtso", "namtso", 8)

# Garze roadtrip / 318 (6)
add_group("roadtrip", "Garze Roadtrip", "garze-road", 6)

# Linzhi to Lhasa road (3)
for i, p in enumerate(groups.get(("roadtrip", "Linzhi to Lhasa"), [])[:3], 1):
    add(p["original_file"], f"road-to-lhasa-{i}.webp", p["description_cn"])

# Mangkang monastery (5)
add_group("monastery", "Changdu Mangkang", "mangkang", 5)

# Glacier 来古冰川 (14)
add_group("glacier", "Bome Laigu", "glacier", 14)

# Linzhi snow (8)
add_group("snow", "Linzhi", "linzhi-snow", 8)

# Drepung 哲蚌寺 — only use full-res files (0973, 3899, 8556)
add("IMG_0973.HEIC", "drepung-1.webp", "哲蚌寺")
add("IMG_3899.HEIC", "drepung-2.webp", "哲蚌寺")
add("IMG_8556.HEIC", "drepung-3.webp", "哲蚌寺")
# drepung 4/5/6 from lower-res but still usable 640×896 sources
add("IMG_7357.HEIC", "drepung-4.webp", "哲蚌寺辩经")
add("IMG_7376.HEIC", "drepung-5.webp", "哲蚌寺辩经")
# drepung-6: use another angle from same set
add("IMG_5708.HEIC", "drepung-6.webp", "哲蚌寺一角")
# Also drepung-debate alias
add("IMG_7357.HEIC", "drepung-debate.webp", "哲蚌寺辩经场")

# Sera 色拉寺 (all 640×896 thumbnails — still usable at web size)
add("IMG_6395.HEIC", "sera-1.webp", "色拉寺")
add("IMG_6416.HEIC", "sera-2.webp", "色拉寺辩经")
add("IMG_6469.HEIC", "sera-3.webp", "色拉寺建筑")
# sera-4 from IMG_6473 is corrupted → use IMG_6478
add("IMG_6478.HEIC", "sera-4.webp", "色拉寺院落")
add("IMG_6478.HEIC", "sera-5.webp", "色拉寺一角")
add("IMG_6501.HEIC", "sera-6.webp", "色拉寺")
add("IMG_6501.HEIC", "sera-offering.webp", "色拉寺供奉")

# Jokhang 大昭寺 + Barkhor 八廓街
add("IMG_5795.HEIC", "jokhang-temple.webp", "大昭寺朝拜者")
add("IMG_5795.HEIC", "jokhang-temple-1.webp", "大昭寺")
add("IMG_5795.HEIC", "jokhang-temple-2.webp", "大昭寺")
add("IMG_5795.HEIC", "barkhor-1.webp", "八廓街转经")

# Potala / lhasa temple area
add("IMG_6011.HEIC", "potala-1.webp", "布达拉宫")
add("IMG_6011.HEIC", "lhasa-temple-night.webp", "拉萨夜景")
add("IMG_6011.HEIC", "lhasa-night-1.webp", "拉萨夜色")

# Flight
add("IMG_7505.HEIC", "flight-aerial.webp", "回程俯瞰雪山")
add("IMG_7505.HEIC", "flight-view.webp", "飞机上俯瞰")

# Preface — use shannan lake as hero (wide landscape), jokhang for prayer scene, drepung for debate
add("5N0A7855.JPG", "preface-hero.webp", "序言配图·羊卓雍错")
add("IMG_5795.HEIC", "preface-1.webp", "清晨转经的朝拜者")
add("IMG_0973.HEIC", "preface-2.webp", "哲蚌寺辩经")

# Memory/final
add("IMG_6277.HEIC", "lhasa-memory-final-1.webp", "拉萨的记忆")

# Wuhan airport - not in JSON (taken before trip), keep or use chengdu-cafe
# Check if wuhan-airport.webp already exists and keep as-is
if not (DST_DIR / "wuhan-airport.webp").exists():
    add("IMG_1876.HEIC", "wuhan-airport.webp", "武汉机场或成都出发")

# ─── Execute ──────────────────────────────────────────────────────────────────

print(f"\n{'='*60}")
print(f"Converting {len(assignments)} images...")
print(f"{'='*60}\n")

success = 0
fail = 0

for src, dst, desc in assignments:
    print(f"[{desc[:35]}]")
    ok = convert(src, dst)
    if ok:
        success += 1
    else:
        fail += 1

print(f"\n{'='*60}")
print(f"Done: {success} success, {fail} failed")
print(f"{'='*60}")

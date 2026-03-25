#!/usr/bin/env python3
"""
川藏线图片转换脚本
将 chengdu-tibet-318 中的 HEIC/JPG 图片转换为 WebP 并复制到 docs/public/images/
"""

import os
import subprocess
import shutil
from pathlib import Path

SOURCE_DIR = Path("/Users/xiongxinwei/Documents/Obsidian/tibet-book/chengdu-tibet-318")
TARGET_DIR = Path("/Users/xiongxinwei/Documents/Obsidian/tibet-book/docs/public/images")
PUBLIC_DIR = Path("/Users/xiongxinwei/Documents/Obsidian/tibet-book/docs/public")

# 图片映射关系 (根据章节内容)
IMAGE_MAP = {
    # 01-wuhan.md
    "wuhan-airport.webp": "IMG_0973.HEIC",
    "milk-tea.webp": "IMG_1161.HEIC",
    "chengdu-hotpot.webp": "IMG_2075.HEIC",
    "panda-1.webp": "IMG_2343 2.HEIC",
    "panda-2.webp": "IMG_2403.HEIC",

    # 03-zheduo.md
    "zheduo-1.webp": "IMG_3105.HEIC",
    "zheduo-2.webp": "IMG_3110.HEIC",
    "garze-panorama.webp": "IMG_3174.HEIC",
    "litang-night.webp": "IMG_3294.heic",

    # 04-glacier.md
    "glacier-1.webp": "IMG_3856.HEIC",
    "glacier-panorama.webp": "IMG_4077.HEIC",
    "glacier-2.webp": "IMG_4087.HEIC",
    "glacier-3.webp": "IMG_4150.HEIC",
    "glacier-4.webp": "IMG_4167.HEIC",

    # 05-arrival.md
    "road-to-lhasa-1.webp": "IMG_4365.HEIC",
    "potala-1.webp": "IMG_4381.HEIC",
    "barkhor-1.webp": "IMG_4409.HEIC",
    "lhasa-night-1.webp": "IMG_4421.HEIC",

    # 07-snowcity.md
    "shannan-snow-1.webp": "IMG_4430.HEIC",
    "shannan-lake-1.webp": "IMG_4483.HEIC",
    "shannan-lake-3.webp": "IMG_4502.HEIC",

    # 08-tsangyang.md
    "jokhang-temple-1.webp": "IMG_4591.HEIC",
    "jokhang-temple-2.webp": "IMG_4755.HEIC",

    # 09-drepung.md
    "drepung-1.webp": "IMG_4819.HEIC",
    "drepung-2.webp": "IMG_4855.HEIC",
    "drepung-debate.webp": "IMG_5029.HEIC",
    "drepung-3.webp": "IMG_5030.heic",
    "drepung-5.webp": "IMG_5047.HEIC",

    # 10-teahouse.md
    "teahouse-1.webp": "IMG_5151.HEIC",
    "lhasa-cityview-2.webp": "IMG_5333.HEIC",

    # 11-namtso.md
    "namtso-sunrise.webp": "IMG_5516.HEIC",
    "namtso-1.webp": "IMG_5556.HEIC",
    "namtso-2.webp": "IMG_5708.HEIC",
    "namtso-peninsula.webp": "IMG_5795.HEIC",
    "namtso-3.webp": "IMG_5939.HEIC",
    "namtso-4.webp": "IMG_6011.HEIC",
    "namtso-5.webp": "IMG_6277.HEIC",

    # 12-fire.md
    "lhasa-museum-4.webp": "IMG_6279.HEIC",
    "lhasa-museum-6.webp": "IMG_6395.HEIC",

    # 06-farewell.md
    "lhasa-museum-1.webp": "IMG_6416.HEIC",
    "lhasa-museum-3.webp": "IMG_6469.HEIC",

    # 13-gifts.md
    "sera-1.webp": "IMG_6473.HEIC",
    "sera-2.webp": "IMG_6478.HEIC",
    "sera-offering.webp": "IMG_6501.HEIC",

    # afterword.md
    "lhasa-memory-final-1.webp": "IMG_7018.HEIC",
    "lhasa-memory-final-2.webp": "IMG_7195.HEIC",

    # preface.md
    "preface-1.webp": "IMG_7244.HEIC",
    "preface-2.webp": "IMG_7357.HEIC",

    # epilogue.md
    "flight-view.webp": "IMG_7376.HEIC",

    # 02-sanxingdui.md
    "sanxingdui-1.webp": "IMG_7423.HEIC",
    "sanxingdui-2.webp": "IMG_7505.HEIC",
    "sanxingdui-4.webp": "IMG_7547.HEIC",

    # jiuzhaigou gallery (01-wuhan.md)
    "jiuzhaigou-1.webp": "IMG_1512.HEIC",
    "jiuzhaigou-2.webp": "IMG_1516.HEIC",
    "jiuzhaigou-3.webp": "IMG_1544.HEIC",
    "jiuzhaigou-4.webp": "IMG_1599.HEIC",

    # panda gallery (01-wuhan.md)
    "panda-gallery-1.webp": "IMG_2328.heic",
    "panda-gallery-2.webp": "IMG_2661.HEIC",
    "panda-gallery-3.webp": "IMG_2671.HEIC",
    "panda-gallery-4.webp": "IMG_2710.HEIC",
}

# Hero 图片（首页）
HERO_MAP = {
    "namtso-hero.webp": "IMG_5556.HEIC",
}

# 章节封面图片
CHAPTER_HERO_MAP = {
    "preface-hero.webp": "IMG_7244.HEIC",  # preface.md
    "chengdu-city.webp": "IMG_1876.HEIC",  # 01-wuhan.md - 成都
    "sanxingdui-3.webp": "IMG_7423.HEIC",  # 02-sanxingdui.md
    "garze-road-3.webp": "IMG_3174.HEIC",  # 03-zheduo.md - 理塘路
    "glacier-7.webp": "IMG_3856.HEIC",     # 04-glacier.md - 来古冰川
    "road-to-lhasa-2.webp": "IMG_4365.HEIC",  # 05-arrival.md - 进藏路
    "lhasa-museum-2.webp": "IMG_6416.HEIC",   # 06-farewell.md - 博物馆
    "shannan-lake-2.webp": "IMG_4483.HEIC",   # 07-snowcity.md - 山南湖
    "jokhang-temple.webp": "IMG_4591.HEIC",   # 08-tsangyang.md - 大昭寺
    "drepung-4.webp": "IMG_4819.HEIC",        # 09-drepung.md - 哲蚌寺
    "lhasa-cityview-1.webp": "IMG_5333.HEIC", # 10-teahouse.md - 拉萨城景
    "namtso-3.webp": "IMG_5939.HEIC",         # 11-namtso.md - 纳木错
    "lhasa-museum-5.webp": "IMG_6279.HEIC",   # 12-fire.md - 博物馆 5
    "sera-3.webp": "IMG_6473.HEIC",           # 13-gifts.md - 色拉寺
    "flight-aerial.webp": "IMG_7376.HEIC",    # epilogue.md - 航拍
}


def convert_image(source_path: Path, target_path: Path, quality: int = 75) -> bool:
    """转换图片为 WebP 格式"""
    if not source_path.exists():
        print(f"  ! 未找到：{source_path.name}")
        return False

    try:
        # 如果是 HEIC 文件，先转换为 PNG
        if source_path.suffix.upper() in ['.HEIC', '.heic']:
            temp_png = Path("/tmp") / f"{source_path.stem}.png"

            # 使用 sips 转换 HEIC 到 PNG
            result = subprocess.run(
                ["sips", "-s", "format", "png", str(source_path), "--out", str(temp_png)],
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                print(f"  ! sips 转换失败：{source_path.name}")
                return False

            # 使用 ffmpeg 转换 PNG 到 WebP
            result = subprocess.run(
                ["ffmpeg", "-i", str(temp_png), "-c:v", "libwebp", "-q:v", str(quality),
                 str(target_path), "-y"],
                capture_output=True,
                text=True
            )

            # 清理临时文件
            temp_png.unlink(missing_ok=True)

        else:
            # JPG 直接转换
            result = subprocess.run(
                ["ffmpeg", "-i", str(source_path), "-c:v", "libwebp", "-q:v", str(quality),
                 str(target_path), "-y"],
                capture_output=True,
                text=True
            )

        if result.returncode == 0:
            print(f"  ✓ 成功：{target_path.name}")
            return True
        else:
            print(f"  ✗ 失败：{target_path.name}")
            return False

    except Exception as e:
        print(f"  ✗ 错误：{e}")
        return False


def main():
    # 创建目标目录
    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    print("开始转换图片...")
    print("=" * 50)

    success_count = 0
    failed_count = 0
    missing_count = 0

    # 转换章节图片
    for target_name, source_file in IMAGE_MAP.items():
        source_path = SOURCE_DIR / source_file
        target_path = TARGET_DIR / target_name

        print(f"转换：{source_file} -> {target_name}")

        if convert_image(source_path, target_path):
            success_count += 1
        else:
            if not source_path.exists():
                missing_count += 1
            else:
                failed_count += 1

    print("=" * 50)

    # 转换章节封面图片
    print("转换章节封面图片...")
    for target_name, source_file in CHAPTER_HERO_MAP.items():
        source_path = SOURCE_DIR / source_file
        target_path = TARGET_DIR / target_name

        print(f"转换封面：{source_file} -> {target_name}")

        if convert_image(source_path, target_path, quality=80):
            success_count += 1
        else:
            if not source_path.exists():
                missing_count += 1
            else:
                failed_count += 1

    print("=" * 50)
    print(f"转换完成！成功：{success_count}, 失败：{failed_count}, 未找到：{missing_count}")


if __name__ == "__main__":
    main()

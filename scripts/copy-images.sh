#!/bin/bash

# 川藏线图片转换脚本
# 将 chengdu-tibet-318 中的 HEIC/JPG 图片转换为 WebP 并复制到 docs/public/images/

SOURCE_DIR="/Users/xiongxinwei/Documents/Obsidian/tibet-book/chengdu-tibet-318"
TARGET_DIR="/Users/xiongxinwei/Documents/Obsidian/tibet-book/docs/public/images"

# 创建目标目录
mkdir -p "$TARGET_DIR/chapters"

# 图片映射关系 (根据章节内容)
declare -A IMAGE_MAP=(
    # 01-wuhan.md
    ["wuhan-airport.webp"]="IMG_0973.HEIC"
    ["milk-tea.webp"]="IMG_1161.HEIC"
    ["chengdu-hotpot.webp"]="IMG_2075.HEIC"
    ["panda-1.webp"]="IMG_2343 2.HEIC"
    ["panda-2.webp"]="IMG_2403.HEIC"

    # 03-zheduo.md
    ["zheduo-1.webp"]="IMG_3105.HEIC"
    ["zheduo-2.webp"]="IMG_3110.HEIC"
    ["garze-panorama.webp"]="IMG_3174.HEIC"
    ["litang-night.webp"]="IMG_3294.heic"

    # 04-glacier.md
    ["glacier-1.webp"]="IMG_3856.HEIC"
    ["glacier-panorama.webp"]="IMG_4077.HEIC"
    ["glacier-2.webp"]="IMG_4087.HEIC"
    ["glacier-3.webp"]="IMG_4150.HEIC"
    ["glacier-4.webp"]="IMG_4167.HEIC"

    # 05-arrival.md
    ["road-to-lhasa-1.webp"]="IMG_4365.HEIC"
    ["potala-1.webp"]="IMG_4381.HEIC"
    ["barkhor-1.webp"]="IMG_4409.HEIC"
    ["lhasa-night-1.webp"]="IMG_4421.HEIC"

    # 07-snowcity.md
    ["shannan-snow-1.webp"]="IMG_4430.HEIC"
    ["shannan-lake-1.webp"]="IMG_4483.HEIC"
    ["shannan-lake-3.webp"]="IMG_4502.HEIC"

    # 08-tsangyang.md
    ["jokhang-temple-1.webp"]="IMG_4591.HEIC"
    ["jokhang-temple-2.webp"]="IMG_4755.HEIC"

    # 09-drepung.md
    ["drepung-1.webp"]="IMG_4819.HEIC"
    ["drepung-2.webp"]="IMG_4855.HEIC"
    ["drepung-debate.webp"]="IMG_5029.HEIC"
    ["drepung-3.webp"]="IMG_5030.heic"
    ["drepung-5.webp"]="IMG_5047.HEIC"

    # 10-teahouse.md
    ["teahouse-1.webp"]="IMG_5151.HEIC"
    ["lhasa-cityview-2.webp"]="IMG_5333.HEIC"

    # 11-namtso.md
    ["namtso-sunrise.webp"]="IMG_5516.HEIC"
    ["namtso-1.webp"]="IMG_5556.HEIC"
    ["namtso-2.webp"]="IMG_5708.HEIC"
    ["namtso-peninsula.webp"]="IMG_5795.HEIC"
    ["namtso-3.webp"]="IMG_5939.HEIC"
    ["namtso-4.webp"]="IMG_6011.HEIC"
    ["namtso-5.webp"]="IMG_6277.HEIC"

    # 12-fire.md
    ["lhasa-museum-4.webp"]="IMG_6279.HEIC"
    ["lhasa-museum-6.webp"]="IMG_6395.HEIC"

    # 06-farewell.md
    ["lhasa-museum-1.webp"]="IMG_6416.HEIC"
    ["lhasa-museum-3.webp"]="IMG_6469.HEIC"

    # 13-gifts.md
    ["sera-1.webp"]="IMG_6473.HEIC"
    ["sera-2.webp"]="IMG_6478.HEIC"
    ["sera-offering.webp"]="IMG_6501.HEIC"

    # afterword.md
    ["lhasa-memory-final-1.webp"]="IMG_7018.HEIC"
    ["lhasa-memory-final-2.webp"]="IMG_7195.HEIC"

    # preface.md
    ["preface-1.webp"]="IMG_7244.HEIC"
    ["preface-2.webp"]="IMG_7357.HEIC"

    # epilogue.md
    ["flight-view.webp"]="IMG_7376.HEIC"

    # 02-sanxingdui.md
    ["sanxingdui-1.webp"]="IMG_7423.HEIC"
    ["sanxingdui-2.webp"]="IMG_7505.HEIC"
    ["sanxingdui-4.webp"]="IMG_7547.HEIC"
)

# Hero 图片
mkdir -p "$TARGET_DIR/../public"
HERO_MAP=(
    ["namtso-hero.webp"]="IMG_5556.HEIC"
)

echo "开始转换图片..."

# 转换章节图片
for target_name in "${!IMAGE_MAP[@]}"; do
    source_file="${IMAGE_MAP[$target_name]}"
    source_path="$SOURCE_DIR/$source_file"

    if [ -f "$source_path" ]; then
        # 根据文件名决定放到哪个章节目录
        chapter_dir=$(echo "$target_name" | sed 's/-[0-9]*\.webp$//')
        target_path="$TARGET_DIR/$target_name"

        echo "转换：$source_file -> $target_name"

        # 使用 sips 转换
        if [[ "$source_file" == *.HEIC || "$source_file" == *.heic ]]; then
            # sips 转换 HEIC 到 PNG，然后 ffmpeg 转 webp
            temp_png=$(mktemp).png
            sips -s format png "$source_path" --out "$temp_png" 2>/dev/null
            if [ $? -eq 0 ]; then
                ffmpeg -i "$temp_png" -c:v libwebp -q:v 75 "$target_path" -y 2>/dev/null
                rm -f "$temp_png"
            fi
        else
            # JPG 直接转换
            ffmpeg -i "$source_path" -c:v libwebp -q:v 75 "$target_path" -y 2>/dev/null
        fi

        if [ $? -eq 0 ]; then
            echo "  ✓ 成功：$target_name"
        else
            echo "  ✗ 失败：$target_name"
        fi
    else
        echo "  ! 未找到：$source_file"
    fi
done

# 转换 Hero 图片
for target_name in "${!HERO_MAP[@]}"; do
    source_file="${HERO_MAP[$target_name]}"
    source_path="$SOURCE_DIR/$source_file"
    target_path="$TARGET_DIR/../public/$target_name"

    if [ -f "$source_path" ]; then
        echo "转换 Hero: $source_file -> $target_name"

        if [[ "$source_file" == *.HEIC || "$source_file" == *.heic ]]; then
            temp_png=$(mktemp).png
            sips -s format png "$source_path" --out "$temp_png" 2>/dev/null
            if [ $? -eq 0 ]; then
                ffmpeg -i "$temp_png" -c:v libwebp -q:v 80 "$target_path" -y 2>/dev/null
                rm -f "$temp_png"
            fi
        fi

        if [ $? -eq 0 ]; then
            echo "  ✓ 成功：$target_name"
        else
            echo "  ✗ 失败：$target_name"
        fi
    fi
done

echo ""
echo "图片转换完成！"

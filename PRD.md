# 《减法之地》VitePress 网站 — 产品需求文档 (PRD)

> **项目名称**：减法之地 · 川西入藏 · 拉萨旅居手记
> **技术栈**：VitePress 1.6.x + Vue 3 + 自定义主题
> **目标**：将 18,000+ 字的旅居非虚构书稿深度嵌入 VitePress，打造一个**优雅、高级、内容至上**的在线阅读体验
> **执行方式**：ralph-loop 自动化循环完成

---

## 一、项目概述

### 1.1 定位

这不是一个"文档站"，而是一本**在线文学书**。读者打开网站的感受，应该接近于翻开一本精心排版的书——留白充足、字体舒适、节奏从容、图文交融。

### 1.2 核心原则

| 原则 | 具体表现 |
|------|---------|
| **内容至上** | 正文是主角，所有设计服务于阅读体验 |
| **减法美学** | 去掉多余装饰，留白即设计；呼应书名"减法" |
| **沉浸阅读** | 正文区域最大阅读宽度 680px，行间距 1.8，字号 17px |
| **图文交融** | 旅途照片不是"插图"，而是叙事的一部分 |
| **双语友好** | 中文排版优先，偶有英文地名自然混排 |

### 1.3 信息架构

```
首页 (/)
├── 序言：凌晨五点                    /chapters/preface
│
├── 第一部分：天路
│   ├── 第一章：武汉机场的茶颜悦色      /chapters/01-wuhan
│   ├── 第二章：三星堆的间隙            /chapters/02-sanxingdui
│   ├── 第三章：折多山，第二次           /chapters/03-zheduo
│   └── 第四章：来古冰川与那堆无用的石头  /chapters/04-glacier
│
├── 第二部分：拉萨
│   ├── 第五章：抵达                    /chapters/05-arrival
│   ├── 第六章：告别                    /chapters/06-farewell
│   ├── 第七章：雪城之下                /chapters/07-snowcity
│   ├── 第八章：仓央嘉措的夜晚          /chapters/08-tsangyang
│   ├── 第九章：哲蚌寺：知识即减法       /chapters/09-drepung
│   ├── 第十章：甜茶馆与拉漂众生相       /chapters/10-teahouse
│   └── 第十一章：纳木错，天湖           /chapters/11-namtso
│
├── 第三部分：减法
│   ├── 第十二章：1959 年的那把火        /chapters/12-fire
│   └── 第十三章：高原的馈赠             /chapters/13-gifts
│
├── 尾声：出发的理由                    /chapters/epilogue
├── 后记                               /chapters/afterword
├── 关于                               /about
└── 旅程地图                           /journey-map
```

---

## 二、设计系统

### 2.1 色彩体系

灵感来自藏区的天空、湖水、酥油灯和经幡。

```css
:root {
  /* 主色：天湖蓝 */
  --color-primary: #2C5F7C;
  --color-primary-light: #3A7CA5;
  --color-primary-soft: #E8F0F5;

  /* 强调色：酥油灯金 */
  --color-accent: #C4933F;
  --color-accent-soft: #F5EBD7;

  /* 文字 */
  --color-text-primary: #1A1A1A;
  --color-text-secondary: #555555;
  --color-text-muted: #999999;

  /* 背景 */
  --color-bg-primary: #FAFAF8;         /* 微暖白，不是纯白 */
  --color-bg-secondary: #F2F0EC;
  --color-bg-quote: #F8F6F2;

  /* 暗色模式 */
  --color-dark-bg: #1A1D21;
  --color-dark-bg-secondary: #242830;
  --color-dark-text: #E0DDD8;
}
```

### 2.2 字体系统

```css
:root {
  /* 正文字体：优先思源宋体，回退到系统宋体 */
  --font-body: 'Noto Serif SC', 'Source Han Serif SC', 'STSong',
               'Songti SC', serif;

  /* 标题字体：无衬线，干净有力 */
  --font-heading: 'Noto Sans SC', 'Source Han Sans SC', 'PingFang SC',
                  'Microsoft YaHei', sans-serif;

  /* 引用字体：楷体 */
  --font-quote: 'STKaiti', 'KaiTi', 'Noto Serif SC', serif;

  /* 正文排版参数 */
  --font-size-body: 17px;
  --line-height-body: 1.9;
  --max-width-content: 680px;
  --paragraph-indent: 2em;
}
```

### 2.3 排版规范

| 元素 | 规格 |
|------|------|
| 正文段落 | 首行缩进 2em，段间距 1.2em，两端对齐 |
| 章节标题 (H1) | 居中，28px，标题字体，上方 4em 间距 |
| 小节分隔 | 居中 `——` 或 `* * *`，上下各 2em |
| 引用块 | 左右缩进 2em，楷体，字号缩小为 15px，浅暖色背景 |
| 日期标注 | 右对齐，9px，灰色楷体 |
| 图片 | 全宽或 2/3 宽度，下方附图注（10px 灰色） |
| 全屏图片 | 突破内容区域，撑到浏览器全宽 |

### 2.4 自定义 Vue 组件

```
docs/.vitepress/theme/
├── index.ts                  # 主题入口
├── custom.css                # 全局自定义样式
├── Layout.vue                # 自定义布局（可选）
└── components/
    ├── PhotoGallery.vue      # 照片画廊（瀑布流/轮播）
    ├── FullWidthImage.vue    # 全宽大图 + 图注
    ├── ImageWithCaption.vue  # 正文内图片 + 图注
    ├── QuoteBlock.vue        # 风格化引用块
    ├── ChapterHeader.vue     # 章节页头（标题+副标题+日期+氛围图）
    ├── TimelineStep.vue      # 旅程时间线节点
    ├── JourneyMap.vue        # 旅程地图页（可交互）
    ├── Divider.vue           # 章节分隔符
    └── ReadingProgress.vue   # 阅读进度条（顶部细线）
```

---

## 三、页面详细设计

### 3.1 首页 (index.md)

**不使用 VitePress 默认 Hero 布局**，改用自定义全屏设计：

```
┌─────────────────────────────────────────┐
│                                         │
│     [全屏背景图：拉萨天空/纳木错]        │
│                                         │
│              减 法 之 地                 │
│         川西入藏·拉萨旅居手记            │
│                                         │
│     37天 · 39个停留 · 7354公里           │
│                                         │
│          [ 开始阅读 ]                    │
│                                         │
└─────────────────────────────────────────┘

┌─ 题记 ──────────────────────────────────┐
│                                         │
│   "知识在这里不是积累，而是减法。"        │
│                    ——写于哲蚌寺辨经院     │
│                                         │
└─────────────────────────────────────────┘

┌─ 旅程概览 ──────────────────────────────┐
│                                         │
│  武汉 → 成都 → 三星堆 → 九寨沟          │
│  → 折多山 → 理塘 → 芒康 → 72拐          │
│  → 来古冰川 → 林芝 → 拉萨               │
│  → 山南 → 纳木错 → 重庆                 │
│                                         │
│  （横向时间轴，带关键节点图标）           │
│                                         │
└─────────────────────────────────────────┘

┌─ 三部分结构预览 ────────────────────────┐
│                                         │
│  🛣️ 第一部分·天路    4 章               │
│  🏔️ 第二部分·拉萨    7 章               │
│  📿 第三部分·减法    2 章               │
│                                         │
└─────────────────────────────────────────┘
```

### 3.2 章节页面

每个章节页面结构：

```
┌─ 章节头 ────────────────────────────────┐
│  第九章                                  │
│  哲蚌寺：知识即减法                       │
│  2026年3月7日，哲蚌寺，拉萨城关区西郊      │
│  [氛围大图]                               │
└─────────────────────────────────────────┘

┌─ 正文 ──────────────────────────────────┐
│                                         │
│  (正文段落，首行缩进，两端对齐)           │
│                                         │
│        ——                               │
│                                         │
│  (正文段落...)                            │
│                                         │
│  ┌──────────────────────────┐           │
│  │    [照片: 辩经院]          │           │
│  │    辨经结束，两人相拥       │           │
│  └──────────────────────────┘           │
│                                         │
│  (正文段落...)                            │
│                                         │
│  > "曾虑多情损梵行..."  (引用块)          │
│                                         │
│  (正文段落...)                            │
│                                         │
└─────────────────────────────────────────┘

┌─ 上一章 / 下一章导航 ──────────────────┐
│  ← 第八章：仓央嘉措的夜晚               │
│            第十章：甜茶馆 →              │
└─────────────────────────────────────────┘
```

### 3.3 旅程地图页 (/journey-map)

使用 Mapbox/Leaflet 展示 Polarsteps 路线：
- 从武汉到重庆的完整轨迹
- 39 个停留点标记
- 点击标记可以跳转到对应章节
- 时间轴滑块：拖动显示不同日期的位置

### 3.4 关于页 (/about)

更新为匹配书稿：
- 书的缘起
- 关于作者（技术背景 + 旅行者）
- 数据概览（37 天 / 7354 公里 / 39 个停留）
- 致谢（小兔子、摄影大哥、贡嘎机场司机等）

---

## 四、图片策略

### 4.1 图片分类

| 分类 | 用途 | 位置 | 尺寸要求 |
|------|------|------|---------|
| **氛围大图** | 章节开头全宽 | ChapterHeader heroImage | 1920×800px, WebP |
| **全宽风景** | 突破内容区域，单独成段 | `<FullWidthImage>` | 1920×auto, WebP |
| **双图并排** | 叙事中2张同时插入 | `<ImageWithCaption>` × 2，CSS grid | 800×auto, WebP |
| **照片画廊** | 多图展示（≥4张同主题） | `<PhotoGallery>` | 各尺寸, lazy load |
| **首页背景** | Hero 区域全屏 | CSS background | 1920×1080, WebP + fallback |

> **核心原则：每个插入点至少同时放置 2 张照片，不出现孤立单张。** 风景全宽图例外（FullWidthImage 本身视觉体量足够）。

### 4.2 图片目录结构（含实际文件清单）

实际照片文件共 **118 张**，已按场景命名。ralph-loop 执行时须将原始 `.jpg` 文件转换为 `.webp` 并复制到对应目录：

```
docs/public/images/
├── hero/
│   ├── namtso-hero.webp          ← 20260306_namtso_lake_7195.jpg（纳木错大景，首页用）
│   └── lhasa-dusk.webp           ← 20260308_lhasa_city_city_7423.jpg（拉萨夕照，备用）
│
├── chapters/
│   ├── preface/
│   │   ├── flight-aerial.webp    ← 20260309_flight_back_aerial_7505.jpg
│   │   └── lhasa-cityview-1.webp ← 20260225_lhasa_nanshan_cityview_6277.jpg
│   │
│   ├── 01-wuhan/
│   │   ├── chengdu-city.webp       ← 20260204_chengdu_city_1161.jpg
│   │   ├── chengdu-cafe.webp       ← 20260208_chengdu_cafe_cafe_1876.jpg
│   │   ├── jiuzhaigou-1.webp       ← 20260209_jiuzhaigou_lake_2075.jpg
│   │   ├── jiuzhaigou-2.webp       ← 20260209_jiuzhaigou_lake_2150.jpg
│   │   ├── jiuzhaigou-3.webp       ← 20260209_jiuzhaigou_lake_2403.jpg
│   │   ├── jiuzhaigou-4.webp       ← 20260209_jiuzhaigou_lake_2475.jpg
│   │   ├── jiuzhaigou-5.webp       ← 20260209_jiuzhaigou_lake_2568.jpg
│   │   ├── jiuzhaigou-6.webp       ← 20260209_jiuzhaigou_lake_2623.jpg
│   │   ├── jiuzhaigou-7.webp       ← 20260209_jiuzhaigou_lake_2661.jpg
│   │   ├── jiuzhaigou-8.webp       ← 20260209_jiuzhaigou_lake_2671.jpg
│   │   ├── jiuzhaigou-9.webp       ← 20260209_jiuzhaigou_lake_2710.jpg
│   │   └── jiuzhaigou-10.webp      ← 20260209_jiuzhaigou_lake_2343 2.jpg
│   │
│   ├── 02-sanxingdui/
│   │   ├── sanxingdui-1.webp     ← 20260205_sanxingdui_museum_1275.jpg
│   │   ├── sanxingdui-2.webp     ← 20260205_sanxingdui_museum_1280.jpg
│   │   ├── sanxingdui-3.webp     ← 20260205_sanxingdui_museum_1301.jpg
│   │   ├── sanxingdui-4.webp     ← 20260205_sanxingdui_museum_1309.jpg
│   │   ├── sanxingdui-5.webp     ← 20260205_sanxingdui_museum_1318.jpg
│   │   ├── sanxingdui-6.webp     ← 20260205_sanxingdui_museum_1328.jpg
│   │   ├── sanxingdui-7.webp     ← 20260205_sanxingdui_museum_1350.jpg
│   │   ├── sanxingdui-8.webp     ← 20260205_sanxingdui_museum_1358.jpg
│   │   ├── sanxingdui-9.webp     ← 20260205_sanxingdui_museum_1359.jpg
│   │   ├── sanxingdui-10.webp    ← 20260205_sanxingdui_museum_1402.jpg
│   │   ├── sanxingdui-11.webp    ← 20260205_sanxingdui_museum_1417.jpg
│   │   └── sanxingdui-12.webp    ← 20260205_sanxingdui_museum_1387.jpg
│   │
│   ├── 03-zheduo/
│   │   ├── garze-road-1.webp     ← 20260210_garze_roadtrip_roadtrip_2793.jpg
│   │   ├── garze-road-2.webp     ← 20260210_garze_roadtrip_roadtrip_2883.jpg
│   │   ├── garze-road-3.webp     ← 20260210_garze_roadtrip_roadtrip_2913.jpg
│   │   ├── garze-road-4.webp     ← 20260210_garze_roadtrip_roadtrip_2957.jpg
│   │   ├── garze-road-5.webp     ← 20260210_garze_roadtrip_roadtrip_3009.jpg
│   │   ├── garze-road-6.webp     ← 20260210_garze_roadtrip_roadtrip_3061.jpg
│   │   ├── litang-1.webp         ← 20260211_litang_city_3105.jpg
│   │   ├── litang-2.webp         ← 20260211_litang_city_3110.jpg
│   │   ├── litang-3.webp         ← 20260211_litang_city_3174.jpg
│   │   ├── litang-4.webp         ← 20260211_litang_city_3185.jpg
│   │   ├── litang-5.webp         ← 20260211_litang_city_3193.jpg
│   │   ├── litang-6.webp         ← 20260211_litang_city_3199.jpg
│   │   ├── litang-7.webp         ← 20260211_litang_city_3228.jpg
│   │   ├── litang-8.webp         ← 20260211_litang_city_3232.jpg
│   │   ├── litang-9.webp         ← 20260211_litang_city_3243.jpg
│   │   ├── litang-10.webp        ← 20260211_litang_city_3251.jpg
│   │   ├── litang-11.webp        ← 20260211_litang_city_3294.jpg
│   │   ├── litang-12.webp        ← 20260211_litang_city_3309.jpg
│   │   ├── litang-13.webp        ← 20260211_litang_city_3368.jpg
│   │   ├── litang-14.webp        ← 20260211_litang_city_3373.jpg
│   │   ├── litang-15.webp        ← 20260211_litang_city_3406.jpg
│   │   ├── litang-16.webp        ← 20260211_litang_city_3437.jpg
│   │   ├── litang-17.webp        ← 20260211_litang_city_3442.jpg
│   │   └── litang-18.webp        ← 20260211_litang_city_3469.jpg
│   │
│   ├── 04-glacier/
│   │   ├── mangkang-1.webp       ← 20260212_changdu_mangkang_monastery_3571.jpg
│   │   ├── mangkang-2.webp       ← 20260212_changdu_mangkang_monastery_3607.jpg
│   │   ├── mangkang-3.webp       ← 20260212_changdu_mangkang_monastery_3622.jpg
│   │   ├── mangkang-4.webp       ← 20260212_changdu_mangkang_monastery_3645.jpg
│   │   ├── mangkang-5.webp       ← 20260212_changdu_mangkang_monastery_3692.jpg
│   │   ├── glacier-1.webp        ← 20260213_bome_laigu_glacier_3856.jpg
│   │   ├── glacier-2.webp        ← 20260213_bome_laigu_glacier_3881.jpg
│   │   ├── glacier-3.webp        ← 20260213_bome_laigu_glacier_4077.jpg
│   │   ├── glacier-4.webp        ← 20260213_bome_laigu_glacier_4087.jpg
│   │   ├── glacier-5.webp        ← 20260213_bome_laigu_glacier_4150.jpg
│   │   ├── glacier-6.webp        ← 20260213_bome_laigu_glacier_4167.jpg
│   │   ├── glacier-7.webp        ← 20260213_bome_laigu_glacier_4192.jpg
│   │   ├── glacier-8.webp        ← 20260213_bome_laigu_glacier_4242.jpg
│   │   ├── glacier-9.webp        ← 20260213_bome_laigu_glacier_4245.jpg
│   │   ├── glacier-10.webp       ← 20260213_bome_laigu_glacier_4247.jpg
│   │   ├── glacier-11.webp       ← 20260213_bome_laigu_glacier_4256.jpg
│   │   ├── glacier-12.webp       ← 20260213_bome_laigu_glacier_4313.jpg
│   │   ├── glacier-13.webp       ← 20260213_bome_laigu_glacier_4320.jpg
│   │   └── glacier-14.webp       ← 20260213_bome_laigu_glacier_4328.jpg
│   │
│   ├── 05-arrival/
│   │   ├── linzhi-snow-1.webp    ← 20260214_linzhi_snow_4365.jpg
│   │   ├── linzhi-snow-2.webp    ← 20260214_linzhi_snow_4381.jpg
│   │   ├── linzhi-snow-3.webp    ← 20260214_linzhi_snow_4409.jpg
│   │   ├── linzhi-snow-4.webp    ← 20260214_linzhi_snow_4421.jpg
│   │   ├── linzhi-snow-5.webp    ← 20260214_linzhi_snow_4430.jpg
│   │   ├── linzhi-snow-6.webp    ← 20260214_linzhi_snow_4483.jpg
│   │   ├── linzhi-snow-7.webp    ← 20260214_linzhi_snow_4502.jpg
│   │   ├── linzhi-snow-8.webp    ← 20260214_linzhi_snow_4591.jpg
│   │   ├── road-to-lhasa-1.webp  ← 20260215_linzhi_to_lhasa_roadtrip_4755.jpg
│   │   ├── road-to-lhasa-2.webp  ← 20260215_linzhi_to_lhasa_roadtrip_4819.jpg
│   │   └── road-to-lhasa-3.webp  ← 20260215_linzhi_to_lhasa_roadtrip_4855.jpg
│   │
│   ├── 06-farewell/
│   │   ├── lhasa-museum-1.webp   ← 20260216_lhasa_city_museum_5029.jpg
│   │   ├── lhasa-museum-2.webp   ← 20260216_lhasa_city_museum_5030.jpg
│   │   └── lhasa-museum-3.webp   ← 20260216_lhasa_city_museum_5047.jpg
│   │
│   ├── 07-snowcity/
│   │   ├── shannan-lake-1.webp   ← 20260217_shannan_lake_5333.jpg
│   │   ├── shannan-lake-2.webp   ← 20260217_shannan_lake_5516.jpg
│   │   ├── shannan-lake-3.webp   ← 20260217_shannan_lake_5556.jpg
│   │   ├── shannan-lake-4.webp   ← 20260217_shannan_lake_7855.jpg
│   │   └── shannan-lake-5.webp   ← 20260217_shannan_lake_7881.jpg
│   │
│   ├── 08-tsangyang/
│   │   ├── jokhang-temple.webp   ← 20260219_jokhang_temple_temple_5795.jpg
│   │   └── lhasa-temple-night.webp ← 20260221_lhasa_city_temple_6011.jpg
│   │
│   ├── 09-drepung/
│   │   ├── drepung-1.webp        ← 20260307_drepung_monastery_temple_0973.jpg
│   │   ├── drepung-2.webp        ← 20260307_drepung_monastery_temple_3899.jpg
│   │   ├── drepung-3.webp        ← 20260307_drepung_monastery_temple_5708.jpg
│   │   ├── drepung-4.webp        ← 20260307_drepung_monastery_temple_7357.jpg
│   │   ├── drepung-5.webp        ← 20260307_drepung_monastery_temple_7376.jpg
│   │   └── drepung-6.webp        ← 20260307_drepung_monastery_temple_8556.jpg
│   │
│   ├── 10-teahouse/
│   │   ├── lhasa-cityview-1.webp ← 20260225_lhasa_nanshan_cityview_6277.jpg
│   │   ├── lhasa-cityview-2.webp ← 20260225_lhasa_nanshan_cityview_6279.jpg
│   │   └── lhasa-city-final.webp ← 20260308_lhasa_city_city_7423.jpg
│   │
│   ├── 11-namtso/
│   │   ├── namtso-1.webp         ← 20260306_namtso_lake_5939.jpg
│   │   ├── namtso-2.webp         ← 20260306_namtso_lake_7018.jpg
│   │   ├── namtso-3.webp         ← 20260306_namtso_lake_7195.jpg
│   │   ├── namtso-4.webp         ← 20260306_namtso_lake_7244.jpg
│   │   └── namtso-5.webp         ← 20260306_namtso_lake_7836.jpg
│   │
│   ├── 12-fire/
│   │   ├── lhasa-museum-4.webp   ← 20260216_lhasa_city_museum_5151.jpg
│   │   ├── lhasa-museum-5.webp   ← 20260216_lhasa_city_museum_7796.jpg
│   │   └── lhasa-museum-6.webp   ← 20260216_lhasa_city_museum_7801.jpg
│   │
│   ├── 13-gifts/
│   │   ├── sera-1.webp           ← 20260226_sera_monastery_temple_6395.jpg
│   │   ├── sera-2.webp           ← 20260226_sera_monastery_temple_6416.jpg
│   │   ├── sera-3.webp           ← 20260226_sera_monastery_temple_6469.jpg
│   │   ├── sera-4.webp           ← 20260226_sera_monastery_temple_6473.jpg
│   │   ├── sera-5.webp           ← 20260226_sera_monastery_temple_6478.jpg
│   │   └── sera-6.webp           ← 20260226_sera_monastery_temple_6501.jpg
│   │
│   ├── epilogue/
│   │   ├── flight-aerial.webp    ← 20260309_flight_back_aerial_7505.jpg
│   │   └── chongqing-city.webp   ← 20260310_chongqing_city_7547.jpg
│   │
│   └── panda/                    # 熊猫基地（备用，第一章或about页）
│       ├── panda-1.webp          ← 20260206_chengdu_panda_base_panda_1512.jpg
│       ├── panda-2.webp          ← 20260206_chengdu_panda_base_panda_1516.jpg
│       ├── panda-3.webp          ← 20260206_chengdu_panda_base_panda_1544.jpg
│       └── panda-4.webp          ← 20260206_chengdu_panda_base_panda_1599.jpg
│
└── map/
    └── route-overlay.png
```

### 4.3 图片插入原则

1. **每章至少 1 张氛围大图**（ChapterHeader 的 heroImage，通常取该章最具代表性的全景）
2. **每个插入点放 2 张以上**：双图并排（CSS grid two-column）或 `<PhotoGallery>` 展示
3. **全宽图**（`<FullWidthImage>`）：用于自然风光大景，单张即可，因为视觉本身已足够
4. **图注必须有**：每张图 < 20 字，楷体灰色，用 `caption` prop 传入
5. **人物照片**：不全宽，在内容区内以双图或画廊形式出现
6. **`<PhotoGallery>`**：当同主题照片 ≥ 4 张时使用（三星堆/理塘/哲蚌寺/色拉寺均适用）

### 4.4 图片加载优化

```
- 所有图片转换为 WebP 格式（bash: for f in *.jpg; do cwebp $f -o ${f%.jpg}.webp; done）
- lazy loading (loading="lazy")，首屏 hero 图用 loading="eager" + rel="preload"
- 响应式 srcset (640w / 960w / 1920w)
- blurhash 或 低质量占位符（LQIP）防止布局跳动
- 建议在 build 脚本中加入自动 WebP 转换步骤
```

### 4.5 逐章图片插入方案（具体文件映射）

> 说明：
> - `heroImage` = ChapterHeader 的全宽氛围大图
> - `插入点 N` = 正文叙事中的照片插入位置，每次至少 2 张
> - `[全宽]` = 使用 `<FullWidthImage>`；`[双图]` = 并排两张；`[画廊]` = `<PhotoGallery>`

---

#### 序言：凌晨五点

**heroImage**：`/images/chapters/preface/lhasa-cityview-1.webp`
（南山俯瞰拉萨城，有人物剪影，清晨气氛）

| 插入点 | 位置触发 | 照片文件 | 组件 | 图注建议 |
|--------|---------|---------|------|---------|
| 插入点 1 | 叙述凌晨街道，第一段结尾后 | `flight-aerial.webp` + `lhasa-cityview-1.webp` | [双图] | "37天后从高空望下来，只剩下云和山脊" / "城关区的清晨，路灯还亮着" |

---

#### 第一章：武汉机场的茶颜悦色

**heroImage**：`/images/chapters/01-wuhan/chengdu-city.webp`
（成都街道，有人物，出发前的城市感）

| 插入点 | 位置触发 | 照片文件 | 组件 | 图注建议 |
|--------|---------|---------|------|---------|
| 插入点 1 | 到达成都、提及双流机场/咖啡厅段落后 | `chengdu-city.webp` + `chengdu-cafe.webp` | [双图] | "成都，旅程真正的起点" / "在咖啡馆等出发，什么都没想" |
| 插入点 2 | 九寨沟游览段落后（2月9日） | `jiuzhaigou-1.webp` + `jiuzhaigou-2.webp` + `jiuzhaigou-3.webp` + `jiuzhaigou-4.webp` + `jiuzhaigou-5.webp` + `jiuzhaigou-6.webp` | [画廊] | "九寨沟，2026年2月9日，海子的蓝色不像自然界应有的颜色" |
| 插入点 3 | 提及熊猫基地（如有叙述）或章末 | `panda-1.webp` + `panda-2.webp` + `panda-3.webp` + `panda-4.webp` | [画廊] | "成都大熊猫繁育研究基地，出发前一天" |

---

#### 第二章：三星堆的间隙

**heroImage**：`/images/chapters/02-sanxingdui/sanxingdui-3.webp`
（三星堆文物特写，最具视觉冲击力的一张作为章节大图）

| 插入点 | 位置触发 | 照片文件 | 组件 | 图注建议 |
|--------|---------|---------|------|---------|
| 插入点 1 | 进入博物馆展厅，第一组文物描写后 | `sanxingdui-1.webp` + `sanxingdui-2.webp` | [双图] | "三星堆一号坑出土青铜器" / "三千年前的眼睛，目光朝向不知名的远方" |
| 插入点 2 | 中段：面具/神像叙述后 | `sanxingdui-5.webp` + `sanxingdui-6.webp` + `sanxingdui-7.webp` + `sanxingdui-8.webp` | [画廊] | "2026年2月5日，三星堆博物馆" |
| 插入点 3 | 章末沉思段落后 | `sanxingdui-10.webp` + `sanxingdui-11.webp` | [双图] | "文明的残片，比任何完整的答案都更诚实" |

---

#### 第三章：折多山，第二次

**heroImage**：`/images/chapters/03-zheduo/garze-road-3.webp`
（川西公路全景，山路蜿蜒，用作章节氛围图）

| 插入点 | 位置触发 | 照片文件 | 组件 | 图注建议 |
|--------|---------|---------|------|---------|
| 插入点 1 | 出发，甘孜公路描写段落后 | `garze-road-1.webp` + `garze-road-2.webp` | [双图] | "318国道，云在公路这边，也在那边" / "甘孜，大雪后的路" |
| 插入点 2 | 过折多山/理塘出现，全宽公路大景 | `garze-road-4.webp` + `garze-road-5.webp` | [全宽×2，各独立] | "折多山垭口，海拔4298米" |
| 插入点 3 | 抵达理塘，街道与人物描写后 | `litang-1.webp` + `litang-2.webp` + `litang-3.webp` + `litang-4.webp` | [画廊] | "理塘，海拔4014米的高城" |
| 插入点 4 | 理塘人物/市集/寺院细节叙述后 | `litang-7.webp` + `litang-8.webp` + `litang-9.webp` + `litang-10.webp` | [画廊] | "理塘的人，眼神里有一种习惯了海拔的平静" |

---

#### 第四章：来古冰川与那堆无用的石头

**heroImage**：`/images/chapters/04-glacier/glacier-7.webp`
（冰川全景，蓝灰色调，用作章节最具震撼力的大图）

| 插入点 | 位置触发 | 照片文件 | 组件 | 图注建议 |
|--------|---------|---------|------|---------|
| 插入点 1 | 途经芒康，寺院描述段落后 | `mangkang-1.webp` + `mangkang-2.webp` | [双图] | "昌都芒康，藏东走廊上的寺庙" / "转经筒在风中，每转一圈都是一个祈愿" |
| 插入点 2 | 第一眼看到冰川的叙述后 | `glacier-1.webp` + `glacier-2.webp` | [双图] | "来古冰川，从山脊流下来的蓝色" |
| 插入点 3 | 深入冰川、石头细节描写时（全宽） | `glacier-5.webp` | [全宽] | "冰川末端，冰碛石堆满了所有人不需要的重量" |
| 插入点 4 | 冰川全景段落，最高潮时 | `glacier-8.webp` + `glacier-9.webp` + `glacier-10.webp` + `glacier-11.webp` | [画廊] | "2026年2月13日，波密来古村，海拔3900米" |
| 插入点 5 | 离开冰川、章末沉思时 | `mangkang-4.webp` + `mangkang-5.webp` | [双图] | "芒康寺的残墙，石头比意义更耐久" |

---

#### 第五章：抵达

**heroImage**：`/images/chapters/05-arrival/road-to-lhasa-2.webp`
（林芝至拉萨公路，雪山公路大景，驶入拉萨前的最后一段路）

| 插入点 | 位置触发 | 照片文件 | 组件 | 图注建议 |
|--------|---------|---------|------|---------|
| 插入点 1 | 描述林芝雪景段落后 | `linzhi-snow-1.webp` + `linzhi-snow-2.webp` | [双图] | "林芝，2月14日，情人节下了雪" / "桃花还没开，雪先来了" |
| 插入点 2 | 雪后公路、翻山段落（全宽） | `linzhi-snow-5.webp` | [全宽] | "林芝至拉萨，色季拉山口附近，海拔4728米" |
| 插入点 3 | 进入拉萨前，公路最后段落 | `road-to-lhasa-1.webp` + `road-to-lhasa-3.webp` | [双图] | "318国道最后一百公里，窗外开始出现经幡" / "入城前的路，像一个长句的最后一个字" |
| 插入点 4 | 林芝雪地细节补充，或作章末照片组 | `linzhi-snow-3.webp` + `linzhi-snow-4.webp` + `linzhi-snow-6.webp` + `linzhi-snow-7.webp` | [画廊] | "雅鲁藏布江流域，2026年2月14日" |

---

#### 第六章：告别

**heroImage**：`/images/chapters/06-farewell/lhasa-museum-2.webp`
（拉萨博物馆，安静的室内，与"告别"主题呼应）

| 插入点 | 位置触发 | 照片文件 | 组件 | 图注建议 |
|--------|---------|---------|------|---------|
| 插入点 1 | 博物馆参观叙述段落后（这是告别前最后同行的地方） | `lhasa-museum-1.webp` + `lhasa-museum-3.webp` | [双图] | "西藏博物馆，2026年2月16日，她出发前最后一天" / "文物橱窗里，每一件都是一次告别" |

> **注**：本章是情感最重的一章（小兔子离开），图片不宜过多。1个插入点，2张即可，留白给文字。

---

#### 第七章：雪城之下

**heroImage**：`/images/chapters/07-snowcity/shannan-lake-2.webp`
（山南湖景，辽阔，蓝天白云，雪域之下）

| 插入点 | 位置触发 | 照片文件 | 组件 | 图注建议 |
|--------|---------|---------|------|---------|
| 插入点 1 | 山南行程，湖边叙述后（全宽） | `shannan-lake-3.webp` | [全宽] | "山南，雅鲁藏布江以南，藏文明的源头" |
| 插入点 2 | 湖泊细节，独处段落后 | `shannan-lake-1.webp` + `shannan-lake-4.webp` | [双图] | "湖面上没有船，只有光在移动" / "2月17日，这片湖的名字我没记住" |
| 插入点 3 | 章末，广阔感收尾 | `shannan-lake-5.webp` + `shannan-lake-2.webp` | [双图] | "雪城之下，万物安静而庞大" |

---

#### 第八章：仓央嘉措的夜晚

**heroImage**：`/images/chapters/08-tsangyang/jokhang-temple.webp`
（大昭寺，有人物，金顶与朝拜者，是本章最核心的空间）

| 插入点 | 位置触发 | 照片文件 | 组件 | 图注建议 |
|--------|---------|---------|------|---------|
| 插入点 1 | 大昭寺、八廓街描写，叙事进入高潮后 | `jokhang-temple.webp` + `lhasa-temple-night.webp` | [双图] | "大昭寺广场，转经的人走了又来" / "夜里十点，八廓街的酥油灯还在燃" |

> **注**：仓央嘉措章节以诗歌引用和内心独白为主，图片不宜过多。2张精准插入即可。

---

#### 第九章：哲蚌寺：知识即减法

**heroImage**：`/images/chapters/09-drepung/drepung-4.webp`
（哲蚌寺，有僧侣人物，辩经院气氛）

| 插入点 | 位置触发 | 照片文件 | 组件 | 图注建议 |
|--------|---------|---------|------|---------|
| 插入点 1 | 进入哲蚌寺，第一印象描写后 | `drepung-1.webp` + `drepung-2.webp` | [双图] | "哲蚌寺，藏传佛教格鲁派最大寺院" / "白色建筑从山坡蔓延下来，像一场还未结束的梦" |
| 插入点 2 | 辩经院核心场景，全宽冲击力 | `drepung-5.webp` | [全宽] | "2026年3月7日，哲蚌寺辩经院，下午三点" |
| 插入点 3 | 辩经结束，僧侣细节，"减法"主题升华处 | `drepung-3.webp` + `drepung-6.webp` | [双图] | "击掌辩经，声音比寂静更有力" / "辩经结束，两人相拥走回宿舍" |

---

#### 第十章：甜茶馆与拉漂众生相

**heroImage**：`/images/chapters/10-teahouse/lhasa-cityview-1.webp`
（南山俯瞰拉萨全城，有人物剪影，甜茶馆的城市背景）

| 插入点 | 位置触发 | 照片文件 | 组件 | 图注建议 |
|--------|---------|---------|------|---------|
| 插入点 1 | 描述拉漂众生、城市日常段落后 | `lhasa-cityview-1.webp` + `lhasa-cityview-2.webp` | [双图] | "南山半腰，拉萨城散落在谷地" / "布达拉宫在那里，其他的事情也在那里" |
| 插入点 2 | 章末，在拉萨的时间感，最后一次俯瞰 | `lhasa-city-final.webp` | [全宽] | "3月8日，离开前两天，城市和我都没变" |

---

#### 第十一章：纳木错，天湖

**heroImage**：`/images/chapters/11-namtso/namtso-3.webp`
（纳木错大景，蓝色分层，最震撼的一张作为章节图）

| 插入点 | 位置触发 | 照片文件 | 组件 | 图注建议 |
|--------|---------|---------|------|---------|
| 插入点 1 | 抵达纳木错，第一眼描写后（全宽） | `namtso-1.webp` | [全宽] | "纳木错，海拔4718米，天湖的蓝色不像人间的颜色" |
| 插入点 2 | 湖边细节，时间流逝段落后 | `namtso-2.webp` + `namtso-4.webp` | [双图] | "湖水分五个蓝色层次，越远越深" / "站在湖边两小时，脑子里什么都不是" |
| 插入点 3 | 日落/光线变化最高潮处 | `namtso-5.webp` | [全宽] | "下午五点，光从念青唐古拉山斜射过来" |
| 插入点 4 | 章末 | `namtso-3.webp` + `namtso-1.webp` | [双图] | "带走不了的，就让它留在这里" |

---

#### 第十二章：1959 年的那把火

**heroImage**：`/images/chapters/12-fire/lhasa-museum-5.webp`
（拉萨博物馆展厅，历史文物氛围，暗色调）

| 插入点 | 位置触发 | 照片文件 | 组件 | 图注建议 |
|--------|---------|---------|------|---------|
| 插入点 1 | 进入历史叙述，博物馆展品描写后 | `lhasa-museum-4.webp` + `lhasa-museum-5.webp` | [双图] | "西藏博物馆，历史陈列区" / "每一件器物都是一个没有答案的问题" |
| 插入点 2 | 叙述1959年，情绪最沉重处 | `lhasa-museum-6.webp` | [全宽] | "2026年2月16日，这些东西在橱窗里沉默了很久" |

> **注**：本章处理历史重量，图片克制为佳。博物馆3张足够，不用堆砌。

---

#### 第十三章：高原的馈赠

**heroImage**：`/images/chapters/13-gifts/sera-3.webp`
（色拉寺，有僧侣人物，午后阳光，馈赠感）

| 插入点 | 位置触发 | 照片文件 | 组件 | 图注建议 |
|--------|---------|---------|------|---------|
| 插入点 1 | 色拉寺到访，寺院环境描写后 | `sera-1.webp` + `sera-2.webp` | [双图] | "色拉寺，每天下午三点有辩经" / "寺墙是红色的，阳光也是红色的" |
| 插入点 2 | 辩经院，人物互动核心段落（全宽） | `sera-5.webp` | [全宽] | "2026年2月26日，色拉寺辩经院，僧侣们还在辩" |
| 插入点 3 | 最后的馈赠、章末升华处 | `sera-3.webp` + `sera-4.webp` + `sera-6.webp` | [画廊] | "高原给的，不是答案，是另一种提问方式" |

---

#### 尾声：出发的理由

**heroImage**：`/images/chapters/epilogue/flight-aerial.webp`
（飞机上俯瞰，离开西藏时的天空，俯视感与"结束"契合）

| 插入点 | 位置触发 | 照片文件 | 组件 | 图注建议 |
|--------|---------|---------|------|---------|
| 插入点 1 | 离开拉萨、机场候机段落后 | `flight-aerial.webp` + `chongqing-city.webp` | [双图] | "3月9日，飞机从贡嘎机场起飞" / "重庆，回到潮湿的南方，高原已经是另一个时态" |

---

#### 后记

无独立 heroImage（后记不设章节头）

| 插入点 | 位置触发 | 照片文件 | 组件 | 图注建议 |
|--------|---------|---------|------|---------|
| 插入点 1 | 后记末尾，全书收官处 | `namtso-3.webp` + `drepung-5.webp` | [双图] | "纳木错与哲蚌寺，两种安静，同一片天空" |

---

### 4.6 图片处理脚本（ralph-loop 执行参考）

```bash
# 将原始 jpg 批量转换为 webp 并归档到对应目录
# 依赖：cwebp (libwebp) 或 ffmpeg

SRC_DIR="/path/to/original/photos"
DST_DIR="docs/public/images/chapters"

convert_and_copy() {
  local src="$1"
  local dst_dir="$2"
  local dst_name="$3"
  mkdir -p "$dst_dir"
  cwebp -q 85 "$src" -o "$dst_dir/$dst_name"
}

# 示例：三星堆
convert_and_copy "$SRC_DIR/20260205_sanxingdui_museum_1275.jpg" "$DST_DIR/02-sanxingdui" "sanxingdui-1.webp"
# ... 其余按 4.2 节文件清单逐一执行
```

> **备注**：原始照片文件需放在用户指定的 `SRC_DIR` 目录下。ralph-loop 执行 Phase 4 时，优先检查文件是否已存在，跳过已转换的文件。

---

## 五、技术实现

### 5.1 文件变更清单

```
DELETE (旧结构):
  docs/chapters/preface.md        → 替换
  docs/chapters/01-arrival.md     → 替换
  docs/chapters/02-adaptation.md  → 删除
  docs/chapters/03-daily-life.md  → 删除
  docs/chapters/04-temples.md     → 删除
  docs/chapters/05-people.md      → 删除
  docs/chapters/06-time.md        → 删除
  docs/chapters/07-belief.md      → 删除
  docs/chapters/08-modernity.md   → 删除
  docs/chapters/09-kora.md        → 删除
  docs/chapters/epilogue.md       → 替换

CREATE (新结构):
  docs/.vitepress/theme/index.ts
  docs/.vitepress/theme/custom.css
  docs/.vitepress/theme/components/ChapterHeader.vue
  docs/.vitepress/theme/components/ImageWithCaption.vue
  docs/.vitepress/theme/components/FullWidthImage.vue
  docs/.vitepress/theme/components/PhotoGallery.vue
  docs/.vitepress/theme/components/QuoteBlock.vue
  docs/.vitepress/theme/components/Divider.vue
  docs/.vitepress/theme/components/ReadingProgress.vue
  docs/.vitepress/theme/components/TimelineStep.vue

  docs/chapters/preface.md          # 序言：凌晨五点
  docs/chapters/01-wuhan.md         # 第一章
  docs/chapters/02-sanxingdui.md    # 第二章
  docs/chapters/03-zheduo.md        # 第三章
  docs/chapters/04-glacier.md       # 第四章
  docs/chapters/05-arrival.md       # 第五章
  docs/chapters/06-farewell.md      # 第六章
  docs/chapters/07-snowcity.md      # 第七章
  docs/chapters/08-tsangyang.md     # 第八章
  docs/chapters/09-drepung.md       # 第九章
  docs/chapters/10-teahouse.md      # 第十章
  docs/chapters/11-namtso.md        # 第十一章
  docs/chapters/12-fire.md          # 第十二章
  docs/chapters/13-gifts.md         # 第十三章
  docs/chapters/epilogue.md         # 尾声
  docs/chapters/afterword.md        # 后记
  docs/journey-map.md               # 旅程地图
  docs/about.md                     # 关于（重写）
  docs/index.md                     # 首页（重写）

UPDATE:
  docs/.vitepress/config.ts          # 完全重写
  package.json                       # 可能追加依赖
```

### 5.2 config.ts 重构要点

```typescript
export default defineConfig({
  lang: 'zh-CN',
  title: '减法之地',
  titleTemplate: ':title — 减法之地',
  description: '川西入藏·拉萨旅居手记 | 37天 7354公里的非虚构旅居记录',
  head: [
    ['meta', { property: 'og:title', content: '减法之地' }],
    ['meta', { property: 'og:description', content: '川西入藏·拉萨旅居手记' }],
    ['meta', { property: 'og:type', content: 'book' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
    ['link', { href: 'https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700&family=Noto+Sans+SC:wght@400;500;700&display=swap', rel: 'stylesheet' }],
  ],
  // ... 完整侧边栏结构见 §1.3
})
```

### 5.3 自定义主题入口

```typescript
// docs/.vitepress/theme/index.ts
import DefaultTheme from 'vitepress/theme'
import './custom.css'

// 全局注册组件
import ChapterHeader from './components/ChapterHeader.vue'
import ImageWithCaption from './components/ImageWithCaption.vue'
import FullWidthImage from './components/FullWidthImage.vue'
import QuoteBlock from './components/QuoteBlock.vue'
import Divider from './components/Divider.vue'
import ReadingProgress from './components/ReadingProgress.vue'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('ChapterHeader', ChapterHeader)
    app.component('ImageWithCaption', ImageWithCaption)
    app.component('FullWidthImage', FullWidthImage)
    app.component('QuoteBlock', QuoteBlock)
    app.component('Divider', Divider)
    app.component('ReadingProgress', ReadingProgress)
  }
}
```

### 5.4 关键 CSS 变量

```css
/* custom.css 核心 */

/* 覆盖 VitePress 默认最大宽度 */
.vp-doc {
  max-width: var(--max-width-content) !important;
}

/* 正文排版 */
.vp-doc p {
  font-family: var(--font-body);
  font-size: var(--font-size-body);
  line-height: var(--line-height-body);
  text-indent: var(--paragraph-indent);
  text-align: justify;
  margin: 0.8em 0;
}

/* 标题不缩进 */
.vp-doc h1, .vp-doc h2, .vp-doc h3 {
  font-family: var(--font-heading);
  text-indent: 0;
}

/* 引用块 */
.vp-doc blockquote {
  font-family: var(--font-quote);
  font-style: normal;
  background: var(--color-bg-quote);
  border-left: 3px solid var(--color-accent);
  padding: 1.2em 2em;
  margin: 2em 0;
  font-size: 15px;
}

/* 暗色模式 */
.dark {
  --color-bg-primary: var(--color-dark-bg);
  --color-text-primary: var(--color-dark-text);
}
```

---

## 六、内容迁移规范

### 6.1 从 docx 到 Markdown 的转换规则

| docx 元素 | Markdown 表示 |
|-----------|--------------|
| 正文段落 | 普通段落（CSS 处理首行缩进） |
| 分隔线（——） | `<Divider />` 组件 |
| 日期标注 | `<div class="date-note">...</div>` |
| 引用块 | `> 引用内容` 或 `<QuoteBlock>` |
| 斜体心理独白 | `*斜体文字*` |
| 章节标题 | frontmatter 配置 + ChapterHeader 组件 |

### 6.2 章节 Markdown 模板

```markdown
---
title: "哲蚌寺：知识即减法"
chapter: 9
part: 2
partName: "拉萨"
date: "2026年3月7日"
location: "哲蚌寺，拉萨城关区西郊"
heroImage: "/images/chapters/09-drepung/hero.webp"
excerpt: "知识在这里不是积累，而是减法。"
prev: "/chapters/08-tsangyang"
next: "/chapters/10-teahouse"
---

<ChapterHeader />

正文内容开始...

<Divider />

继续正文...

<ImageWithCaption
  src="/images/chapters/09-drepung/debate.webp"
  alt="哲蚌寺辩经院"
  caption="辩经结束后，两个僧侣相拥走回宿舍" />

继续正文...

> "曾虑多情损梵行，入山又恐别倾城。
> 世间安得双全法，不负如来不负卿。"

继续正文...
```

---

## 七、性能与 SEO

### 7.1 性能目标

| 指标 | 目标 |
|------|------|
| LCP (Largest Contentful Paint) | < 2.5s |
| CLS (Cumulative Layout Shift) | < 0.1 |
| FID (First Input Delay) | < 100ms |
| 首页加载体积 | < 500KB (gzip) |
| 图片加载策略 | 首屏 eager, 其余 lazy |

### 7.2 SEO 策略

- 每个章节页面独立 `<title>` 和 `<meta description>`
- Open Graph 标签（og:title, og:image, og:description）
- 结构化数据：Book schema (schema.org/Book)
- Sitemap 自动生成
- canonical URL

### 7.3 可访问性

- 所有图片有 alt 文字
- 色彩对比度符合 WCAG 2.1 AA
- 键盘导航支持
- 阅读模式友好

---

## 八、待用户提供

### 8.1 图片素材

用户将提供 Polarsteps 旅途照片目录，需要：

1. **提供图片文件夹路径**
2. 每张图片的大致拍摄地点/场景说明（如果文件名不自解释）
3. 需要特别标注的图片（如希望用作章节大图的）

收到图片后，将：
- 按章节分类归档到 `docs/public/images/chapters/`
- 自动压缩为 WebP 格式
- 在对应章节的正确位置插入
- 为每张图片撰写图注

### 8.2 补充文字素材

用户可能补充的内容：
- 更多旅途日记/语音转文字
- 小兔子的部分视角（如果她同意）
- 摄影大哥的照片（如果有授权）
- Polarsteps 的详细 GPS 数据

---

## 九、执行计划（ralph-loop 任务清单）

### Phase 1：基础架构（高优先级）

- [ ] 重写 `config.ts`（新侧边栏、新导航、新 meta）
- [ ] 创建 `theme/index.ts` 和 `custom.css`
- [ ] 创建核心 Vue 组件（ChapterHeader, Divider, QuoteBlock, ImageWithCaption）
- [ ] 重写 `index.md` 首页

### Phase 2：内容迁移（高优先级）

- [ ] 将 docx 书稿 14 章 + 序言 + 尾声 + 后记全部转为 Markdown
- [ ] 每个章节配置正确的 frontmatter
- [ ] 引用块、分隔符、日期标注全部使用组件
- [ ] 重写 `about.md`

### Phase 3：视觉优化（中优先级）

- [ ] 实现全局排版样式（正文首行缩进、行间距、字体）
- [ ] 暗色模式适配
- [ ] 移动端响应式优化
- [ ] 阅读进度条组件
- [ ] 首页全屏 Hero（待图片素材）

### Phase 4：图片集成（素材已就绪，按 §4.5 执行）

- [ ] 将 118 张原始 jpg 按 §4.2 清单批量转换为 WebP，归档到 `docs/public/images/chapters/`
- [ ] 按 §4.5 逐章插入方案，在每章 Markdown 中插入对应 `<ImageWithCaption>`、`<FullWidthImage>`、`<PhotoGallery>` 组件
- [ ] 每个插入点保证 ≥ 2 张同时出现（FullWidthImage 全宽单图除外）
- [ ] 为每张图片填写 `caption` prop（参考 §4.5 图注建议）
- [ ] 更新每章 frontmatter 的 `heroImage` 字段（参考 §4.5 各章 heroImage 指定）
- [ ] 实现 `<PhotoGallery>` 组件（三星堆、理塘、哲蚌寺、色拉寺章节使用）
- [ ] 首页 Hero 背景图设置为 `namtso-hero.webp`

### Phase 5：高级功能（低优先级）

- [ ] 旅程地图页面（Leaflet/Mapbox）
- [ ] 阅读时间估算
- [ ] 章节间平滑过渡动画
- [ ] 分享功能（微信/微博/Twitter）
- [ ] PWA 支持（离线阅读）

### Phase 6：验证与部署

- [ ] `vitepress build` 无报错
- [ ] Lighthouse 性能评分 > 90
- [ ] 全部链接可用
- [ ] 移动端/桌面端视觉检查
- [ ] 内容校对

---

## 十、最终效果预期

打开网站，首屏是一张安静的拉萨天空或纳木错湖面，书名 "减法之地" 以宋体大字居中，下方是旅途的数据——37天、7354公里。没有动画，没有花哨的特效，只有一张照片和几行字。

点击进入，侧边栏以书籍目录的方式展开三部分十四章。正文区域干净利落，宋体正文，首行缩进两字，行间距充足，左右留白，像一本被打开的纸质书。

照片出现在叙事需要它的地方——折多山的日落、来古冰川的蓝灰色、哲蚌寺辩经院的斜阳、纳木错的层次蓝——不多不少，每一张都被图注锚定在故事里。

读完尾声，回到首页，发现那行数据变得有重量了。

**这就是减法的力量：少一点，但每一点都实。**

---

*PRD v1.1 — 2026.03.25（新增 §4.5 逐章图片插入方案，§4.6 转换脚本；§4.1/4.3 更新插入原则为"每次 ≥ 2 张"；Phase 4 清单细化）*

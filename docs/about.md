---
title: 关于
layout: page
---

<script setup>
import Divider from '../.vitepress/theme/components/Divider.vue'
</script>

# 关于这本书

## 缘起

2025 年夏天，我做了一个决定：去拉萨，住一段时间。

不是走马观花的旅行，不是打卡拍照的 tourist，而是真正地生活在那里。租了一间八廓街附近的民居，买了厚棉被，学会了在 3658 米的高度慢慢走路，学会了用藏语说"扎西德勒"，学会了在甜茶馆里一坐就是一下午。

这本书就是这四个月的记录与思考。

它不是旅游攻略，不会告诉你哪家藏面好吃、哪家青旅便宜。它也不是文化研究，不会深入分析藏传佛教的历史、拉萨的社会结构。它只是一个普通人，在一个特殊的地方，度过的一段特殊时光。

## 关于作者

一个普通人。

在拉萨之前，是城市里的技术工作者，每天对着电脑写代码，周末逛商场看电影，过着和千万年轻人一样的生活。

在拉萨之后，也许还是普通的城市生活——但某些东西变了。说不清楚，只好写下来试试。

**技术背景**：多年软件开发经验，相信代码可以改变世界，但也开始怀疑代码是不是世界的全部。

**旅行者身份**：走过一些地方，拍过一些照片，写过一些文字。相信旅行不是逃避，而是为了更好地回来。

## 旅程数据

<div class="stats-grid">
  <div class="stat-item">
    <span class="stat-number">37</span>
    <span class="stat-label">天</span>
    <span class="stat-desc">从武汉到拉萨的旅程</span>
  </div>
  <div class="stat-item">
    <span class="stat-number">7354</span>
    <span class="stat-label">公里</span>
    <span class="stat-desc">总行驶里程</span>
  </div>
  <div class="stat-item">
    <span class="stat-number">39</span>
    <span class="stat-label">个停留</span>
    <span class="stat-desc">沿途停留的地点</span>
  </div>
  <div class="stat-item">
    <span class="stat-number">4</span>
    <span class="stat-label">个月</span>
    <span class="stat-desc">在拉萨的生活时间</span>
  </div>
</div>

## 路线

**武汉 → 成都 → 三星堆 → 九寨沟 → 折多山 → 理塘 → 芒康 → 72 拐 → 来古冰川 → 林芝 → 拉萨 → 山南 → 纳木错 → 重庆**

这是一条川藏南线（G318）的经典路线，也是中国最美的景观大道。

<Divider />

## 致谢

这本书的完成，离不开以下人的帮助：

**小兔子** —— 在我最犹豫的时候说："想去就去，工作可以等等，但青春不能。"没有你的鼓励，不会有这段旅程。

**摄影大哥** —— 在来古冰川的清晨，帮我拍下了最美的日出。你说："年轻人，多出来走走，世界比你想的大。"

**贡嘎机场司机师傅** —— 一路上的故事比风景还精彩。你说你开了三十年车，见过无数过客，但每个人都有自己的故事。

**所有在旅途中相遇的人** —— 青旅的室友、甜茶馆的茶友、寺庙的喇嘛、转经的老人……你们让这段旅程变得完整。

## 联系

如果你也去过拉萨，或者正在考虑去，或者只是对这本书有什么想法，欢迎通过以下方式联系我：

- GitHub: [@cubxxw](https://github.com/cubxxw)
- Email: [your-email@example.com](mailto:your-email@example.com)

---

*知识在这里不是积累，而是减法。*

*谨以此书，献给所有在路上的灵魂。*

扎西德勒。

<style>
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1.5em;
  margin: 2em 0;
  padding: 1.5em;
  background: var(--vp-c-bg-soft);
  border-radius: 8px;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.stat-number {
  font-family: var(--font-heading);
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--vp-c-brand-1);
  line-height: 1;
}

.stat-label {
  font-family: var(--font-quote);
  font-size: 1.1rem;
  color: var(--vp-c-text-2);
  margin: 0.3em 0;
}

.stat-desc {
  font-size: 0.85rem;
  color: var(--vp-c-text-3);
}

@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .stat-number {
    font-size: 2rem;
  }
}
</style>

---
title: 旅程地图
layout: page
---

<script setup>
import Divider from './.vitepress/theme/components/Divider.vue'
</script>

# 旅程地图

## 川藏南线 · G318

这是一条从中国中部平原到世界屋脊的旅程，沿着川藏南线（G318 国道），穿越横断山脉，最终抵达拉萨。

<div class="journey-timeline">
  <a href="/chapters/preface" class="timeline-item start">
    <span class="city">武汉</span>
    <span class="province">湖北</span>
    <span class="chapter">序言</span>
  </a>

  <a href="/chapters/01-wuhan" class="timeline-item">
    <span class="city">成都</span>
    <span class="province">四川</span>
    <span class="chapter">第一章</span>
  </a>

  <a href="/chapters/02-sanxingdui" class="timeline-item">
    <span class="city">三星堆</span>
    <span class="province">四川广汉</span>
    <span class="chapter">第二章</span>
  </a>

  <a href="/chapters/01-wuhan" class="timeline-item">
    <span class="city">九寨沟</span>
    <span class="province">四川阿坝</span>
    <span class="chapter">第一章</span>
  </a>

  <a href="/chapters/03-zheduo" class="timeline-item">
    <span class="city">折多山</span>
    <span class="province">四川甘孜</span>
    <span class="chapter">第三章</span>
  </a>

  <a href="/chapters/03-zheduo" class="timeline-item">
    <span class="city">理塘</span>
    <span class="province">四川甘孜</span>
    <span class="chapter">第三章</span>
  </a>

  <a href="/chapters/03-zheduo" class="timeline-item">
    <span class="city">芒康</span>
    <span class="province">西藏昌都</span>
    <span class="chapter">第三章</span>
  </a>

  <a href="/chapters/03-zheduo" class="timeline-item">
    <span class="city">72 拐</span>
    <span class="province">西藏昌都</span>
    <span class="chapter">第三章</span>
  </a>

  <a href="/chapters/04-glacier" class="timeline-item">
    <span class="city">来古冰川</span>
    <span class="province">西藏昌都</span>
    <span class="chapter">第四章</span>
  </a>

  <a href="/chapters/03-zheduo" class="timeline-item">
    <span class="city">林芝</span>
    <span class="province">西藏</span>
    <span class="chapter">第三章</span>
  </a>

  <a href="/chapters/05-arrival" class="timeline-item highlight">
    <span class="city">拉萨</span>
    <span class="province">西藏</span>
    <span class="chapter">第二部分（5-11 章）</span>
  </a>

  <a href="/chapters/07-snowcity" class="timeline-item">
    <span class="city">山南</span>
    <span class="province">西藏</span>
    <span class="chapter">第七章</span>
  </a>

  <a href="/chapters/11-namtso" class="timeline-item">
    <span class="city">纳木错</span>
    <span class="province">西藏</span>
    <span class="chapter">第十一章</span>
  </a>

  <div class="timeline-item end">
    <span class="city">重庆</span>
    <span class="province">重庆</span>
    <span class="chapter">旅程终点</span>
  </div>
</div>

<Divider />

## 旅程统计

<div class="stats-grid">
  <div class="stat-item">
    <span class="stat-number">37</span>
    <span class="stat-label">天</span>
    <span class="stat-desc">从武汉到拉萨</span>
  </div>
  <div class="stat-item">
    <span class="stat-number">7354</span>
    <span class="stat-label">公里</span>
    <span class="stat-desc">总行驶里程</span>
  </div>
  <div class="stat-item">
    <span class="stat-number">39</span>
    <span class="stat-label">个停留</span>
    <span class="stat-desc">沿途停留地点</span>
  </div>
  <div class="stat-item">
    <span class="stat-number">4</span>
    <span class="stat-label">个月</span>
    <span class="stat-desc">在拉萨生活时间</span>
  </div>
</div>

<Divider />

## 关于互动地图

> 完整互动地图将在 GPS 数据就绪后上线。

目前展示的是静态文字时间轴。未来计划集成 Mapbox 或类似地图服务，展示：
- 完整的行驶轨迹
- 每个停留点的 GPS 坐标
- 海拔变化曲线
- 沿途照片标记点

---

*沿着 G318，从平原到高原，从喧嚣到宁静。*

<style>
.journey-timeline {
  display: flex;
  flex-direction: column;
  gap: 0.5em;
  margin: 2em 0;
  padding: 1.5em;
  background: var(--vp-c-bg-soft);
  border-radius: 8px;
}

.timeline-item {
  display: flex;
  align-items: center;
  gap: 1em;
  padding: 1em 1.2em;
  background: var(--vp-c-bg);
  border-radius: 6px;
  text-decoration: none;
  transition: all 0.2s ease;
  border-left: 3px solid var(--vp-c-divider);
}

.timeline-item:hover {
  transform: translateX(8px);
  border-left-color: var(--vp-c-brand-1);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.timeline-item.start {
  border-left-color: #27ae60;
  background: rgba(39, 174, 96, 0.05);
}

.timeline-item.highlight {
  border-left-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}

.timeline-item.end {
  border-left-color: #e74c3c;
  background: rgba(231, 76, 60, 0.05);
}

.timeline-item .city {
  font-family: var(--font-heading);
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--vp-c-text-1);
  min-width: 80px;
}

.timeline-item .province {
  font-size: 0.9rem;
  color: var(--vp-c-text-2);
  flex: 1;
}

.timeline-item .chapter {
  font-family: var(--font-quote);
  font-size: 0.85rem;
  color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
  padding: 0.3em 0.8em;
  border-radius: 4px;
}

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
  .journey-timeline {
    padding: 1em;
  }

  .timeline-item {
    flex-wrap: wrap;
    gap: 0.5em;
  }

  .timeline-item .city {
    min-width: auto;
    font-size: 1rem;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .stat-number {
    font-size: 2rem;
  }
}
</style>

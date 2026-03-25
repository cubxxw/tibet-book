---
layout: home
---

<script setup>
import ChapterHeader from '../.vitepress/theme/components/ChapterHeader.vue'
import QuoteBlock from '../.vitepress/theme/components/QuoteBlock.vue'
import Divider from '../.vitepress/theme/components/Divider.vue'
</script>

<div class="homepage">
  <!-- 全屏背景图区域 -->
  <div class="hero-section">
    <div class="hero-content">
      <h1 class="book-title">减法之地</h1>
      <p class="book-subtitle">川西入藏·拉萨旅居手记</p>
      <p class="journey-stats">37 天 · 39 个停留 · 7354 公里</p>
      <a href="/chapters/preface" class="read-button">开始阅读</a>
    </div>
  </div>

  <!-- 题记 -->
  <div class="epigraph-section">
    <QuoteBlock content="知识在这里不是积累，而是减法。" attribution="写于哲蚌寺辨经院" />
  </div>

  <Divider />

  <!-- 旅程路线概览 -->
  <div class="journey-route">
    <h2 class="section-title">旅程路线</h2>
    <div class="route-timeline">
      <div class="route-item">
        <span class="route-city">武汉</span>
        <span class="route-arrow">→</span>
      </div>
      <div class="route-item">
        <span class="route-city">成都</span>
        <span class="route-arrow">→</span>
      </div>
      <div class="route-item">
        <span class="route-city">三星堆</span>
        <span class="route-arrow">→</span>
      </div>
      <div class="route-item">
        <span class="route-city">九寨沟</span>
        <span class="route-arrow">→</span>
      </div>
      <div class="route-item">
        <span class="route-city">折多山</span>
        <span class="route-arrow">→</span>
      </div>
      <div class="route-item">
        <span class="route-city">理塘</span>
        <span class="route-arrow">→</span>
      </div>
      <div class="route-item">
        <span class="route-city">芒康</span>
        <span class="route-arrow">→</span>
      </div>
      <div class="route-item">
        <span class="route-city">72 拐</span>
        <span class="route-arrow">→</span>
      </div>
      <div class="route-item">
        <span class="route-city">来古冰川</span>
        <span class="route-arrow">→</span>
      </div>
      <div class="route-item">
        <span class="route-city">林芝</span>
        <span class="route-arrow">→</span>
      </div>
      <div class="route-item">
        <span class="route-city highlight">拉萨</span>
        <span class="route-arrow">→</span>
      </div>
      <div class="route-item">
        <span class="route-city">山南</span>
        <span class="route-arrow">→</span>
      </div>
      <div class="route-item">
        <span class="route-city">纳木错</span>
        <span class="route-arrow">→</span>
      </div>
      <div class="route-item">
        <span class="route-city">重庆</span>
      </div>
    </div>
  </div>

  <Divider />

  <!-- 三部分结构预览 -->
  <div class="book-structure">
    <h2 class="section-title">书籍结构</h2>
    <div class="structure-grid">
      <a href="/chapters/01-wuhan" class="structure-card part-1">
        <span class="part-number">第一部分</span>
        <span class="part-name">天路</span>
        <span class="chapter-count">4 章</span>
        <p class="part-desc">从成都平原到藏区腹地，穿越横断山脉，在海拔 4000 米的高原上追逐冰川的足迹</p>
      </a>
      <a href="/chapters/05-arrival" class="structure-card part-2">
        <span class="part-number">第二部分</span>
        <span class="part-name">拉萨</span>
        <span class="chapter-count">7 章</span>
        <p class="part-desc">在圣城停留四个月，转经、辩经、甜茶馆，在信仰与日常的交织中重新理解生活</p>
      </a>
      <a href="/chapters/12-fire" class="structure-card part-3">
        <span class="part-number">第三部分</span>
        <span class="part-name">减法</span>
        <span class="chapter-count">2 章</span>
        <p class="part-desc">离开前的沉思，高原的馈赠——知识不是积累，而是剥离层层外壳看见本质</p>
      </a>
    </div>
  </div>
</div>

<style>
.homepage {
  max-width: 100%;
}

/* Hero 区域 */
.hero-section {
  min-height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, rgba(44, 95, 124, 0.9), rgba(62, 124, 165, 0.8)),
              url('/namtso-hero.webp') center/cover no-repeat;
  padding: 4em 2em;
  text-align: center;
}

.hero-content {
  max-width: 680px;
}

.book-title {
  font-family: var(--font-heading);
  font-size: 4rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  color: white;
  margin: 0 0 0.5em 0;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

.book-subtitle {
  font-family: var(--font-quote);
  font-size: 1.2rem;
  color: rgba(255, 255, 255, 0.9);
  margin: 0 0 1em 0;
}

.journey-stats {
  font-family: var(--font-heading);
  font-size: 1.1rem;
  font-weight: 500;
  color: var(--color-accent);
  background: rgba(0, 0, 0, 0.3);
  display: inline-block;
  padding: 0.5em 1.5em;
  border-radius: 4px;
  margin-bottom: 2em;
}

.read-button {
  display: inline-block;
  background: var(--color-accent);
  color: white;
  font-family: var(--font-heading);
  font-size: 1.1rem;
  font-weight: 500;
  padding: 1em 3em;
  border-radius: 6px;
  text-decoration: none;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(196, 147, 63, 0.4);
}

.read-button:hover {
  background: #D4A34F;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(196, 147, 63, 0.5);
}

/* Section titles */
.section-title {
  font-family: var(--font-heading);
  font-size: 1.8rem;
  font-weight: 700;
  text-align: center;
  letter-spacing: 0.1em;
  margin: 2em 0 1.5em;
  color: var(--vp-c-brand-1);
}

/* Epigraph */
.epigraph-section {
  max-width: 680px;
  margin: 3em auto;
  padding: 0 2em;
}

/* Journey route */
.journey-route {
  max-width: 900px;
  margin: 3em auto;
  padding: 2em;
}

.route-timeline {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 0.5em;
}

.route-item {
  display: flex;
  align-items: center;
  gap: 0.5em;
}

.route-city {
  font-family: var(--font-quote);
  font-size: 1rem;
  color: var(--vp-c-text-1);
  padding: 0.4em 0.8em;
  background: var(--vp-c-bg-soft);
  border-radius: 4px;
  white-space: nowrap;
}

.route-city.highlight {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  font-weight: 600;
}

.route-arrow {
  color: var(--color-divider);
  font-size: 1.2em;
}

/* Book structure */
.book-structure {
  max-width: 900px;
  margin: 3em auto;
  padding: 2em;
}

.structure-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5em;
  margin-top: 2em;
}

.structure-card {
  display: block;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-bg-mute);
  border-radius: 8px;
  padding: 2em 1.5em;
  text-decoration: none;
  transition: all 0.3s ease;
  cursor: pointer;
}

.structure-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
  border-color: var(--vp-c-brand-3);
}

.structure-card .part-number {
  display: block;
  font-family: var(--font-heading);
  font-size: 0.85rem;
  color: var(--vp-c-text-3);
  letter-spacing: 0.05em;
  margin-bottom: 0.5em;
}

.structure-card .part-name {
  display: block;
  font-family: var(--font-heading);
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--vp-c-brand-1);
  margin-bottom: 0.3em;
}

.structure-card .chapter-count {
  display: block;
  font-family: var(--font-quote);
  font-size: 0.9rem;
  color: var(--color-accent);
  margin-bottom: 1em;
}

.structure-card .part-desc {
  font-family: var(--font-body);
  font-size: 0.95rem;
  line-height: 1.8;
  color: var(--vp-c-text-2);
  margin: 0;
  text-indent: 0;
}

/* Responsive */
@media (max-width: 768px) {
  .hero-section {
    min-height: 60vh;
    padding: 3em 1.5em;
  }

  .book-title {
    font-size: 2.5rem;
  }

  .route-timeline {
    flex-direction: column;
    align-items: flex-start;
  }

  .route-item {
    width: 100%;
    justify-content: flex-start;
  }

  .structure-grid {
    grid-template-columns: 1fr;
  }
}
</style>

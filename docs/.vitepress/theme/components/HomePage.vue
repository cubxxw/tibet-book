<template>
  <div class="homepage">

    <!-- Hero 区域：雪山渐变 -->
    <div class="hero-section">
      <div class="hero-bg"></div>
      <div class="mountain-silhouette"></div>
      <div class="hero-content">
        <p class="hero-eyebrow">旅行文学 · 2026 年</p>
        <h1 class="book-title">减法之地</h1>
        <p class="book-subtitle">川西入藏 · 拉萨旅居手记</p>
        <p class="journey-stats">37 天  ·  7354 公里  ·  海拔 0 → 4718 米</p>
        <div class="hero-actions">
          <a href="/chapters/preface" class="read-button primary">开始阅读</a>
          <a href="#polarsteps" class="read-button secondary">旅程轨迹</a>
        </div>
      </div>
      <div class="scroll-indicator">
        <span>向下探索</span>
        <div class="scroll-arrow"></div>
      </div>
    </div>

    <!-- 双题记 -->
    <div class="epigraph-section">
      <blockquote class="epigraph-quote">
        <p>知识在这里不是积累，而是减法。</p>
        <cite>—— 写于哲蚌寺辨经院，2026 年 3 月 7 日</cite>
      </blockquote>
      <blockquote class="epigraph-quote">
        <p>世间安得双全法，不负如来不负卿。</p>
        <cite>—— 仓央嘉措</cite>
      </blockquote>
    </div>

    <div class="divider-line"></div>

    <!-- Polarsteps 嵌入式旅程地图 -->
    <div class="polarsteps-section" id="polarsteps">
      <h2 class="section-title">旅程轨迹</h2>
      <p class="section-desc">沿 318 国道入藏，穿越横断山脉，抵达世界屋脊</p>

      <div class="polarsteps-embed">
        <div class="embed-container">
          <iframe
            src="https://www.polarsteps.com/cubxxw/23988248-chuan-xi-zi-jia?embed=1&skin=light&showshare=0&showtitle=1&showuser=1"
            frameborder="0"
            allowfullscreen
            loading="lazy"
            title="川西自驾 - Polarsteps 旅程地图">
          </iframe>
        </div>
        <div class="polarsteps-attribution">
          <span>📍 实时旅程轨迹由 Polarsteps 记录</span>
        </div>
      </div>
    </div>

    <div class="divider-line"></div>

    <!-- 海拔剖面图 -->
    <div class="elevation-profile-section">
      <h2 class="section-title">海拔天路</h2>
      <p class="section-desc">从平原到屋脊，每一次爬升都是对身体的拷问</p>

      <div class="elevation-chart">
        <div class="chart-wrapper">
          <div class="elevation-line">
            <div class="elevation-point" style="--height: 2%; --label: '武汉'; --elev: '23m'"></div>
            <div class="elevation-point" style="--height: 10%; --label: '成都'; --elev: '500m'"></div>
            <div class="elevation-point" style="--height: 9%; --label: '三星堆'; --elev: '480m'"></div>
            <div class="elevation-point highlight" style="--height: 82%; --label: '折多山'; --elev: '4298m'"></div>
            <div class="elevation-point" style="--height: 74%; --label: '理塘'; --elev: '3900m'"></div>
            <div class="elevation-point" style="--height: 74%; --label: '来古冰川'; --elev: '3900m'"></div>
            <div class="elevation-point" style="--height: 55%; --label: '林芝'; --elev: '2900m'"></div>
            <div class="elevation-point highlight" style="--height: 69%; --label: '拉萨'; --elev: '3650m'"></div>
            <div class="elevation-point" style="--height: 84%; --label: '羊湖'; --elev: '4440m'"></div>
            <div class="elevation-point highlight" style="--height: 90%; --label: '纳木错'; --elev: '4718m'"></div>
            <div class="elevation-point" style="--height: 5%; --label: '重庆'; --elev: '244m'"></div>
          </div>
          <div class="elevation-labels">
            <span class="label-high">↑ 4718m</span>
            <span class="label-low">↓ 23m</span>
          </div>
        </div>
        <div class="stops-row">
          <div class="stop-item">
            <span class="stop-name">武汉</span>
            <span class="stop-elevation">23m</span>
          </div>
          <div class="stop-item">
            <span class="stop-name">成都</span>
            <span class="stop-elevation">500m</span>
          </div>
          <div class="stop-item">
            <span class="stop-name">折多山</span>
            <span class="stop-elevation">4298m</span>
          </div>
          <div class="stop-item">
            <span class="stop-name">理塘</span>
            <span class="stop-elevation">3900m</span>
          </div>
          <div class="stop-item">
            <span class="stop-name">来古冰川</span>
            <span class="stop-elevation">3900m</span>
          </div>
          <div class="stop-item">
            <span class="stop-name">林芝</span>
            <span class="stop-elevation">2900m</span>
          </div>
          <div class="stop-item highlight">
            <span class="stop-name">拉萨</span>
            <span class="stop-elevation">3650m</span>
          </div>
          <div class="stop-item">
            <span class="stop-name">羊湖</span>
            <span class="stop-elevation">4440m</span>
          </div>
          <div class="stop-item">
            <span class="stop-name">纳木错</span>
            <span class="stop-elevation">4718m</span>
          </div>
          <div class="stop-item">
            <span class="stop-name">重庆</span>
            <span class="stop-elevation">244m</span>
          </div>
        </div>
      </div>
    </div>

    <div class="divider-line"></div>

    <!-- 三部分结构 -->
    <div class="book-structure">
      <h2 class="section-title">书籍结构</h2>
      <div class="structure-grid">
        <a href="/chapters/01-wuhan" class="structure-card">
          <span class="part-number">第一部分</span>
          <span class="part-name">天路</span>
          <span class="chapter-range">第 1 — 4 章</span>
          <p class="part-desc">从成都平原到藏区腹地，穿越横断山脉，在海拔 4000 米的高原上追逐冰川的足迹。她在来古冰川的冰碛上认真堆石头——那种无用的专注，是全书最重要的意象。</p>
        </a>
        <a href="/chapters/05-arrival" class="structure-card">
          <span class="part-number">第二部分</span>
          <span class="part-name">拉萨</span>
          <span class="chapter-range">第 5 — 11 章</span>
          <p class="part-desc">在圣城停留一个月，转经、辩经、甜茶馆。哲蚌寺里的辩经告诉我：知识不是积累，而是减法。仓央嘉措的诗，是在罩子里做自己的武器。</p>
        </a>
        <a href="/chapters/12-fire" class="structure-card">
          <span class="part-number">第三部分</span>
          <span class="part-name">减法</span>
          <span class="chapter-range">第 12 — 13 章 + 尾声</span>
          <p class="part-desc">离开前的沉思，高原的馈赠。贡嘎机场的司机说：那就好好写。减去了一些东西，但也挺好的。</p>
        </a>
      </div>
    </div>

    <!-- 雪山装饰带 -->
    <div class="mountain-divider">
      <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
        <path class="mountain-path" d="M0,80 L150,20 L280,90 L400,40 L520,100 L620,30 L750,85 L880,25 L1000,75 L1200,45 L1200,120 L0,120 Z"/>
      </svg>
    </div>

    <div style="height: 3em;"></div>

  </div>
</template>

<style scoped>
.homepage {
  max-width: 100%;
  background: var(--vp-c-bg);
}

/* ═══════════════════════════════════════════════
   Hero 区域 · 雪山主题
   ═══════════════════════════════════════════════ */
.hero-section {
  position: relative;
  min-height: 90vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  text-align: center;
  padding: 4em 2em 6em;
}

.hero-bg {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse at 50% 70%, rgba(76, 140, 185, 0.35) 0%, transparent 50%),
    radial-gradient(ellipse at 20% 30%, rgba(50, 80, 110, 0.4) 0%, transparent 40%),
    radial-gradient(ellipse at 80% 25%, rgba(60, 100, 140, 0.35) 0%, transparent 45%),
    linear-gradient(180deg,
      #0a0e14 0%,
      #111a25 20%,
      #1a2835 40%,
      #233445 60%,
      #2d4055 80%,
      #3a506b 100%);
  z-index: 0;
}

/* 星空效果 */
.hero-bg::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    radial-gradient(1px 1px at 10% 20%, rgba(255,255,255,0.5) 0%, transparent 50%),
    radial-gradient(1px 1px at 20% 50%, rgba(255,255,255,0.4) 0%, transparent 50%),
    radial-gradient(1px 1px at 30% 15%, rgba(255,255,255,0.6) 0%, transparent 50%),
    radial-gradient(1px 1px at 45% 40%, rgba(255,255,255,0.3) 0%, transparent 50%),
    radial-gradient(1px 1px at 55% 25%, rgba(255,255,255,0.5) 0%, transparent 50%),
    radial-gradient(1px 1px at 65% 55%, rgba(255,255,255,0.4) 0%, transparent 50%),
    radial-gradient(1px 1px at 75% 10%, rgba(255,255,255,0.5) 0%, transparent 50%),
    radial-gradient(1px 1px at 85% 45%, rgba(255,255,255,0.4) 0%, transparent 50%),
    radial-gradient(1px 1px at 90% 20%, rgba(255,255,255,0.6) 0%, transparent 50%),
    radial-gradient(1px 1px at 15% 75%, rgba(255,255,255,0.3) 0%, transparent 50%),
    radial-gradient(1px 1px at 50% 80%, rgba(255,255,255,0.4) 0%, transparent 50%),
    radial-gradient(1px 1px at 80% 70%, rgba(255,255,255,0.3) 0%, transparent 50%);
  animation: twinkle 8s ease-in-out infinite;
}

@keyframes twinkle {
  0%, 100% { opacity: 0.7; }
  50% { opacity: 1; }
}

/* 雪山剪影 */
.mountain-silhouette {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 35%;
  z-index: 1;
  opacity: 0.8;
}

.mountain-silhouette::before {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 100%;
  background:
    linear-gradient(180deg, transparent 0%, rgba(30, 45, 60, 0.9) 100%),
    repeating-linear-gradient(
      135deg,
      transparent 0px,
      transparent 40px,
      rgba(40, 55, 75, 0.3) 41px,
      rgba(40, 55, 75, 0.5) 42px
    );
  clip-path: polygon(
    0% 100%,
    5% 60%, 10% 35%, 15% 55%, 20% 40%, 25% 65%,
    30% 45%, 35% 70%, 40% 50%, 45% 75%, 50% 30%,
    55% 55%, 60% 35%, 65% 60%, 70% 40%, 75% 65%,
    80% 45%, 85% 70%, 90% 50%, 95% 75%, 100% 100%
  );
}

.mountain-silhouette::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 10%;
  right: 10%;
  height: 70%;
  background: linear-gradient(180deg, transparent 0%, rgba(25, 35, 50, 0.95) 100%);
  clip-path: polygon(
    0% 100%,
    8% 50%, 15% 25%, 22% 45%, 30% 20%, 38% 55%,
    45% 30%, 52% 60%, 60% 25%, 68% 50%, 75% 35%,
    82% 55%, 90% 30%, 100% 100%
  );
}

/* 雪峰高光 */
.mountain-silhouette + .hero-bg::after {
  content: '';
  position: absolute;
  bottom: 20%;
  left: 5%;
  width: 90%;
  height: 2px;
  background: linear-gradient(90deg,
    transparent 0%,
    rgba(255,255,255,0.1) 20%,
    rgba(255,255,255,0.3) 50%,
    rgba(255,255,255,0.1) 80%,
    transparent 100%);
}

.hero-content {
  position: relative;
  z-index: 2;
  max-width: 680px;
  animation: heroFadeIn 1.4s ease-out forwards;
}

@keyframes heroFadeIn {
  from { opacity: 0; transform: translateY(32px); }
  to   { opacity: 1; transform: translateY(0); }
}

.hero-eyebrow {
  font-family: var(--font-quote);
  font-size: 0.85rem;
  color: rgba(196, 147, 63, 0.9);
  letter-spacing: 0.25em;
  margin-bottom: 1em;
  text-transform: uppercase;
}

.book-title {
  font-family: var(--font-heading);
  font-size: clamp(3rem, 10vw, 5.5rem);
  font-weight: 700;
  letter-spacing: 0.3em;
  color: #ffffff;
  margin: 0 0 0.2em 0;
  text-shadow: 0 4px 30px rgba(0, 0, 0, 0.6), 0 0 60px rgba(255,255,255,0.1);
  border: none !important;
  padding: 0 !important;
}

.book-subtitle {
  font-family: var(--font-quote);
  font-size: 1.15rem;
  color: rgba(255, 255, 255, 0.8);
  margin: 0 0 1.4em 0;
  letter-spacing: 0.1em;
}

.journey-stats {
  font-family: var(--font-heading);
  font-size: 0.95rem;
  font-weight: 500;
  color: rgba(196, 147, 63, 0.95);
  background: rgba(0, 0, 0, 0.35);
  border: 1px solid rgba(196, 147, 63, 0.3);
  display: inline-block;
  padding: 0.6em 2em;
  border-radius: 100px;
  margin-bottom: 2em;
  letter-spacing: 0.08em;
  backdrop-filter: blur(10px);
}

.hero-actions {
  display: flex;
  gap: 1em;
  justify-content: center;
  flex-wrap: wrap;
}

.read-button {
  display: inline-block;
  font-family: var(--font-heading);
  font-size: 1rem;
  font-weight: 500;
  padding: 1em 3em;
  border-radius: 8px;
  text-decoration: none;
  transition: all 0.3s ease;
  letter-spacing: 0.08em;
}

.read-button.primary {
  background: linear-gradient(135deg, var(--color-accent) 0%, #D4A34F 100%);
  color: white;
  box-shadow: 0 6px 24px rgba(196, 147, 63, 0.4);
}

.read-button.primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 32px rgba(196, 147, 63, 0.5);
}

.read-button.secondary {
  background: transparent;
  color: rgba(255, 255, 255, 0.9);
  border: 1.5px solid rgba(255, 255, 255, 0.4);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
}

.read-button.secondary:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.7);
  transform: translateY(-2px);
}

/* 向下滚动提示 */
.scroll-indicator {
  position: absolute;
  bottom: 2em;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5em;
  color: rgba(255, 255, 255, 0.5);
  font-family: var(--font-quote);
  font-size: 0.75rem;
  letter-spacing: 0.15em;
  animation: scrollBounce 2s ease-in-out infinite;
}

.scroll-arrow {
  width: 20px;
  height: 20px;
  border-right: 2px solid rgba(255, 255, 255, 0.5);
  border-bottom: 2px solid rgba(255, 255, 255, 0.5);
  transform: rotate(45deg);
}

@keyframes scrollBounce {
  0%, 100% { transform: translateX(-50%) translateY(0); }
  50% { transform: translateX(-50%) translateY(8px); }
}

/* ═══════════════════════════════════════════════
   题记区域
   ═══════════════════════════════════════════════ */
.epigraph-section {
  max-width: 680px;
  margin: 4em auto 3em;
  padding: 0 2em;
}

.epigraph-quote {
  border-left: 3px solid var(--color-accent);
  margin: 0 0 2em 0;
  padding: 1em 0 1em 1.8em;
  background: transparent;
}

.epigraph-quote p {
  font-family: var(--font-quote);
  font-size: 1.08rem;
  color: var(--vp-c-text-1);
  margin: 0 0 0.5em 0;
  line-height: 1.8;
}

.epigraph-quote cite {
  font-family: var(--font-quote);
  font-size: 0.85rem;
  color: var(--color-text-date);
  font-style: normal;
}

/* ═══════════════════════════════════════════════
   分割线
   ═══════════════════════════════════════════════ */
.divider-line {
  max-width: 680px;
  margin: 2.5em auto;
  height: 1px;
  background: linear-gradient(90deg,
    transparent 0%,
    var(--vp-c-divider) 20%,
    var(--vp-c-divider) 80%,
    transparent 100%);
  opacity: 0.6;
}

/* ═══════════════════════════════════════════════
   Polarsteps 嵌入区域
   ═══════════════════════════════════════════════ */
.polarsteps-section {
  max-width: 1100px;
  margin: 3em auto;
  padding: 0 2em;
}

.polarsteps-embed {
  margin-top: 2em;
}

.embed-container {
  position: relative;
  width: 100%;
  height: 520px;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 8px 40px rgba(0, 0, 0, 0.12);
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
}

.embed-container iframe {
  width: 100%;
  height: 100%;
  border: none;
}

.polarsteps-attribution {
  text-align: center;
  margin-top: 1em;
  font-family: var(--font-quote);
  font-size: 0.82rem;
  color: var(--color-text-date);
}

/* ═══════════════════════════════════════════════
   海拔剖面图
   ═══════════════════════════════════════════════ */
.elevation-profile-section {
  max-width: 1000px;
  margin: 3em auto;
  padding: 0 2em;
}

.elevation-chart {
  margin-top: 2em;
}

.chart-wrapper {
  position: relative;
  height: 280px;
  background: linear-gradient(180deg,
    rgba(44, 95, 124, 0.05) 0%,
    rgba(44, 95, 124, 0.02) 100%);
  border-radius: 12px 12px 0 0;
  border: 1px solid var(--vp-c-divider);
  border-bottom: none;
  padding: 2em 2em 0;
  overflow: hidden;
}

.elevation-line {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  height: 100%;
  gap: 0.3em;
}

.elevation-point {
  flex: 1;
  max-width: 60px;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
}

.elevation-point::before {
  content: '';
  width: 100%;
  height: calc(var(--height) * 2.2);
  min-height: 8px;
  background: linear-gradient(to top,
    var(--vp-c-brand-2) 0%,
    var(--vp-c-brand-3) 70%,
    rgba(196, 147, 63, 0.8) 100%);
  border-radius: 4px 4px 0 0;
  transition: all 0.3s ease;
  opacity: 0.75;
}

.elevation-point.highlight::before {
  background: linear-gradient(to top,
    var(--color-accent) 0%,
    #E8B86D 70%,
    #F5D890 100%);
  opacity: 1;
  box-shadow: 0 0 20px rgba(196, 147, 63, 0.5);
}

.elevation-point::after {
  content: attr(--label);
  position: absolute;
  bottom: -2.2em;
  font-family: var(--font-heading);
  font-size: 0.7rem;
  color: var(--vp-c-text-1);
  white-space: nowrap;
  text-align: center;
}

.elevation-point:hover::before {
  opacity: 1;
  transform: scaleY(1.05);
}

.elevation-labels {
  position: absolute;
  top: 1em;
  right: 1.5em;
  display: flex;
  flex-direction: column;
  gap: 0.3em;
  font-family: var(--font-quote);
  font-size: 0.7rem;
  color: var(--color-text-date);
}

.stops-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.5em;
  padding: 1em 1.5em;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 0 0 12px 12px;
  border-top: none;
}

.stop-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0.5em 0.8em;
  min-width: 70px;
  border-radius: 6px;
  transition: all 0.2s ease;
}

.stop-item:hover {
  background: rgba(196, 147, 63, 0.1);
}

.stop-item.highlight {
  background: rgba(196, 147, 63, 0.15);
}

.stop-name {
  font-family: var(--font-heading);
  font-size: 0.75rem;
  color: var(--vp-c-text-1);
}

.stop-elevation {
  font-family: var(--font-quote);
  font-size: 0.65rem;
  color: var(--color-text-date);
  margin-top: 0.2em;
}

.stop-item.highlight .stop-name {
  color: var(--color-accent);
  font-weight: 600;
}

/* ═══════════════════════════════════════════════
   书籍结构
   ═══════════════════════════════════════════════ */
.book-structure {
  max-width: 960px;
  margin: 3em auto;
  padding: 0 2em;
}

.structure-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1.5em;
  margin-top: 1.5em;
}

.structure-card {
  display: block;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
  padding: 2em 1.6em;
  text-decoration: none;
  transition: all 0.3s ease;
  cursor: pointer;
}

.structure-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.1);
  border-color: var(--color-accent);
}

.structure-card .part-number {
  display: block;
  font-family: var(--font-heading);
  font-size: 0.75rem;
  color: var(--vp-c-text-3);
  letter-spacing: 0.1em;
  margin-bottom: 0.4em;
}

.structure-card .part-name {
  display: block;
  font-family: var(--font-heading);
  font-size: 1.6rem;
  font-weight: 700;
  background: linear-gradient(135deg, var(--vp-c-brand-1) 0%, var(--color-accent) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 0.3em;
}

.structure-card .chapter-range {
  display: block;
  font-family: var(--font-quote);
  font-size: 0.8rem;
  color: var(--color-accent);
  margin-bottom: 1em;
}

.structure-card .part-desc {
  font-family: var(--font-body);
  font-size: 0.88rem;
  line-height: 1.9;
  color: var(--vp-c-text-2);
  margin: 0;
}

/* ═══════════════════════════════════════════════
   雪山装饰带
   ═══════════════════════════════════════════════ */
.mountain-divider {
  width: 100%;
  height: 100px;
  margin-top: 4em;
  position: relative;
  overflow: hidden;
}

.mountain-divider svg {
  width: 100%;
  height: 100%;
}

.mountain-path {
  fill: linear-gradient(180deg,
    rgba(44, 95, 124, 0.1) 0%,
    rgba(44, 95, 124, 0.2) 100%);
  opacity: 0.5;
}

/* ═══════════════════════════════════════════════
   响应式
   ═══════════════════════════════════════════════ */
@media (max-width: 768px) {
  .hero-section {
    min-height: 75vh;
    padding: 3em 1.5em;
  }

  .book-title {
    font-size: 3rem;
    letter-spacing: 0.2em;
  }

  .hero-actions {
    flex-direction: column;
    align-items: center;
  }

  .scroll-indicator {
    display: none;
  }

  .epigraph-section {
    padding: 0 1.5em;
  }

  .polarsteps-section,
  .elevation-profile-section,
  .book-structure {
    padding: 0 1.5em;
  }

  .embed-container {
    height: 420px;
  }

  .chart-wrapper {
    height: 220px;
    padding: 1.5em 1em 0;
  }

  .stops-row {
    gap: 0.3em;
  }

  .stop-item {
    min-width: 60px;
    padding: 0.4em 0.5em;
  }

  .structure-grid {
    grid-template-columns: 1fr;
  }

  .mountain-divider {
    height: 60px;
  }
}

@media (max-width: 480px) {
  .book-title {
    font-size: 2.4rem;
  }

  .journey-stats {
    font-size: 0.85rem;
    padding: 0.5em 1.2em;
  }

  .read-button {
    padding: 0.9em 2em;
    font-size: 0.95rem;
  }
}
</style>

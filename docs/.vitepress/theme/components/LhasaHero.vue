<template>
  <div class="lhasa-hero-container">

    <!-- 第一屏：雪山日出 Hero -->
    <section class="hero-section">
      <!-- 天空背景 -->
      <div class="sky-bg"></div>

      <!-- 太阳/月亮 -->
      <div class="sun"></div>

      <!-- 远山 -->
      <div class="mountains mountains-far">
        <svg viewBox="0 0 1200 300" preserveAspectRatio="none">
          <path d="M0,300 L0,200 L100,120 L200,180 L300,100 L400,160 L500,80 L600,150 L700,90 L800,170 L900,110 L1000,190 L1100,130 L1200,220 L1200,300 Z"/>
        </svg>
      </div>

      <!-- 近山（雪山） -->
      <div class="mountains mountains-near">
        <svg viewBox="0 0 1200 400" preserveAspectRatio="none">
          <defs>
            <linearGradient id="snowGrad" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#ffffff"/>
              <stop offset="100%" stop-color="#94a3b8"/>
            </linearGradient>
          </defs>
          <path d="M0,400 L0,250 L150,150 L250,220 L350,120 L500,200 L650,100 L800,180 L950,90 L1100,170 L1200,130 L1200,400 Z" fill="url(#snowGrad)"/>
        </svg>
      </div>

      <!-- 经幡 -->
      <div class="prayer-flags">
        <div class="flag-string" v-for="i in 3" :key="i" :style="{ top: `${i * 25}%` }">
          <span class="flag" v-for="j in 12" :key="j" :style="{
            '--flag-color': flagColors[(i * j) % 5],
            'animation-delay': `${(i * j) * 0.1}s`
          }"></span>
        </div>
      </div>

      <!-- 标题内容 -->
      <div class="hero-content">
        <p class="eyebrow">旅行文学 · 2026 年</p>
        <h1 class="title">减法之地</h1>
        <p class="subtitle">川西入藏 · 拉萨旅居手记</p>
        <div class="stats">
          <span>37 天</span>
          <span class="dot">·</span>
          <span>7354 公里</span>
          <span class="dot">·</span>
          <span>海拔 4718 米</span>
        </div>
        <div class="actions">
          <a href="/chapters/preface" class="btn btn-primary">开始阅读</a>
          <button @click="scrollDown" class="btn btn-secondary">沉浸体验</button>
        </div>
      </div>

      <!-- 雪花 -->
      <div class="snow-container" ref="snowContainer"></div>

      <!-- 滚动提示 -->
      <div class="scroll-hint" @click="scrollDown">
        <span>向下探索</span>
        <div class="arrow"></div>
      </div>
    </section>

    <!-- 第二屏：旅程海拔 -->
    <section class="journey-section">
      <div class="section-content">
        <h2 class="section-title">旅程轨迹</h2>
        <p class="section-subtitle">沿 318 国道入藏，穿越横断山脉</p>

        <div class="elevation-chart">
          <div class="elevation-bar" style="--height: 3%; --name: '武汉'">
            <span class="bar-label">23m</span>
          </div>
          <div class="elevation-bar" style="--height: 8%; --name: '成都'">
            <span class="bar-label">500m</span>
          </div>
          <div class="elevation-bar highlight" style="--height: 85%; --name: '折多山'">
            <span class="bar-label">4298m</span>
          </div>
          <div class="elevation-bar" style="--height: 65%; --name: '理塘'">
            <span class="bar-label">3900m</span>
          </div>
          <div class="elevation-bar" style="--height: 45%; --name: '林芝'">
            <span class="bar-label">2900m</span>
          </div>
          <div class="elevation-bar highlight" style="--height: 55%; --name: '拉萨'">
            <span class="bar-label">3650m</span>
          </div>
          <div class="elevation-bar" style="--height: 75%; --name: '羊湖'">
            <span class="bar-label">4440m</span>
          </div>
          <div class="elevation-bar highlight" style="--height: 95%; --name: '纳木错'">
            <span class="bar-label">4718m</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 第三屏：章节目录 -->
    <section class="chapters-section">
      <div class="section-content">
        <h2 class="section-title">目录</h2>
        <p class="section-subtitle">一场 37 天、7354 公里的内心旅程</p>

        <div class="chapter-grid">
          <div class="chapter-group">
            <h3 class="group-title">第一部分 · 天路</h3>
            <a href="/chapters/01-wuhan" class="chapter-link">
              <span class="num">01</span>
              <span class="text">武汉机场的茶颜悦色</span>
            </a>
            <a href="/chapters/02-sanxingdui" class="chapter-link">
              <span class="num">02</span>
              <span class="text">三星堆的间隙</span>
            </a>
            <a href="/chapters/03-zheduo" class="chapter-link">
              <span class="num">03</span>
              <span class="text">折多山，第二次</span>
            </a>
            <a href="/chapters/04-glacier" class="chapter-link">
              <span class="num">04</span>
              <span class="text">来古冰川与那堆无用的石头</span>
            </a>
          </div>

          <div class="chapter-group">
            <h3 class="group-title">第二部分 · 拉萨</h3>
            <a href="/chapters/05-arrival" class="chapter-link">
              <span class="num">05</span>
              <span class="text">抵达</span>
            </a>
            <a href="/chapters/06-farewell" class="chapter-link">
              <span class="num">06</span>
              <span class="text">告别</span>
            </a>
            <a href="/chapters/07-snowcity" class="chapter-link">
              <span class="num">07</span>
              <span class="text">雪城之下</span>
            </a>
            <a href="/chapters/08-tsangyang" class="chapter-link">
              <span class="num">08</span>
              <span class="text">仓央嘉措的夜晚</span>
            </a>
            <a href="/chapters/09-drepung" class="chapter-link">
              <span class="num">09</span>
              <span class="text">哲蚌寺：知识即减法</span>
            </a>
            <a href="/chapters/10-teahouse" class="chapter-link">
              <span class="num">10</span>
              <span class="text">甜茶馆与拉漂众生相</span>
            </a>
            <a href="/chapters/11-namtso" class="chapter-link">
              <span class="num">11</span>
              <span class="text">纳木错，天湖</span>
            </a>
          </div>

          <div class="chapter-group">
            <h3 class="group-title">第三部分 · 减法</h3>
            <a href="/chapters/12-fire" class="chapter-link">
              <span class="num">12</span>
              <span class="text">1959 年的那把火</span>
            </a>
            <a href="/chapters/13-gifts" class="chapter-link">
              <span class="num">13</span>
              <span class="text">高原的馈赠</span>
            </a>
          </div>
        </div>

        <div class="final-cta">
          <a href="/chapters/preface" class="btn btn-primary btn-large">
            <span>✨</span> 开始阅读
          </a>
        </div>
      </div>
    </section>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const snowContainer = ref(null)

const flagColors = ['#1E88E5', '#FDD835', '#E53935', '#43A047', '#8E24AA']

const scrollDown = () => {
  window.scrollTo({ top: window.innerHeight, behavior: 'smooth' })
}

const createSnowflakes = () => {
  if (!snowContainer.value) return
  for (let i = 0; i < 50; i++) {
    const flake = document.createElement('span')
    flake.className = 'snowflake'
    flake.style.cssText = `
      left: ${Math.random() * 100}%;
      animation-duration: ${Math.random() * 5 + 5}s;
      animation-delay: ${Math.random() * 5}s;
      opacity: ${Math.random() * 0.5 + 0.2};
      width: ${Math.random() * 3 + 2}px;
      height: ${Math.random() * 3 + 2}px;
    `
    snowContainer.value.appendChild(flake)
  }
}

onMounted(() => {
  createSnowflakes()
})
</script>

<style>
/* 全局样式 - 不 scoped，确保全屏效果 */
.lhasa-hero-container {
  width: 100%;
  min-height: 100vh;
  background: #0a0e1a;
}

/* ═══════════════════════════════════════════════
   Hero Section
   ═══════════════════════════════════════════════ */
.hero-section {
  position: relative;
  height: 100vh;
  min-height: 700px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.sky-bg {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg,
    #0a0e1a 0%,
    #1a2338 40%,
    #2d3848 70%,
    #4a5f6f 100%);
}

.sun {
  position: absolute;
  top: 20%;
  left: 50%;
  transform: translateX(-50%);
  width: 100px;
  height: 100px;
  background: radial-gradient(circle, #fef3c7 0%, #fbbf24 50%, #f59e0b 100%);
  border-radius: 50%;
  box-shadow: 0 0 60px rgba(251, 191, 36, 0.6);
  animation: sunGlow 4s ease-in-out infinite;
}

@keyframes sunGlow {
  0%, 100% { opacity: 0.8; transform: translateX(-50%) scale(1); }
  50% { opacity: 1; transform: translateX(-50%) scale(1.05); }
}

.mountains {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
}

.mountains svg {
  width: 100%;
  height: 100%;
}

.mountains-far {
  height: 40%;
  opacity: 0.5;
}

.mountains-far svg path {
  fill: #1a2338;
}

.mountains-near {
  height: 50%;
  bottom: 0;
  opacity: 0.8;
}

/* 经幡 */
.prayer-flags {
  position: absolute;
  top: 10%;
  left: 0;
  right: 0;
  height: 150px;
  pointer-events: none;
  z-index: 10;
}

.flag-string {
  position: absolute;
  left: 50%;
  right: 50%;
  height: 2px;
  background: rgba(255, 255, 255, 0.2);
  transform: translateX(-50%);
}

.flag {
  position: absolute;
  width: 12px;
  height: 18px;
  background: var(--flag-color, #E53935);
  border-radius: 2px;
  animation: flagWave 2s ease-in-out infinite;
}

.flag:nth-child(1) { left: calc(-50% + 0px); }
.flag:nth-child(2) { left: calc(-50% + 15px); }
.flag:nth-child(3) { left: calc(-50% + 30px); }
.flag:nth-child(4) { left: calc(-50% + 45px); }
.flag:nth-child(5) { left: calc(-50% + 60px); }
.flag:nth-child(6) { left: calc(-50% + 75px); }
.flag:nth-child(7) { left: calc(-50% + 90px); }
.flag:nth-child(8) { left: calc(-50% + 105px); }
.flag:nth-child(9) { left: calc(-50% + 120px); }
.flag:nth-child(10) { left: calc(-50% + 135px); }
.flag:nth-child(11) { left: calc(-50% + 150px); }
.flag:nth-child(12) { left: calc(-50% + 165px); }

@keyframes flagWave {
  0%, 100% { transform: scaleY(1) rotate(2deg); }
  50% { transform: scaleY(0.95) rotate(-2deg); }
}

/* Hero 内容 */
.hero-content {
  position: relative;
  z-index: 20;
  text-align: center;
  max-width: 800px;
  padding: 0 20px;
}

.eyebrow {
  font-family: var(--font-quote), 'KaiTi', serif;
  font-size: 0.9rem;
  color: #D4A34F;
  letter-spacing: 0.3em;
  margin-bottom: 1rem;
  text-transform: uppercase;
}

.title {
  font-family: var(--font-heading), sans-serif;
  font-size: clamp(3rem, 10vw, 6rem);
  font-weight: 700;
  color: #ffffff;
  letter-spacing: 0.2em;
  margin: 0;
  text-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
}

.subtitle {
  font-family: var(--font-quote), 'KaiTi', serif;
  font-size: 1.2rem;
  color: rgba(255, 255, 255, 0.7);
  margin-top: 0.5rem;
  letter-spacing: 0.1em;
}

.stats {
  display: inline-flex;
  align-items: center;
  gap: 1rem;
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(212, 163, 79, 0.3);
  padding: 0.7rem 2rem;
  border-radius: 100px;
  margin: 1.5rem 0;
  backdrop-filter: blur(10px);
}

.stats .dot {
  color: rgba(212, 163, 79, 0.4);
}

.stats span {
  font-family: var(--font-heading), sans-serif;
  font-size: 0.95rem;
  color: rgba(212, 163, 79, 0.9);
}

.actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  font-family: var(--font-heading), sans-serif;
  font-size: 1rem;
  font-weight: 500;
  padding: 1rem 2.5rem;
  border-radius: 8px;
  text-decoration: none;
  transition: all 0.3s ease;
  letter-spacing: 0.08em;
  cursor: pointer;
  border: none;
}

.btn-primary {
  background: linear-gradient(135deg, #D4A34F 0%, #E8B86D 100%);
  color: #0a0e1a;
  box-shadow: 0 6px 24px rgba(212, 163, 79, 0.4);
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 36px rgba(212, 163, 79, 0.6);
}

.btn-secondary {
  background: transparent;
  color: rgba(255, 255, 255, 0.9);
  border: 1.5px solid rgba(255, 255, 255, 0.4);
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: rgba(212, 163, 79, 0.6);
  transform: translateY(-2px);
}

.btn-large {
  font-size: 1.1rem;
  padding: 1.2rem 3.5rem;
}

/* 雪花 */
.snow-container {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 5;
}

.snowflake {
  position: absolute;
  top: -10px;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 50%;
  animation: snowFall linear infinite;
}

@keyframes snowFall {
  0% { transform: translateY(-10px) translateX(0); opacity: 0; }
  10% { opacity: 0.8; }
  90% { opacity: 0.8; }
  100% { transform: translateY(100vh) translateX(30px); opacity: 0; }
}

/* 滚动提示 */
.scroll-hint {
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  z-index: 20;
}

.scroll-hint span {
  font-family: var(--font-quote), 'KaiTi', serif;
  font-size: 0.75rem;
  color: rgba(255, 255, 255, 0.4);
  letter-spacing: 0.2em;
}

.arrow {
  width: 20px;
  height: 20px;
  border-right: 2px solid rgba(255, 255, 255, 0.4);
  border-bottom: 2px solid rgba(255, 255, 255, 0.4);
  transform: rotate(45deg);
  animation: arrowBounce 2s ease-in-out infinite;
}

@keyframes arrowBounce {
  0%, 100% { transform: rotate(45deg) translateY(0); }
  50% { transform: rotate(45deg) translateY(8px); }
}

/* ═══════════════════════════════════════════════
   Journey Section
   ═══════════════════════════════════════════════ */
.journey-section {
  position: relative;
  min-height: 80vh;
  padding: 4rem 2rem;
  background: linear-gradient(180deg, #0a0e1a 0%, #1a2338 100%);
  display: flex;
  align-items: center;
}

.section-content {
  max-width: 1000px;
  margin: 0 auto;
  width: 100%;
}

.section-title {
  font-family: var(--font-heading), sans-serif;
  font-size: 2rem;
  font-weight: 700;
  text-align: center;
  color: #ffffff;
  letter-spacing: 0.2em;
  margin-bottom: 0.5rem;
}

.section-subtitle {
  font-family: var(--font-quote), 'KaiTi', serif;
  font-size: 1rem;
  text-align: center;
  color: rgba(255, 255, 255, 0.5);
  margin-bottom: 3rem;
}

.elevation-chart {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  height: 300px;
  gap: 0.5rem;
  padding: 2rem;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 12px;
}

.elevation-bar {
  flex: 1;
  position: relative;
  background: linear-gradient(to top, #2563eb 0%, #3b82f6 70%, #D4A34F 100%);
  border-radius: 4px 4px 0 0;
  opacity: 0.75;
  transition: all 0.3s ease;
  height: calc(var(--height) * 3px);
  min-height: 8px;
}

.elevation-bar.highlight {
  background: linear-gradient(to top, #D4A34F 0%, #E8B86D 70%, #F5D890 100%);
  opacity: 1;
  box-shadow: 0 0 20px rgba(212, 163, 79, 0.5);
}

.elevation-bar:hover {
  transform: scaleY(1.05);
  opacity: 1;
}

.bar-label {
  position: absolute;
  bottom: -2rem;
  left: 50%;
  transform: translateX(-50%);
  font-family: var(--font-heading), sans-serif;
  font-size: 0.7rem;
  color: rgba(255, 255, 255, 0.6);
  white-space: nowrap;
}

.elevation-bar::after {
  content: attr(--name);
  position: absolute;
  bottom: -3.5rem;
  left: 50%;
  transform: translateX(-50%);
  font-family: var(--font-heading), sans-serif;
  font-size: 0.75rem;
  color: rgba(255, 255, 255, 0.8);
  white-space: nowrap;
}

/* ═══════════════════════════════════════════════
   Chapters Section
   ═══════════════════════════════════════════════ */
.chapters-section {
  position: relative;
  min-height: 100vh;
  padding: 4rem 2rem;
  background: linear-gradient(180deg, #1a2338 0%, #0a0e1a 100%);
  display: flex;
  align-items: center;
}

.chapter-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  margin: 2rem 0 3rem;
}

.chapter-group {
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  padding: 1.5rem;
}

.group-title {
  font-family: var(--font-heading), sans-serif;
  font-size: 1.1rem;
  font-weight: 600;
  color: #D4A34F;
  margin-bottom: 1rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid rgba(212, 163, 79, 0.2);
}

.chapter-link {
  display: flex;
  gap: 0.8rem;
  align-items: baseline;
  padding: 0.6rem 0;
  text-decoration: none;
  transition: all 0.2s ease;
}

.chapter-link:hover {
  transform: translateX(5px);
}

.chapter-link .num {
  font-family: var(--font-heading), sans-serif;
  font-size: 0.85rem;
  color: rgba(212, 163, 79, 0.8);
  letter-spacing: 0.1em;
}

.chapter-link .text {
  font-family: var(--font-body), serif;
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.4;
}

.chapter-link:hover .text {
  color: rgba(255, 255, 255, 0.9);
}

.final-cta {
  text-align: center;
  margin-top: 2rem;
}

/* ═══════════════════════════════════════════════
   Responsive
   ═══════════════════════════════════════════════ */
@media (max-width: 768px) {
  .hero-section {
    min-height: 100vh;
  }

  .title {
    font-size: clamp(2.5rem, 12vw, 4rem);
  }

  .actions {
    flex-direction: column;
    align-items: center;
  }

  .btn {
    width: 100%;
    max-width: 250px;
  }

  .scroll-hint {
    display: none;
  }

  .chapter-grid {
    grid-template-columns: 1fr;
  }

  .elevation-chart {
    height: 200px;
  }
}
</style>

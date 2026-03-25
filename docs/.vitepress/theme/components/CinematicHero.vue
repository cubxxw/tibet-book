<template>
  <div class="cinematic-hero" ref="heroContainer">

    <!-- 顶部导航栏 -->
    <header class="cinematic-nav" :class="{ 'nav-show': navVisible }">
      <div class="nav-content">
        <div class="nav-left">
          <span class="site-title">减法之地</span>
        </div>
        <nav class="nav-links">
          <a href="/chapters/preface" class="nav-link">开始阅读</a>
          <a href="/journey-map" class="nav-link">旅程地图</a>
          <a href="/about" class="nav-link">关于</a>
        </nav>
        <div class="nav-right">
          <button class="menu-toggle" @click="toggleSidebar" aria-label="菜单">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="3" y1="6" x2="21" y2="6"></line>
              <line x1="3" y1="12" x2="21" y2="12"></line>
              <line x1="3" y1="18" x2="21" y2="18"></line>
            </svg>
          </button>
        </div>
      </div>
    </header>

    <!-- 侧边栏 -->
    <aside class="cinematic-sidebar" :class="{ 'sidebar-show': sidebarVisible }">
      <div class="sidebar-header">
        <span class="sidebar-title">减法之地</span>
        <button class="sidebar-close" @click="toggleSidebar" aria-label="关闭菜单">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>
      </div>
      <div class="sidebar-content">
        <div class="sidebar-section">
          <h3 class="sidebar-heading">序言</h3>
          <a href="/chapters/preface" class="sidebar-link">凌晨五点</a>
        </div>

        <div class="sidebar-section">
          <h3 class="sidebar-heading">第一部分 · 天路</h3>
          <a href="/chapters/01-wuhan" class="sidebar-link">一 · 武汉机场的茶颜悦色</a>
          <a href="/chapters/02-sanxingdui" class="sidebar-link">二 · 三星堆的间隙</a>
          <a href="/chapters/03-zheduo" class="sidebar-link">三 · 折多山，第二次</a>
          <a href="/chapters/04-glacier" class="sidebar-link">四 · 来古冰川与那堆无用的石头</a>
        </div>

        <div class="sidebar-section">
          <h3 class="sidebar-heading">第二部分 · 拉萨</h3>
          <a href="/chapters/05-arrival" class="sidebar-link">五 · 抵达</a>
          <a href="/chapters/06-farewell" class="sidebar-link">六 · 告别</a>
          <a href="/chapters/07-snowcity" class="sidebar-link">七 · 雪城之下</a>
          <a href="/chapters/08-tsangyang" class="sidebar-link">八 · 仓央嘉措的夜晚</a>
          <a href="/chapters/09-drepung" class="sidebar-link">九 · 哲蚌寺：知识即减法</a>
          <a href="/chapters/10-teahouse" class="sidebar-link">十 · 甜茶馆与拉漂众生相</a>
          <a href="/chapters/11-namtso" class="sidebar-link">十一 · 纳木错，天湖</a>
        </div>

        <div class="sidebar-section">
          <h3 class="sidebar-heading">第三部分 · 减法</h3>
          <a href="/chapters/12-fire" class="sidebar-link">十二 · 1959 年的那把火</a>
          <a href="/chapters/13-gifts" class="sidebar-link">十三 · 高原的馈赠</a>
        </div>

        <div class="sidebar-section">
          <h3 class="sidebar-heading">尾声</h3>
          <a href="/chapters/epilogue" class="sidebar-link">出发的理由</a>
          <a href="/chapters/afterword" class="sidebar-link">后记</a>
        </div>
      </div>
    </aside>

    <!-- 遮罩层 -->
    <div class="sidebar-overlay" :class="{ 'overlay-show': sidebarVisible }" @click="toggleSidebar"></div>

    <!-- 第一幕：静态开场 -->
    <section class="act-1" ref="act1">
      <div class="dark-void-bg"></div>
      <div class="particle-field" ref="particleField"></div>

      <div class="title-container" ref="titleContainer">
        <div class="main-title" ref="mainTitle">
          <span class="title-char">减</span>
          <span class="title-char">法</span>
          <span class="title-char">之</span>
          <span class="title-char">地</span>
        </div>
      </div>

      <div class="floating-words" ref="floatingWords">
        <span class="float-word" style="--x: -30%; --y: -20%">318</span>
        <span class="float-word" style="--x: 35%; --y: -15%">拉萨</span>
        <span class="float-word" style="--x: -25%; --y: 25%">海拔</span>
        <span class="float-word" style="--x: 40%; --y: 30%">雪山</span>
        <span class="float-word" style="--x: -35%; --y: -35%">折多山</span>
        <span class="float-word" style="--x: 30%; --y: -35%">哲蚌寺</span>
        <span class="float-word" style="--x: -40%; --y: 15%">纳木错</span>
        <span class="float-word" style="--x: 45%; --y: -25%">来古冰川</span>
        <span class="float-word" style="--x: -20%; --y: 40%">甜茶馆</span>
        <span class="float-word" style="--x: 25%; --y: 40%">仓央嘉措</span>
        <span class="float-word" style="--x: -45%; --y: -10%">横断山脉</span>
        <span class="float-word" style="--x: 50%; --y: 20%">羊湖</span>
        <span class="float-word" style="--x: -15%; --y: -40%">成都</span>
        <span class="float-word" style="--x: 20%; --y: -45%">理塘</span>
        <span class="float-word" style="--x: -50%; --y: 35%">林芝</span>
        <span class="float-word" style="--x: 55%; --y: -10%">贡嘎</span>
      </div>

      <div class="scroll-prompt" ref="scrollPrompt">
        <span>向下进入</span>
        <div class="scroll-line"></div>
      </div>
    </section>

    <!-- 第二幕：裂开与解构 -->
    <section class="act-2" ref="act2">
      <div class="shattering-title">
        <div class="shard-left">
          <span class="shard-char">减</span>
          <span class="shard-char">法</span>
        </div>
        <div class="shard-right">
          <span class="shard-char">之</span>
          <span class="shard-char">地</span>
        </div>
      </div>

      <div class="ground-crack" ref="groundCrack">
        <svg viewBox="0 0 800 200" preserveAspectRatio="none">
          <path class="crack-path" d="M400,0 L398,5 L405,12 L395,20 L402,28 L390,38 L408,48 L395,60 L410,72 L398,85 L405,98 L392,112 L408,128 L395,145 L412,165 L400,185 L398,200" />
          <path class="crack-branch-1" d="M405,30 L420,25 L435,32 L425,45 L440,55" />
          <path class="crack-branch-2" d="M395,50 L380,55 L370,45 L385,65 L375,80" />
          <path class="crack-branch-3" d="M408,80 L425,75 L440,85 L430,100 L445,115" />
          <path class="crack-branch-4" d="M392,100 L375,110 L360,100 L378,125 L365,145" />
        </svg>
      </div>
    </section>

    <!-- 第三幕：雪山裂缝与小车驶入 -->
    <section class="act-3" ref="act3">
      <div class="distant-mountains" ref="distantMountains">
        <svg viewBox="0 0 1200 300" preserveAspectRatio="none">
          <path class="mountain-far" d="M0,250 L100,180 L200,240 L300,150 L400,220 L500,120 L600,200 L700,100 L800,190 L900,140 L1000,220 L1100,160 L1200,250 Z" />
        </svg>
      </div>

      <div class="mid-mountains" ref="midMountains">
        <svg viewBox="0 0 1200 400" preserveAspectRatio="none">
          <path class="mountain-mid" d="M0,350 L150,200 L280,320 L400,180 L520,290 L620,150 L750,270 L880,190 L1000,300 L1200,220 L1200,400 L0,400 Z" />
        </svg>
      </div>

      <div class="foreground-snow" ref="foregroundSnow">
        <svg viewBox="0 0 1200 500" preserveAspectRatio="none">
          <defs>
            <linearGradient id="snowGrad" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" style="stop-color:#f8fafc;stop-opacity:0.95" />
              <stop offset="50%" style="stop-color:#e2e8f0;stop-opacity:0.9" />
              <stop offset="100%" style="stop-color:#94a3b8;stop-opacity:0.85" />
            </linearGradient>
          </defs>
          <path class="mountain-foreground" d="M0,450 L80,300 L180,400 L280,250 L380,360 L480,200 L600,320 L720,180 L840,290 L960,220 L1080,340 L1200,260 L1200,500 L0,500 Z" fill="url(#snowGrad)" />
        </svg>
      </div>

      <div class="central-chasm" ref="centralChasm">
        <div class="chasm-left"></div>
        <div class="chasm-right"></div>
        <div class="chasm-void">
          <div class="chasm-mist"></div>
        </div>
      </div>

      <div class="vehicle" ref="vehicle">
        <div class="car-silhouette">
          <div class="car-body"></div>
          <div class="car-window"></div>
          <div class="car-light-left"></div>
          <div class="car-light-right"></div>
          <div class="car-light-beam-left"></div>
          <div class="car-light-beam-right"></div>
        </div>
      </div>

      <div class="snow-fall" ref="snowFall"></div>
    </section>

    <!-- 第四幕：目录展现 -->
    <section class="act-4" ref="act4">
      <div class="chapter-reveal">
        <div class="chapter-list" ref="chapterList">
          <div class="chapter-intro">
            <h2 class="section-heading">目录</h2>
            <p class="section-subtitle">一场 37 天、7354 公里的内心旅程</p>
          </div>

          <div class="chapters-grid">
            <a href="/chapters/01-wuhan" class="chapter-item">
              <span class="chapter-num">01</span>
              <span class="chapter-title">武汉机场的茶颜悦色</span>
            </a>
            <a href="/chapters/02-sanxingdui" class="chapter-item">
              <span class="chapter-num">02</span>
              <span class="chapter-title">三星堆的间隙</span>
            </a>
            <a href="/chapters/03-zheduo" class="chapter-item">
              <span class="chapter-num">03</span>
              <span class="chapter-title">折多山，第二次</span>
            </a>
            <a href="/chapters/04-glacier" class="chapter-item">
              <span class="chapter-num">04</span>
              <span class="chapter-title">来古冰川与那堆无用的石头</span>
            </a>
            <a href="/chapters/05-arrival" class="chapter-item">
              <span class="chapter-num">05</span>
              <span class="chapter-title">抵达</span>
            </a>
            <a href="/chapters/06-farewell" class="chapter-item">
              <span class="chapter-num">06</span>
              <span class="chapter-title">告别</span>
            </a>
            <a href="/chapters/07-snowcity" class="chapter-item">
              <span class="chapter-num">07</span>
              <span class="chapter-title">雪城之下</span>
            </a>
            <a href="/chapters/08-tsangyang" class="chapter-item">
              <span class="chapter-num">08</span>
              <span class="chapter-title">仓央嘉措的夜晚</span>
            </a>
            <a href="/chapters/09-drepung" class="chapter-item">
              <span class="chapter-num">09</span>
              <span class="chapter-title">哲蚌寺：知识即减法</span>
            </a>
            <a href="/chapters/10-teahouse" class="chapter-item">
              <span class="chapter-num">10</span>
              <span class="chapter-title">甜茶馆与拉漂众生相</span>
            </a>
            <a href="/chapters/11-namtso" class="chapter-item">
              <span class="chapter-num">11</span>
              <span class="chapter-title">纳木错，天湖</span>
            </a>
            <a href="/chapters/12-fire" class="chapter-item">
              <span class="chapter-num">12</span>
              <span class="chapter-title">1959 年的那把火</span>
            </a>
            <a href="/chapters/13-gifts" class="chapter-item">
              <span class="chapter-num">13</span>
              <span class="chapter-title">高原的馈赠</span>
            </a>
          </div>

          <div class="chapter-cta">
            <a href="/chapters/preface" class="cta-button">开始阅读</a>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const heroContainer = ref(null)
const act1 = ref(null)
const act2 = ref(null)
const act3 = ref(null)
const act4 = ref(null)
const titleContainer = ref(null)
const mainTitle = ref(null)
const floatingWords = ref(null)
const scrollPrompt = ref(null)
const particleField = ref(null)
const groundCrack = ref(null)
const distantMountains = ref(null)
const midMountains = ref(null)
const foregroundSnow = ref(null)
const centralChasm = ref(null)
const vehicle = ref(null)
const snowFall = ref(null)
const chapterList = ref(null)

let scrollProgress = 0
let animationFrameId = null
let particles = []
let snowflakes = []
let sidebarVisible = false
let navVisible = false

const toggleSidebar = () => {
  sidebarVisible = !sidebarVisible
}

const createParticles = () => {
  if (!particleField.value) return
  particleField.value.innerHTML = ''
  particles = []
  for (let i = 0; i < 60; i++) {
    const particle = document.createElement('span')
    particle.className = 'particle'
    particle.style.left = Math.random() * 100 + '%'
    particle.style.top = Math.random() * 100 + '%'
    particle.style.opacity = Math.random() * 0.5 + 0.2
    particle.style.animationDelay = Math.random() * 5 + 's'
    particleField.value.appendChild(particle)
    particles.push(particle)
  }
}

const createSnowflakes = () => {
  if (!snowFall.value) return
  snowFall.value.innerHTML = ''
  snowflakes = []
  for (let i = 0; i < 80; i++) {
    const flake = document.createElement('span')
    flake.className = 'snowflake'
    flake.style.left = Math.random() * 100 + '%'
    flake.style.animationDuration = (Math.random() * 3 + 5) + 's'
    flake.style.animationDelay = Math.random() * 5 + 's'
    flake.style.opacity = Math.random() * 0.6 + 0.2
    snowFall.value.appendChild(flake)
    snowflakes.push(flake)
  }
}

const updateNavVisibility = () => {
  const act4Start = window.innerHeight * 2.5
  const shouldShow = window.scrollY > act4Start
  if (shouldShow !== navVisible) {
    navVisible = shouldShow
  }
}

const handleScroll = () => {
  const scrollTop = window.scrollY
  const windowHeight = window.innerHeight
  scrollProgress = Math.min(scrollTop / (windowHeight * 4), 1)
  updateAnimation()
  updateNavVisibility()
}

const updateAnimation = () => {
  const scrollY = window.scrollY
  const windowHeight = window.innerHeight

  // Act 1
  if (act1.value && titleContainer.value) {
    const act1Progress = Math.min(scrollY / (windowHeight * 0.8), 1)
    titleContainer.value.style.transform = `scale(${1 + act1Progress * 0.15}) translateY(${act1Progress * -50}px)`
    titleContainer.value.style.opacity = 1 - act1Progress * 1.2
    mainTitle.value.style.letterSpacing = `${0.1 + act1Progress * 0.4}em`

    if (floatingWords.value) {
      const words = floatingWords.value.querySelectorAll('.float-word')
      words.forEach((word) => {
        const x = word.style.getPropertyValue('--x') || '0%'
        const y = word.style.getPropertyValue('--y') || '0%'
        const scatterX = parseFloat(x) * (1 + act1Progress * 2)
        const scatterY = parseFloat(y) * (1 + act1Progress * 2)
        word.style.transform = `translate(${scatterX}vw, ${scatterY}vh) scale(${1 - act1Progress * 0.5})`
        word.style.opacity = 1 - act1Progress * 1.3
      })
    }

    if (scrollPrompt.value) {
      scrollPrompt.value.style.opacity = 1 - act1Progress * 2
    }
  }

  // Act 2
  if (act2.value) {
    const act2Start = windowHeight * 0.6
    const act2Progress = Math.min(Math.max((scrollY - act2Start) / (windowHeight * 0.7), 0), 1)

    const shardLeft = act2.value.querySelector('.shard-left')
    const shardRight = act2.value.querySelector('.shard-right')
    const crack = act2.value.querySelector('.ground-crack')

    if (shardLeft) {
      shardLeft.style.transform = `translateX(${-150 * act2Progress}px) rotate(${-5 * act2Progress}deg)`
      shardLeft.style.opacity = 1 - act2Progress * 1.1
    }
    if (shardRight) {
      shardRight.style.transform = `translateX(${150 * act2Progress}px) rotate(${5 * act2Progress}deg)`
      shardRight.style.opacity = 1 - act2Progress * 1.1
    }
    if (crack) {
      crack.style.transform = `scaleY(${0.3 + act2Progress * 1.5})`
      crack.style.opacity = act2Progress * 0.8
    }
  }

  // Act 3
  if (act3.value) {
    const act3Start = windowHeight * 1.5
    const act3Progress = Math.min(Math.max((scrollY - act3Start) / (windowHeight * 0.8), 0), 1)
    const easeProgress = easeInOutCubic(act3Progress)

    if (distantMountains.value) {
      distantMountains.value.style.opacity = easeProgress * 0.6
      distantMountains.value.style.transform = `translateY(${20 - easeProgress * 20}px)`
    }
    if (midMountains.value) {
      midMountains.value.style.opacity = easeProgress * 0.8
      midMountains.value.style.transform = `translateY(${30 - easeProgress * 30}px)`
    }
    if (centralChasm.value) {
      const chasmLeft = centralChasm.value.querySelector('.chasm-left')
      const chasmRight = centralChasm.value.querySelector('.chasm-right')
      const chasmVoid = centralChasm.value.querySelector('.chasm-void')
      if (chasmLeft) chasmLeft.style.transform = `translateX(${-80 * easeProgress}px)`
      if (chasmRight) chasmRight.style.transform = `translateX(${80 * easeProgress}px)`
      if (chasmVoid) {
        chasmVoid.style.opacity = easeProgress * 0.9
        chasmVoid.style.transform = `scaleY(${0.5 + easeProgress * 0.5})`
      }
    }
    if (vehicle.value) {
      const carProgress = easeInOutCubic(Math.min(act3Progress * 1.3, 1))
      vehicle.value.style.transform = `translateX(${-50 + carProgress * 50}px) translateY(${carProgress * 30}px) scale(${0.6 + carProgress * 0.4})`
      vehicle.value.style.opacity = carProgress
    }
  }

  // Act 4
  if (act4.value && chapterList.value) {
    const act4Start = windowHeight * 2.5
    const act4Progress = Math.min(Math.max((scrollY - act4Start) / (windowHeight * 0.6), 0), 1)
    const easeAct4 = easeInOutCubic(act4Progress)

    chapterList.value.style.opacity = easeAct4
    chapterList.value.style.transform = `translateY(${50 - easeAct4 * 50}px)`

    const chapterItems = chapterList.value.querySelectorAll('.chapter-item')
    chapterItems.forEach((item, i) => {
      const delay = i * 0.05
      const itemProgress = Math.min(Math.max((act4Progress - delay) * 1.5, 0), 1)
      item.style.opacity = itemProgress
      item.style.transform = `translateX(${-20 + itemProgress * 20}px)`
    })
  }
}

const easeInOutCubic = (x) => x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2

onMounted(() => {
  createParticles()
  createSnowflakes()
  window.addEventListener('scroll', handleScroll, { passive: true })
  updateAnimation()
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  if (animationFrameId) cancelAnimationFrame(animationFrameId)
})
</script>

<style scoped>
.cinematic-hero {
  position: relative;
  width: 100%;
  overflow-x: hidden;
}

/* ═══════════════════════════════════════════════
   顶部导航栏
   ═══════════════════════════════════════════════ */
.cinematic-nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  background: linear-gradient(180deg, rgba(5, 7, 10, 0.9) 0%, transparent 100%);
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.8s ease;
}

.cinematic-nav.nav-show {
  opacity: 1;
  pointer-events: auto;
}

.nav-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1.2em 2em;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-left .site-title {
  font-family: var(--font-heading);
  font-size: 1.1rem;
  font-weight: 700;
  color: #ffffff;
  letter-spacing: 0.15em;
}

.nav-links {
  display: flex;
  gap: 2em;
}

.nav-link {
  font-family: var(--font-heading);
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  transition: color 0.2s ease;
}

.nav-link:hover {
  color: #ffffff;
}

.nav-right .menu-toggle {
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 0.5em;
  color: rgba(255, 255, 255, 0.7);
  transition: color 0.2s ease;
}

.nav-right .menu-toggle:hover {
  color: #ffffff;
}

/* ═══════════════════════════════════════════════
   侧边栏
   ═══════════════════════════════════════════════ */
.cinematic-sidebar {
  position: fixed;
  top: 0;
  left: 0;
  width: 280px;
  height: 100vh;
  background: linear-gradient(180deg, #0a0f18 0%, #142030 100%);
  z-index: 101;
  transform: translateX(-100%);
  transition: transform 0.5s ease;
  overflow-y: auto;
  border-right: 1px solid rgba(255, 255, 255, 0.05);
}

.cinematic-sidebar.sidebar-show {
  transform: translateX(0);
}

.sidebar-header {
  padding: 1.5em;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.sidebar-title {
  font-family: var(--font-heading);
  font-size: 1rem;
  font-weight: 700;
  color: #ffffff;
  letter-spacing: 0.1em;
}

.sidebar-close {
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 0.3em;
  color: rgba(255, 255, 255, 0.5);
}

.sidebar-content {
  padding: 1em 0;
}

.sidebar-section {
  padding: 0.8em 1.5em;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.sidebar-heading {
  font-family: var(--font-heading);
  font-size: 0.8rem;
  color: rgba(196, 147, 63, 0.8);
  letter-spacing: 0.1em;
  margin-bottom: 0.6em;
  font-weight: 600;
}

.sidebar-link {
  display: block;
  font-family: var(--font-body);
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.6);
  text-decoration: none;
  padding: 0.4em 0;
  transition: color 0.2s ease, padding-left 0.2s ease;
}

.sidebar-link:hover {
  color: rgba(196, 147, 63, 0.8);
  padding-left: 0.5em;
}

.sidebar-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  z-index: 100;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.5s ease;
  backdrop-filter: blur(4px);
}

.sidebar-overlay.overlay-show {
  opacity: 1;
  pointer-events: auto;
}

/* ═══════════════════════════════════════════════
   Act 1 - 静态开场
   ═══════════════════════════════════════════════ */
.act-1 {
  position: relative;
  height: 100vh;
  min-height: 700px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.dark-void-bg {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse at 50% 70%, rgba(30, 45, 65, 0.4) 0%, transparent 50%),
    radial-gradient(ellipse at 30% 30%, rgba(20, 30, 45, 0.5) 0%, transparent 40%),
    radial-gradient(ellipse at 70% 25%, rgba(25, 40, 60, 0.35) 0%, transparent 45%),
    linear-gradient(180deg, #05070a 0%, #0a0f18 25%, #0d1520 50%, #0f1a28 75%, #142030 100%);
}

.particle-field {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 1;
}

.particle {
  position: absolute;
  width: 2px;
  height: 2px;
  background: rgba(255, 255, 255, 0.4);
  border-radius: 50%;
  animation: particleFloat 8s ease-in-out infinite;
}

@keyframes particleFloat {
  0%, 100% { transform: translateY(0) translateX(0); opacity: 0.2; }
  25% { transform: translateY(-10px) translateX(5px); opacity: 0.5; }
  50% { transform: translateY(-5px) translateX(-3px); opacity: 0.3; }
  75% { transform: translateY(-15px) translateX(2px); opacity: 0.4; }
}

.title-container {
  position: relative;
  z-index: 2;
  will-change: transform, opacity, letter-spacing;
}

.main-title {
  display: flex;
  gap: 0;
  font-family: var(--font-heading);
  font-size: clamp(4rem, 15vw, 12rem);
  font-weight: 700;
  color: #ffffff;
  letter-spacing: 0.1em;
  text-shadow: 0 4px 40px rgba(0, 0, 0, 0.8), 0 0 80px rgba(255, 255, 255, 0.1);
}

.title-char {
  display: inline-block;
}

.floating-words {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 1;
}

.float-word {
  position: absolute;
  left: 50%;
  top: 50%;
  font-family: var(--font-quote);
  font-size: clamp(0.7rem, 2vw, 1rem);
  color: rgba(255, 255, 255, 0.25);
  white-space: nowrap;
  will-change: transform, opacity;
}

.scroll-prompt {
  position: absolute;
  bottom: 3em;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.8em;
  z-index: 2;
  opacity: 1;
  transition: opacity 0.1s linear;
}

.scroll-prompt span {
  font-family: var(--font-quote);
  font-size: 0.75rem;
  color: rgba(255, 255, 255, 0.4);
  letter-spacing: 0.2em;
}

.scroll-line {
  width: 1px;
  height: 40px;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.5) 0%, rgba(255, 255, 255, 0.1) 100%);
  animation: scrollLinePulse 2s ease-in-out infinite;
}

@keyframes scrollLinePulse {
  0%, 100% { opacity: 0.4; height: 40px; }
  50% { opacity: 0.8; height: 50px; }
}

/* Act 2, 3, 4 样式保持不变... */
.act-2 {
  position: relative;
  height: 80vh;
  min-height: 600px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.shattering-title {
  position: relative;
  display: flex;
  gap: 2em;
}

.shard-left, .shard-right {
  display: flex;
  gap: 0.5em;
  will-change: transform, opacity;
}

.shard-char {
  font-family: var(--font-heading);
  font-size: clamp(3rem, 10vw, 8rem);
  font-weight: 700;
  color: rgba(255, 255, 255, 0.7);
  text-shadow: 0 2px 20px rgba(0, 0, 0, 0.6);
}

.ground-crack {
  position: absolute;
  bottom: 20%;
  left: 50%;
  transform: translateX(-50%) scaleY(0.3);
  width: 200px;
  height: 300px;
  opacity: 0;
  will-change: transform, opacity;
}

.crack-path {
  fill: none;
  stroke: rgba(255, 255, 255, 0.6);
  stroke-width: 2;
  stroke-linecap: round;
  filter: drop-shadow(0 0 8px rgba(255, 255, 255, 0.4));
}

.crack-branch-1, .crack-branch-2, .crack-branch-3, .crack-branch-4 {
  fill: none;
  stroke: rgba(255, 255, 255, 0.4);
  stroke-width: 1.5;
  stroke-linecap: round;
  opacity: 0.6;
}

.act-3 {
  position: relative;
  height: 120vh;
  min-height: 900px;
  overflow: hidden;
}

.distant-mountains, .mid-mountains {
  position: absolute;
  left: 0;
  right: 0;
  height: 40%;
  opacity: 0;
  will-change: opacity, transform;
}

.distant-mountains { top: 15%; }
.mid-mountains { top: 25%; height: 50%; }

.mountain-far { fill: rgba(40, 55, 75, 0.5); filter: blur(2px); }
.mountain-mid { fill: rgba(50, 65, 85, 0.7); }

.foreground-snow {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 60%;
}

.central-chasm {
  position: absolute;
  top: 35%;
  left: 50%;
  transform: translateX(-50%);
  width: 200px;
  height: 400px;
  display: flex;
}

.chasm-left, .chasm-right {
  position: absolute;
  top: 0;
  width: 50%;
  height: 100%;
  background: linear-gradient(135deg, rgba(248, 250, 252, 0.9) 0%, rgba(226, 232, 240, 0.85) 50%, rgba(148, 163, 184, 0.8) 100%);
  will-change: transform;
}

.chasm-left { left: 0; clip-path: polygon(0 0, 100% 0, 80% 100%, 0% 100%); }
.chasm-right { right: 0; clip-path: polygon(20% 0, 100% 0, 100% 100%, 0% 100%); }

.chasm-void {
  position: absolute;
  left: 50%;
  top: 0;
  transform: translateX(-50%) scaleY(0.5);
  width: 60px;
  height: 100%;
  background: linear-gradient(180deg, rgba(10, 15, 24, 0.9) 0%, rgba(20, 30, 45, 0.8) 100%);
  opacity: 0;
  will-change: opacity, transform;
}

.chasm-mist {
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 50% 50%, rgba(200, 210, 220, 0.3) 0%, transparent 70%);
  animation: mistPulse 4s ease-in-out infinite;
}

@keyframes mistPulse {
  0%, 100% { opacity: 0.4; }
  50% { opacity: 0.7; }
}

.vehicle {
  position: absolute;
  top: 45%;
  left: 30%;
  transform: translateX(-50%) scale(0.6);
  opacity: 0;
  will-change: transform, opacity;
  z-index: 10;
}

.car-silhouette {
  position: relative;
  width: 80px;
  height: 35px;
}

.car-body {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 20px;
  background: linear-gradient(180deg, #2d3a4a 0%, #1a2330 100%);
  border-radius: 4px 8px 2px 2px;
}

.car-window {
  position: absolute;
  top: 5px;
  left: 20px;
  width: 35px;
  height: 15px;
  background: linear-gradient(180deg, rgba(100, 120, 140, 0.6) 0%, rgba(60, 80, 100, 0.8) 100%);
  border-radius: 3px 5px 0 0;
}

.car-light-left, .car-light-right {
  position: absolute;
  right: 2px;
  width: 4px;
  height: 8px;
  background: rgba(255, 220, 150, 0.8);
  border-radius: 2px;
}

.car-light-left { bottom: 5px; }
.car-light-right { bottom: 5px; right: 1px; }

.car-light-beam-left, .car-light-beam-right {
  position: absolute;
  right: 5px;
  width: 120px;
  height: 30px;
  background: linear-gradient(90deg, rgba(255, 240, 200, 0.4) 0%, transparent 100%);
  clip-path: polygon(0 30%, 100% 0, 100% 100%, 0 70%);
  opacity: 0;
}

.car-light-beam-left { bottom: 4px; transform: rotate(-5deg); }
.car-light-beam-right { bottom: 8px; transform: rotate(5deg); }

.snow-fall {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 20;
  overflow: hidden;
}

.snowflake {
  position: absolute;
  top: -10px;
  width: 4px;
  height: 4px;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 50%;
  filter: blur(1px);
  animation: snowFall linear infinite;
}

@keyframes snowFall {
  0% { transform: translateY(-10px) translateX(0); opacity: 0; }
  10% { opacity: 0.8; }
  90% { opacity: 0.8; }
  100% { transform: translateY(100vh) translateX(20px); opacity: 0; }
}

.act-4 {
  position: relative;
  min-height: 100vh;
  padding: 6em 2em 4em;
  background: linear-gradient(180deg, #0f1620 0%, #141d28 30%, #1a2330 100%);
}

.chapter-reveal {
  max-width: 900px;
  margin: 0 auto;
}

.chapter-list {
  opacity: 0;
  transform: translateY(50px);
  transition: opacity 0.8s ease, transform 0.8s ease;
}

.section-heading {
  font-family: var(--font-heading);
  font-size: 2.5rem;
  font-weight: 700;
  text-align: center;
  color: #ffffff;
  letter-spacing: 0.2em;
  margin-bottom: 0.5em;
}

.section-subtitle {
  font-family: var(--font-quote);
  font-size: 1rem;
  text-align: center;
  color: rgba(255, 255, 255, 0.5);
  margin-bottom: 3em;
}

.chapters-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 0.8em;
  margin-bottom: 3em;
}

.chapter-item {
  display: flex;
  align-items: baseline;
  gap: 0.8em;
  padding: 1em 1.2em;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 6px;
  text-decoration: none;
  transition: all 0.25s ease;
  opacity: 0;
  transform: translateX(-20px);
}

.chapter-item:hover {
  background: rgba(255, 255, 255, 0.06);
  border-color: rgba(196, 147, 63, 0.4);
  transform: translateX(5px) !important;
}

.chapter-num {
  font-family: var(--font-heading);
  font-size: 0.85rem;
  color: rgba(196, 147, 63, 0.8);
  letter-spacing: 0.1em;
  flex-shrink: 0;
}

.chapter-num::before { content: '['; margin-right: 2px; opacity: 0.5; }
.chapter-num::after { content: ']'; margin-left: 2px; opacity: 0.5; }

.chapter-title {
  font-family: var(--font-body);
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.4;
}

.chapter-cta {
  text-align: center;
  margin-top: 2em;
}

.cta-button {
  display: inline-block;
  font-family: var(--font-heading);
  font-size: 1.05rem;
  font-weight: 500;
  color: #ffffff;
  background: linear-gradient(135deg, var(--color-accent) 0%, #D4A34F 100%);
  padding: 1em 3.5em;
  border-radius: 8px;
  text-decoration: none;
  box-shadow: 0 6px 24px rgba(196, 147, 63, 0.35);
  transition: all 0.3s ease;
  letter-spacing: 0.08em;
}

.cta-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 36px rgba(196, 147, 63, 0.5);
}

@media (max-width: 768px) {
  .act-1 { height: 80vh; }
  .act-2 { height: 60vh; }
  .act-3 { height: 100vh; }

  .main-title {
    font-size: clamp(2.5rem, 18vw, 6rem);
    flex-wrap: wrap;
    justify-content: center;
  }

  .chapters-grid {
    grid-template-columns: 1fr;
  }

  .nav-links {
    display: none;
  }

  .cinematic-sidebar {
    width: 260px;
  }
}
</style>

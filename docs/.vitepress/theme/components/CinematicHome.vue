<template>
  <div class="cinematic-home" ref="container">
    <!-- Hero 视口区域 - fixed 定位元素容器 -->
    <div class="hero-viewport">
      <!-- Canvas 容器 -->
      <canvas ref="canvas" class="webgl-canvas"></canvas>

      <!-- 开场文字 -->
      <div class="opening-text" :style="openingStyle">
        <div class="title-glow"></div>
        <h1 class="main-title">
          <span v-for="(char, i) in title" :key="i"
                class="title-char"
                :style="getCharStyle(i)">
            {{ char }}
          </span>
        </h1>
      </div>

      <!-- 碎片效果 -->
      <div class="fragments-container">
        <div v-for="(fragment, i) in fragments"
             :key="i"
             class="fragment"
             :style="fragment.style">
          {{ fragment.text }}
        </div>
      </div>

      <!-- 滚动提示 -->
      <div class="scroll-hint" :style="scrollHintStyle">
        <span>向下探索</span>
        <div class="scroll-arrow"></div>
      </div>

      <!-- 裂缝效果 -->
      <div class="crack-overlay" :style="crackStyle"></div>

      <!-- 小车剪影 -->
      <div class="car-silhouette" :style="carStyle">
        <div class="car-body">
          <div class="car-wheel-front"></div>
        </div>
        <div class="car-light"></div>
      </div>
    </div>

    <!-- 内容区域 -->
    <div class="content-section" ref="contentSection">
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

      <!-- Polarsteps 嵌入旅程地图 -->
      <div class="polarsteps-section" id="polarsteps">
        <h2 class="section-title">旅程轨迹</h2>
        <p class="section-desc">沿 318 国道入藏，穿越横断山脉，抵达世界屋脊</p>
        <div class="polarsteps-embed">
          <div class="embed-container">
            <iframe src="https://www.polarsteps.com/cubxxw/23988248-chuan-xi-zi-jia?embed=1&skin=light&showshare=0&showtitle=1&showuser=1" frameborder="0" allowfullscreen loading="lazy"></iframe>
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
              <div class="elevation-point" style="--height: 2%"></div>
              <div class="elevation-point" style="--height: 10%"></div>
              <div class="elevation-point" style="--height: 9%"></div>
              <div class="elevation-point highlight" style="--height: 82%"></div>
              <div class="elevation-point" style="--height: 74%"></div>
              <div class="elevation-point" style="--height: 74%"></div>
              <div class="elevation-point" style="--height: 55%"></div>
              <div class="elevation-point highlight" style="--height: 69%"></div>
              <div class="elevation-point" style="--height: 84%"></div>
              <div class="elevation-point highlight" style="--height: 90%"></div>
              <div class="elevation-point" style="--height: 5%"></div>
            </div>
            <div class="elevation-labels">
              <span class="label-high">↑ 4718m</span>
              <span class="label-low">↓ 23m</span>
            </div>
          </div>
          <div class="stops-row">
            <div class="stop-item"><span class="stop-name">武汉</span><span class="stop-elevation">23m</span></div>
            <div class="stop-item"><span class="stop-name">成都</span><span class="stop-elevation">500m</span></div>
            <div class="stop-item"><span class="stop-name">折多山</span><span class="stop-elevation">4298m</span></div>
            <div class="stop-item"><span class="stop-name">理塘</span><span class="stop-elevation">3900m</span></div>
            <div class="stop-item"><span class="stop-name">来古冰川</span><span class="stop-elevation">3900m</span></div>
            <div class="stop-item"><span class="stop-name">林芝</span><span class="stop-elevation">2900m</span></div>
            <div class="stop-item highlight"><span class="stop-name">拉萨</span><span class="stop-elevation">3650m</span></div>
            <div class="stop-item"><span class="stop-name">羊湖</span><span class="stop-elevation">4440m</span></div>
            <div class="stop-item"><span class="stop-name">纳木错</span><span class="stop-elevation">4718m</span></div>
            <div class="stop-item"><span class="stop-name">重庆</span><span class="stop-elevation">244m</span></div>
          </div>
        </div>
      </div>

      <div class="divider-line"></div>

      <!-- 书籍结构 -->
      <div class="book-structure">
        <h2 class="section-title">书籍结构</h2>
        <div class="structure-grid">
          <a href="/chapters/01-wuhan" class="structure-card">
            <span class="part-number">第一部分</span>
            <span class="part-name">天路</span>
            <span class="chapter-range">第 1 — 4 章</span>
            <p class="part-desc">从成都平原到藏区腹地，穿越横断山脉，在海拔 4000 米的高原上追逐冰川的足迹。</p>
          </a>
          <a href="/chapters/05-arrival" class="structure-card">
            <span class="part-number">第二部分</span>
            <span class="part-name">拉萨</span>
            <span class="chapter-range">第 5 — 11 章</span>
            <p class="part-desc">在圣城停留一个月，转经、辩经、甜茶馆。哲蚌寺里的辩经告诉我：知识不是积累，而是减法。</p>
          </a>
          <a href="/chapters/12-fire" class="structure-card">
            <span class="part-number">第三部分</span>
            <span class="part-name">减法</span>
            <span class="chapter-range">第 12 — 13 章 + 尾声</span>
            <p class="part-desc">离开前的沉思，高原的馈赠。减去了一些东西，但也挺好的。</p>
          </a>
        </div>
      </div>

      <!-- 开始阅读 CTA -->
      <div class="final-cta">
        <a href="/chapters/preface" class="read-button">
          <span class="button-text">开始阅读</span>
          <span class="button-arrow">→</span>
        </a>
      </div>

      <div style="height: 4em;"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, shallowRef, markRaw } from 'vue'
import * as THREE from 'three'
import gsap from 'gsap'

const container = ref(null)
const canvas = ref(null)
const contentSection = ref(null)

// 平滑滚动变量
let targetScrollProgress = 0
let currentScrollProgress = 0

// 平滑插值函数
const lerp = (start, end, factor) => {
  return start + (end - start) * factor
}

// 标题文字
const title = '减法之地'

// 碎片名词
const fragmentWords = ref([
  '318', '川西', '西藏', '拉萨', '海拔', '雪山', '冰川', '经幡',
  '折多山', '理塘', '林芝', '羊湖', '纳木错', '来古', '然乌',
  '布达拉宫', '大昭寺', '哲蚌寺', '仓央嘉措', '甜茶馆',
  'G318', '4718m', '3650m', '理塘', '巴塘', '芒康', '邦达',
  '八宿', '波密', '鲁朗', '色季拉山', '南迦巴瓦',
  '转山', '朝圣', '修行', '空性', '无常', '放下',
  '日照金山', '梅里', '亚丁', '稻城', '雅江', '新都桥',
  '塔公', '墨石', '四姑娘山', '九寨沟', '黄龙'
])

const fragments = ref([])

// 动画状态
const scrollProgress = ref(0)
const isAnimating = ref(false)
const scene = shallowRef(null)
const camera = shallowRef(null)
const renderer = shallowRef(null)
const particles = shallowRef(null)
const snowflakes = shallowRef(null)
const mountainGroup = shallowRef(null)
const car = shallowRef(null)
const crackLine = shallowRef(null)

// 开场文字样式
const openingStyle = computed(() => ({
  opacity: 1 - scrollProgress.value * 1.5,
  transform: `translateY(${scrollProgress.value * 200}px) scale(${1 + scrollProgress.value * 0.2})`,
}))

const getCharStyle = (i) => {
  const progress = scrollProgress.value
  const charProgress = progress + i * 0.12

  // 计算裂纹偏移 - 每个字符不同方向的随机偏移
  const crackOffsetX = Math.sin(progress * 15 + i * 0.7) * 80 * progress
  const crackOffsetY = Math.cos(progress * 12 + i * 0.5) * 50 * progress
  const rotation = (i - 1.5) * progress * 20 + Math.sin(progress * Math.PI) * 10 * progress

  return {
    transform: `
      translateX(${crackOffsetX}px)
      translateY(${crackOffsetY}px)
      rotate(${rotation}deg)
      scale(${1 + progress * 0.4})
    `,
    opacity: Math.max(0, 1 - progress * 2.5),
    letterSpacing: `${i * 0.2 + progress * 30}px`,
    filter: `blur(${progress * 4}px) brightness(${1 + progress * 0.3})`,
    textShadow: `
      0 0 ${20 + progress * 50}px rgba(196, 147, 63, ${0.3 + progress * 0.4}),
      0 ${progress * 10}px ${30 + progress * 40}px rgba(0, 0, 0, 0.8)
    `,
  }
}

const scrollHintStyle = computed(() => ({
  opacity: Math.max(0, 1 - scrollProgress.value * 3),
  transform: `translateY(${scrollProgress.value * 50}px)`,
}))

const crackStyle = computed(() => ({
  opacity: scrollProgress.value > 0.5 ? (scrollProgress.value - 0.5) * 2 : 0,
  transform: `scale(${0.8 + scrollProgress.value * 0.4})`,
}))

const carStyle = computed(() => ({
  opacity: scrollProgress.value > 0.3 ? (1 - scrollProgress.value) * 0.8 : 0,
  transform: `translateX(${(scrollProgress.value - 0.3) * 200}px) translateY(${scrollProgress.value * 50}px)`,
}))

// 初始化 Three.js 场景
const initScene = () => {
  console.log('[CinematicHome] initScene called, canvas:', canvas.value)

  if (!canvas.value) {
    console.error('[CinematicHome] Canvas element not found')
    return
  }

  const width = window.innerWidth
  const height = window.innerHeight

  // 场景
  const newScene = markRaw(new THREE.Scene())
  newScene.background = markRaw(new THREE.Color('#030610'))
  newScene.fog = markRaw(new THREE.FogExp2('#030610', 0.015))
  scene.value = newScene

  // 相机
  camera.value = markRaw(new THREE.PerspectiveCamera(75, width / height, 0.1, 1000))
  camera.value.position.z = 5

  // 渲染器
  renderer.value = markRaw(new THREE.WebGLRenderer({
    canvas: canvas.value,
    antialias: true,
    alpha: true
  }))
  renderer.value.setSize(width, height)
  renderer.value.setPixelRatio(Math.min(window.devicePixelRatio, 2))

  // 创建粒子系统 - 雪花
  const snowGeometry = markRaw(new THREE.BufferGeometry())
  const snowCount = 2000
  const snowPositions = new Float32Array(snowCount * 3)

  for (let i = 0; i < snowCount * 3; i += 3) {
    snowPositions[i] = (Math.random() - 0.5) * 20
    snowPositions[i + 1] = (Math.random() - 0.5) * 20 + 5
    snowPositions[i + 2] = (Math.random() - 0.5) * 10 - 5
  }

  snowGeometry.setAttribute('position', new THREE.BufferAttribute(snowPositions, 3))

  const snowMaterial = markRaw(new THREE.PointsMaterial({
    color: 0xffffff,
    size: 0.06,
    transparent: true,
    opacity: 0.7,
    sizeAttenuation: true,
    blending: THREE.AdditiveBlending
  }))

  snowflakes.value = markRaw(new THREE.Points(snowGeometry, snowMaterial))
  scene.value.add(snowflakes.value)

  // 创建氛围粒子 - 模拟经幡碎片和尘埃
  const particlesGeometry = markRaw(new THREE.BufferGeometry())
  const particlesCount = 500
  const positions = new Float32Array(particlesCount * 3)

  for (let i = 0; i < particlesCount * 3; i += 3) {
    positions[i] = (Math.random() - 0.5) * 15
    positions[i + 1] = (Math.random() - 0.5) * 10
    positions[i + 2] = (Math.random() - 0.5) * 8
  }

  particlesGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3))

  const particlesMaterial = markRaw(new THREE.PointsMaterial({
    color: 0xD4A34F,  // 藏式金色
    size: 0.08,
    transparent: true,
    opacity: 0.5,
    sizeAttenuation: true,
    blending: THREE.AdditiveBlending
  }))

  particles.value = markRaw(new THREE.Points(particlesGeometry, particlesMaterial))
  scene.value.add(particles.value)

  // 创建雪山剪影 - 多层山脉，增强层次感
  mountainGroup.value = markRaw(new THREE.Group())

  // 前层山脉 - 较暗，细节更少
  const frontMountainShape = markRaw(new THREE.Shape())
  frontMountainShape.moveTo(-10, -3)
  frontMountainShape.lineTo(-8, -1.5)
  frontMountainShape.lineTo(-6, -3)
  frontMountainShape.lineTo(-4, -1)
  frontMountainShape.lineTo(-2, -2.5)
  frontMountainShape.lineTo(0, -0.5)
  frontMountainShape.lineTo(2, -2)
  frontMountainShape.lineTo(4, -0.8)
  frontMountainShape.lineTo(6, -2.5)
  frontMountainShape.lineTo(8, -1)
  frontMountainShape.lineTo(10, -2)
  frontMountainShape.lineTo(10, -3)
  frontMountainShape.closePath()

  const frontMountainGeometry = markRaw(new THREE.ShapeGeometry(frontMountainShape))
  const frontMountainMaterial = markRaw(new THREE.MeshBasicMaterial({
    color: 0x0a0f1a,
    transparent: true,
    opacity: 0.9
  }))

  const frontMountain = markRaw(new THREE.Mesh(frontMountainGeometry, frontMountainMaterial))
  frontMountain.rotation.x = Math.PI
  frontMountain.position.y = -2.5
  mountainGroup.value.add(frontMountain)

  // 中层山脉 - 中等亮度
  const midMountainShape = markRaw(new THREE.Shape())
  midMountainShape.moveTo(-10, -2)
  midMountainShape.lineTo(-7, 0)
  midMountainShape.lineTo(-5, -1.5)
  midMountainShape.lineTo(-3, 0.5)
  midMountainShape.lineTo(0, -1)
  midMountainShape.lineTo(3, 0)
  midMountainShape.lineTo(5, -1.5)
  midMountainShape.lineTo(7, 0.5)
  midMountainShape.lineTo(10, -1)
  midMountainShape.lineTo(10, -2)
  midMountainShape.closePath()

  const midMountainGeometry = markRaw(new THREE.ShapeGeometry(midMountainShape))
  const midMountainMaterial = markRaw(new THREE.MeshBasicMaterial({
    color: 0x1a2338,
    transparent: true,
    opacity: 0.7
  }))

  const midMountain = markRaw(new THREE.Mesh(midMountainGeometry, midMountainMaterial))
  midMountain.rotation.x = Math.PI
  midMountain.position.y = -1.8
  midMountain.position.z = -2
  mountainGroup.value.add(midMountain)

  // 远景雪山 - 最亮，带金光效果
  const backMountainShape = markRaw(new THREE.Shape())
  backMountainShape.moveTo(-10, -1)
  backMountainShape.lineTo(-6, 1.5)
  backMountainShape.lineTo(-3, 0)
  backMountainShape.lineTo(0, 2)
  backMountainShape.lineTo(3, 0.5)
  backMountainShape.lineTo(6, 1.8)
  backMountainShape.lineTo(10, 0)
  backMountainShape.lineTo(10, -1)
  backMountainShape.closePath()

  const backMountainGeometry = markRaw(new THREE.ShapeGeometry(backMountainShape))
  const backMountainMaterial = markRaw(new THREE.MeshBasicMaterial({
    color: 0x2d4055,
    transparent: true,
    opacity: 0.5
  }))

  const backMountain = markRaw(new THREE.Mesh(backMountainGeometry, backMountainMaterial))
  backMountain.rotation.x = Math.PI
  backMountain.position.y = -1.2
  backMountain.position.z = -4
  mountainGroup.value.add(backMountain)

  scene.value.add(mountainGroup.value)

  // 添加环境光
  const ambientLight = markRaw(new THREE.AmbientLight(0x404040, 0.5))
  scene.value.add(ambientLight)

  // 添加点光源 - 模拟月光
  const moonLight = markRaw(new THREE.PointLight(0x6688aa, 0.3))
  moonLight.position.set(5, 5, 5)
  scene.value.add(moonLight)

  // 添加暖色点光源 - 模拟日照金山效果
  const sunLight = markRaw(new THREE.PointLight(0xffaa66, 0.15))
  sunLight.position.set(-5, 3, 2)
  scene.value.add(sunLight)
}

// 动画循环
const animate = () => {
  if (!renderer.value || !scene.value || !camera.value) return

  const time = Date.now() * 0.001

  // 更新雪花 - 更自然的飘落效果
  if (snowflakes.value) {
    const positions = snowflakes.value.geometry.attributes.position.array
    for (let i = 0; i < positions.length; i += 3) {
      // Y 轴下落
      positions[i + 1] -= 0.015 + Math.random() * 0.01
      // X 轴轻微飘动
      positions[i] += Math.sin(time * 2 + positions[i + 1]) * 0.01
      // Z 轴轻微飘动
      positions[i + 2] += Math.cos(time * 1.5 + positions[i + 1]) * 0.005

      if (positions[i + 1] < -5) {
        positions[i + 1] = 10 // 重置到顶部
        positions[i] = (Math.random() - 0.5) * 20
        positions[i + 2] = (Math.random() - 0.5) * 10 - 5
      }
    }
    snowflakes.value.geometry.attributes.position.needsUpdate = true
    snowflakes.value.rotation.y = time * 0.02
  }

  // 更新氛围粒子 - 模拟经幡碎片缓缓飘动
  if (particles.value) {
    particles.value.rotation.y = time * 0.03
    particles.value.rotation.x = Math.sin(time * 0.1) * 0.05
    particles.value.rotation.z = Math.cos(time * 0.08) * 0.03
  }

  // 更新雪山 - 多层视差效果
  if (mountainGroup.value) {
    const time = Date.now() * 0.001
    mountainGroup.value.position.y = -2 + Math.sin(time * 0.2) * 0.05

    // 多层山脉的视差滚动
    mountainGroup.value.children.forEach((mountain, index) => {
      mountain.position.x = Math.sin(time * 0.1 + index) * 0.2
    })
  }

  // 相机轻微移动
  if (camera.value) {
    camera.value.position.x += Math.sin(time * 0.3) * 0.002
    camera.value.position.y += Math.cos(time * 0.2) * 0.002
  }

  // 更新平滑滚动
  updateScrollProgress()

  renderer.value.render(scene.value, camera.value)
  requestAnimationFrame(animate)
}

// 处理滚动 - 使用平滑插值
const handleScroll = () => {
  if (!container.value) return

  const scrollTop = window.scrollY
  const windowHeight = window.innerHeight
  const maxScroll = windowHeight * 0.8

  targetScrollProgress = Math.min(scrollTop / maxScroll, 1)
}

// 平滑滚动更新函数
const updateScrollProgress = () => {
  currentScrollProgress = lerp(currentScrollProgress, targetScrollProgress, 0.08)
  scrollProgress.value = currentScrollProgress

  // 根据平滑滚动更新相机
  if (camera.value) {
    camera.value.position.z = 5 - currentScrollProgress * 2
    camera.value.rotation.x = currentScrollProgress * 0.08
  }
}

// 创建碎片效果
const createFragments = () => {
  const newFragments = []
  const containerWidth = window.innerWidth

  fragmentWords.value.forEach((word, index) => {
    const angle = (index / fragmentWords.value.length) * Math.PI * 2
    const radius = Math.min(containerWidth, 600) * (0.5 + Math.random() * 0.5)
    const x = Math.cos(angle) * radius
    const y = Math.sin(angle) * radius

    // 为藏式关键词添加金色高亮
    const tibetanWords = ['西藏', '拉萨', '布达拉宫', '大昭寺', '哲蚌寺', '仓央嘉措', '经幡', '转山', '朝圣', '修行', '空性', '无常', '放下']
    const isTibetanWord = tibetanWords.includes(word)

    newFragments.push({
      text: word,
      style: {
        left: `calc(50% + ${x}px)`,
        top: `calc(50% + ${y}px)`,
        opacity: 0.1 + Math.random() * 0.25,
        fontSize: `${0.7 + Math.random() * 0.5}rem`,
        transform: `rotate(${Math.random() * 60 - 30}deg)`,
        color: isTibetanWord ? 'rgba(212, 163, 79, 0.4)' : 'rgba(255, 255, 255, 0.15)',
        textShadow: isTibetanWord ? '0 0 10px rgba(196, 147, 63, 0.5)' : '0 0 10px rgba(255, 255, 255, 0.1)',
      }
    })
  })

  fragments.value = newFragments
}

onMounted(async () => {
  console.log('[CinematicHome] Component mounted')
  console.log('[CinematicHome] Canvas element:', canvas.value)

  // 等待 DOM 更新
  await new Promise(resolve => setTimeout(resolve, 100))

  initScene()
  animate()
  createFragments()

  window.addEventListener('scroll', handleScroll)
  window.addEventListener('resize', () => {
    if (camera.value && renderer.value) {
      camera.value.aspect = window.innerWidth / window.innerHeight
      camera.value.updateProjectionMatrix()
      renderer.value.setSize(window.innerWidth, window.innerHeight)
    }
  })

  // 入场动画 - 确保元素已渲染
  if (document.querySelector('.main-title')) {
    gsap.from('.main-title', {
      duration: 2.5,
      opacity: 0,
      scale: 0.85,
      y: 30,
      ease: 'power3.out',
      delay: 0.3
    })
  }

  // 标题金光效果动画
  if (document.querySelector('.title-glow')) {
    gsap.from('.title-glow', {
      duration: 3,
      opacity: 0,
      scale: 0.8,
      ease: 'power2.out',
      delay: 0.5
    })
  }

  // 等待碎片元素渲染后再执行动画
  await new Promise(resolve => setTimeout(resolve, 50))
  if (document.querySelector('.fragment')) {
    gsap.from('.fragment', {
      duration: 4,
      opacity: 0,
      stagger: {
        amount: 2.5,
        from: 'random'
      },
      ease: 'power1.out'
    })
  }

  // 滚动提示动画
  if (document.querySelector('.scroll-hint')) {
    gsap.from('.scroll-hint', {
      duration: 2,
      opacity: 0,
      y: 20,
      ease: 'power2.out',
      delay: 1
    })
  }

  // 裂缝效果初始隐藏
  if (document.querySelector('.crack-overlay')) {
    gsap.set('.crack-overlay', { opacity: 0 })
  }

  console.log('[CinematicHome] Initialization complete')
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  if (renderer.value) {
    renderer.value.dispose()
  }
  if (scene.value) {
    scene.value.clear()
  }
})
</script>

<style scoped>
.cinematic-home {
  position: relative;
  width: 100%;
  height: 200vh;
  overflow: visible;
  background: #030610;
}

.hero-viewport {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  pointer-events: none;
  z-index: 50;
  background: #030610;
}

.webgl-canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
}

/* ═══════════════════════════════════════════════
   开场文字
   ═══════════════════════════════════════════════ */
.opening-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 100;
  pointer-events: none;
  transition: all 0.1s ease-out;
  will-change: opacity, transform;
}

/* 标题金光效果 */
.title-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 400px;
  height: 400px;
  background: radial-gradient(ellipse,
    rgba(196, 147, 63, 0.15) 0%,
    rgba(196, 147, 63, 0.05) 30%,
    transparent 70%);
  filter: blur(20px);
  animation: glowPulse 4s ease-in-out infinite;
  pointer-events: none;
}

@keyframes glowPulse {
  0%, 100% { opacity: 0.6; transform: translate(-50%, -50%) scale(1); }
  50% { opacity: 1; transform: translate(-50%, -50%) scale(1.1); }
}

.main-title {
  position: relative;
  z-index: 2;
  display: flex;
  justify-content: center;
  gap: 0;
  margin: 0;
  font-family: 'Noto Serif SC', 'Source Han Serif SC', serif;
  font-size: clamp(3rem, 15vw, 12rem);
  font-weight: 700;
  color: rgba(255, 255, 255, 0.95);
  letter-spacing: 0.2em;
  text-shadow:
    0 0 60px rgba(255, 255, 255, 0.3),
    0 0 120px rgba(255, 255, 255, 0.1),
    0 4px 30px rgba(0, 0, 0, 0.8),
    0 0 200px rgba(196, 147, 63, 0.15);
  background: linear-gradient(180deg,
    rgba(255, 255, 255, 0.98) 0%,
    rgba(255, 255, 255, 0.85) 50%,
    rgba(196, 147, 63, 0.8) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.title-char {
  display: inline-block;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  will-change: transform, opacity, filter;
}

/* ═══════════════════════════════════════════════
   碎片效果
   ═══════════════════════════════════════════════ */
.fragments-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 50;
  overflow: hidden;
}

.fragment {
  position: absolute;
  font-family: var(--font-heading), sans-serif;
  color: rgba(255, 255, 255, 0.15);
  white-space: nowrap;
  transition: all 0.5s ease;
  animation: fragmentFloat 10s ease-in-out infinite, fragmentGlow 5s ease-in-out infinite;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
}

@keyframes fragmentFloat {
  0%, 100% {
    opacity: 0.08;
    transform: translateY(0) rotate(var(--rotation, 0deg)) scale(1);
  }
  25% {
    opacity: 0.25;
    transform: translateY(-15px) rotate(var(--rotation, 0deg)) scale(1.02);
  }
  50% {
    opacity: 0.35;
    transform: translateY(-25px) rotate(var(--rotation, 0deg)) scale(1.05);
  }
  75% {
    opacity: 0.2;
    transform: translateY(-10px) rotate(var(--rotation, 0deg)) scale(1.02);
  }
}

@keyframes fragmentGlow {
  0%, 100% {
    filter: brightness(1);
  }
  50% {
    filter: brightness(1.3);
  }
}

/* ═══════════════════════════════════════════════
   滚动提示
   ═══════════════════════════════════════════════ */
.scroll-hint {
  position: absolute;
  bottom: 3em;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1em;
  z-index: 80;
  transition: all 0.3s ease;
}

.scroll-hint span {
  font-family: var(--font-quote), 'KaiTi', serif;
  font-size: 0.8rem;
  color: rgba(255, 255, 255, 0.3);
  letter-spacing: 0.3em;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
}

.scroll-arrow {
  width: 24px;
  height: 24px;
  border-right: 2px solid rgba(196, 147, 63, 0.5);
  border-bottom: 2px solid rgba(196, 147, 63, 0.5);
  transform: rotate(45deg);
  animation: arrowBounce 2s ease-in-out infinite;
  box-shadow: 0 0 10px rgba(196, 147, 63, 0.3);
}

@keyframes arrowBounce {
  0%, 100% { transform: rotate(45deg) translateY(0); }
  50% { transform: rotate(45deg) translateY(10px); }
}

/* ═══════════════════════════════════════════════
   裂缝效果 - 冰雪裂缝
   ═══════════════════════════════════════════════ */
.crack-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 300px;
  height: 300px;
  pointer-events: none;
  z-index: 40;
  transition: all 0.5s ease-out;
}

.crack-overlay::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg,
    transparent 0%,
    rgba(196, 147, 63, 0.4) 20%,
    rgba(255, 255, 255, 0.9) 50%,
    rgba(196, 147, 63, 0.4) 80%,
    transparent 100%);
  box-shadow:
    0 0 30px rgba(196, 147, 63, 0.5),
    0 0 60px rgba(255, 255, 255, 0.3);
  filter: blur(1px);
}

.crack-overlay::after {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  bottom: 0;
  width: 2px;
  background: linear-gradient(180deg,
    transparent 0%,
    rgba(196, 147, 63, 0.3) 30%,
    rgba(255, 255, 255, 0.7) 50%,
    rgba(196, 147, 63, 0.3) 70%,
    transparent 100%);
  box-shadow:
    0 0 20px rgba(196, 147, 63, 0.4),
    0 0 40px rgba(255, 255, 255, 0.2);
  filter: blur(1px);
}

/* ═══════════════════════════════════════════════
   小车剪影 - 驶入未知
   ═══════════════════════════════════════════════ */
.car-silhouette {
  position: absolute;
  bottom: 35%;
  left: 15%;
  pointer-events: none;
  z-index: 35;
  transition: all 0.5s ease-out;
  opacity: 0;
  filter: drop-shadow(0 0 20px rgba(255, 200, 100, 0.3));
}

.car-body {
  width: 55px;
  height: 16px;
  background: linear-gradient(90deg,
    rgba(45, 64, 85, 0.8) 0%,
    rgba(58, 80, 107, 0.6) 50%,
    rgba(45, 64, 85, 0.8) 100%);
  border-radius: 4px 10px 4px 4px;
  position: relative;
  box-shadow:
    0 0 20px rgba(255, 255, 255, 0.1),
    inset 0 1px 2px rgba(255, 255, 255, 0.1);
}

.car-body::before {
  /* 车顶 */
  content: '';
  position: absolute;
  top: -8px;
  left: 14px;
  width: 22px;
  height: 9px;
  background: linear-gradient(180deg,
    rgba(58, 80, 107, 0.5) 0%,
    rgba(45, 64, 85, 0.7) 100%);
  border-radius: 8px 8px 0 0;
}

.car-body::after {
  /* 后轮 */
  content: '';
  position: absolute;
  bottom: -5px;
  left: 10px;
  width: 9px;
  height: 9px;
  background: radial-gradient(circle,
    rgba(30, 41, 59, 0.8) 0%,
    rgba(51, 65, 85, 0.6) 70%);
  border-radius: 50%;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.car-wheel-front {
  position: absolute;
  bottom: -5px;
  right: 12px;
  width: 9px;
  height: 9px;
  background: radial-gradient(circle,
    rgba(30, 41, 59, 0.8) 0%,
    rgba(51, 65, 85, 0.6) 70%);
  border-radius: 50%;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.car-light {
  position: absolute;
  top: 50%;
  right: -35px;
  width: 45px;
  height: 8px;
  background: linear-gradient(90deg,
    rgba(255, 200, 100, 0.8) 0%,
    rgba(255, 180, 80, 0.4) 50%,
    transparent 100%);
  transform: translateY(-50%);
  filter: blur(4px);
  animation: lightPulse 2.5s ease-in-out infinite;
}

/* 车灯光束 */
.car-light::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  width: 80px;
  height: 40px;
  background: linear-gradient(90deg,
    rgba(255, 200, 100, 0.15) 0%,
    transparent 100%);
  transform: translateY(-50%) rotate(-10deg);
  filter: blur(8px);
}

@keyframes lightPulse {
  0%, 100% { opacity: 0.6; }
  50% { opacity: 1; }
}

/* ═══════════════════════════════════════════════
   内容区域
   ═══════════════════════════════════════════════ */
.content-section {
  position: relative;
  z-index: 100;
  background: linear-gradient(180deg,
    transparent 0%,
    #050810 5%,
    #0a0e1a 15%,
    #0f141f 35%,
    #1a1f2e 60%,
    #232838 100%);
  padding: 0;
  min-height: 100vh;
  margin-top: 100vh;
  padding-top: 4em;
}

/* ═══════════════════════════════════════════════
   题记区域
   ═══════════════════════════════════════════════ */
.epigraph-section {
  max-width: 680px;
  margin: 8em auto 4em;
  padding: 0 2em;
}

.epigraph-quote {
  border-left: 2px solid rgba(196, 147, 63, 0.4);
  margin: 0 0 2.5em 0;
  padding: 0 0 0 1.5em;
  background: transparent;
}

.epigraph-quote p {
  font-family: var(--font-quote);
  font-size: 1.05rem;
  color: rgba(200, 196, 188, 0.9);
  margin: 0 0 0.6em 0;
  line-height: 1.9;
}

.epigraph-quote cite {
  font-family: var(--font-quote);
  font-size: 0.8rem;
  color: rgba(120, 116, 108, 0.8);
  font-style: normal;
}

/* ═══════════════════════════════════════════════
   分割线
   ═══════════════════════════════════════════════ */
.divider-line {
  max-width: 680px;
  margin: 3em auto;
  height: 1px;
  background: linear-gradient(90deg,
    transparent 0%,
    rgba(192, 184, 168, 0.2) 20%,
    rgba(192, 184, 168, 0.2) 80%,
    transparent 100%);
}

/* ═══════════════════════════════════════════════
   Polarsteps 嵌入区域
   ═══════════════════════════════════════════════ */
.polarsteps-section {
  max-width: 1100px;
  margin: 4em auto;
  padding: 0 2em;
}

.section-title {
  font-family: var(--font-heading);
  font-size: 1.5rem;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.9);
  text-align: center;
  letter-spacing: 0.15em;
  margin-bottom: 0.5em;
  text-shadow: 0 0 20px rgba(196, 147, 63, 0.3);
}

.section-desc {
  font-family: var(--font-quote);
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.5);
  text-align: center;
  margin-bottom: 2em;
  letter-spacing: 0.05em;
}

.polarsteps-embed {
  margin-top: 2em;
}

.embed-container {
  position: relative;
  width: 100%;
  height: 550px;
  border-radius: 4px;
  overflow: hidden;
  box-shadow: 0 4px 40px rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.embed-container iframe {
  width: 100%;
  height: 100%;
  border: none;
}

.polarsteps-attribution {
  text-align: center;
  margin-top: 1.2em;
  font-family: var(--font-quote);
  font-size: 0.8rem;
  color: rgba(255, 255, 255, 0.4);
}

/* ═══════════════════════════════════════════════
   海拔剖面图
   ═══════════════════════════════════════════════ */
.elevation-profile-section {
  max-width: 1000px;
  margin: 4em auto;
  padding: 0 2em;
}

.elevation-chart {
  margin-top: 2em;
}

.chart-wrapper {
  position: relative;
  height: 300px;
  background: linear-gradient(180deg,
    rgba(44, 95, 124, 0.08) 0%,
    rgba(44, 95, 124, 0.03) 100%);
  border-radius: 4px 4px 0 0;
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-bottom: none;
  padding: 2em 2em 0;
  overflow: hidden;
}

.elevation-line {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  height: 100%;
  gap: 0.4em;
}

.elevation-point {
  flex: 1;
  max-width: 70px;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
}

.elevation-point::before {
  content: '';
  width: 100%;
  height: calc(var(--height) * 2.5);
  min-height: 10px;
  background: linear-gradient(to top,
    rgba(44, 95, 124, 0.6) 0%,
    rgba(58, 124, 165, 0.7) 70%,
    rgba(196, 147, 63, 0.6) 100%);
  border-radius: 2px 2px 0 0;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  opacity: 0.6;
}

.elevation-point.highlight::before {
  background: linear-gradient(to top,
    rgba(196, 147, 63, 0.6) 0%,
    rgba(232, 184, 109, 0.8) 70%,
    rgba(245, 216, 144, 0.9) 100%);
  opacity: 1;
  box-shadow: 0 0 30px rgba(196, 147, 63, 0.4);
}

.elevation-point::after {
  content: attr(--label);
  position: absolute;
  bottom: -2.5em;
  font-family: var(--font-heading);
  font-size: 0.65rem;
  color: rgba(255, 255, 255, 0.6);
  white-space: nowrap;
  text-align: center;
}

.elevation-point:hover::before {
  opacity: 1;
  transform: scaleY(1.08);
}

.elevation-labels {
  position: absolute;
  top: 1em;
  right: 1.5em;
  display: flex;
  flex-direction: column;
  gap: 0.4em;
  font-family: var(--font-quote);
  font-size: 0.7rem;
  color: rgba(255, 255, 255, 0.4);
}

.stops-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.3em;
  padding: 1.2em 1.5em;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 0 0 4px 4px;
  border-top: none;
}

.stop-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0.5em 0.9em;
  min-width: 75px;
  border-radius: 4px;
  transition: all 0.3s ease;
}

.stop-item:hover {
  background: rgba(196, 147, 63, 0.08);
}

.stop-item.highlight {
  background: rgba(196, 147, 63, 0.12);
}

.stop-name {
  font-family: var(--font-heading);
  font-size: 0.7rem;
  color: rgba(255, 255, 255, 0.7);
}

.stop-elevation {
  font-family: var(--font-quote);
  font-size: 0.6rem;
  color: rgba(255, 255, 255, 0.4);
  margin-top: 0.2em;
}

.stop-item.highlight .stop-name {
  color: rgba(212, 163, 79, 0.9);
  font-weight: 600;
}

/* ═══════════════════════════════════════════════
   书籍结构
   ═══════════════════════════════════════════════ */
.book-structure {
  max-width: 960px;
  margin: 5em auto;
  padding: 0 2em;
}

.structure-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.8em;
  margin-top: 2em;
}

.structure-card {
  display: block;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 6px;
  padding: 2.2em 1.8em;
  text-decoration: none;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

.structure-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.3);
  border-color: rgba(196, 147, 63, 0.3);
  background: rgba(255, 255, 255, 0.03);
}

.structure-card .part-number {
  display: block;
  font-family: var(--font-heading);
  font-size: 0.7rem;
  color: rgba(255, 255, 255, 0.4);
  letter-spacing: 0.15em;
  margin-bottom: 0.5em;
}

.structure-card .part-name {
  display: block;
  font-family: var(--font-heading);
  font-size: 1.8rem;
  font-weight: 700;
  background: linear-gradient(135deg, rgba(44, 95, 124, 0.9) 0%, rgba(196, 147, 63, 0.9) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 0.4em;
}

.structure-card .chapter-range {
  display: block;
  font-family: var(--font-quote);
  font-size: 0.75rem;
  color: rgba(196, 147, 63, 0.7);
  margin-bottom: 1.2em;
}

.structure-card .part-desc {
  font-family: var(--font-body);
  font-size: 0.9rem;
  line-height: 1.9;
  color: rgba(255, 255, 255, 0.6);
  margin: 0;
}

/* ═══════════════════════════════════════════════
   最终 CTA
   ═══════════════════════════════════════════════ */
.final-cta {
  text-align: center;
  margin: 5em auto 3em;
  padding: 0 2em;
}

.read-button {
  display: inline-flex;
  align-items: center;
  gap: 0.8em;
  font-family: var(--font-heading);
  font-size: 1.05rem;
  font-weight: 500;
  padding: 1.2em 3.5em;
  background: linear-gradient(135deg, rgba(196, 147, 63, 0.9) 0%, rgba(212, 163, 79, 0.9) 100%);
  color: white;
  border-radius: 4px;
  text-decoration: none;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  letter-spacing: 0.1em;
  box-shadow: 0 10px 40px rgba(196, 147, 63, 0.3);
}

.read-button:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 60px rgba(196, 147, 63, 0.5);
}

.button-arrow {
  font-size: 1.2em;
  transition: transform 0.3s ease;
}

.read-button:hover .button-arrow {
  transform: translateX(6px);
}

/* ═══════════════════════════════════════════════
   响应式
   ═══════════════════════════════════════════════ */
@media (max-width: 768px) {
  .main-title {
    font-size: clamp(2.5rem, 18vw, 6rem);
    letter-spacing: 0.1em;
  }

  .title-glow {
    width: 280px;
    height: 280px;
  }

  .scroll-hint {
    display: none;
  }

  .car-silhouette {
    display: none;
  }

  .epigraph-section {
    margin: 4em auto 2em;
    padding: 0 1.5em;
  }

  .structure-grid {
    grid-template-columns: 1fr;
  }

  .embed-container {
    height: 400px;
  }

  .chart-wrapper {
    height: 220px;
    padding: 1.5em 1em 0;
  }

  .fragment {
    font-size: 0.6rem !important;
  }
}
</style>

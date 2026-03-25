<script setup>
import { useData } from 'vitepress'
import { ref } from 'vue'

const { frontmatter } = useData()

const isPortrait = ref(false)

function onHeroLoad(e) {
  const img = e.target
  isPortrait.value = img.naturalHeight > img.naturalWidth
}
</script>

<template>
  <div class="chapter-header" v-if="frontmatter.chapter || frontmatter.title">
    <div class="chapter-number" v-if="frontmatter.partName">
      {{ frontmatter.partName }}
    </div>
    <div class="chapter-number" v-if="frontmatter.chapter">
      第{{ ['一','二','三','四','五','六','七','八','九','十','十一','十二','十三'][frontmatter.chapter - 1] }}章
    </div>
    <h1 class="chapter-title">{{ frontmatter.subtitle || frontmatter.title }}</h1>
    <div class="chapter-meta" v-if="frontmatter.date || frontmatter.location">
      <span v-if="frontmatter.date">{{ frontmatter.date }}</span>
      <span v-if="frontmatter.date && frontmatter.location"> · </span>
      <span v-if="frontmatter.location">{{ frontmatter.location }}</span>
    </div>
    <div class="chapter-hero" v-if="frontmatter.heroImage">
      <img
        :src="frontmatter.heroImage"
        :alt="frontmatter.subtitle || frontmatter.title"
        :class="{ portrait: isPortrait }"
        loading="eager"
        fetchpriority="high"
        @load="onHeroLoad"
      />
    </div>
    <div class="chapter-epigraph" v-if="frontmatter.excerpt">
      <p>{{ frontmatter.excerpt }}</p>
    </div>
  </div>
</template>

<style scoped>
.chapter-header {
  text-align: center;
  padding: 3em 0 2em;
  margin-bottom: 2.5em;
  position: relative;
}

/* 装饰性细线 - 藏式金色 */
.chapter-header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 1px;
  background: linear-gradient(90deg,
    transparent 0%,
    rgba(196, 147, 63, 0.3) 20%,
    rgba(196, 147, 63, 0.5) 50%,
    rgba(196, 147, 63, 0.3) 80%,
    transparent 100%);
  border-radius: 1px;
}

.chapter-number {
  font-family: var(--font-heading);
  font-size: 0.75rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  background: linear-gradient(135deg,
    rgba(196, 147, 63, 0.7) 0%,
    rgba(212, 163, 79, 0.9) 50%,
    rgba(196, 147, 63, 0.7) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 0.5em;
  font-weight: 500;
}
.chapter-title {
  font-family: var(--font-heading) !important;
  font-size: 1.65rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.08em;
  margin: 0.6em 0 0.4em !important;
  line-height: 1.5;
  color: var(--vp-c-text-1);
  border: none !important;
  padding: 0 !important;
}
.chapter-meta {
  font-family: var(--font-quote);
  font-size: 0.8rem;
  color: var(--color-text-date);
  margin-top: 1em;
  font-style: italic;
  letter-spacing: 0.05em;
}
.chapter-hero {
  margin-top: 2.5em;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 8px 40px rgba(0, 0, 0, 0.08);
}
.chapter-hero img {
  width: 100%;
  max-height: 450px;
  object-fit: cover;
  object-position: center 30%;
  display: block;
}
/* 竖向图片：不裁切，完整展示，限制宽度居中 */
.chapter-hero img.portrait {
  width: auto;
  max-width: 100%;
  max-height: 600px;
  object-fit: contain;
  display: block;
  margin: 0 auto;
}
.chapter-epigraph {
  margin-top: 2em;
  font-family: var(--font-quote);
  font-size: 0.95rem;
  color: var(--vp-c-text-2);
  font-style: italic;
  max-width: 520px;
  margin-left: auto;
  margin-right: auto;
}
.chapter-epigraph p {
  text-indent: 0 !important;
  text-align: center !important;
  line-height: 1.8;
}

/* 暗色模式优化 */
.dark .chapter-header::before {
  background: linear-gradient(90deg,
    transparent 0%,
    rgba(212, 163, 79, 0.5) 20%,
    rgba(212, 163, 79, 0.7) 50%,
    rgba(212, 163, 79, 0.5) 80%,
    transparent 100%);
}

/* 移动端适配 */
@media (max-width: 768px) {
  .chapter-header {
    padding: 2em 0 1.5em;
  }
  .chapter-header::before {
    width: 40px;
  }
  .chapter-title {
    font-size: 1.35rem !important;
  }
  .chapter-hero {
    margin-top: 1.8em;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
  }
  .chapter-hero img {
    max-height: 320px;
  }
  .chapter-hero img.portrait {
    max-height: 420px;
  }
}
</style>

<script setup>
import { useData } from 'vitepress'

const { frontmatter } = useData()

const props = defineProps({
  prev: { type: Object, default: null }, // { link, text }
  next: { type: Object, default: null },
})

// 支持两种使用方式：直接传 props，或从 frontmatter 读
const prevLink = props.prev?.link || frontmatter.value.prev || null
const prevText = props.prev?.text || frontmatter.value.prevTitle || null
const nextLink = props.next?.link || frontmatter.value.next || null
const nextText = props.next?.text || frontmatter.value.nextTitle || null
</script>

<template>
  <nav class="chapter-nav" aria-label="章节导航">
    <a v-if="prevLink" :href="prevLink" class="nav-card nav-prev">
      <span class="nav-direction">← 上一章</span>
      <span class="nav-title" v-if="prevText">{{ prevText }}</span>
    </a>
    <div v-else class="nav-card nav-empty" aria-hidden="true"></div>

    <a v-if="nextLink" :href="nextLink" class="nav-card nav-next">
      <span class="nav-direction">下一章 →</span>
      <span class="nav-title" v-if="nextText">{{ nextText }}</span>
    </a>
    <div v-else class="nav-card nav-empty" aria-hidden="true"></div>
  </nav>
</template>

<style scoped>
.chapter-nav {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1em;
  margin: 3.5em 0 1em;
  padding-top: 2em;
  border-top: 1px solid var(--vp-c-divider);
}

.nav-card {
  display: flex;
  flex-direction: column;
  gap: 0.35em;
  padding: 1.2em 1.4em;
  background: var(--color-bg-quote);
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  text-decoration: none;
  transition: border-color 0.2s ease, background 0.2s ease;
  min-height: 64px;
}

.nav-card:not(.nav-empty):hover {
  border-color: var(--color-accent);
  background: var(--color-accent-soft);
}

.nav-next {
  text-align: right;
  align-items: flex-end;
}

.nav-empty {
  background: transparent;
  border-color: transparent;
}

.nav-direction {
  font-family: var(--font-heading);
  font-size: 0.72rem;
  letter-spacing: 0.1em;
  color: var(--color-accent);
  text-transform: uppercase;
}

.nav-title {
  font-family: var(--font-body);
  font-size: 0.9rem;
  color: var(--vp-c-text-1);
  line-height: 1.5;
}

@media (max-width: 600px) {
  .chapter-nav {
    grid-template-columns: 1fr;
  }
  .nav-next {
    text-align: left;
    align-items: flex-start;
  }
}
</style>

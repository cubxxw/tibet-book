<script setup>
import { useData } from 'vitepress'

const { frontmatter } = useData()
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
        loading="eager"
        fetchpriority="high"
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
  padding: 2em 0 1.5em;
  margin-bottom: 2em;
  border-bottom: 1px solid var(--vp-c-divider);
}
.chapter-number {
  font-family: var(--font-heading);
  font-size: 0.85rem;
  letter-spacing: 0.15em;
  color: var(--color-accent);
  margin-bottom: 0.3em;
}
.chapter-title {
  font-family: var(--font-heading) !important;
  font-size: 1.8rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.06em;
  margin: 0.3em 0 !important;
  line-height: 1.4;
  border: none !important;
  padding: 0 !important;
}
.chapter-meta {
  font-family: var(--font-quote);
  font-size: 0.85rem;
  color: var(--color-text-date);
  margin-top: 0.8em;
  text-align: right;
  font-style: italic;
}
.chapter-hero {
  margin-top: 2em;
  border-radius: 6px;
  overflow: hidden;
}
.chapter-hero img {
  width: 100%;
  max-height: 400px;
  object-fit: cover;
}
.chapter-epigraph {
  margin-top: 1.5em;
  font-family: var(--font-quote);
  font-size: 0.9rem;
  color: var(--vp-c-text-2);
  font-style: italic;
}
.chapter-epigraph p {
  text-indent: 0 !important;
  text-align: center !important;
}
</style>

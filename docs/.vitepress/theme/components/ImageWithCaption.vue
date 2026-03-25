<script setup lang="ts">
import { ref } from 'vue'

defineProps<{
  src: string
  alt?: string
  caption?: string
}>()

const isPortrait = ref(false)

function onLoad(e: Event) {
  const img = e.target as HTMLImageElement
  isPortrait.value = img.naturalHeight > img.naturalWidth * 1.1
}
</script>

<template>
  <figure class="image-with-caption" :class="{ portrait: isPortrait }">
    <img
      :src="src"
      :alt="alt || caption || ''"
      loading="lazy"
      @load="onLoad"
    />
    <figcaption class="caption" v-if="caption">{{ caption }}</figcaption>
  </figure>
</template>

<style scoped>
.image-with-caption {
  margin: 2.8em auto;
  text-align: center;
  max-width: 720px;
}
.image-with-caption img {
  max-width: 100%;
  border-radius: 3px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.10), 0 1px 4px rgba(0,0,0,0.06);
  transition: box-shadow 0.3s ease, transform 0.3s ease;
  display: block;
  margin: 0 auto;
}
.image-with-caption img:hover {
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15), 0 2px 8px rgba(0,0,0,0.08);
  transform: translateY(-1px);
}
/* 竖向图片：限宽居中，不强制撑满 */
.image-with-caption.portrait img {
  max-width: min(420px, 100%);
  max-height: 72vh;
  object-fit: contain;
}
.caption {
  font-family: var(--font-quote);
  font-size: 0.78rem;
  color: var(--color-text-date, #999);
  margin-top: 0.75em;
  text-indent: 0 !important;
  line-height: 1.6;
  letter-spacing: 0.02em;
  display: block;
}
</style>

<script setup lang="ts">
defineProps<{
  src: string
  alt?: string
  caption?: string
  eager?: boolean
}>()
</script>

<template>
  <figure class="full-width-image">
    <div class="image-wrap">
      <img :src="src" :alt="alt || caption || ''" :loading="eager ? 'eager' : 'lazy'" />
      <figcaption class="caption-overlay" v-if="caption">{{ caption }}</figcaption>
    </div>
  </figure>
</template>

<style scoped>
.full-width-image {
  margin: 3em 0;
  width: 100%;
  position: relative;
}

.image-wrap {
  position: relative;
  overflow: hidden;
  border-radius: 4px;
  line-height: 0;
}

img {
  width: 100%;
  display: block;
  object-fit: cover;
  object-position: center 50%;
  max-height: 65vh;
}

.caption-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 3em 1.5em 1em;
  background: linear-gradient(to top, rgba(0,0,0,0.5) 0%, transparent 100%);
  font-family: var(--font-quote, 'STKaiti', serif);
  font-size: 0.82rem;
  color: rgba(255, 255, 255, 0.9);
  text-align: center;
  text-indent: 0 !important;
  line-height: 1.6;
  letter-spacing: 0.04em;
}
</style>

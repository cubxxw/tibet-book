<script setup>
defineProps<{
  src: string
  alt?: string
  caption?: string
}>()
</script>

<template>
  <figure class="image-with-caption">
    <img :src="src" :alt="alt || caption || ''" loading="lazy" />
    <figcaption class="caption" v-if="caption">{{ caption }}</figcaption>
  </figure>
</template>

<style scoped>
.image-with-caption {
  margin: 2.5em 0;
  text-align: center;
}
.image-with-caption img {
  max-width: 100%;
  border-radius: 4px;
  box-shadow: 0 2px 16px rgba(0, 0, 0, 0.08);
  transition: box-shadow 0.3s ease;
}
.image-with-caption img:hover {
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.12);
}
.caption {
  font-family: var(--font-quote);
  font-size: 9px;
  color: var(--color-text-date, #999);
  margin-top: 0.8em;
  text-indent: 0 !important;
}
</style>

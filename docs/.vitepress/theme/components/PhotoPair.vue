<script setup lang="ts">
defineProps<{
  left: { src: string; caption?: string; alt?: string }
  right: { src: string; caption?: string; alt?: string }
}>()
</script>

<template>
  <div class="photo-pair">
    <figure class="pair-item">
      <img :src="left.src" :alt="left.alt || left.caption || ''" loading="lazy" />
      <figcaption v-if="left.caption">{{ left.caption }}</figcaption>
    </figure>
    <figure class="pair-item">
      <img :src="right.src" :alt="right.alt || right.caption || ''" loading="lazy" />
      <figcaption v-if="right.caption">{{ right.caption }}</figcaption>
    </figure>
  </div>
</template>

<style scoped>
.photo-pair {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1em;
  margin: 2.8em 0;
  align-items: start;
}
.pair-item {
  margin: 0;
  text-align: center;
}
.pair-item img {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 4px;
  box-shadow: 0 3px 16px rgba(0,0,0,0.10);
  transition: box-shadow 0.3s ease, transform 0.3s ease;
}
.pair-item img:hover {
  box-shadow: 0 6px 24px rgba(0,0,0,0.15);
  transform: translateY(-1px);
}
.pair-item figcaption {
  font-family: var(--font-quote);
  font-size: 0.76rem;
  color: var(--color-text-date);
  margin-top: 0.65em;
  line-height: 1.5;
  text-align: center;
  letter-spacing: 0.01em;
}
@media (max-width: 600px) {
  .photo-pair {
    grid-template-columns: 1fr;
    gap: 1.5em;
  }
}
</style>

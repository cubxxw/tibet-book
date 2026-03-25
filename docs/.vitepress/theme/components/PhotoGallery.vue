<script setup lang="ts">
interface Image {
  src: string
  alt?: string
  caption?: string
}

defineProps<{
  images: Image[]
}>()
</script>

<template>
  <div class="photo-gallery">
    <figure v-for="(image, index) in images" :key="index" class="gallery-item">
      <img :src="image.src" :alt="image.alt || image.caption" loading="lazy" />
      <figcaption v-if="image.caption" class="caption">{{ image.caption }}</figcaption>
    </figure>
  </div>
</template>

<style scoped>
.photo-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5em;
  margin: 2.5em 0;
}

.gallery-item {
  margin: 0;
}

.gallery-item img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 4px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  transition: box-shadow 0.3s ease;
}

.gallery-item img:hover {
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.12);
}

.gallery-item .caption {
  font-family: var(--font-quote);
  font-size: 9px;
  color: var(--color-text-date, #999);
  margin-top: 0.6em;
  text-indent: 0 !important;
  text-align: center;
}

@media (min-width: 768px) {
  .photo-gallery {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .photo-gallery {
    grid-template-columns: repeat(3, 1fr);
  }
}
</style>

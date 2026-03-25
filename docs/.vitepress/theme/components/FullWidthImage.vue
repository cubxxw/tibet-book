<script setup>
defineProps<{
  src: string
  alt?: string
  caption?: string
  eager?: boolean
}>()
</script>

<template>
  <figure class="full-width-image">
    <img :src="src" :alt="alt || caption || ''" :loading="eager ? 'eager' : 'lazy'" />
    <figcaption class="caption" v-if="caption">{{ caption }}</figcaption>
  </figure>
</template>

<style scoped>
.full-width-image {
  margin: 3em 0;
  margin-left: calc(-50vw + 50%);
  margin-right: calc(-50vw + 50%);
  width: 100vw;
  max-width: 100vw;
  text-align: center;
  position: relative;
}
.full-width-image img {
  width: 100%;
  max-height: 55vh;
  object-fit: cover;
}
.caption {
  font-family: var(--font-quote);
  font-size: 0.8rem;
  color: var(--color-text-date, #999);
  margin-top: 0.8em;
  text-indent: 0 !important;
}

@media (max-width: 768px) {
  .full-width-image {
    margin-left: -24px;
    margin-right: -24px;
    width: calc(100% + 48px);
    max-width: none;
  }
}
</style>

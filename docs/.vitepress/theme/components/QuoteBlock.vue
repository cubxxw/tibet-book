<script setup>
defineProps<{
  content?: string
  attribution?: string
}>()
</script>

<template>
  <div class="quote-block">
    <p v-if="content">{{ content }}</p>
    <slot v-else />
    <div class="attribution" v-if="attribution">
      —— {{ attribution }}
    </div>
  </div>
</template>

<style scoped>
.quote-block {
  font-family: var(--font-quote);
  background: var(--color-bg-quote, #F8F6F2);
  border-left: 3px solid var(--color-accent, #C4933F);
  border-radius: 0 6px 6px 0;
  padding: 1.4em 2em;
  margin: 2em 0;
  font-size: 15px;
  line-height: 1.9;
  color: var(--vp-c-text-2);
}
.quote-block :deep(p) {
  text-indent: 0 !important;
  font-family: var(--font-quote) !important;
  text-align: left !important;
  margin: 0.3em 0;
  font-size: 15px;
}
.attribution {
  text-align: right;
  margin-top: 0.8em;
  font-size: 0.85em;
  color: var(--color-text-date, #999);
}
</style>

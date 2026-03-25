<template>
  <div class="philosophy-compare">
    <div class="compare-item compare-left">
      <div class="compare-tradition">{{ left.tradition }}</div>
      <div class="compare-title">{{ left.title }}</div>
      <div class="compare-content">{{ left.content }}</div>
    </div>
    <div class="compare-divider">
      <div class="divider-line"></div>
      <div class="divider-icon">⇄</div>
      <div class="divider-line"></div>
    </div>
    <div class="compare-item compare-right">
      <div class="compare-tradition">{{ right.tradition }}</div>
      <div class="compare-title">{{ right.title }}</div>
      <div class="compare-content">{{ right.content }}</div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  left: {
    type: Object,
    required: true
    // { tradition, title, content }
  },
  right: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.philosophy-compare {
  display: flex;
  align-items: stretch;
  gap: 0;
  margin: 3em 0;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  overflow: hidden;
}

.compare-item {
  flex: 1;
  padding: 1.8em;
  background: var(--vp-c-bg-soft);
}

.compare-left {
  border-right: none;
}

.compare-right {
  border-left: none;
}

.compare-tradition {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--color-accent);
  margin-bottom: 0.5em;
  font-family: 'Noto Sans SC', sans-serif;
}

.compare-title {
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--vp-c-text-1);
  margin-bottom: 0.8em;
  font-family: 'Noto Sans SC', sans-serif;
}

.compare-content {
  font-size: 0.9rem;
  line-height: 1.9;
  color: var(--vp-c-text-2);
  font-family: 'Noto Serif SC', serif;
  text-indent: 0;
}

.compare-divider {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 2.5em;
  flex-shrink: 0;
  background: var(--vp-c-bg-mute);
  color: var(--color-accent);
  gap: 0.4em;
  padding: 1em 0;
}

.divider-line {
  flex: 1;
  width: 1px;
  background: var(--vp-c-divider);
  max-height: 40px;
}

.divider-icon {
  font-size: 1.1rem;
  color: var(--color-accent);
}

@media (max-width: 640px) {
  .philosophy-compare {
    flex-direction: column;
  }

  .compare-divider {
    flex-direction: row;
    width: auto;
    height: 2.5em;
    padding: 0 1em;
  }

  .divider-line {
    height: 1px;
    width: auto;
    flex: 1;
    max-height: none;
  }
}
</style>

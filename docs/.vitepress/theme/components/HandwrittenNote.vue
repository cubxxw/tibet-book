<template>
  <div class="handwritten-note">
    <div class="note-content">
      <slot>{{ text }}</slot>
    </div>
    <div v-if="location" class="note-location">{{ location }}</div>
  </div>
</template>

<script setup>
defineProps({
  text: {
    type: String,
    default: ''
  },
  location: {
    type: String,
    default: ''
  }
})
</script>

<style scoped>
.handwritten-note {
  position: relative;
  margin: 2.5em auto;
  max-width: 480px;
  padding: 1.8em 2em 1.5em;
  background: #fdf8f0;
  border: 1px solid #e8dcc8;
  box-shadow: 2px 3px 8px rgba(0, 0, 0, 0.08), -1px -1px 4px rgba(0, 0, 0, 0.04);
  border-radius: 2px;
  transform: rotate(-0.5deg);
}

.handwritten-note::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #d4a04a 0%, #c4933f 50%, #b8842c 100%);
  border-radius: 2px 2px 0 0;
}

.note-content {
  font-family: 'STKaiti', 'KaiTi', 'SimKai', cursive;
  font-size: 1rem;
  line-height: 2;
  color: #3a3228;
  text-indent: 0;
  white-space: pre-line;
}

.note-location {
  margin-top: 1em;
  font-size: 0.8rem;
  color: #888;
  font-style: italic;
  text-align: right;
  font-family: 'Noto Sans SC', sans-serif;
  border-top: 1px dashed #d5c9b5;
  padding-top: 0.6em;
}

/* Dark mode */
:root.dark .handwritten-note {
  background: #1e1a14;
  border-color: #3a3020;
  box-shadow: 2px 3px 8px rgba(0, 0, 0, 0.3);
}

:root.dark .note-content {
  color: #d4c8b0;
}

:root.dark .note-location {
  color: #777;
  border-top-color: #3a3020;
}
</style>

<template>
  <div class="route-marker">
    <div class="marker-pin">
      <svg viewBox="0 0 24 24" fill="currentColor" width="18" height="18">
        <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/>
      </svg>
    </div>
    <div class="marker-info">
      <span class="marker-location">{{ location }}</span>
      <span v-if="altitude" class="marker-altitude">{{ altitude }}</span>
      <span v-if="date" class="marker-date">{{ date }}</span>
    </div>
  </div>
</template>

<script setup>
defineProps({
  location: {
    type: String,
    required: true
  },
  altitude: {
    type: String,
    default: ''
  },
  date: {
    type: String,
    default: ''
  }
})
</script>

<style scoped>
.route-marker {
  display: inline-flex;
  align-items: center;
  gap: 0.6em;
  margin: 0.5em 0 1.5em;
  padding: 0.5em 1em 0.5em 0.7em;
  background: var(--color-bg-quote);
  border: 1px solid var(--vp-c-divider);
  border-radius: 100px;
  font-family: 'Noto Sans SC', sans-serif;
}

.marker-pin {
  color: var(--color-accent);
  display: flex;
  align-items: center;
  flex-shrink: 0;
}

.marker-info {
  display: flex;
  align-items: center;
  gap: 0.6em;
  flex-wrap: wrap;
}

.marker-location {
  font-size: 0.85rem;
  color: var(--vp-c-text-1);
  font-weight: 500;
}

.marker-altitude {
  font-size: 0.75rem;
  color: var(--color-accent);
  background: var(--color-accent-soft);
  padding: 0.1em 0.5em;
  border-radius: 100px;
}

.marker-date {
  font-size: 0.75rem;
  color: var(--color-text-date);
}
</style>

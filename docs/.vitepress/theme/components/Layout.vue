<template>
  <div class="custom-layout" :class="{ 'is-home-page': isHomePage }">
    <!-- 首页使用自定义布局 -->
    <template v-if="isHomePage">
      <slot name="layout-top" />
      <div class="custom-layout-content">
        <Content />
      </div>
      <slot name="layout-bottom" />
    </template>
    <!-- 其他页面使用默认布局 -->
    <DefaultThemeLayout v-else />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vitepress'
import DefaultTheme from 'vitepress/theme'

const DefaultThemeLayout = DefaultTheme.Layout

const route = useRoute()

const isHomePage = computed(() => {
  return route.path === '/'
})
</script>

<style>
/* 首页完全自定义布局 */
.custom-layout.is-home-page {
  width: 100%;
  max-width: 100%;
  padding: 0;
  margin: 0;
}

.custom-layout.is-home-page .custom-layout-content {
  width: 100%;
  max-width: 100%;
  padding: 0;
  margin: 0;
}

/* 其他页面使用默认布局样式 */
.custom-layout:not(.is-home-page) {
  width: 100%;
  max-width: 100%;
}
</style>

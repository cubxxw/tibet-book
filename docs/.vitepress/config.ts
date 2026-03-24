import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'zh-CN',
  title: '拉萨四个月',
  description: '在世界屋脊上寻找自己',

  themeConfig: {
    nav: [
      { text: '开始阅读', link: '/chapters/preface' },
      { text: '关于', link: '/about' },
    ],

    sidebar: [
      {
        text: '前言',
        items: [
          { text: '序：为什么去拉萨', link: '/chapters/preface' },
        ],
      },
      {
        text: '第一部分：抵达',
        items: [
          { text: '第一章：3658米的第一口气', link: '/chapters/01-arrival' },
          { text: '第二章：高原反应与适应', link: '/chapters/02-adaptation' },
        ],
      },
      {
        text: '第二部分：生活',
        items: [
          { text: '第三章：八廓街的日常', link: '/chapters/03-daily-life' },
          { text: '第四章：寺庙与信仰', link: '/chapters/04-temples' },
          { text: '第五章：藏人与汉人', link: '/chapters/05-people' },
        ],
      },
      {
        text: '第三部分：思考',
        items: [
          { text: '第六章：时间在这里慢下来', link: '/chapters/06-time' },
          { text: '第七章：信仰是什么', link: '/chapters/07-belief' },
          { text: '第八章：现代性与传统', link: '/chapters/08-modernity' },
        ],
      },
      {
        text: '第四部分：离开',
        items: [
          { text: '第九章：最后的转山', link: '/chapters/09-kora' },
          { text: '尾声：带走了什么', link: '/chapters/epilogue' },
        ],
      },
    ],

    socialLinks: [],

    footer: {
      message: '记录真实的拉萨，记录真实的自己',
    },

    search: {
      provider: 'local',
    },

    outline: {
      label: '本节目录',
    },

    docFooter: {
      prev: '上一节',
      next: '下一节',
    },

    lastUpdated: {
      text: '最后更新',
    },
  },

  markdown: {
    theme: {
      light: 'github-light',
      dark: 'github-dark',
    },
  },
})

import { defineConfig } from 'vitepress'

const HOSTNAME = 'https://tibet.cubxxw.com'
const SITE_NAME = '减法之地'
const DEFAULT_OG_IMAGE = '/namtso-hero.webp'

/** Absolute URL for a VitePress page path, e.g. "chapters/09-drepung.md". */
function pageUrl(relativePath: string): string {
  const path = relativePath.replace(/(index)?\.md$/, '').replace(/\/$/, '')
  return path ? `${HOSTNAME}/${path}` : `${HOSTNAME}/`
}

export default defineConfig({
  lang: 'zh-CN',
  title: SITE_NAME,
  titleTemplate: `:title — ${SITE_NAME}`,
  description: '川西入藏·拉萨旅居手记 | 37天 7354公里的非虚构旅居记录',

  lastUpdated: true,
  cleanUrls: true,
  sitemap: { hostname: HOSTNAME },

  head: [
    ['meta', { property: 'og:type', content: 'book' }],
    ['meta', { property: 'og:site_name', content: SITE_NAME }],
    ['meta', { property: 'og:locale', content: 'zh_CN' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'author', content: '鑫伟 (cubxxw)' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
    ['link', {
      href: 'https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700&family=Noto+Sans+SC:wght@400;500;700&display=swap',
      rel: 'stylesheet',
    }],
  ],

  // Per-page canonical / OG / structured data, driven by chapter frontmatter.
  transformPageData(pageData) {
    const fm = pageData.frontmatter
    const url = pageUrl(pageData.relativePath)
    const title = fm.title ? `${fm.title} — ${SITE_NAME}` : SITE_NAME
    const description = fm.excerpt || fm.description || '川西入藏·拉萨旅居手记 | 37天 7354公里的非虚构旅居记录'
    const image = HOSTNAME + (fm.heroImage || DEFAULT_OG_IMAGE)

    // Set description here rather than pushing a <meta> tag: VitePress renders
    // the site-level description first, and the earlier tag is the one that wins.
    pageData.description = description

    pageData.frontmatter.head ??= []
    pageData.frontmatter.head.push(
      ['link', { rel: 'canonical', href: url }],
      ['meta', { property: 'og:title', content: title }],
      ['meta', { property: 'og:description', content: description }],
      ['meta', { property: 'og:url', content: url }],
      ['meta', { property: 'og:image', content: image }],
      ['meta', { name: 'twitter:title', content: title }],
      ['meta', { name: 'twitter:description', content: description }],
      ['meta', { name: 'twitter:image', content: image }],
    )

    // Chapters are Article nodes; everything else inherits the site-level Book.
    if (fm.chapter) {
      if (fm.date) {
        pageData.frontmatter.head.push(
          ['meta', { property: 'article:published_time', content: new Date(fm.date).toISOString() }],
        )
      }
      pageData.frontmatter.head.push([
        'script',
        { type: 'application/ld+json' },
        JSON.stringify({
          '@context': 'https://schema.org',
          '@type': 'Article',
          headline: fm.title,
          description,
          image,
          url,
          inLanguage: 'zh-CN',
          author: { '@type': 'Person', name: '鑫伟 (cubxxw)' },
          ...(fm.date && { datePublished: new Date(fm.date).toISOString() }),
          ...(fm.location && {
            contentLocation: { '@type': 'Place', name: fm.location },
          }),
          isPartOf: {
            '@type': 'Book',
            name: SITE_NAME,
            url: `${HOSTNAME}/`,
          },
        }),
      ])
    }
  },

  themeConfig: {
    nav: [
      { text: '开始阅读', link: '/chapters/preface' },
      { text: '旅程地图', link: '/journey-map' },
      { text: '关于', link: '/about' },
    ],

    sidebar: [
      {
        text: '序言',
        items: [
          { text: '凌晨五点', link: '/chapters/preface' },
        ],
      },
      {
        text: '第一部分 · 天路',
        collapsed: false,
        items: [
          { text: '一 · 武汉机场的茶颜悦色', link: '/chapters/01-wuhan' },
          { text: '二 · 三星堆的间隙', link: '/chapters/02-sanxingdui' },
          { text: '三 · 折多山，第二次', link: '/chapters/03-zheduo' },
          { text: '四 · 来古冰川与那堆无用的石头', link: '/chapters/04-glacier' },
        ],
      },
      {
        text: '第二部分 · 拉萨',
        collapsed: false,
        items: [
          { text: '五 · 抵达', link: '/chapters/05-arrival' },
          { text: '六 · 告别', link: '/chapters/06-farewell' },
          { text: '七 · 雪城之下', link: '/chapters/07-snowcity' },
          { text: '八 · 仓央嘉措的夜晚', link: '/chapters/08-tsangyang' },
          { text: '九 · 哲蚌寺：知识即减法', link: '/chapters/09-drepung' },
          { text: '十 · 甜茶馆与拉漂众生相', link: '/chapters/10-teahouse' },
          { text: '十一 · 纳木错，天湖', link: '/chapters/11-namtso' },
        ],
      },
      {
        text: '第三部分 · 减法',
        collapsed: false,
        items: [
          { text: '十二 · 1959 年的那把火', link: '/chapters/12-fire' },
          { text: '十三 · 高原的馈赠', link: '/chapters/13-gifts' },
        ],
      },
      {
        text: '尾声',
        items: [
          { text: '出发的理由', link: '/chapters/epilogue' },
          { text: '后记', link: '/chapters/afterword' },
        ],
      },
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/cubxxw' },
    ],

    footer: {
      message: '知识在这里不是积累，而是减法',
      copyright: '减法之地 · 川西入藏·拉萨旅居手记 · 2026',
    },

    search: {
      provider: 'local',
      options: {
        translations: {
          button: { buttonText: '搜索', buttonAriaLabel: '搜索' },
          modal: {
            noResultsText: '无法找到相关结果',
            resetButtonTitle: '清除查询条件',
            footer: { selectText: '选择', navigateText: '切换', closeText: '关闭' },
          },
        },
      },
    },

    outline: {
      label: '本章目录',
      level: [2, 3],
    },

    docFooter: {
      prev: '上一章',
      next: '下一章',
    },

    lastUpdated: {
      text: '最后更新',
    },

    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '目录',
    darkModeSwitchLabel: '深色模式',
  },

  markdown: {
    html: true,
    theme: {
      light: 'github-light',
      dark: 'github-dark',
    },
  },
})

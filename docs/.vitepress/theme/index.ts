import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import './custom.css'

import ChapterHeader from './components/ChapterHeader.vue'
import ImageWithCaption from './components/ImageWithCaption.vue'
import FullWidthImage from './components/FullWidthImage.vue'
import QuoteBlock from './components/QuoteBlock.vue'
import Divider from './components/Divider.vue'
import ReadingProgress from './components/ReadingProgress.vue'
import PhotoGallery from './components/PhotoGallery.vue'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('ChapterHeader', ChapterHeader)
    app.component('ImageWithCaption', ImageWithCaption)
    app.component('FullWidthImage', FullWidthImage)
    app.component('QuoteBlock', QuoteBlock)
    app.component('Divider', Divider)
    app.component('ReadingProgress', ReadingProgress)
    app.component('PhotoGallery', PhotoGallery)
  },
} satisfies Theme

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
import HandwrittenNote from './components/HandwrittenNote.vue'
import PhilosophyCompare from './components/PhilosophyCompare.vue'
import RouteMarker from './components/RouteMarker.vue'
import ChapterNav from './components/ChapterNav.vue'
import PhotoPair from './components/PhotoPair.vue'
import HomePage from './components/HomePage.vue'
import LhasaHero from './components/LhasaHero.vue'
import CinematicHome from './components/CinematicHome.vue'
import Layout from './components/Layout.vue'

export default {
  extends: DefaultTheme,
  Layout: Layout,
  enhanceApp({ app }) {
    app.component('ChapterHeader', ChapterHeader)
    app.component('ImageWithCaption', ImageWithCaption)
    app.component('FullWidthImage', FullWidthImage)
    app.component('QuoteBlock', QuoteBlock)
    app.component('Divider', Divider)
    app.component('ReadingProgress', ReadingProgress)
    app.component('PhotoGallery', PhotoGallery)
    app.component('HandwrittenNote', HandwrittenNote)
    app.component('PhilosophyCompare', PhilosophyCompare)
    app.component('RouteMarker', RouteMarker)
    app.component('ChapterNav', ChapterNav)
    app.component('PhotoPair', PhotoPair)
    app.component('HomePage', HomePage)
    app.component('LhasaHero', LhasaHero)
    app.component('CinematicHome', CinematicHome)
  },
} satisfies Theme

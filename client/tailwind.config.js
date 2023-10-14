/** @type {import('tailwindcss').Config} */

import common from './src/styles/tailwind/common'
import { legacy } from './src/styles/tailwind/colors'

export default {
  content: ['./src/scripts/**/*.{js,ts,vue}', './pages/**/**/*.html'],
  theme: {
    colors: {
      ...legacy
    },
    ...common.theme
  },
  plugins: []
}

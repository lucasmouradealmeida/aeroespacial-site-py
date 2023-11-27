/** @type {import('tailwindcss').Config} */

import common from './src/styles/tailwind/common'
import { theme, oldTokens } from './src/styles/tailwind/colors'

export default {
  content: ['./src/scripts/**/*.{js,ts,vue}', './pages/**/**/*.html'],
  theme: {
    colors: {
      ...oldTokens,
      ...theme
    },
    ...common.theme
  },
  plugins: []
}

import { theme } from '@styles/tailwind/colors'

const getTailwindColor = (token) => {
  return theme[token] || null
}

const themeColors = Object.keys(theme).reduce((acc, color) => {
  acc[color] = () => getTailwindColor(color)
  return acc
}, {})

export { getTailwindColor, themeColors }

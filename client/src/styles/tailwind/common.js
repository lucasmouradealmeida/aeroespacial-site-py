import defaultTheme from 'tailwindcss/defaultTheme'

export const defaultTokens = {
  container: {
    padding: '1rem',
    center: true
  },
  extend: {
    borderRadius: {
      xs: '3px'
    },
    fontFamily: {
      open: ['"Open Sans"', ...defaultTheme.fontFamily.sans]
    },
    transitionProperty: {
      button: 'background, color, border-color, box-shadow, transform, opacity'
    },
    animation: {
      fadeIn: 'fadeIn 150ms ease-in',
      fadeOut: 'fadeOut 150ms ease-out'
    },
    keyframes: () => ({
      fadeIn: {
        '0%': { opacity: 0 },
        '100%': { opacity: 1 }
      },
      fadeOut: {
        '100%': { opacity: 1 },
        '0%': { opacity: 0 }
      }
    })
  },
  variants: {
    color: ['primary', 'secondary'],
    size: ['sm', 'md', 'md'],
    type: ['radio', 'checkbox']
  }
}

export default {
  theme: defaultTokens
}

import defaultTheme from 'tailwindcss/defaultTheme'

export const defaultTokens = {
  container: {
    padding: '1rem',
    center: true
  },
  extend: {
    fontSize: {
      base: ['16px']
    },
    borderRadius: {
      xs: '3px'
    },
    fontFamily: {
      open: ['"Lato Sans"', ...defaultTheme.fontFamily.sans]
    },
    transitionProperty: {
      height: 'height',
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
    }),
    breakpoints: {
      xs: '650px',
      sm: '960px',
      md: '1280px',
      lg: '1400px',
      xl: '1920px'
    },
    container: {
      xs: '650px',
      sm: '960px',
      md: '1280px',
      lg: '1400px',
      xl: '1920px'
    }
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

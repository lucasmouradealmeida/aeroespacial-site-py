import defaultTheme from 'tailwindcss/defaultTheme'

export default {
  content: ['./src/**/*.{js,ts,jsx,tsx}', '../**/**/*.php'],
  theme: {
    colors: {
      primary: '#ED1C24',
      'primary-hover': '#F14950',
      secondary: '#222222',
      'secondary-hover': '#424242',
      red: '#ec0000',
      'red-100': '#FABBBD',
      'red-400': '#F14950',
      success: '#00A774',
      'green-100': '#cdede3',
      black: '#222',
      white: '#FFF',
      'gray-100': '#F5F8FA',
      'gray-200': '#ECEFF1',
      'gray-300': '#CFD8DC',
      'gray-400': '#B0BEC5',
      'gray-500': '#90A4AE',
      'gray-600': '#607D8B',
      'gray-700': '#546E7A',
      'gray-800': '#455A64',
      'gray-900': '#37474F',
      'gray-dark': '#263238'
    },
    container: {
      padding: '1rem',
      center: true
    },
    extend: {
      borderRadius: {
        xs: '3px'
      },
      fontFamily: {
        open: ['"Oxanium"', ...defaultTheme.fontFamily.sans]
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
  },
  plugins: []
}

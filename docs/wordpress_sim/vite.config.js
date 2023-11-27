import { resolve } from 'path'
import { defineConfig } from 'vite'
import liveReload from 'vite-plugin-live-reload'
import terser from '@rollup/plugin-terser'

const isProd = process.env.NODE_ENV === 'production'

module.exports = defineConfig({
  root: '',
  build: {
    outDir: 'assets',
    emptyOutDir: false,
    sourcemap: !isProd,
    target: 'es2020',
    manifest: false,
    rollupOptions: {
      input: {
        // Scripts
        core: resolve(__dirname, '/src/scripts/core/'),
        'page-financiamento': resolve(__dirname, '/src/scripts/pages/financiamento/'),
        // Styles
        main: resolve(__dirname, '/src/styles/main.scss')
      },
      output: {
        entryFileNames: `[name].js`,
        chunkFileNames: `[name].js`,
        assetFileNames: `[name].[ext]`
      }
    }
  },
  server: {
    cors: true,
    strictPort: true,
    port: 3000,
    https: false,
    open: 'http://localhost:2080/financiamento?o=MTMyMDoyMDIzMDcxNDExMzQ1NA%3D%3D&passo=1'
  },
  resolve: {
    extensions: ['.mjs', '.js', '.ts', '.jsx', '.tsx', '.json', '.vue', '.scss', '.css'],
    alias: {
      '@': resolve(__dirname, '/src/scripts/'),
      '@styles': resolve(__dirname, '/src/styles/'),
      $tatic: '/static/'
    }
  },
  plugins: [
    liveReload([resolve(__dirname + '/../**/*.php')]),
    terser({
      compress: true,
      mangle: true,
      format: {
        comments: false,
        beautify: false
      }
    })
  ]
})

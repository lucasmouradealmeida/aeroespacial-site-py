import { resolve, parse, join } from 'path'
import { readdirSync } from 'fs'
import { defineConfig, splitVendorChunkPlugin } from 'vite'
import vue from '@vitejs/plugin-vue'
import liveReload from 'vite-plugin-live-reload'
import terser from '@rollup/plugin-terser'

const path = {
  js: resolve(__dirname + '/src/scripts/'),
  css: resolve(__dirname + '/src/styles/'),
  html: resolve(__dirname + '/pages/**/*.html'),
  output: resolve(__dirname + '/public/dist'),
  files: resolve(__dirname, 'src/scripts/build')
}

const isProd = process.env.NODE_ENV === 'production'
const filesToBuild = readdirSync(path.files)
const jsFilesToBuild = filesToBuild.reduce((acc, file) => {
  if (file.endsWith('.js')) {
    const key = parse(file).name
    acc[key] = join(path.files, file)
  }
  return acc
}, {})

export default defineConfig({
  resolve: {
    extensions: ['.js', '.ts', '.scss', '.vue'],
    alias: {
      '@': path.js,
      '@/build': '/dev/null',
      '@styles': path.css
    }
  },
  publicDir: 'static',
  build: {
    outDir: path.output,
    emptyOutDir: true,
    sourcemap: !isProd,
    target: 'es2020',
    manifest: false,
    rollupOptions: {
      input: jsFilesToBuild,
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
    open: 'http://localhost:5000'
  },
  test: {
    exclude: ['**/node_modules/**', '**/public/**'],
    testTimeout: 20000
  },
  plugins: [
    splitVendorChunkPlugin(),
    vue(),
    liveReload([path.html]),
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

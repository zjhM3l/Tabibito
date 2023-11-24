import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: '127.0.0.1',
    port: 5173,
    https: false
  },
  build: {
    minify:'terser',
    terserOptions: {
      compress:{
        drop_console: true,
        drop_debugger: false
      }
    }
  }
})

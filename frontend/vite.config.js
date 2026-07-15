import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { VitePWA } from 'vite-plugin-pwa'

export default defineConfig({
  plugins: [
    vue(),
    VitePWA({
      registerType: 'autoUpdate',
      manifest: {
        name: 'Placement Portal',
        short_name: 'Placement Portal',
        description: 'IIT Madras Placement Portal',
        theme_color: '#800000',
        background_color: '#ffffff',
        display: 'standalone',
        start_url: '/',
        icons: [
          {
            src: 'pwa-192x192.PNG',
            sizes: '192x192',
            type: 'image/png'
          },
          {
            src: 'pwa-512x512.PNG',
            sizes: '512x512',
            type: 'image/png'
          }
        ]
      }
    })
  ]
})

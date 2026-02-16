import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  define: {
    'process.env': {}
  }
})</content>
<parameter name="filePath">c:\Users\CW\Desktop\SmartBite\vite.config.ts
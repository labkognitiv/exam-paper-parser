import tailwindcss from '@tailwindcss/postcss';
import vinext from 'vinext';
import { defineConfig } from 'vite';

// macOS Seatbelt blocks FSEvents, so Codex previews need polling for HMR.
const isCodexSeatbeltSandbox = process.env.CODEX_SANDBOX === 'seatbelt';

export default defineConfig(() => {
  return {
    css: { postcss: { plugins: [tailwindcss()] } },
    server: {
      watch: {
        ignored: ['**/public/data/**', '**/review-state.json'],
        ...(isCodexSeatbeltSandbox ? { useFsEvents: false, usePolling: true } : {}),
      },
      fs: {
        allow: [
          '/Users/abdullahaftab/Kognitiv/exam-paper-parser',
        ],
      },
      proxy: { '/api': 'http://127.0.0.1:3003' },
    },
    plugins: [vinext()],
  };
});

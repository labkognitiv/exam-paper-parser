/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          navy: '#1c2135',
          'navy-hover': '#292f4c',
          teal: '#14b8a6',
          'teal-dark': '#0d9488',
          orange: '#f97316',
          'orange-dark': '#ea580c',
          purple: '#8b5cf6',
          'purple-dark': '#7c3aed',
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
      }
    },
  },
  plugins: [],
}

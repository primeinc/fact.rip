/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['IBM Plex Sans', 'sans-serif'],
        serif: ['IBM Plex Serif', 'serif'],
        mono: ['IBM Plex Mono', 'monospace'],
      },
      colors: {
        'truth-blue': '#0F52BA',
        'valid-green': '#228B22',
        'caution-amber': '#FFBF00',
        'error-red': '#D32F2F',
        'soft-blue': '#6495ED',
      },
    },
  },
  plugins: [],
};

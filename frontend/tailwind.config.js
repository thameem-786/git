/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        automotive: {
          darkbg: '#0B1220',
          card: '#16213E',
          primary: '#00C2FF',
          accent: '#00D9FF',
          success: '#00FF41',
          warning: '#FFD700',
          danger: '#FF6B6B',
        },
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },
    },
  },
  plugins: [],
}

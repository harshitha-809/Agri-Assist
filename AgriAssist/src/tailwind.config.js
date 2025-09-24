/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["templates/{HTML,JS}/*.{html,css,js}", "templates/{HTML,JS}/farmer/*.{html,css,js}"],
  theme: {
    fontFamily: {
      sans: ["Poppins"],
    },
    extend: {
      colors: {
        'default': '#e5e7eb',
        'primary': '#4c6eeb'
      }
    },
  },
  plugins: [],
}


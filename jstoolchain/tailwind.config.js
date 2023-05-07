/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../catalog/templates/**/*.{html,js}"],
  theme: {
      extend: {
          colors: {
              'primary': '#36BBCE',
              'middle': '#5FC0CE',
              'secondary': '#03899C',
          },
      },
  },
  plugins: [],
}


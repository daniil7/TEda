/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../catalog/templates/**/*.{html,js}"],
  theme: {
      extend: {
          colors: {
              'primary': '#00AEEF',
              'middle': '#FAFAFA',
              'secondary': '#FFFFFF',
              'text': '#015965',
              'text-primary': '#FFFFFF',
              'text-middle': '#222222',
              'text-secondary': '#000000',
          },
      },
  },
  plugins: [],
}


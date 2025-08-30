/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/*.{html,svelte,js,ts}",
    "./src/**/*.{html,svelte,js,ts}",
  ],
  theme: {
    extend: {
      colors: {
        languages: {
          "natural-ancient": "#A855F7",
          "natural-modern": "#A855F7",
          "conlang": "#A855F7",
          "default": "#E0E0E0"
        }
      }
    }
  },
  plugins: [require("@tailwindcss/typography"), require("daisyui")],
  daisyui: {
    styled: true,
    themes: [
      "light",
      "dark"],
    base: true,
    utils: true,
    logs: true,
    rtl: false,
    prefix: "",
  },
};

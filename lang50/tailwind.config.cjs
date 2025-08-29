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
          "natural-ancient": "#EBC06D",
          "natural-modern": "#89B4FA",
          "conlang": "#E49B5D",
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

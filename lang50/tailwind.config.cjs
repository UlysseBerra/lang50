/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/*.{html,svelte,js,ts}",
    "./src/**/*.{html,svelte,js,ts}",
  ],
  theme: {
    extend: {},
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

// /** @type {import("tailwindcss").Config} */
const colors = require("tailwindcss/colors");


module.exports = {
  content: ["{{cookiecutter.project_slug}}/**/*.{html,js}"],
  theme: {
    colors: {
      primary: "{{cookiecutter.primary_color}}",
      secondary: colors.gray,
    }
  },
  plugins: []
};



// /** @type {import("tailwindcss").Config} */
const colors = require("tailwindcss/colors");


module.exports = {
    content: ["imeleo/**/*.{html,js}"],
    theme: {
        colors: {
            primary: colors.blue,
            secondary: colors.gray,
            white: colors.white,
            gray: colors.gray,
            transparent: 'transparent',
            current: 'currentColor',
            black: colors.black,
            emerald: colors.emerald,
            indigo: colors.indigo,
            yellow: colors.yellow,
            neutral: colors.neutral,
        }
    },
    plugins: []
};



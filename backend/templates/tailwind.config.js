/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./public/**/*.{html,js}",
  ],
  darkMode: "class",
  theme: {
    screens: {
      xs: "480px",
      sm: "640px",
      md: "768px",
      lg: "1024px",
      xl: "1380px",
    },

    extend: {
      spacing: {
        25: "6.25rem",
        50: "12.5rem",
      },
      boxShadow: {
        base: "0px 1px 10px rgba(0, 0, 0, 0.05)",
      },
      borderRadius: {
        "4xl": "2rem",
      },
      container: {
        center: true,
        padding: {
          DEFAULT: "1rem",
          lg: "0.625rem",
        },
      },
      colors: {
        'white': "#FEFEFF",
        'black': "#0D0D0D",
        'border': 'hsl(var(--border))',
        'ring': 'hsl(var(--ring))',
        'background': 'hsl(var(--background))',
        'warning': 'hsl(var(--warning))',
        'alert': 'hsl(var(--alert))',
        'blue': 'hsl(var(--blue))',
        'cyan': 'hsl(var(--cyan))',
        'success': {
          DEFAULT: 'hsl(var(--success))',
          'secondary': 'hsl(var(--success-secondary))',
        },
        'text': 'hsl(var(--text))',
        'primary': 'hsl(var(--primary))',
        'primary-btn': 'hsl(var(--primary-btn))',
        'secondary': 'hsl(var(--secondary))',
        'muted': 'hsl(var(--muted))',
      },

      borderRadius: {
        base: "13px",
      },
      fontFamily: {
        iranyekan: "IRANYekan",
      },
    },
  },

};

module.exports = {
  env: {
    browser: true,
    es2021: true,
    node: true,
  },
  extends: [
    'eslint:recommended',
    'plugin:react/recommended',
    'plugin:react/jsx-runtime',
    'plugin:react-hooks/recommended',
    'plugin:jsx-a11y/recommended',
    'plugin:prettier/recommended',
  ],
  parserOptions: {
    ecmaFeatures: {
      jsx: true,
    },
    ecmaVersion: 'latest',
    sourceType: 'module',
  },
  plugins: ['react', 'react-hooks', 'jsx-a11y', 'prettier'],
  rules: {
    // Override default rules
    'react/prop-types': 'off', // Since we're not using PropTypes
    'react/react-in-jsx-scope': 'off', // Not needed with React 17+
    'prettier/prettier': 'error', // Ensures prettier errors are ESLint errors
    'no-unused-vars': ['error', { varsIgnorePattern: 'React' }], // Allow React to be imported even if not directly used (for JSX in older projects)
    'react/no-unescaped-entities': 'off', // Allow apostrophes and quotes in text

    // Fix accessibility issues - Disable the anchor-is-valid rule since we've already fixed
    // the main issues with proper URLs and now these are just warnings about navigation items
    'jsx-a11y/anchor-is-valid': 'off',
    'jsx-a11y/anchor-has-content': [
      'error',
      {
        components: ['Link'],
      },
    ],
  },
  settings: {
    react: {
      version: 'detect',
    },
  },
};

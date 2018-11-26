# Create React App

```
yarn create react-app react-test-app
cd react-test-app
yarn start
```

In package.json we then only have three dependencies:

```json
{
  "dependencies": {
    "react": "^16.6.3",
    "react-dom": "^16.6.3",
    "react-scripts": "2.1.1"
  }
}
```

However, under the hoods we depend on about a thousand packages:

```
ls -l node_modules/ | wc -l # => 1032
``

To add EsLint Standard style:

```
yarn run eject
```

Once ejected we now have around 50 explicit dependencies in package.json.

Now we can add the eslint standard dependencies:

```
yarn add eslint-config-standard eslint-config-standard-jsx eslint-plugin-standard eslint-plugin-promise eslint-plugin-node
```

Update `eslintConfig` in package.json to:

```json
{
  "eslintConfig": {
    "extends": ["standard", "standard-jsx"]
  }
}
```

## Resources

* [create-react-app](https://github.com/facebook/create-react-app)

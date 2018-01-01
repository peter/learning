# React Introduction Notes

## Writing Your First Component

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>svideo</title>
    <link rel="stylesheet" href="/public/normalize.css">
    <link rel="stylesheet" href="/public/style.css">
</head>
<body>
    <div id="app"></div>
    <script src="node_modules/react/dist/react.js"></script>
    <script src="node_modules/react-dom/dist/react-dom.js"></script>
    <script>
      var div = React.DOM.div
      var h1 = React.DOM.h1

      var MyFirstComponent = (
        div({style: {color: 'red'}},
          h1(null, 'This is my first component')
        )
      )

      ReactDOM.render(MyFirstComponent, document.getElementById('app'))
    </script>
</body>
</html>
```

## Modularizing the Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>svideo</title>
    <link rel="stylesheet" href="/public/normalize.css">
    <link rel="stylesheet" href="/public/style.css">
</head>
<body>
    <div id="app"></div>
    <script src="node_modules/react/dist/react.js"></script>
    <script src="node_modules/react-dom/dist/react-dom.js"></script>
    <script src="js/ClientApp.js"></script>
</body>
</html>
```

In `js/ClientApp.js`:

```javascript
var div = React.DOM.div
var h1 = React.DOM.h1

var MyTitle = React.createClass({
  render() {
    return (
      div(null,
        h1(null, 'Check out this other thing')
      )
    )
  }
})

var MyFirstComponent = (
  div(null,
    React.createElement(MyTitle, null),
    React.createElement(MyTitle, null),
    React.createElement(MyTitle, null)
  )
)

ReactDOM.render(MyFirstComponent, document.getElementById('app'))
```

With factory:

```javascript
var div = React.DOM.div
var h1 = React.DOM.h1

var MyTitle = React.createClass({
  render() {
    return (
      div(null,
        h1(null, 'Check out this other thing')
      )
    )
  }
})

var MyTitleFact = React.createFactory(MyTitle)

var MyFirstComponent = (
  div(null,
    MyTitleFact(null),
    MyTitleFact(null),
    MyTitleFact(null)
  )
)

ReactDOM.render(MyFirstComponent, document.getElementById('app'))
```

## Props

```javascript
var div = React.DOM.div
var h1 = React.DOM.h1

var MyTitle = React.createClass({
  render() {
    return (
      div(null,
        h1({style: {color: this.props.color}},
           this.props.title)
      )
    )
  }
})

var MyTitleFact = React.createFactory(MyTitle)

var MyFirstComponent = (
  div(null,
    MyTitleFact({title: 'Props are great!'}),
    React.createElement(MyTitle, {
      title: 'Use props everywhere',
      color: 'mediumaquamarine'}),
    MyTitleFact(null)
  )
)

ReactDOM.render(MyFirstComponent, document.getElementById('app'))
```

You can pass in everything as a property, i.e. a function.

## Composite Components and Factories

* Each component must have one top level element, i.e. typically a div.
* Each component must have a render method that must return a component.
  The render function must be pure. You don't know how many times render
  is going to get called.

## Standard JS and EditorConfig

```
npm install standard -g
standard
```

Add global comment at the top of js file:

```
/* global React ReactDOM */
```

There is an `.editorconfig` file in the root folder and there are plugins for most editors to support it.

## NPM Scripts

In package.json:

```json
{
  "scripts": {
    "test": "standard"
  }
}
```

## Webpack

The most popular module bundler (build) library in the React community.

You don't want to expose global variables such as React and ReactDOM.

An alternative to Webpack is rollup.js which automatically includes only those modules that you use.

We extract MyTitle.js and make it do `module.exports = MyTitle` and then in ClientApp.js we do:

```javascript
var React = require('react')
var ReactDOM = require('react-dom')
var MyTitle = require('./MyTitle')
```

This means we also no longer need the global declaration for React and ReactDOM.

Remove the library script includes from index.html:

```
<script src="node_modules/react/dist/react.js"></script>
<script src="node_modules/react-dom/dist/react-dom.js"></script>
```

Run webpack:

```
webpack js/ClientApp.js public/bundle.js
```

Add build script to package.json:

```json
{
  "scripts": {
    "test": "standard",
    "build": "webpack js/ClientApp.js public/bundle.js"
  }
}
```

```
npm run build
```

## Babel

To use JSX we need Babel. Most React developers use JSX.

Add a .babelrc file:

```json
{
  "presets": ["react", "es2015"]
}
```

The `es2015` preset will include all the polyfills for ES2015 and you probably don't need all of them. In production you should only include the plugins that you need.
The presets correspond to packages in the devDependencies (babel-preset-es2015 and babel-preset-react).

Webpack will run babel for us (as a loader). We have a `babel-loader` dev dependency for this purpose. Webpack can also run tests and do linting etc. Let's tell webpack to run all js code through babel:

```json
{
  "scripts": {
    "test": "standard",
    "build": "webpack --module-bind 'js=babel' js/ClientApp.js public/bundle.js"
  }
}
```

Now that we have babel all ES6 features are available to us.

## Configuring Webpack

We are going to abstract out webpack config into webpack.config.js:

```javascript
const path = require('path')

module.exports = {
  context: __dirname,
  entry: './js/ClientApp.js',
  output: {
    path: path.join(__dirname, '/public'),
    filename: 'bundle.js'
  },
  resolve: {
    extensions: ['', '.js', '.jsx', '.json']
  },
  stats: {
    colors: true,
    reasons: true,
    chunks: false
  },
  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        loader: 'babel-loader'
      }
    ]
  }
}
```

Then we can modify the npm build script to just run webpack and we can run webpack directly or via npm run build:

```
webpack
npm run build
```

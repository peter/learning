# Learning React.js

## History

"React was created by Jordan Walke, a software engineer at Facebook. He was influenced by XHP, an HTML component framework for PHP.[9] It was first deployed on Facebook's newsfeed in 2011 and later on Instagram.com in 2012.[10] It was open-sourced at JSConf US in May 2013."

## Hello World

HTML:

```html
<div id="root"></div>
```

JavaScript:

```javascript
ReactDOM.render(
  <h1>Hello, world!</h1>,
  document.getElementById('root')
);
```

## Creating a React App

See [create-react-app.md](create-react-app.md)

## Main Concepts

See [main-concepts.md](main-concepts.md)

## React Developer Tools for Chrome

[Chrome Web Store: React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi)

For local examples you need to check "Allow access to file URLs" for the extension in Chrome.

## Redux and the Flux Architecture

[Redux](redux.md)

## Important Lifecycle Methods

* `shouldComponentUpdate` allows the developer to prevent unnecessary re-rendering of a component by returning false if a render is not required.
* `componentDidMount` is called once the component has 'mounted' (the component has been created in the user interface, often by associating it with a DOM node). This is commonly used to trigger data loading from a remote source via an API.

# Routing

TODO

## Miscellaneous

* [Binding handler functions to this](bind-handler-functions.md)
* [Setting inner HTML](setting-inner-html.md)

## Advanced Guides

TODO

## Ajax

[Ajax](ajax.md)

## Hooks

TODO

https://reactjs.org/docs/hooks-intro.html

## Resources

* [React on Wikipedia](https://en.wikipedia.org/wiki/React_(JavaScript_library))
* [How to Learn React (Link Collection)](https://medium.freecodecamp.org/learning-react-roadmap-from-scratch-to-advanced-bff7735531b6)

* [React Component API Reference](https://reactjs.org/docs/react-component.html)

* [create-react-app](https://github.com/facebook/create-react-app)

* [Babel REPL](https://babeljs.io/repl)
* [Codepen](https://codepen.io)

* [Linting React Using ESLint with Create React App](https://alligator.io/react/linting-react/)

* [React Docs - Main Concepts](https://reactjs.org/docs/hello-world.html)
* [Learn React Crash Course (Video)](https://youtu.be/Ke90Tje7VS0)

* [Course: Complete Introduction to React (feat. Redux and React Router)](https://frontendmasters.com/courses/react-intro)

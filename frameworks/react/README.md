# Learning React.js

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

## Redux

[Redux](redux.md)

## Miscellaneous

* [Binding handler functions to this](bind-handler-functions.md)
* [Setting inner HTML](setting-inner-html.md)

## Advanced Guides

TODO

## Ajax

Ajax example:

```babel
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      items: []
    };
  }

  componentDidMount() {
    fetch("https://api.example.com/items")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            items: result.items
          });
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
  }

  render() {
    const { error, isLoaded, items } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <ul>
          {items.map(item => (
            <li key={item.name}>
              {item.name} {item.price}
            </li>
          ))}
        </ul>
      );
    }
  }
}
```

## Hooks

TODO

https://reactjs.org/docs/hooks-intro.html

## Resources

* [How to Learn React (Link Collection)](https://medium.freecodecamp.org/learning-react-roadmap-from-scratch-to-advanced-bff7735531b6)

* [React Component API Reference](https://reactjs.org/docs/react-component.html)

* [create-react-app](https://github.com/facebook/create-react-app)

* [Babel REPL](https://babeljs.io/repl)
* [Codepen](https://codepen.io)

* [Linting React Using ESLint with Create React App](https://alligator.io/react/linting-react/)

* [React Docs - Main Concepts](https://reactjs.org/docs/hello-world.html)
* [Learn React Crash Course (Video)](https://youtu.be/Ke90Tje7VS0)

* [Course: Complete Introduction to React (feat. Redux and React Router)](https://frontendmasters.com/courses/react-intro)

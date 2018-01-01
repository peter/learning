# JSX

## What is JSX?

JSX was very controversial, especially right after React.js was released. JSX allows
you to write HTML in your JavaScript.

Let's rename `MyTitle.js` to `MyTitle.jsx`. This is in order to indicate that the file must be transpiled with Babel.

```javascript
const MyTitle = React.createClass({
  render () {
    return (
      <div>
        <h1 style: {color: this.props.color}>
          {this.props.title}
        </h1>
      </div>
    )
  }
})
```

Alternative style interpolation:

```javascript
const MyTitle = React.createClass({
  render () {
    const style = {color: this.props.color}
    return (
      <div>
        <h1 style: { style }>
          {this.props.title}
        </h1>
      </div>
    )
  }
})
```

Running `standard` is not going to work yet.

Since we are in ES6 land now we can convert var statements to const. Using const is a good default. If something needs to change we can use `let` instead.

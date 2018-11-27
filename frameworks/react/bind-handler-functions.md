# Bind Handler Functions

```babel
function inheritedProperties(obj) {
    var props = []
    let currentObj = obj
    do {
        props = props.concat(Object.getOwnPropertyNames(currentObj))
    } while (currentObj = Object.getPrototypeOf(currentObj))
    return props.sort().filter((prop, i) => prop !== props[i + 1])
}

function handlerFunctions (obj) {
  return inheritedProperties(obj).filter(property => {
    return typeof obj[property] === 'function' && property.startsWith('handle')
  })
}

function bindHandlerFunctions (obj) {
  handlerFunctions(obj).forEach(handler => obj[handler] = obj[handler].bind(obj))
}
```

Usage:

```babel
class TodoApp extends React.Component {
  constructor (props) {
    super(props)
    this.state = {items: [], text: ''}
    bindHandlerFunctions(this)
  }
  // ...
}
```

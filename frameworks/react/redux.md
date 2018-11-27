# Redux

Redux is a predictable state container for JavaScript apps.

Following in the steps of Flux, CQRS, and Event Sourcing, Redux attempts to make state mutations predictable by imposing certain restrictions on how and when updates can happen. These restrictions are reflected in the three principles of Redux.

To change something in the state, you need to dispatch an action. An action is a plain JavaScript object

```javascript
{ type: 'ADD_TODO', text: 'Go to swimming pool' }
{ type: 'TOGGLE_TODO', index: 1 }
{ type: 'SET_VISIBILITY_FILTER', filter: 'SHOW_ALL' }
```

Finally, to tie state and actions together, we write a function called a reducer.

```javascript
function todos(state = [], action) {
  switch (action.type) {
    case 'ADD_TODO':
      return state.concat([{ text: action.text, completed: false }])
    case 'TOGGLE_TODO':
      return state.map(
        (todo, index) =>
          action.index === index
            ? { text: todo.text, completed: !todo.completed }
            : todo
      )
    default:
      return state
  }
}
```

Three principles:

* Single source of truth
* State is read-only
* Changes are made with pure functions

As actions are just plain objects, they can be logged, serialized, stored, and later replayed for debugging or testing purposes.

Reducers are just pure functions that take the previous state and an action, and return the next state.

## Resources

* [Redux Homepage - Motivation](https://redux.js.org/introduction/motivation)

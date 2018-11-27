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

## Use of the Flux architecture

"To support React's concept of unidirectional data flow (which might be contrasted with Angular's bidirectional flow), the Flux architecture represents an alternative to the popular model-view-controller architecture. Flux features actions which are sent through a central dispatcher to a store, and changes to the store are propagated back to the view. When used with React, this propagation is accomplished through component properties.

Flux can be considered a variant of the observer pattern.

A React component under the Flux architecture should not directly modify any props passed to it, but should be passed callback functions that create actions which are sent by the dispatcher to modify the store. The action is an object whose responsibility is to describe what has taken place: for example, an action describing one user 'following' another might contain a user id, a target user id, and the type USER_FOLLOWED_ANOTHER_USER. The stores (which can be thought of as models) can alter themselves in response to actions received from the dispatcher.

This pattern is sometimes expressed as "properties flow down, actions flow up". Many implementations of Flux have been created since its inception, perhaps the most well-known being Redux which features a single store, often called a single source of truth"

## Resources

* [React on Wikipedia](https://en.wikipedia.org/wiki/React_(JavaScript_library))
* [Redux Homepage - Motivation](https://redux.js.org/introduction/motivation)
* [Redux DevTools - Chrome Extension](https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd)

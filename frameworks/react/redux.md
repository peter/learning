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

## Redux Tutorial

Project setup:

```
npx create-react-app redux-tutorial
cd redux-tutorial
yarn add redux react-redux
```

Create basic store and action:

```babel
// index.js
import { createStore } from 'redux'
function reducer (state, action) {
  if (action.type === 'CHANGE_STATE') {
    return action.payload.newState
  }
  return 'STATE'
}
const store = createStore(reducer)
const action = {
  type: 'CHANGE_STATE',
  payload: {
    newState: 'NEW STATE'
  }
}
console.log('store.getState() before action', store.getState());

store.dispatch(action)

console.log('store.getState() after action', store.getState());
```

More advanced example where we connect Redux to React:

```babel
import { createStore, combineReducers } from 'redux'
import { Provider } from 'react-redux'
import productsReducer from './reducers/products_reducer'
import userReducer from './reducers/user_reducer'

const allReducers = combineReducers({
  products: productsReducer,
  user: userReducer
})

const initialState = {
  products: [{name: 'iPhone'}],
  user: 'Peter'
}
const enhancer = window.devToolsExtension && window.devToolsExtension() // For Redux Chrome extension
// https://redux.js.org/api/createstore
const store = createStore(allReducers, initialState, enhancer)

ReactDOM.render(<Provider store={store}><App /></Provider>, document.getElementById('root'));
```

We can put the user actions in their own file:

```babel
// actions/user_actions.js
export const UPDATE_USER = 'users.updateUser'

export function updateUser (newUser) {
  return {
    type: UPDATE_USER,
    payload: {
      user: newUser
    }
  }
}
```

And use [connect](https://react-redux.js.org/docs/api#connect) to hook up Redux with the App via
the props passed to components:

```babel
// App.js
import { connect } from 'react-redux'
import { updateUser } from './actions/user_actions'

class App extends Component {
  constructor (props) {
    super(props)
    this.onUpdateUser = this.onUpdateUser.bind(this)
  }

  onUpdateUser () {
    this.props.onUpdateUser('Sammy')
  }

  render() {
    return (
      <div className="App">
        <div onClick={this.onUpdateUser}>
          Update user
        </div>
        {this.props.user}
      </div>
    );
  }
}

const mapStateToProps = state => {
  return state
}

const mapDispatchToProps = {
  onUpdateUser: updateUser
}

export default connect(mapStateToProps, mapDispatchToProps)(App);
```

To use Ajax with Redux:

```
yarn add redux-thunk
```

A thunk is a function that wraps an expression to delay its evaluation.

```babel
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './reducers/index';

// Note: this API requires redux@>=3.1.0
const store = createStore(
  rootReducer,
  applyMiddleware(thunk)
);
```

Direct approach:

```babel
import { createStore } from 'redux'

const UPDATE_USER = 'UPDATE_USER'
const INITIAL_STATE = {
  user: 'peter'
}
function reducer (state = INITIAL_STATE, {type, payload}) {
  switch (type) {
    case UPDATE_USER:
      return {
        ...state,
        user: payload.user
      }
    default:
      return state
  }
}
const enhancer = window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
const store = createStore(reducer, enhancer)

const action = {
  type: 'UPDATE_USER',
  payload: {
    user: 'Joe'
  }
}
console.log('pm debug before dispatch', store.getState())
store.dispatch(action)
console.log('pm debug after dispatch', store.getState());
```

## Resources

* [React on Wikipedia](https://en.wikipedia.org/wiki/React_(JavaScript_library))
* [Redux Homepage - Motivation](https://redux.js.org/introduction/motivation)
* [Redux DevTools - Chrome Extension](https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd)
* [Redux Tutorial - Learn React/Redux in one video](https://www.youtube.com/watch?v=OSSpVLpuVWA&t=606s)
* [react-redux-realworld-example-app](https://github.com/gothinkster/react-redux-realworld-example-app)
* [The react-redux connect function](https://react-redux.js.org/docs/api#connect)
* [redux-thunk](https://github.com/reduxjs/redux-thunk)

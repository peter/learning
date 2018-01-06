# Learning Vue.js

Notes in learning the Vue.js framework

## Examples

* [DOM Interactions](examples/dom-interactions.html)

## DOM Interaction and Templates

Vue templates are rendered in a virtual DOM before they update the real DOM.

Vue will HTML escape curly brace expressions (double curlies) by default.
You can't use curly brace expressions in HTML attribute values. Instead
you should use `v-bind` (i.e. <a v-bind:href="url">click me</a>).

If you add the `v-once` to HTML element its contents will only be rendered once, i.e.
it won't be re-rendered when the data changes.

Vue has computer properties that are synchronous functions that only get executed if
one of the properties that are used by the function has changed.

You can also set up a watch on a property which is a function that gets executed
with the value of the property on change. The watch functions can have asynchronous code
(Ajax calls, setTimeout etc.).

## The Vue Instance

You can have multiple Vue instances associated with different DOM elements (templates).
Each Vue instance is a self contained Vue.js application and communication between
instances is possible but can be an anti pattern.

You can set data properties and invoke methods on view instances:

```javascript
var vm1 = new Vue({
  el: '#app',
  data: {foo: 'bar'},
  methods: {
    bar: function() {
      alert('bar invoked')
    }
  }
})
setTimeout(function() {
  vm1.foo = 'changed by timer'
}, 3000)
vm1.bar()
console.log("vm1.$data=", vm1.$data)
```

However, you cannot set new properties on an existing Vue instances as they will
not be watched - they don't have getters and setters (there is proxying going on
under the hood).

Instead of setting the `el` property you can invoke the `$mount(selector)` method
after the instance has been created. The Vue instance can only be mounted on one
element in the DOM.

You can add `ref` properties to DOM elements that Vue will recognize but when
you modify the `ref` element you are modifying the DOM directly so changes
may be overwritten by Vue:

```html
<div id="app">
  <button type="button" ref="myButton" @click="show">{{ button }}</button>  
</div>
<script type="text/javascript">
  new Vue({
    el: '#app',
    data: {
      button: 'Click Me'
    },
    methods: {
      show: function() {
        this.$refs.myButton.innerText = 'Button Clicked!'
        var self = this
        setTimeout(function() {
          self.button = 'And overwritten...'
        }, 1000)
      }
    }
  })
</script>
```

## Components

For components the `data` property needs to be a function otherwise data would be
shared between component instances.

```html
<div id="app">
  <server-status></server-status>
  <server-status></server-status>
</div>
<script type="text/javascript">
  Vue.component('server-status', {
    template: '<div><h1>Server status: {{ status }}</h1><button @click="changeStatus">Change</button></div>',
    data: function() {
      return {
        status: 'Critical'
      }
    },
    methods: {
      changeStatus: function() {
        this.status = 'Changed'
      }
    }
  })
  new Vue({
    el: '#app'
  })
</script>
```

Components can be registered globally with `Vue.component()` (for all Vue instances, see above) or locally with the
`components` property of a Vue instance:

```html
<div id="app">
  <server-status></server-status>
  <server-status></server-status>
</div>
<script type="text/javascript">
  var serverStatus = {
    template: '<div><h1>Server status: {{ status }}</h1><button @click="changeStatus">Change</button></div>',
    data: function() {
      return {
        status: 'Critical'
      }
    },
    methods: {
      changeStatus: function() {
        this.status = 'Changed'
      }
    }
  }
  new Vue({
    el: '#app',
    components: {
      'server-status': serverStatus
    }
  })
</script>
```

## Understanding .vue Files

The `.vue` files typically have an HTML `template` tag at the top, then a `script` (JavaScript) section, and a `style` (CSS) section at the bottom. The `script` section behaves like a Vue instance.

## Global Vue Config

[Vue.config](https://vuejs.org/v2/api/#Global-Config) is an object containing Vue’s global configurations. You can modify its properties before bootstrapping your application.

## Resources

* [Udemy Course](https://www.udemy.com/vuejs-2-the-complete-guide)
* [Vue.js in 30 Minutes Video](https://www.youtube.com/watch?v=VPUdtEf3oXI)
* [Vue Chrome DevTools Extension](https://github.com/vuejs/vue-devtools)
* [Vuex - State Management for Vue](https://github.com/vuejs/vuex)
* [Using a Simple Vue Event Bus](https://vuejs.org/v2/guide/components.html#Non-Parent-Child-Communication)

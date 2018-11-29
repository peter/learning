# JavaScript

## Composition and Pipe

```javascript
const a = v => v + 'a'
const b = v => v + 'b'
const c = v => v + 'c'

function compose (...fns) {
  if (fns.length === 0) return arg => arg
  if (fns.length === 1) return fns[0]

  return fns.reduce((a, b) => {
    return (...args) => a(b(...args))
  })
}

function reverseCompose (...fns) {
  const reverseFns = [...fns].reverse()
  return compose(...reverseFns)
}

function pipe (args, ...fns) {
  const makeArray = v => Array.isArray(v) ? v : [v]
  return reverseCompose(...fns).apply(null, makeArray(args))
}

compose(a, b, c)('v') // => 'vcba'
pipe('v', a, b, c) // => 'vabc'
```

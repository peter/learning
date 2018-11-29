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

function rCompose (...fns) {
  const reverseFns = [...fns].reverse()
  return compose(...reverseFns)
}

function pipe (args, fns) {
  return rCompose(...fns).apply(null, args)
}

compose(a, b, c)('v') // => 'vcba'
pipe(['v'], [a, b, c]) // => 'vabc'
```

Pipeline with abort/shortcutting:

```javascript
function callIf (condition, fn) {
  return (arg) => condition(arg) ? fn(arg) : arg
}

const notNull = v => v != null

const trim = v => v.trim()
const upperCase = v => v.toUpperCase()

callIf(notNull, trim)(' foobar ') // => 'foobar'
callIf(notNull, trim)(null) // => null

function pipeIf (condition, arg, fns) {
  const fnsWithIf = fns.map(fn => callIf(condition, fn))
  return pipe([arg], fnsWithIf)
}

pipeIf(notNull, ' foobar ', [trim, upperCase]) // => 'FOOBAR'
```

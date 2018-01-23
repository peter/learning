# Functions

## Keyword Function Arguments and Default Values

Python:

```python
def foo(a, b, c=3, d=4):
  return [a, b, c, d]

foo(1, 2) # [1, 2, 3, 4]
foo(1, b=2) # [1, 2, 3, 4]
foo(a=1, b=2) # [1, 2, 3, 4]
foo(1, b=2, c=5, d=6) # [1, 2, 5, 6]
```

## Implicit Function Return Values

Ruby: yes, the last evaluated expression is the return value

JavaScript: no, you need an explicit return except in single line lambdas

Python: no, you need an explicit return except in single line lambdas

Clojure: yes, the last evaluated expression is the return value

## Proxying/Wrapping Functions (Forwarding Arguments)

Python:

```python
def proxy_no_args(f):
  def f_proxy(*args, **kwargs):
    print('Before invoking f')
    result = f(*args, **kwargs)
    print('After invoking f')
    return result
  return f_proxy

@proxy_no_args
def foo(a, b=2):
  return [a, b]

foo(1, b=3) # => [1, 3]
```

```python
class ProxyWithConfig(object):
    def __init__(self, *args):
        self.config = list(args)
    def __call__(self, f):
        def proxy(*args, **kwargs):
            return self.config + f(*args, **kwargs)
        return proxy

@ProxyWithConfig(1, 2, 3)
def bar(a, b=2):
  return [a, b]

bar(4, b=5) # => [1, 2, 3, 4, 5]
```

## Anomymous Functions

Python:

```python
foo = lambda n: n*n
foo(3) # => 9
# NOTE: Python lambdas are single line only
```

JavaScript:

```javascript
const foo = (n) => n*n
foo(3)
```

Clojure:

```clojure
(let [foo #(* % %)]
  (foo 3))
; Alternative syntax with argument names
(let [foo (fn [n] (* n n))]
  (foo 3))
```

## Partial Function Application and Currying

Python:

```python
from functools import partial
basetwo = partial(int, base=2)
basetwo('10010')
```

Clojure:

```clojure
(defn add [a b] (+ a b))
(map (partial add 2) [3 5]) ; => [5, 7]
```

JavaScript:

```javascript
function add(a, b) {
  return a + b
}
[3, 5].map(add.bind(null, 2))
```

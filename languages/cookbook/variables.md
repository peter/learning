# Variables and Assignment

## Destructuring Assignments

[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment):

```javascript
const {a, b, ...rest} = {a: 10, b: 20, c: 30, d: 40} // => a=10, b=20, rest={c: 30, d: 40}
const [c, d, ...rest] = [3, 4, 5, 6] // => c=3, d=4, rest=[5, 6]
[a, b] = [b, a] // swap values
```

Python:

```python
n, *numbers = list(map(int, sys.stdin.read().split()))
```

## Initialize Variable with Default if Null

Ruby:

```
my_var ||= 'some-default-value'
```

Python:

```python
my_var = 'some-default-value' if my_var is None else my_var

# Alternative 1:
if my_var is None:
  my_var = 'some-default-value'

# Alternative 2:
my_var = vars().get('my_var', 'some-default-value')

# For dictionaries:
from collections import defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
  d[k].append(v)
```

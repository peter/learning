# Sequences

## Ranges

Python:

```python
for n in range(10):
  print(n)

[n for n in range(10)] # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Get n:th value from list/array or default

Python

```python
my_list = [1, 2, 3]
my_list[3] if len(my_list) > 3 else 'default-value'

def nth(items, index, default=None):
  return items[index] if len(items) > index else default

nth([1, 2, 3], 3) # => None
nth([1, 2, 3], 3, 'default value') # => 'default value'
```

JavaScript:

```javascript
const myList = [1, 2, 3]
myList[3] || 'default-value'
```

Ruby:

```ruby
my_list = [1, 2, 3]
my_list[3] || 'default-value'
```

Clojure:

```clojure
(let [my-list [1, 2, 3]]
  (nth my-list 3 "default-value")) ; => "default-value"
```

## For loop with index

Python:

```python
my_list = [3, 2, 1]
for i, item in enumerate(my_list):
    print(i, item)
```

## Looping Backwards

Python:

```python
colors = ['red', 'green', 'blue']

for color in reversed(colors):
  print(color)
```

## Looping Two Collections

Python:

```python
names = ['foo', 'bar', 'baz']
colors = ['red', 'green', 'blue']

n = min(len(names), len(colors))
for i in range(n):
  print(names[i], '-->', colors[i])

for name, color in zip(names, colors):
  print(name, '-->', color)
```

## Sorting a Collection

Python:

```python
colors = ['red', 'green', 'blue', 'yellow']
sorted(colors) # => ['blue', 'green', 'red', 'yellow']
sorted(colors, key=len) # => ['red', 'blue', 'green', 'yellow']
```

## Slicing a List

Python:

```python
my_list = ['a', 'b', 'c', 'd']
my_list[1:-1]  # => ['b', 'c']
my_list[0:2] = 'z' # replace ['a', 'b'] with ['z']
my_list  # => ['z', 'c', 'd']
```

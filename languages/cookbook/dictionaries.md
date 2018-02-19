# Dictionaries

## Transforming a Dictionary

Python:

```python
my_dict = {'foo': 1, 'bar': 2}
{k: 2*v for k, v in my_dict.items()} # => {'bar': 4, 'foo': 2}
```

## Converting a Dictionary to a Sequence/List

Getting a sequence of key/value tuples from a dictionary.

Python:

```python
my_dict = {'foo': 1, 'bar': 2}
my_dict.items() # => dict_items([('foo', 1), ('bar', 2)])
```

Clojure:

```clojure
(def my-dict {:foo 1 :bar 2})
(seq my-dict) ; => ([:foo 1] [:bar 2])
```

## Merging Dictionaries

Python:

```python
# Does not mutate
def merge(dict1, dict2):
  return dict(dict1.items() + dict2.items())

# Mutates first dict
def merge_mutate(dict1, dict2):
  dict1.update(dict2)
```

## Create a Dictionary from Arrays/Lists

Python:

```python
keys = ['foo', 'bar']
values = [1, 2]
dict(zip(keys, values)) # => {'bar': 2, 'foo': 1}
```

## Looping over a Dictionary

Python:

```python
my_dict = {'foo': 1, 'bar': 2}
for k, v in my_dict.items():
  print(k, v)
```

## Deep Get/Set of Dictionary Values

Python:

```python
import copy

def deep_get(dictionary, keys, default=None):
    if not isinstance(dictionary, dict):
        return default
    path = keys.split('.') if isinstance(keys, str) else keys
    result = dictionary
    def valid_index(key, _list):
        return valid_int(key) and int(key) >= 0
    for key in path:
        if isinstance(result, dict) and key in result:
            result = result[key]
        elif isinstance(result, list) and valid_index(key, result):
            result = result[int(key)] if int(key) < len(result) else None
        elif isinstance(result, list) and len(result) > 0:
            result = list(map(lambda v: v.get(key, None) if isinstance(v, dict) else None,
                              result))
        else:
            result = default
            break
    return copy.deepcopy(result)

def deep_set(dictionary, keys, value):
    if dictionary is None:
        dictionary = {}
    path = keys.split('.')
    result = copy.deepcopy(dictionary)
    nested_dict = result
    for i, key in enumerate(path):
        if i == (len(path) - 1):
            nested_dict[key] = value
        else:
            if not key in nested_dict or not isinstance(nested_dict[key], dict):
                nested_dict[key] = {}
            nested_dict = nested_dict[key]
    return result

def test_deep_get():
    assert deep_get(None, 'foo.bar') is None
    assert deep_get({'foo': 1}, 'foo') == 1
    assert deep_get({'foo': 1}, 'foo.bar.baz') is None
    assert deep_get({'foo': 1}, 'bar') is None
    assert deep_get({'foo': 1}, 'bar', 'default-value') == 'default-value'
    assert deep_get({'foo': {'bar': 1}}, 'foo.bar') == 1
    assert deep_get({'foo': {'bar': 1}}, 'foo.baz') is None

def test_deep_get_array_index():
    assert deep_get({'foo': {'bar': [1]}}, 'foo.bar') == [1]
    assert deep_get({'foo': {'bar': [1]}}, 'foo.bar.0') == 1
    assert deep_get({'foo': {'bar': [1]}}, 'foo.bar.1') is None
    assert deep_get({'foo': {'bar': [{'baz': 1}]}}, 'foo.bar.0.baz') == 1
    assert deep_get({'foo': {'bar': [{'baz': 1}]}}, 'foo.bar.1.baz') is None

def test_deep_get_list_keys():
    assert deep_get({'foo': {'bar': 1}}, ['foo', 'bar']) == 1
    assert deep_get({'foo': {'bar': [1]}}, ['foo', 'bar', '0']) == 1
    assert deep_get({'foo': {'bar': [1]}}, ['foo', 'bar', 0]) == 1

def test_deep_get_array_map():
    assert deep_get({'foo': {'bar': [{'baz': 1}]}}, 'foo.bar') == [{'baz': 1}]
    assert deep_get({'foo': {'bar': [{'baz': 1}]}}, 'foo.bar.baz') == [1]
    assert deep_get({'foo': {'bar': [{'baz': 1}]}}, 'foo.bar.baz.bla') == [None]
    assert deep_get({'foo': {'bar': [1]}}, 'foo.bar.baz') == [None]

def test_deep_set():
    assert deep_set(None, 'foo.bar', 1) == {'foo': {'bar': 1}}
    assert deep_set({}, 'foo.bar', 1) == {'foo': {'bar': 1}}
    assert deep_set({'foo': 2}, 'foo.bar', 1) == {'foo': {'bar': 1}}
    assert deep_set({'foo': {'bar': 2}}, 'foo.bar', 1) == {'foo': {'bar': 1}}
    assert deep_set({'foo': {'bar': 2, 'baz': 1}, 'bla': 0}, 'foo.bar', 1) == {'foo': {'bar': 1, 'baz': 1}, 'bla': 0}
    assert deep_set({'foo': {'bar': 1}}, 'foo.baz', 0) == {'foo': {'bar': 1, 'baz': 0}}
```

# Dictionaries

## Transforming a Dictionary

Python:

```python
my_dict = {'foo': 1, 'bar': 2}
{k: 2*v for k, v in my_dict.items()} # => {'bar': 4, 'foo': 2}
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

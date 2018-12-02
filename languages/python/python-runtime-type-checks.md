# Python Runtime Type Checks

## Python Dependencies

* [Python 3.7.1](https://www.python.org/downloads/release/python-371/)
* iPython for a better REPL - `pip3 install ipython`

## Python Basics: Type Checks

Checking type of built-in types:

```python
type('') is str # => True
type({}) # => dict
type([]) # => list
type(()) # => tuple
(5).__class__ # => int
type(0) is int # => True
type(5.3) # => float
```

Checking type of custom class instances:

```python
class Test1 (object):
  pass
class Test2 (Test1):
  pass
t1 = Test1()
t2 = Test2()

type(t1) is Test1 # => True
type(t1) is Test2 # => False

type(t2) is Test1 # => False
type(t2) is Test2 # => True

isinstance(t2, Test1) # => True
isinstance(t2, Test2) # => True
```

"isinstance() is usually the preferred way to ensure the type of an object because it will also accept derived types. So unless you actually need the type object (for whatever reason), using isinstance() is preferred over type()"

### Python Basics: Truthy/Falsy

The general rule is that `False`, `None`, numerical `0`, and empty collections/sequences (list, str, dict, tuple, set, range etc.) will evaluate as boolean false. In particular, "an object is considered true unless its class defines either a `__bool__()` method that returns False or a `__len__()` method that returns zero".

### Python Basics: Value-Based Equality

"Non-identical instances of a class normally compare as non-equal unless the class defines the __eq__() method."

```python
[1, 2, 3] == [1, 2, 3] # => True
{'foo': 1} == {'foo': 1} # => True
```

## Resources

* [Python Documentation: Built-in Types](https://docs.python.org/3/library/stdtypes.html)
* [Python Documentation: Built-in Functions](https://docs.python.org/3/library/functions.html#repr)

* [Python typing module - Support for type hints](https://docs.python.org/3/library/typing.html)

* [mypy - optional static type checker for Python](http://mypy-lang.org)
* [Carl Meyer - Type-checked Python in the real world - PyCon 2018 (Video)](https://www.youtube.com/watch?v=pMgmKJyWKn8)

* [Python Metaclasses](https://realpython.com/python-metaclasses/)

Runtime type checking libraries:

* [ceronman/typeannotations](https://github.com/ceronman/typeannotations)
* [agronholm/typeguard](https://github.com/agronholm/typeguard)
* [peter/type_spec](https://github.com/peter/type_spec)

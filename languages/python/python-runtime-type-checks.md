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

## Using Python Meta Classes for Custom Type Checks

```python
class PredicateMeta(type):
    """Metaclass for a predicate.
    An object is an instance of a predicate if applying the predicate to the
    object returns True.
    >>> Positive = predicate(lambda x: x > 0)
    >>> isinstance(1, Positive)
    True
    >>> isinstance(0, Positive)
    False
    """
    def __new__(mcls, name, bases, namespace):
        return super().__new__(mcls, name, bases, namespace)

    def __instancecheck__(cls, instance):
        try:
            return cls.__predicate__(instance)
        except AttributeError:
            return False

    def __subclasscheck__(cls, subclass):
        return False


def predicate(function, name=None):
    """Convenience function to create predicates. See PredicateMeta.
    >>> Even = predicate(lambda x: x % 2 == 0)
    >>> isinstance(2, Even)
    True
    >>> isinstance(1, Even)
    False
    """
    name = name or function.__name__
    return PredicateMeta(name, (), {'__predicate__': function})

LargeInt = predicate(lambda v: isinstance(v, int) and v >= 1000)
isinstance(5, LargeInt) # => False
isinstance(1000, LargeInt) # => True
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

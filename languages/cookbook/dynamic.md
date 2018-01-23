# Dynamic Access to Functions/Variables

## Dynamic Function Invocation

Python:

```python
import sys

def current_module():
    return sys.modules[__name__]

def lookup_function(name):
    return getattr(current_module(), name)

def my_function():
  return 'foobar'

lookup_function('my_function')() # => 'foobar'
```

Ruby:

```ruby
def my_function
  'foobar'
end

self.send('my_function') # => 'foobar'
```

## Dynamic Listing of Functions and Variables in Module

Python:

```python
import sys

def current_module():
    return sys.modules[__name__]

dir(current_module())

# Alternative:
import inspect
inspect.getmembers(current_module())
```

* [inspect module](https://docs.python.org/3/library/inspect.html)

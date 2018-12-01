# Learning Python

## What is Python?

* A high-level general-purpose programming language
* Supports multiple paradigms: object-oriented, imperative, functional
* Dynamically typed (interpreted)
* Automatic memory management and comprehensive standard library
* Significant whitespace (indentation)

Python is optimized for programmer productivity, code readability, and software quality.

## Tour

```
which python
python --version
python --help
python -c 'print("hello world")'
```

```python
# This is a comment

"""This is a
   multiline comment"""

print("Hello World")

import csv
from datetime import date, timedelta, datetime

my_int = 5
my_float = 1.23
my_true = True
my_false = False

def foo():
  bar = 12
  return bar

print foo()

# Implicit return value of a function is None

8 / 3 + 2 ** 3 + 3 % 2

if __name__ == '__main__':
    main()

# Unpacking arguments (instead of using apply)
range(3, 6)
args = [3, 6]
range(*args)

# Anonymous functions:
incrementor = lambda x: x + 1
incrementor(1)

# Default Argument Values

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
  # ...

# Keyword Arguments
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
  # ...

# Valid invocations:
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# Invalid invocations:
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument

# Arbitrary Argument Lists
def write_multiple_items(file, separator, *args):
  # ...

# Looping with for
words = ['cat', 'window', 'defenestrate']
for w in words:
  print w, len(w)

# Conditionals
x = int(raw_input("Please enter an integer: "))
if x < 0:
  x = 0
  print 'Negative changed to zero'
elif x == 0:
  print 'Zero'
elif x == 1:
  print 'Single'
else:
  print 'More'

# Use 4-space indentation, and no tabs.

# Name your classes and functions consistently; the convention is to use CamelCase for classes and lower_case_with_underscores for functions and methods. Always use self as the name for the first method argument.

# Sequence Types — str, unicode, list, tuple, bytearray, buffer, xrange

# Set Types — set, frozenset

# Mapping Types — dict
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
a == b == c == d == e

# A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

# Truth Value Testing - the following are considered false:
None
False
0 # zero numeric
'', (), [] # empty sequence
{} # empty mapping
# user defined type that defines __nonzero__() or __len__()

# Boolean Operations — and, or, not

# Single and double quotes are identical when creating strings

# String interpolation?

"my {0} string: {1}".format("cool", "Hello there!")

# Ternary operator
'true' if True else 'false'

# Writing a file
with open("file-path-here", "w") as f:
  f.write("file contents here")

# Reading/slurping a file
open('file-path-here').read()
open('file-path-here').readlines()
with open('x.txt') as x: f = x.read()
with open('x.txt') as x: f = x.readlines()

[x.lower() for x in 'ABC']

import os
_, filename = os.path.split('/home/peter/.ssh/id_rsa.pub')

a, b, *rest = range(5)

# Dict comprehension
{code: country.upper() for country, code in country_code.items() if code < 66}
{v: k for k, v in my_dict.items()}
```

## Built-in Types and type checks

```
isinstance('foo', str)
isinstance(5, int)
isinstance(5.3, float)
isinstance(True, bool)
isinstance([], list)
isinstance((), tuple)
isinstance(set(['foo', 'bar']), set)
isinstance({}, dict)

type(lambda n: n * n) # => <class 'function'>
callable(lambda n: n) # => True
```

## Arithmetic

```python
5 + 2
5 - 2
5 * 2
5 / 2
5 % 2
5 ** 2
5 // 2
```

## Strings

In Python, a string is a sequence of Unicode characters. Strings are immutable.

Strings (str) in Python 3 are unicode encoded (ASCII in Python 2).

String literals can be enclosed by either double or single quotes, although single quotes are more commonly used. Backslash escapes work the usual way within both single and double quoted literals.

A "raw" string literal is prefixed by an 'r' and passes all the chars through without special treatment of backslashes. Important methods on strings:

```
lower
upper
strip
startswith
endswith
find
replace
split
join
```

Using the % operator for interpolation:

```python
text = ("%d little pigs come out or I'll %s and %s and %s" %
         (3, 'huff', 'puff', 'blow down'))
```

## Slicing

All sequence types - list, type, str - support slicing.

The slice arguments are `start:stop:step`.

```
'foobar'[0:2] # => 'fo'
'foobar'[0:100] # => 'foobar'
'foobar'[2:] # => 'obar'
```

Using step:

```
'foobar'[::3] # => 'fb' (every third item)
'foobar'[3:1:-1] # => 'bo'
```

Delete/replace with slicing (does not work with strings):

```
del s[5:7] # => delete slice
s[3:2] = [11, 12] # => replace slice
```

## String interpolation

```python
print("My name is %s and I'm %s years old" % ('Joe', 5))
```

## Lists

```python
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
first = grocery_list[0]
grocery_list[0] = 'Green Juice'
grocery_list[0:3] # Slicing
grocery_list.append('Onions') # mutates grocery_list
# Other methods: insert, remove, sort, reverse
grocery_list + ['More food'] # concat
[0] * 5 # => [0, 0, 0, 0, 0]
len([1, 2]) # => 2

# Indexing: start (inclusive), end (exlusive), step length
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list[4] # => 4
my_list[4:7] # => [4, 5, 6]
my_list[0::3] # => [0, 3, 6, 9]
my_list[-1] # => 9
my_list[::-1] # => reverse
my_list[3:1:-1] # => [3, 2]
```

```python
tup = ('foo', 'bar', 'baz')
b_list = list(tup)
b_list[1] = 'peekaboo'
b_list.append('dwarf')
b_list.insert(1, 'red')
b_list.pop(2) # => 'peekaboo' - inverse of insert
b_list.remove('foo') # => removes first occurence
'dwarf' in b_list # => True
```
In place concatenation without creating new list is done with `extend()`

Sorting:

```python
a = [7, 2, 5, 1, 3]
a.sort()
b = ['saw', 'small', 'He', 'foxes', 'six']
b.sort(key=len) # => in place sort by function
sorted(b, key=len) # => creates new list
```

Reverse:

```python
list(reversed(b))
```

The built-in bisect module implements binary-search and insertion into a sorted list.
bisect.bisect finds the location where an element should be inserted to keep it sorted,
while bisect.insort actually inserts the element into that location:

## Tuples

Tuples are enclosed in parentheses and are immutable and fixed length.

```python
# literal
pi_tuple = (3,1,4,1,5,9)

# convert between list and tuple
list(pi_tuple)
tuple(list(pi_tuple))

# length
len(pi_tuple)

# min/max
min(pi_tuple)
max(pi_tuple)
```

Unpacking tuples:

```python
tup = (4, 5, 6)
a, b, c = tup

tup = 4, 5, (6, 7)
a, b, (c, d) = tup

seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
  pass
```

Tuple `count()`:

```
(1, 2, 2, 2, 3, 4, 2).count(2) # => 4
```

## Set

```python
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}

a | b # union (or)
a & b # intersection (and)
a - b # difference
a ^ b # symmetric difference (xor)

a_set = {1, 2, 3, 4, 5}
{1, 2, 3}.issubset(a_set) # => True
a_set.issuperset({1, 2, 3}) # => True
```

Set methods: add, remove, union, intersection, difference, symmetric_difference, issubset, issuperset, isdisjoint.

## Dictionaries

```python
# literal
my_dict = {'foo': 1, 'bar': 2}

# get
my_dict['foo']

# get with default
my_dict.get('bla', 'default value')

# set
my_dict['foo'] = 3

# length
len(my_dict)

d1 = {'a' : 'some value', 'b' : [1, 2, 3, 4]}
d1[7] = 'an integer'
d1['b']
'b' in d1 # => True

d1[5] = 'some value'
d1['dummy'] = 'another value'
del d1[5]
ret = d1.pop('dummy') # => 'another value'

d1.keys()
d1.values()

d1.update({'b' : 'foo', 'c' : 12}) # Merge
```

Creating dicts from sequences

```python
mapping = {}
for key, value in zip(key_list, value_list):
  mapping[key] = value

# dict type function accepts a list of 2-tuples:
mapping = dict(zip(range(5), reversed(range(5)))) # => {0: 4, 1: 3, 2: 2, 3: 1, 4: 0}
```

Dicts with default values

```python
from collections import defaultdict
by_letter = defaultdict(list)
for word in words:
  by_letter[word[0]].append(word)

counts = defaultdict(lambda: 4)
```

While the values of a dict can be any Python object, the keys have to be immutable
objects like scalar types (int, float, string) or tuples (all the objects in the tuple need to
be immutable, too). The technical term here is hashability. You can check whether an
object is hashable (can be used as a key in a dict) with the `hash` function

## Equality

```python
[1, 2, 3] == [1, 2, 3] # => True
{'foo': 1} == {'foo': 1} # => True
a = [1, 2, 3]
b = [1, 2, 3]
a is b # => False
a is not b # => True
c = None
c == None # => True
c is None # => True
```

## Mutability

Most objects in Python are mutable (lists, dicts, NumPy arrays, class instances).
The main exceptions are strings and tuples that are immutable.

## Type Casting

```python
str(5)
bool(5)
int('5')
int(5.3) # => 5
float('7')
float('7asdf') # => ValueError
```

## Conditionals and Boolean operators

```python
age = 21

if age >= 21:
  print('Old enough to drive trailer')
elif age >= 16:
  print('Old enough to drive car')
else:
  print('Not old enough to drive')

# boolean operators: and, or, not
if (age > 16 and not(age > 21)):
  print('between 16 and 21')
```

## Looping

```python
for x in range(0, 10):
  print(x)

import random
random_num = random.randrange(0, 100)
while(random_num != 15):
  print(random_num)
  random_num = random.randrange(0, 100)
```

## List Comprehensions

Basic form:

```
[expr for val in collection if condition]
```

```python
[x**2 for x in range(10)]
```

Imperative building of a list in a range:

```python
my_list = []
for number in range(0, 1000):
  if number % 2 == 0:
    my_list.append(number)
```

Equivalent list comprehension:

```
my_list = [number for number in range(0, 1000) if number % 2 == 0]
```

Listcomps can generate lists from the cartesian product of two or more iterables:

```python
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
```

```python
def top_counts(count_dict, n=10):
  value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
  value_key_pairs.sort()
  return value_key_pairs[-n:]

from collections import Counter
counts = Counter(time_zones)
counts.most_common(10)
```

## Dates and times

The built-in Python datetime module provides datetime, date, and time types. The
datetime type as you may imagine combines the information stored in date and time
and is the most commonly used:

```python
from datetime import datetime, date, time

dt = datetime(2011, 10, 29, 20, 30, 21)
dt.day
dt.minute
```

Given a datetime instance, you can extract the equivalent date and time objects by
calling the `date()` and `time()` methods on the datetime object.

Formatting, parsing, replacing, and deltas:

```python
dt.strftime('%m/%d/%Y %H:%M')
datetime.strptime('20091031', '%Y%m%d')
dt.replace(minute=0, second=0)
dt2 = datetime(2011, 11, 15, 22, 30)
delta = dt2 - dt
dt + delta
```

## Exception Handling


```python
def attempt_float(x):
  try:
    return float(x)
  except (TypeError, ValueError):
    return x

f = open(path, 'w')
try:
  write_to_file(f)
except:
  print 'Failed'
else:
  print 'Succeeded'
finally:
  f.close()
```

## Ternary Expressions

```python
'Non-negative' if x >= 0 else 'Negative'
```

## Functions

Multiple return values:

```python
def f():
  a = 5
  b = 6
  c = 7
  return a, b, c

a, b, c = f()
return_value = f() # => 3 tuple
```

Functions as objects:

```python
import re
def remove_punctuation(value):
  return re.sub('[!#?]', '', value)

clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops):
  result = []
  for value in strings:
    for function in ops:
      value = function(value)
      result.append(value)
  return result
```

Compose functions:

```python
import functools
def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

clean = compose(*list(reversed(clean_ops)))
clean(' foo.bar ') # => 'Foo.Bar'
```

Lambdas:

```python
def apply_to_list(some_list, f):
  return [f(x) for x in some_list]

ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2)
```

Closures:

```python
def make_closure(a):
  def closure():
    print('I know the secret: %d' % a)
  return closure

closure = make_closure(5)
closure() # => I know the secret: 5
```

However, one technical limitation to keep in mind is that while you can mutate any
internal state objects (like adding key-value pairs to a dict), you cannot bind variables
in the enclosing function scope. One way to work around this is to modify a dict or list
rather than binding variables:

```python
def make_counter():
  count = [0]
  def counter():
    count[0] += 1
    return count[0]
  return counter

counter = make_counter()
counter() # => 1
counter() # => 2
counter() # => 3 ...
```

Dynamic argument handling, variable length argument lists, keyword args:

```python
def say_hello_then_call_f(f, *args, **kwargs):
  print('args is', args)
  print('kwargs is', kwargs)
  print("Hello! Now I'm going to call %s" % f)
  return f(*args, **kwargs)

def g(x, y, z=1):
  return (x + y) / z

say_hello_then_call_f(g, 1, 2, z=5.)
# args is (1, 2)
# kwargs is {'z': 5.0}
# Hello! Now I'm going to call <function g at 0x10bdd6bf8>
# 0.6
```

Partial application:

```python
def add_numbers(x, y):
  return x + y

from functools import partial
add_five = partial(add_numbers, 5)
```

## Named Tuples (Structs)

```python
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])
card = Card('7', 'diamonds')
card == Card(rank='7', suit='diamonds')
```

## Python Data Model (dunder methods)

```python
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
len(deck)
deck[:3]
Card('Q', 'hearts') in deck
for card in deck:
  print(card)
for card in reversed(deck):
  print(card)
for n, card in enumerate(deck, 1):
  print(n, card)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
   rank_value = FrenchDeck.ranks.index(card.rank)
   return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
   print(card)
```

Useful dunder methods:

* __repr__ - string representation
* __eq__
* __setitem__
* __contains__
* __add__/__sub__/__mul__/__truediv__
* __bool__ - called by `bool()`. If not defined and `__len__` is non-zero then object is considered true.
* __hash__ - should return integer. Objects which compare equal should have same value. Suggestion - hash a tuple (see below).
* __call__

```python
def __hash__(self):
    return hash((self.name, self.nick, self.color))
```

## Sequences

* Container sequences: `list`, `tuple`, `collections.deque`
* Flat sequences: `str`, `bytes`, `bytearray`, `memoryview`, `array.array`

Immutable sequences: `tuple`, `str`, `bytes`

## Plotting

From [Pyplot tutorial](https://matplotlib.org/xkcd/users/pyplot_tutorial.html):

```python
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0., 5., 0.2) # time at 200ms intervals
plt.plot(t, t, 'r--', # red dashes
         t, t**2, 'bs', # blue squares
         t, t**3, 'g^') # green triangles
plt.show()

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211) # two rows, one column, figure 1
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212) # two rows, one column, figure 2
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
```

## Pandas

```python
import json
path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]

from pandas import DataFrame, Series
import pandas as pd
frame = DataFrame(records)
frame['tz'][:10]
frame['tz'].value_counts()
clean_tz = frame['tz'].fillna('Missing')
tz_counts[:10].plot(kind='barh', rot=0)
```

## Regular Expressions

[Regular expressions API doc](https://docs.python.org/2/library/re.html)

For regular expressions you typically use Python’s raw string notation with
an r prefix:

```python
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
re.match(r'[a-z]{2}', 'foobar')
```

## Decorators

A [decorator](http://www.artima.com/weblogs/viewpost.jsp?thread=240845) for type checks
(see the [type_spec library](https://github.com/peter/type_spec) for more):

```python
def Maybe(required_type):
  def type_check(v):
    if v == None:
      return None
    else:
      return required_type(v)
  return type_check

def AnyOf(*allowed_types):
  def type_check(v):
    for allowed_type in allowed_types:
      result = type_check_value(v, allowed_type)
      if result == None:
        return result
    return 'must be one of these types: {}'.format(', '.join(map(str, allowed_types)))
  return type_check

def AllOf(*required_types):
  def type_check(v):
    for required_type in required_types:
      result = type_check_value(v, required_type)
      if result != None:
        return result
  return type_check

def Positive(v):
  if v <= 0:
    return 'must be positive'

def Number(v):
  if isinstance(v, int) or isinstance(v, float):
    return None
  else:
    return 'Must be number (int or float)'

class MyNumber:
  def __init__(self, n):
    self.n = n
  def __add__(self, other):
    return MyNumber(self.n + other.n)
  def typeCheck(my_number):
    return Number(my_number.n)

class SafeNumber:
  def __init__(self, n):
    self.n = n
    assert_type(n, Number)
  def __add__(self, other):
    return SafeNumber(self.n + other.n)

def type_check_value(v, required_type):
  def check_callable(v, callable_type):
    result = callable_type(v)
    error_message = 'invalid (returned False)' if result == False else result
    if result != True and error_message:
      return error_message
  if type(required_type) == type:
    callable_type = getattr(required_type, 'typeCheck', None)
    if not isinstance(v, required_type):
      return 'needs to be of type {}'.format(required_type)
    elif callable_type:
      return check_callable(v, callable_type)
  else:
    return check_callable(v, required_type)

def assert_type(v, required_type, message = ''):
  error_message = type_check_value(v, required_type)
  if error_message:
    raise ValueError(message + error_message)

class typeCheck(object):
  def __init__(self, *signature):
    if len(signature) < 1:
      raise ValueError('Signature is empty')
    self.arg_types = signature[:-1]
    self.return_type = signature[-1]

  def __call__(self, f):
    def with_type_check(*args, **kwargs):
      for i, arg in enumerate(args):
        assert_type(arg, self.arg_types[i], message='typeCheck: arg {} with value {} of type {} - '.format(i, arg, type(arg)))
      result = f(*args, **kwargs)
      assert_type(result, self.return_type, message='typeCheck: return type with value {} of type {} - '.format(result, type(result)))
      return result
    return with_type_check

@typeCheck(int, int, int)
def add_ints(a, b):
  return a + b

@typeCheck(Number, lambda n: n > 0, Number)
def div_numbers(a, b):
  return a / b

@typeCheck(Number, AllOf(Number, Positive), Number)
def div_numbers2(a, b):
  return a / b

@typeCheck(Number, Number, Number)
def add(a, b):
  return a + b

@typeCheck(AnyOf(int, float), AnyOf(int, float), AnyOf(int, float))
def add2(a, b):
  return a + b

@typeCheck(int, int, int)
def faulty_add_ints(a, b):
  return 'foobar'

@typeCheck(MyNumber, MyNumber, int)
def add_my_numbers(a, b):
  return (a + b).n
add_my_numbers(MyNumber(5), MyNumber(5)) # => 10

number = MyNumber('foobar')
MyNumber.typeCheck(number) # => 'Must be number (int or float)'

@typeCheck(SafeNumber, SafeNumber, int)
def add_safe_numbers(a, b):
  return (a + b).n
add_safe_numbers(SafeNumber(5), SafeNumber(5)) # => 10
```

## Resources: General

* [Python Tutorial](https://docs.python.org/3.6/tutorial)
* [Python.org](https://www.python.org)
* [Python on Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language))
* [Built-in Functions](https://docs.python.org/3/library/functions.html)
* [Built-in Types](https://docs.python.org/3/library/stdtypes.html)
* [Python Course on Codecademy](https://www.codecademy.com/learn/python)
* [Python for JavaScript Programmers](http://hg.toolness.com/python-for-js-programmers/raw-file/tip/PythonForJsProgrammers.html)
* [Video: Python Programming (Derek Banas)](https://www.youtube.com/watch?v=N4mEzFDjqtA&t=1831s)
* [Video: What Does It Take To Be An Expert At Python?](https://www.youtube.com/watch?v=7lmCu8wz8ro&feature=youtu.be)
* [Underscores in Python](https://shahriar.svbtle.com/underscores-in-python)
* [Python data model (dunder methods)](https://docs.python.org/3.6/reference/datamodel.html)
* [10 Basic Python Examples](https://www.makeuseof.com/tag/basic-python-examples-learn-fast)
* [Replacing Bash with Python](https://medium.com/capital-one-tech/bashing-the-bash-replacing-shell-scripts-with-python-d8d201bc0989)

## Style and Idioms

* [Transforming Code into Beautiful, Idiomatic Python - Raymond Hettinger](https://www.youtube.com/watch?v=OSGv2VnC0go&feature=youtu.be)
* [Raymond Hettinger - Beyond PEP 8 -- Best practices for beautiful intelligible code - PyCon 2015 - Raymond Hettinger](https://www.youtube.com/watch?v=wf-BqAjZb8M&feature=youtu.be)

## Python 2 vs Python 3

* [Porting Code to Python 3 with 2to3](http://www.diveintopython3.net/porting-code-to-python-3-with-2to3.html)

## Resources: Books

* [Learning Python](http://shop.oreilly.com/product/0636920028154.do)
* [Programming Python](http://shop.oreilly.com/product/9780596158118.do)
* [Fluent Python](https://www.amazon.com/Fluent-Python-Concise-Effective-Programming/dp/1491946008)
* [Effective Python](https://www.amazon.com/Effective-Python-Specific-Software-Development/dp/0134034287)
* [Python Cookbook](https://www.amazon.com/Python-Cookbook-Third-David-Beazley/dp/1449340377)

## Resources: Example Code

* [Code for Fluent Python Book](https://github.com/fluentpython/example-code)
* [Code for Python Cookbook](https://github.com/dabeaz/python-cookbook)
* [realpython/python-scripts](https://github.com/realpython/python-scripts/tree/master/scripts)

## Resources: Functional Programming

* [A practical introduction to functional programming](https://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming)

## Resources: Fundamentals

* [Single Quotes vs Double Quotes](http://stackoverflow.com/questions/56011/single-quotes-vs-double-quotes-in-python)
* [Reserved Words](https://docs.python.org/2.5/ref/keywords.html)
* [Assignments in Conditionals](http://stackoverflow.com/questions/2603956/can-we-have-assignment-in-a-condition)

## Resources: Modules

* [How to import other Python files](http://stackoverflow.com/questions/2349991/python-how-to-import-other-python-files)
* [Modules and Packages](http://www.learnpython.org/en/Modules_and_Packages)
* [Project Structure](http://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application)

## Resources: Testing

* [pytest](http://pytest.org/latest/getting-started.html)
* [Testing Your Code](http://docs.python-guide.org/en/latest/writing/tests)
* [unittest](https://docs.python.org/2/library/unittest.html)
* [Testing Command Line Argument Parsing](http://stackoverflow.com/questions/18160078/how-do-you-write-tests-for-the-argparse-portion-of-a-python-module)
* [pylint](http://www.pylint.org)
* [pyflakes](https://github.com/megies/pyflakes)

## Resources: Courses and Learning

* [Codecademy Course](https://www.codecademy.com/learn/python)
* [learnpython.org](https://www.learnpython.org)
* [Google Python Class](https://developers.google.com/edu/python)

## Resources: Style/Idioms/Conventions

* [Official Coding Conventions](https://www.python.org/dev/peps/pep-0008/)
* [Code Style](http://docs.python-guide.org/en/latest/writing/style/)

## Resources: Web

* [Book: Flask Web Development](http://shop.oreilly.com/product/0636920031116.do)
* [Library: Flask SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/)

## Resources: Databases

* [Library: psycopg PostgreSQL driver](http://initd.org/psycopg)

## Resources: Serialization

* [JSON](http://python-guide-pt-br.readthedocs.io/en/latest/scenarios/json)

## Resources: Deployment

* [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
* [Flask Heroku Template](https://github.com/zachwill/flask_heroku)
* [Powerful Python One-Liners](https://wiki.python.org/moin/Powerful%20Python%20One-Liners)

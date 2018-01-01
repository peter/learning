# Week 1 - Python Fundamentals

## Introduction

"In this specialization, we're focused on teaching applied skills using the Python programming language"

"Python is now the language of choice for introducing university students to programming. It's used in eight out of 10 of the US's top computer science programs"

"Python has a significant set of data science libraries one can use. The base of these is called the SciPy Ecosystem"

* Jupiter Notebooks
* Pandas
* Matplotlib

"...provide an excellent basis for moving into machine learning, text mining and network analysis."

## Data Science

Data Science as a term started to establish in 2004. People usually think of companies as Facebook and Google when they think of Data Science. But it's used much more broadly.

Data science is at the intersection of computer science, statistics, and artificial intelligence.

* Data exploration
* Computation and modeling
* Visualization

Making predictions.

Inference - a conclusion reached on the basis of evidence and reasoning.

## Coursera Jupyter Notebook

Service integrated with Coursera

"Notebook documents are both human-readable documents containing the analysis description and the results (figures, tables, etc..) as well as executable documents which can be run to perform data analysis."

Notebook uses ipython to execute Python code. IPython is a powerful interactive python shell (REPL).

## Python Introduction

Functions:

```python
def add_numbers(x, y):
  return x + y

add_numbers(2, 3) # => 5
```

Optional parameters come last:

```python
def add_numbers(x, y, z=None):
  if (z == None):
    return x + y
  else:
    return x + y + z
add_numbers(2, 3)
add_numbers(2, 3, 4)
add_numbers(2, 3, z=4) # => 9
add_numbers(x=2, y=3, z=4) # => 9
```

Type checking:

```python
type('This is a string')
type('foobar') is str # => true
isinstance('foobar', str) # => true
type(None)
type(1)
type(1.0) # => float
type(add_numbers) # => function
from types import FunctionType
type(add_numbers) == FunctionType # => true
add_numbers.__class__ # => function
type(add_numbers.__class__) # => type
```

Lists:

```python
my_list = [1, 'a', 2, 'b']
len(my_list) # => 4
my_list[0] # => 1
my_list[0:2] # => [1, 'a']
my_list.append('foo') # => in place appending
for item in my_list:
  print(item)
[1, 2] + [3, 4] # => [1, 2, 3, 4]
1 in [1, 2, 3] # => True (set membership)
```

Tuples, unlike lists, are immutable:

```python
my_tuple = (1, 'a', 2, 'b')
my_tuple[0] # => 1
for item in my_tuple:
  print(item)

# convert between list and tuple
list(my_tuple)
tuple(list(my_tuple))

# length
len(my_tuple)

# min/max
min(my_tuple)
max(my_tuple)
```

Strings:

```python
my_str = 'This is a string'
'foo' + 'bar' # => 'foobar'
my_str[0] # => 'T'
my_str[-1] # => 'g'
my_str[-4:-2] # => 'ri'
my_str[2:] # => 'is is a string'
's' in my_str # => True
for c in my_str:
  print(c)
','.join('foo bar'.split(' '))
```

Dictionaries:

```python
my_dict = {'foo': 1, 'bar': 2}
type(my_dict) # => dict
my_dict['foo'] # => 1
my_dict['bla'] # => KeyError
'foo' in my_dict # => True
'bla' in my_dict # => False
```

CSV:

```python
import csv

%precision 2
with open('foo.csv') as csvfile:
  data = list(csv.DictReader(csvfile))
data[:3]
len(data)
data[0].keys()
mean_cty = sum(float(d['cty']) for d in data) / len(data)
set(d['cyl'] for d in data) # Unique/distinct set
```

Dates and time:

```python
import datetime as dt
import time as tm
tm.time()
dtnow = dt.datetime.fromtimestamp(tm.time())
dtnow_parts = [dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second]
today = dt.date.today()
delta = dt.timedelta(days = 100)
today - delta
today > today - delta # => True
```

Classes:

```python
class Person:
  department = 'School of information'

  def foobar():
    return 'this if foobar'

  def set_name(self, new_name):
    self.name = new_name
  def set_location(self, new_location):
    self.location = new_location

Person.department
Person.foobar() # => 'this is foobar'
```

map, filter, reduce:

```python
foo = [1, 8, 3]
bar = [5, 6, 7]
map(min, foo, bar) # => <map at 0x10698e160>
list(map(min, foo, bar)) # => [1, 6, 3]

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
```

## Numpy

The Numpy library lets us work efficiently with arrays and matrices.

NumPy’s main object is the homogeneous multidimensional array.

Numpy has "support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays"

"The Python programming language was not initially designed for numerical computing, but attracted the attention of the scientific/engineering community early on, so that a special interest group called matrix-sig was founded in 1995 with the aim of defining an array computing package. Among its members was Python designer/maintainer Guido van Rossum, who implemented extensions to Python's syntax (in particular the indexing syntax) to make array computing easier"

"Algorithms that are not expressible as a vectorized operation will typically run slowly because they must be implemented in "pure Python", while vectorization may increase memory complexity of some operations from constant to linear, because temporary arrays must be created that are as large as the inputs"

```python
import numpy as np
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
m = np.array([[7, 8, 9], [10, 11, 12]])
m.shape
n = np.arange(0, 30, 2) # range from 0 to 30 with step 2
n.reshape(3, 5) # reshape range to a 3 row, 5 column two dimensional array
o = np.linspace(0, 4, 9) # arrange 9 numbers evenly in range 0-4
o.resize(3, 3) # in place edit
np.ones((3, 2))
np.zeros((2, 3))
np.eye(3)
np.diag(y)
np.array([1, 2, 3, 4] * 3) # repeat
np.repeat([1, 2, 3, 4], 3)
np.ones([2, 3], int)
z = np.array([y, y**2])
x + y
x - y
x * y
x.dot(y)
x.T.shape # transpose
z.dtype
x.sum()
x.max()
x.min()
x.mean()
x.std()
x.argmax() # index of max
x.argmin() # index of min
s = np.arange(13)**2
s[0], s[4], s[0:3]
s[2::2] # start:end:step
s[-5::-2]
r = np.arange(36)
r.resize(6, 6)
r[2, 2]
r[3, 3:6] # third row, columns 3-6
r[r > 30]
r[r > 30] = 30
r2 = r[:3,:3] # a slice, not a copy!
r2[:] = 0
r2 = r.copy()[:3,:3]
test = np.random.randint(0, 10, (4, 3)) # matrix with random numbers
for row in test:
  print(row)
for i, row in enumerate(test):
  print(i, row)
test2 = test**2
for i, j in zip(test, test2):
  print(i, '+', j, '=', i + j)

a = np.array([[1, 2, 3], [3, 4, 6.7], [5, 9.0, 5]])
a.transpose()
b =  np.array([3, 2, 1])
from numpy.linalg import solve
solve(a, b)  # solve the equation ax = b
c = rand(3, 3) * 20  # create a 3x3 random matrix of values within [0,1] scaled by 20
```

Iterable means implementing the `__iter__` method:

```python
def isiterable(obj):
  try:
    iter(obj)
    return True
  except TypeError: # not iterable
    return False

isiterable('a string')
isiterable([1, 2, 3])
isiterable(5) # => False
```

Naming imports:

```python
import some_module as sm
from some_module import PI as pi, g as gf
```

## Resources

* [Numpy: The N-dimensional array](https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.ndarray.html)
* [Numpy Quickstart](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html)
* [Numpy on Wikipedia](https://en.wikipedia.org/wiki/NumPy)

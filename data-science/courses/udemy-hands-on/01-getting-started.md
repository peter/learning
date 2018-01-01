# Section 1 - Getting Started

## Pandas Introduction

Pandas is a Python library that makes handling tabular data easier.

Usually you'll encounter "NumPy arrays", which are multi-dimensional array objects. It is easy to create a Pandas DataFrame from a NumPy array, and Pandas DataFrames can be cast as NumPy arrays. NumPy arrays are mainly important because of...

The machine learning library we'll use throughout this course is scikit_learn, or sklearn, and it generally takes NumPy arrays as its input.
So, a typical thing to do is to load, clean, and manipulate your input data using Pandas. Then convert your Pandas DataFrame into a NumPy array as it's being passed into some Scikit_Learn function. That conversion can often happen automatically.

The two main data types in pandas are Series and DataFrame.

```python
%matplotlib inline
import numpy as np
import pandas as pd

df = pd.read_csv('PastHires.csv')
df.head()
df.tail(4)
df.shape
df.size
len(df)
df.columns
df['Hired']
df.index
df['Hired'][:5] # Column and row range (0-4)
df['Hired'][5] # Single cell in column at certain row index
df[['Years Experience', 'Hired']] # multiple columns
df.sort_values(['Years Experience'])
degree_counts = df['Level of Education'].value_counts() # counts for each unique value (Series)
degree_counts.plot(kind='bar')
```

In order to do plotting with matplotlib in the ipython console, issue `%pylab` first, example:

```
%pylab
x = randn(10000)
hist(x, 100)
```

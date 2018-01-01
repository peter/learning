# Week 2 - Basic Data Processing with Pandas

## Introduction

Pandas is a library created in 2008 by Wes McKinney.

"Flexible and powerful data analysis / manipulation library for Python, providing labeled data structures similar to R data.frame objects, statistical functions, and much more"

"pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python. Additionally, it has the broader goal of becoming the most powerful and flexible open source data analysis / manipulation tool available in any language. It is already well on its way toward this goal."

Pandas is built on top of NumPy.

```
from pandas import Series, DataFrame
import pandas as pd
```

"To get started with pandas, you will need to get comfortable with its two workhorse data structures: Series and DataFrame"

## Series Data Structure

The series is one of the core data structures in pandas. You think of it a cross between a list and a dictionary. The items are all stored in an order and there's labels with which you can retrieve them.

```python
import pandas as pd
import numpy as np

pd.Series?
```

```
pd.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False
```

"One-dimensional ndarray with axis labels (including time series).""

"The object
supports both integer- and label-based indexing and provides a host of
methods for performing operations involving the index. Statistical
methods from ndarray have been overridden to automatically exclude
missing data (currently represented as NaN).

Operations between Series (+, -, /, *, **) align values based on their
associated index values-- they need not be the same length. The result
index will be the sorted union of the two indexes."

```python
pd.Series(['Tiger', 'Bear', 'Moose']) # => dtype: object, 0, 1, 2
pd.Series(['Tiger', 'Bear', None]) # => dtype: object

pd.Series([1, 2, 3]) # => dtype: int64
pd.Series([1, 2, None]) # => dtype: float64, NaN for None

np.isnan(np.nan) # => True

s = pd.Series({'foo1': 'bar1', 'foo2': 'bar2'}) # => dtype: object
s.index # => Index(['foo1', 'foo2'], dtype='object')
s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
s.values # => array(['Tiger', 'Bear', 'Moose'], dtype=object)
```

## Querying a Series

```python
s = pd.Series({'foo1': 'bar1', 'foo2': 'bar2'})
s.iloc[0]
s.loc['foo1']
s[0]
s['foo1']

s = pd.Series([100, 120, 101, 3])

total = 0
for item in s:
  total += item
print(total)

# => Vectorized, faster than loop
total = np.sum(s)
s.sum()

s = pd.Series(np.random.randint(0, 1000, 10000))
s.head()
len(s)

import timeit
timeit.timeit('np.sum(s)', setup='import numpy as np; import pandas as pd; s = pd.Series(np.random.randint(0, 1000, 10000)', number=100)
```

From the command line:

```
python -m timeit -n 100 my-program.py
```

In Jupyter:

```
%%timeit -n 10
```

```python
for label, value in s.iteritems():
  s.set_value(label, value + 2)
  # s.loc[label] = value + 2
s.head()

# More efficient:
s += 2

s = pd.Series([1, 2, 3])
s.loc['Animal'] = 'Bears'
s # => dtype: object
```

## The DataFrame Data Structure

```python
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

df.loc['Store 1']
df.loc['Store 2']
df['Item Purchased']
df.loc['Store 1', 'Cost']
df.loc['Store 1', 'Cost'].sum()

df.T

df.loc['Store 1']['Cost'] # => chaining will copy rather than create view

df.loc[:, ['Name', 'Cost']] # => Name and Cost for all stores

df.drop('Store 1') # => delete all 'Store 1' index data, returns a new copy
copy_df = df.copy()

copy_df.drop?

del copy_df['Name']

df['Location'] = None
```

## DataFrame Indexing and Loading

The common work flow is to read your data into a DataFrame then reduce this DataFrame to the particular columns or rows that you're interested in working with.

```python
costs = df['Cost']
type(costs) # =>  pandas.core.series.Series

costs += 2 # Watch out, this mutates the original dataframe

costs
```

```python
import pandas as pd
import numpy as np

df = pd.read_csv('data-files/olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()

# First country
df.iloc[0]
```


## Querying a DataFrame

Before we talk about how to query data frames, we need to talk about Boolean masking. Boolean masking is the heart of fast and efficient querying in NumPy. It's analogous a bit to masking used in other computational areas.

A Boolean mask is an array which can be of one dimension like a series, or two dimensions like a data frame, where each of the values in the array are either true or false. This array is essentially overlaid on top of the data structure that we're querying. And any cell aligned with the true value will be admitted into our final result, and any sign aligned with a false value will not.

Boolean masking is powerful conceptually and is the cornerstone of efficient NumPy and pandas querying.

```python
df['Gold'] > 0 # => builds the boolean mask with True/False values
only_gold = df.where(df['Gold'] > 0)
only_gold['Gold'].count() # => 100
df['Gold'].count() # => 147
only_gold = only_gold.dropna()

only_gold = df[df['Gold'] > 0]

# chaining:
df[(df['Gold'] > 0) | df['Gold.1'] > 0] # or
df[(df['Gold.1'] > 0) & df['Gold'] == 0] # and
```

Most statistical functions ignore NaN values.

Boolean masks can be chained together.


```python
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

# Names of people with cost greater than 3
df['Name'][df['Cost']>3]

type(df['Name']) # => Series
type(df['Cost']>3) # => Series

df.describe()
df.describe?
df.describe(include='all')
```

## Indexing Dataframes

```python
type(df.index) # => Index
df['country'] = df.index
df.set_index('Gold')

df = df.reset_index() # => Creates default numbered index
```

Multi level index (like composite keys in a database).

Census has summarized levels for country, for county, and for state.

```python
df = pd.read_csv('data-files/census.csv')
df.columns
len(df)
df.describe()
df['SUMLEV'].unique() # => 40, 50
df = df[df['SUMLEV'] == 50]
df.head()
columns_to_keep = ['STNAME', 'CTYNAME', 'BIRTHS2010']
df = df[columns_to_keep]
df.head()
df = df.set_index(['STNAME', 'CTYNAME'])
df.loc['Michigan', 'Washtenaw County']
df.loc[ [('Michigan', 'Washtenaw County'), ('Michigan', 'Wayne County')]]
```

## Missing Values

User video playback log, not sorted by time/user and with lots of NaN:

```python
df = pd.read_csv('data-files/log.csv')
df.fillna?
# method ffill - forward filling (requires sorting!)
# df.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, **kwargs)

df = df.set_index('time')
df = df.sort_index()

df = df.reset_index()
df = df.set_index(['time', 'user'])
df = df.sort_index()
```

Many statistical functions will ignore missing values.

## Assignment 2 - Pandas Introduction

https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table


## Resources

* [Github/pandas](https://github.com/pandas-dev/pandas)
* [Pandas Documentation](http://pandas.pydata.org/pandas-docs/stable)
* [10 Minutes to Pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html)
* [Pandas API Reference](https://pandas.pydata.org/pandas-docs/stable/api.html)
* [DataFrame doc](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html)
* [Python for Data Analysis (Book)](http://shop.oreilly.com/product/0636920023784.do)
* [Learning the Pandas Library (Book)](https://www.amazon.com/Learning-Pandas-Library-Munging-Analysis/dp/153359824X)

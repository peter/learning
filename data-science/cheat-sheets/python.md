# Python Cheat Sheet

## Pandas - Selecting/Slicing/Dropping/Changing Rows and Columns By Name and Index

Columns:

```python
# Column single name
df['MyColumn']

# Extracting just the values of the column
df['MyColumn'].values

# Columns by multiple names
df[['MyColumn1', 'MyColumns2']]

# All rows for the first 10 columns
df[:, 0:10]

# First column
df.iloc[:,0]

# First column value counts
iloc[:,0].value_counts()

# All columns starting with the second column
df.iloc[:,1:]
```

Example test/train split where the classifier is in the last column:

```
from sklearn.model_selection import train_test_split
df = pd.read_csv('fraud_data.csv')
X = df.iloc[:,:-1]
y = df.iloc[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```

Rows:

```python
df.head()

# last three rows
df.tail(3)

# First row
df[0]

# First three rows
df[0:3]

# All rows except the last
df[:-1]
```

```
# drop a row by name
df.drop(['Willard Morris', 'Spencer McDaniel'])

# drop a row by number
df.drop(df.index[0], inplace=True)

# drop first 2 rows (put ':' to left of # to drop last X rows)
df.drop(df.index[:2], inplace=True)

# dropping columns by name
df.drop(['age'], axis = 1, inplace = True)

# Drop rows where there are NaN values in certain column
df.dropna(subset=['columnName'])
```

```
# Show/list datatypes
df.dtypes

# Stats - count/mean/std/min/max/percentiles for numeric columns only
df.describe()

# Change data type (dtype) of a column
df['columnName'].astype('category')

# Change all object datatypes (strings) to numeric (deprecated?)
df.convert_objects(convert_numeric=True)

# Change all object datatypes (strings) to category
for col in df.columns:
  if df[col].dtype.name == 'object':
    df[col] = df[col].astype('category')

# Encoding category features
#  http://scikit-learn.org/stable/modules/preprocessing.html#encoding-categorical-features
# http://fastml.com/converting-categorical-data-into-numbers-with-pandas-and-scikit-learn
cols_to_transform = [ 'a', 'list', 'of', 'categorical', 'column', 'names' ]
df_with_dummies = pd.get_dummies(df, columns = cols_to_transform )
```

## Pandas - Important Descriptive functions

```
df.shape
df.columns
df.dtypes
df.describe()
df.value_counts()
df.nunique()
df.corr()
```

```
# List missing values in column
df['columnName'][X_train['columnName'].isna()]

# List present values in column
df['columnName'][X_train['columnName'].notna()]

# Fill missing values in columnName
df['columnName'].fillna('missing')

def print_na_counts(df):
  for col in df.columns:
    print(col, 'count:', len(df[col]), 'missing count:', len(df[col][df[col].isna()]))

# Fill all na (NaN) values
df.fillna('missing', inplace=True)
```

* Correlation between columns
* Missing values

## Numpy Arrays (and Matrices)

```python
import numpy as np

v = np.array([1, 2, 3])
v.shape # => (3,)
m = np.array([[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]])
m.shape # => (3,3)

3*v # => array([3, 6, 9])
v + v # => array([2, 4, 6])
# Dot product
v * v # => array([1, 4, 9])
np.sqrt(v * v)
# Magnitude of vector
magnitude = np.sqrt(np.sum(np.square(v)))
magnitude = np.linalg.norm(v)
# Unit vector
v/magnitude

# Go from a one dimensional array two dimensional - an array of arrays (matrix)
np.array([1, 2, 3]).reshape(1, 3) # => [[1, 2, 3]]
np.array([1, 2, 3]).reshape(1, -1) # => [[1, 2, 3]]

# Go from one dimensional array to array of arrays with one value
np.array([1, 2, 3]).reshape(-1, 1) # => array([[1], [2], [3]])

# 2x2 matrix with zeroes
np.zeroes((2,2))
# 2x2 matrix with ones
np.ones((2,2))
# 2x2 matrix with value 7
np.full((2,2), 7)
# 2x2 identity matrix
np.eye(2)
# 2x2 array with random values (0-1)
np.random.random((2,2))
```

## Resources

* [10 Minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/10min.html)
* [Indexing and Selecting Data](https://pandas.pydata.org/pandas-docs/stable/indexing.html)
* [12 Useful Pandas Techniques in Python for Data Manipulation](https://www.analyticsvidhya.com/blog/2016/01/12-pandas-techniques-python-data-manipulation)

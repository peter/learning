# Week 3 - Advanced Python Pandas

## Merging Dataframes

Last week, we were introduced to the pandas data manipulation and analysis library. We saw that there is really two-core data structures which are very similar, the one-dimensional series object and the two-dimensional DataFrame object. Querying these two data structures is done in a few different ways, such as using the iloc or loc attributes for row-based querying, or using the square brackets on the object itself for column-based querying. Most importantly, we saw that one can query the DataFrame and Series objects through Boolean masking. And Boolean masking is a powerful filtering method which allows us to use broadcasting to determine what data should be kept in our analysis.

We've already seen how we add new data to an existing DataFrame. We simply use the square bracket operator with the new column name.

This is a Venn Diagram. A Venn Diagram is traditionally used to show set membership. For example, the circle on the left is the population of students at a university. The circle on the right is the population of staff at a university. And the overlapping region in the middle are all of those students who are also staff.

First what if we want a list of all the people regardless of whether they're staff or student, and all of the information we can get on them? In database terminology, this is called a *full outer join*. And in set theory, it's called a union. In the Venn diagram, it represents everyone in any circle.

It's quite possible though that we only want those people who we have maximum information for, those people who are both staff and students. In database terminology, this is called an inner join. Or in set theory, the intersection. And this is represented in the Venn diagram as the overlapping parts of each circle.

```python
import pandas as pd

staff_df = pd.DataFrame([
  {'Name': 'Kelly', 'Role': 'Director of HR'},
  {'Name': 'Sally', 'Role': 'Course liaison'},
  {'Name': 'James', 'Role': 'Grader'}
])
staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([
  {'Name': 'James', 'School': 'Business'},
  {'Name': 'Mike', 'School': 'Law'},
  {'Name': 'Sally', 'School': 'Engineering'}
])
student_df = student_df.set_index('Name')
```

```python
# Union
pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)

# Intersection
pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)

# Left
pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)

# Right
pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True)
```

## Pandas Idioms

An idiomatic solution is often one which has both high performance and high readability.

Using vectorization wherever possible.

Avoid chain indexing: `df.loc['Washtenaw']['Total Population']`

```python
import pandas as pd

df = pd.read_csv('data-files/census.csv')
# NOTE: Start with open parenthesis to expand multiple lines
(df.where(df['SUMLEV'] == 50)
  .dropna()
  .set_index(['STNAME', 'CTYNAME'])
  .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))
```

## Group by

```python
```

## Scales

```python
```

## Pivot Tables

```python
```

## Date Functionality

```python
import pandas as pd
import numpy as np

pd.Timestamp('9/1/2016 10:05AM')

pd.Period('1/2016') # Month
pd.Period('2016-03-05') # Day

# DatetimeIndex
t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
t1.index # => DatetimeIndex

# PeriodIndex
t2 = pd.Series(list('def'), [pd.Timestamp('2016-09'), pd.Timestamp('2016-10'), pd.Timestamp('2016-11')])
t.index # => PeriodIndex

# Parsing strings into Datetime
d1 = ['2 june 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
t3 = pd.DataFrame(np.random.randint(10, 100, (4, 2)), index=d1, columns=list('ab'))
t3.index = pd.to_datetime(t3.index)
pd.to_datetime('4.7.12', dayfirst=True)

# Timedeltas
pd.Timestamp('9/3/2016') - pd.Timestamp('9/1/2016')
# => Timedelta('2 days 00:00:00')
dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
df = pd.DataFrame({
  'Count 1': 100 + 100 + np.random.randint(-5, 5, 9),
  'Count 2': 120 + 100 + np.random.randint(-5, 5, 9)
  }, index=dates)
df.index.weekday_name
df.diff() # diff between each date
df.resample('M').mean()
df['2017']
df['2016-12']
df['2016-12':]
df.asfreq('W', method='ffill')
```

## Resources

* [Pandas API Reference](https://pandas.pydata.org/pandas-docs/stable/api.html)

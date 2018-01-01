# Chapter 2 - Statistics and Probability Refresher, and Python Practise

## IPython Notebook Primer

"The notebook consists of a sequence of cells. A cell is a multi-line text input field, and its contents can be executed by using Shift-Enter, or by clicking either the “Play” button the toolbar, or Cell | Run in the menu bar. The execution behavior of a cell is determined the cell’s type. There are four types of cells: code cells, markdown cells, raw cells and heading cells. Every cell starts off being a code cell, but its type can be changed by using a dropdown on the toolbar (which will be “Code”, initially), or via keyboard shortcuts."

[Keyboard shortcuts](https://ipython.org/ipython-doc/3/notebook/notebook.html#keyboard-shortcuts):

* Shift-Enter: run cell
* Ctrl-Enter: run cell in-place
* Esc and Enter: Command mode and edit mode

Get help with `?` or `object?`. Use tab completion.

There are [magic functions](https://ipython.org/ipython-doc/3/interactive/tutorial.html#magics-explained) like
`%timeit` and `%%timeit` and `%matplotlib inline`.

"If the %matplotlib magic is called without an argument, the output of a plotting command is displayed using the default matplotlib backend in a separate window."

```
# start notebook
ipython notebook
```

Convert from notebook to different formats (html, pdf, slides etc.):

```
ipython nbconvert --to html course-material/MeanMedianMode.ipynb

brew install pandoc # document converter - dependency of nbconvert
# Install Tex: https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex (2.9 GB on Mac)
# Tex is typesetting language for math and technical texts
ipython nbconvert --to pdf course-material/MeanMedianMode.ipynb
```

See [IPython nobebook docs](https://ipython.org/ipython-doc/3/notebook) for more.

## Types of Data

* Numerical data. Quantitative and measurable data. Discrete data (integer based, number of checkouts) and continuous data (infinite number of values, how long time did it take to check out).

* Categorical data. Has no inherent numeric meaning. Gender, race, state of residence. You can assign numbers to categories but they have no inherent meaning.

* Ordinal data. A mixture of numerical and categorical data. The numbers assigned to this data has meaning, there is a numeric relationship (greater than and less than). Example: rating with 1-5 stars.

## Mean, Median, Mode

* Mean/average
* Median, a.k.a 50% percentile, Q2. 50% of values are below and 50% above.
* Mode - most common value, makes sense for discrete data

The median can differ from the mean if there are outliers and the median is not
sensitive to outliers the way the mean is (the mean is skewed by outliers).
The mean household income in the US is 72 thousand but the median is only 51 thousand.

See [course-material/MeanMedianMode.ipynb](course-material/MeanMedianMode.ipynb)

```python
import numpy as np

incomes = np.random.normal(27000, 15000, 10000)

```

## Variation and Standard Deviation

## Probability Density Function, Probability Mass Function

## Common Data Distributions

## Percentiles and Moments

## Matplotlib

## Covariance and Correlation

## Conditional Probability

## Bayes Theorem

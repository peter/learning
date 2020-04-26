# Basic Statistics Week 1 - Exploring Data

## 1.1 Data and Visualization

### Cases, variables and levels of measurement

*Variables* are features of something or someone and *cases* are that something or someone. The basic requirement on a variable is that it needs to vary among cases, i.e. should not be constant.

The combination of a variable and a case is a measurement (observation) and there are different levels (types) of measurement.

Categorical variables:

* Nominal variables don't have an order
* Ordinal variables have an order

Quantitative (numerical) variables can be:

* continuous
* discrete
* binary

### Data matrix and frequency table

The data matrix holds the data of a statistical study and has cases as rows and variables as columns. Each cell in the matrix is an observation.

The complete data matrix is usually large.

Sometimes when there are missing observations (cells) we may need to remove cases from the study (depending on the method of analysis).

We need ways to summarize and visualize the data matrix.

A frequency table shows the number of cases for each possible value of a variable, i.e. for hair color the number of people with each hair color. The frequency can be absolute (number of cases) or relative (percentage), or cumulative.

You need to recode a quantitative continuous variable into intervals (an ordinal variable) to create a frequency table.

You cannot recode ordinal variables into quantitative ones.

### Graphs and shapes of distributions

A frequency table can be visualized with a pie chart or a bar chart. The pie chart is especially useful in showing percentages. The bar chart may be preferable if you have a lot of categories.

For continuous quantitative variables you can use a [dot plot](https://en.wikipedia.org/wiki/Dot_plot_(statistics)) or a [histogram](https://en.wikipedia.org/wiki/Histogram). A histogram is similar to a bar chart but the bars touch eachother to indicate the continuous nature of the underlying data. A histogram "is an estimate of the probability distribution of a continuous variable".

A [bell curve](http://www.statisticshowto.com/bell-curve/) (normal distribution) is:

* Symmetrical - the mean is in the center
* Has only one peak/mode
* Has predictable standard deviations that follow the 68, 95, 99.7 rule

Unlike the bell curve (normal distribution), distributions may be left or right skewed.

A distribution with two peaks is called bimodal.

## 1.2 Measures of central tendency and dispersion

### Mode, median, and mean

* Mode - value that occurs most frequently. The only measure for nominal variables.
* Median - the dividing middle value (50% of observations are below and 50% above)
* Mean - the average value that "balances the scale"

Outliers can cause the mean and median to diverge since they can have a strong effect on the mean but leave the median fairly unchanged. If the outliers are influential or if the distribution is skewed then the median may be a better measure of the center than the mean.

### Range, interquartile range and box plot

Two distributions can have the same center but be very different in terms of dispersion/variance.

* Range - distance between the maximum and minimum value. Strongly affected by outliers (extreme values).
* Interquartile range (IQR) - the distance between the first and third quartile. Unaffected by outliers.

Quartiles each have 25% of the observations and the second quartile is the median.

An observation is considered to be an outlier if it lies more than 1.5 IQR above Q3 or below Q1.

A [box plot](https://en.wikipedia.org/wiki/Box_plot) shows you at a glance:

* Q1, Q2, and Q3 (50% of observations are in the box)
* the minimum value that is not an outlier and the maximum value that is not an outlier
* the outliers

The box plot is thus a good illustration of variability.

### Variance and standard deviation

[Variance](https://en.wikipedia.org/wiki/Variance) and standard deviation take all observations into account to express the dispersion.

The deviation of an observation is its value subtracted by the mean value. The sum of all
deviations is always zero (follows directly from the definition of the mean).

The variance is the sum of squares of deviations divided by the number of observations minus one.

The standard deviation is the root of the variance.

## 1.3 Z-scores and example

Sometimes researchers want to know if a value is common or exceptional. To express
this one can use the z-score which is the number of standard deviations that the
observation is removed from the mean. To recode observations as z-score values
is said to be a standardization of the variable.

The mathematical definition of the z-score is

```
z = (x - avg(x)) / s
```

Negative z-scores are below the mean and are cancelled out by the positive z-scores.

For a bell curve:

* 68% is within z-score (-1, +1)
* 95% within z-score (-2, 2)
* 99% within z-score (-3, 3)

A z-score of more than 3 can be considered exceptional for a bell curve.

For all distributions:

* 75% of data must lie between (-2, 2)
* 89% of data must lie between (-3, 3)

## 1.4 R Lab

See [r-programming](r-programming.md)

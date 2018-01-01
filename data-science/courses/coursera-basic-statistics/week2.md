# Basic Statistics Week 2 - Correlation and Regression

## 2.1 Correlation

### Contingency Tables, Scatter Plots, and Person's R

Suppose we want to investigate the relationship (correlation) between
eating chocolate (independent variable) and body weight (dependant variable). Suppose we have selected 200 students that are all 170 cm tall and that take this survey:

Body Weight (kg):

* < 50
* 50-69
* 70-89
* > 90

Chocolate consumption (g/week):

* < 50
* 50-150
* > 150

In the [Contingency Table](https://en.wikipedia.org/wiki/Contingency_table) we have body weight as rows (4 rows) and chocolate consumption as columns (3 columns). We can look at proportions, i.e. percentages in different cells, i.e. along columns or along rows. For example, here we can look at the percentages of people in different body weight categories for a certain chocolate consumption level and find that high chocolate consumption has high percentages in high weight groups and vice versa. This indicates correlation i.e. that you are more likely to weigh more if you eat more chocolate (positive correlation).

Contingency tables are appropriate for ordinal and nominal variables. For quantitative variables a [Scatter Plot](https://en.wikipedia.org/wiki/Scatter_plot) is better. In the scatter plot we put the independent variable on the x-axis (chocolate consumption) and the dependent variable on the y-axis (weight). The plot suggests at a glance whether there is linear correlation or not.

The [Person's r](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) expresses the strength of linear correlation between two variables and it has a value between -1 (perfect negative linear) and +1 (perfect positive linear). Possible correlation scenarios:

* No correlation (random)
* Negative linear
* Positive linear
* Curved

We calculate the Person's r by summing the product of z-scores for all points divided by n - 1 (number of cases minus 1). The z-score is the value minus the mean divided by the standard deviation (s).

The Person's r is not meaningful if the relationship is not linear. A low value does not indicate lack of correlation, only lack of linear correlation.

## 2.2 Regression

"Regression analysis is one of the most frequently employed statistical methods"

"the best fitting line is the line for which the sum of the squared residuals (vertical distances of the cases in your scatterplot to the line) is the smallest. We therefore talk about ordinary least squares (OLS) regression."

A regression line can help make predications about the dependent variable.

"Here we'll introduce the so-called r-squared. It tells you how much better a regression line predicts your dependent variable than the mean of that variable, and it shows you how much of the variance in your dependent variable is explained by your independent variable."

The regression line is the best fitting line `y = a + b * x` where
b is the regression coefficient, a is the intercept, y is the predicted value and x is the independent variable value. The formula for b is `b = r * (sy / sx)` where r is Person's R, sy is the standard deviation for y, and sx is the standard deviation for x. The intercept is given by `a = avg(y) - b * avg(x)`

By accuracy of prediction we mean how well the regression line fits the data. We can ask ourselves how much better the regression line is than the mean. It turns out that Person's r squared is how much smaller the prediction error of the regression line is than the mean (so r = 0.69 means 69% smaller). The other interpretation of r squared is that it is the percentage of the variance in the dependent variable that is explained by the independent variable (explained variance).

## 2.3 Caveats and Examples

"For at least two reasons we need to be very careful when we interpret the results of a regression analysis. The first reason is that *correlation is not the same as causation*. There might be confounding or lurking variables or causality might run in the opposite direction. A second reason why we should be very careful is that influential outliers can have strong effects on the results of an analysis."

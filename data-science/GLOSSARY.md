# Glossary of Terms Related to Statistics

Useful resources in addition to Wikipedia:

* [Statistics Definitions (statisticshowto.com)](http://www.statisticshowto.com/probability-and-statistics/statistics-definitions)

## [Big Data](#big-data) - [[W](https://en.wikipedia.org/wiki/Big_data)]

"Big data is a term for data sets that are so large or complex that traditional data processing application software is inadequate to deal with them."

"Lately, the term "big data" tends to refer to the use of predictive analytics, user behavior analytics, or certain other advanced data analytics methods that extract value from data, and seldom to a particular size of data set. "There is little doubt that the quantities of data now available are indeed large, but that’s not the most relevant characteristic of this new data ecosystem."[2] Analysis of data sets can find new correlations to "spot business trends, prevent diseases, combat crime and so on.""

## [Case](#case)

Cases in a statistical study are the units of observation, i.e. the persons or things that we are studying. Examples: football players, football teams, companies, schools, countries etc.

## [Categorical Variable](#categorical-variable) [[W](https://en.wikipedia.org/wiki/Categorical_variable)]

"In statistics, a categorical variable is a variable that can take on one of a limited, and usually fixed, number of possible values"

"In computer science and some branches of mathematics, categorical variables are referred to as enumerations or enumerated types."

Examples: the blood type of a person, the state a person lives in, the political party you can vote for, the type of a rock.

"the central tendency of a set of categorical variables is given by its mode; neither the mean nor the median can be defined"

"Categorical variables that have only two possible outcomes (e.g., "yes" vs. "no" or "success" vs. "failure") are known as binary variables (or Bernoulli variables). Because of their importance, these variables are often considered a separate category, with a separate distribution (the Bernoulli distribution) and separate regression models (logistic regression, probit regression, etc.)."

Coding is the conversion of categorical data to quantitative data (numbers).

## [Coefficient of determination](#coefficient-of-determination) [[W](https://en.m.wikipedia.org/wiki/Coefficient_of_determination)]

In statistics, the coefficient of determination, denoted R2 or r2 and pronounced "R squared", is the proportion of the variance in the dependent variable that is predictable from the independent variable(s).

```
y - values y1...yn
f - predicted values f1...fn
SSres = sum((y-f)^2)
SStot = sum((y-avg(y))^2)
R^2 = 1 - SSres/SStot
```

## [Data Science](#data-science) [[W](https://en.wikipedia.org/wiki/Data_science)]

"Data science, also known as data-driven science, is an interdisciplinary field about scientific methods, processes, and systems to extract knowledge or insights from data in various forms, either structured or unstructured,[1][2] similar to data mining.

Data science is a "concept to unify statistics, data analysis and their related methods" in order to "understand and analyze actual phenomena" with data.[3] It employs techniques and theories drawn from many fields within the broad areas of mathematics, statistics, information science, and computer science, in particular from the subdomains of machine learning, classification, cluster analysis, data mining, databases, and visualization."

## [Data Matrix](#data-matrix)

A two dimensional matrix with cases as rows and variables as columns (or vice versa) where each cell (case/variable combination) represents an observation in a statistical study.

See [Matrices and Matrix Algebra](http://www.statisticshowto.com/matrices-and-matrix-algebra)

## [Descriptive Statistics](#descriptive-statistics) [[W](https://en.wikipedia.org/wiki/Descriptive_statistics)]

"Descriptive statistics are statistics that quantitatively describe or summarize features of a collection of information.[1] Descriptive statistics are distinguished from [inferential statistics](https://en.wikipedia.org/wiki/Statistical_inference) (or inductive statistics), in that descriptive statistics aim to summarize a sample, rather than use the data to learn about the population that the sample of data is thought to represent. This generally means that descriptive statistics, unlike inferential statistics, are not developed on the basis of probability theory. Even when a data analysis draws its main conclusions using inferential statistics, descriptive statistics are generally also presented."

## [Neural Network](#neural-network) [[W](https://en.wikipedia.org/wiki/Artificial_neural_network)]

## [Nominal Variable](#nominal-variable)

A [nominal variable](http://www.statisticshowto.com/nominal-variable/) is:

"another name for a categorical variable. Nominal variables have two or more categories without having any kind of natural order. they are variables with no numeric value, such as occupation or political party affiliation. Another way of thinking about nominal variables is that they are named (nominal is from Latin nominalis, meaning pertaining to names)."

## [Nonparametric statistics](#nonparametric-statistics) [[W](https://en.m.wikipedia.org/wiki/Nonparametric_statistics)]

"Nonparametric statistics are statistics not based on parameterized families of probability distributions. They include both descriptive and inferential statistics. The typical parameters are the mean, variance, etc. Unlike parametric statistics, nonparametric statistics make no assumptions about the probability distributions of the variables being assessed. The difference between parametric models and non-parametric models is that the former has a fixed number of parameters, while the latter grows the number of parameters with the amount of training data.[1] Note that the non-parametric model does, counterintuitively, contain parameters: the distinction is that parameters are determined by the training data in the case of non-parametric statistics, not the model."

## [Qualitative Property](#qualitative-property) [[W](https://en.wikipedia.org/wiki/Qualitative_property)]

"Qualitative properties are properties that are observed and can generally not be measured with a numerical result. They are contrasted to quantitative properties which have numerical characteristics."

## [Statistics](#statistics) [[W](https://en.wikipedia.org/wiki/Statistics)]

"Statistics is a branch of mathematics dealing with the collection, analysis, interpretation, presentation, and organization of data.[1][2] In applying statistics to, e.g., a scientific, industrial, or social problem, it is conventional to begin with a statistical population or a statistical model process to be studied. Populations can be diverse topics such as "all people living in a country" or "every atom composing a crystal." Statistics deals with all aspects of data including the planning of data collection in terms of the design of surveys and experiments."

## [Variable](#variable)

A characteristic of a [case](#case). There are categorical (nominal), ordinal, and quantitative variables. Examples: age, weight, hair color, sex, country of origin.

Nominal and ordinal variables are both categorical variables. The difference is that nominal variables are unordered.

Quantitative (numerical) variables can be discrete (integers) or continuous.

You can recode one type of variable (level of measurement) into a different type,
i.e. transform a quantitative variable to an ordinal variable.

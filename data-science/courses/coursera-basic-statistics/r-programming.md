# R Programming

This is an optional lab assignment and it will familiarize yourself with R.
It is based on Datacamps own course [Introduction to R](https://www.datacamp.com/courses/free-introduction-to-r).

## Resources

* [R Project (Homepage)](https://www.r-project.org)
* [An Introduction to R](https://cran.r-project.org/doc/manuals/r-release/R-intro.html)
* [Try R at Codeschool](http://tryr.codeschool.com)

## Basic Features of R

* R has basic arithmetic operators (+, -, /, ...)
* Exponentiation: 3 ^ 2
* [Modulo](https://en.wikipedia.org/wiki/Modulo_operation): 5 %% 3 == 2
* Comments begin with a #
* Variable assignment: my_variable <- 4
* The plus (+) operator does not allow incompatible operand types, i.e. string and integer
* Boolean (logical) values are TRUE and FALSE
* List defined variables: ls()
* Check the data type of a variable: class(my_variable) or is.character(my_variable)
* Coercion: as.numeric("3") (you can use tab completion to find more)

## Notes, Examples, Exercises

Create homogenous vector with c():

```r
numeric_vector <- c(1, 2, 3)
character_vector <- c("a", "b", "c")
boolean_vector <- c(TRUE, FALSE)

numeric_vector[1] # first element
boolean_vector[c(2, 3)] # second and third element
```

Vector indexes are 1-based.

You can construct a matrix in R with the matrix() function. Example - construct matrix
from 9 element vector by row with 3 rows and 3 columns:

```R
matrix(1:9, byrow = TRUE, nrow = 3, ncol = 3)
```

Enumerations, i.e. categorical variables, are handled in R with factors:

```R
student_status <- c("student", "not student", "student", "not student")
categorical_student <- factor(student_status)
```

All the elements that you put in a matrix should be of the same type (homogenous).

A data frame has the variables of a data set as columns and the observations as rows (like a database table, i.e. one datatype per column). This will be a familiar concept for those coming from different statistical software packages such as SAS or SPSS. Functions for inspecting dataframes:

* head: this by default prints the first 6 rows of the dataframe
* tail: this by default prints the last 6 rows to the console
* str: this prints the structure of your dataframe
* dim: this by default prints the dimensions, that is, the number of rows and columns of your dataframe
* colnames: this prints the names of the columns of your dataframe

You construct a data frame with the `data.frame()` function which takes as arguments
the vectors of each column:

```R
planets <- c("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
type <- c("Terrestrial planet", "Terrestrial planet", "Terrestrial planet", "Terrestrial planet", "Gas giant", "Gas giant", "Gas giant", "Gas giant")
diameter <- c(0.382, 0.949, 1, 0.532, 11.209, 9.449, 4.007, 3.883)
rotation <- c(58.64, -243.02, 1, 1.03, 0.41, 0.43, -0.72, 0.67)
rings <- c(FALSE, FALSE, FALSE, FALSE, TRUE, TRUE, TRUE, TRUE)
planet_df <- data.frame(planets, type, diameter, rotation, rings)
```

Dataframe selection:

```R
# select the values in the first row and second and third columns
planet_df[1, 2:3]
# select the entire third column
planet_df$diameter

levels(mtcars$am)
```

A list in R allows you to gather a variety of objects under one name (that is, the name of the list) in an ordered way. These objects can be matrices, vectors, data frames, even other lists, etc. It is not even required that these objects are related to each other.

```R
# Vector with numerics from 1 up to 10
my_vector <- 1:10

# Matrix with numerics from 1 up to 9
my_matrix <- matrix(1:9, ncol = 3)

# First 10 elements of the built-in data frame 'mtcars'
my_df <- mtcars[1:10,]

# Construct my_list with these different elements:
my_list <- list(my_vector, my_matrix, my_df)

# print my_list to the console
my_list
```

Selecting elements from lists:

```R
# First element
my_list[[1]]

# Select by name
my_list[["my_vector"]]
my_list$my_df

# Grab the first column of the third component of `my_list` and print it to the console
my_list[[3]][,1]
```

Getting help:

```R
help(mean)
args(mean)
?mean
```

Remember that R can match arguments both by position and by name.

```
# a grades vector
grades <- c(8.5, 7, 9, 5.5, 6)

# calculate the mean of grades using matching by name
mean(x = grades)

# calculate the mean of grades using matching by position
mean(grades)
```

Signature of mean:

```
mean(x, trim = 0, na.rm = FALSE, ...)
```

```
# a grades vector
grades <- c(8.5, 7, 9, NA, 6)
mean(grades)
mean(grades, na.rm = TRUE)
```

Function definition:

```
sum_a_b <- function(a, b){
  return (a + b)
}
result = sum_a_b(4, 5)
```

```
# make a function called multiply_a_b
multiply_a_b <- function(a, b) {
  return (a * b)
}

# call the function multiply_a_b and store the result into a variable result
result = multiply_a_b(3, 7)
```

One important thing before you actually do analyses on your data, is that you will need to get your data into R. R contains many functions to read in data from different formats. To name only a few:

* read.table: Reads in tabular data such as txt files
* read.csv: Read in data from a comma-separated file format
* readWorksheetFromFile : Reads in an excel worksheet
* read.spss: Reads in data from .sav SPSS format.

Example CSV: http://s3.amazonaws.com/assets.datacamp.com/course/uva/mtcars.csv

```
# load in the data and store it in the variable cars
cars <- read.csv("http://s3.amazonaws.com/assets.datacamp.com/course/uva/mtcars.csv")

# print the first 6 rows of the dataset using the head() function
head(cars)
```

```
# load in the dataset
cars <- read.csv("http://s3.amazonaws.com/assets.datacamp.com/course/uva/mtcars_semicolon.csv", sep = ";")

# print the first 6 rows of the dataset
head(cars)
```

Working with local files:

* getwd(): This function will retrieve the current working directory for the user
* setwd(): This functions allows the user to set her own working directory

```
# list all the files in the working directory
list.files()

# read in the cars dataset and store it in a variable called cars
cars <- read.csv("cars.csv", sep = ";")

# print the first 6 rows of cars
head(cars)
```

Although base R comes with a lot of useful functions, you will not be able to fully leverage the full power of R without being able to import R modules developed by others. Imagine we want to do some great plotting and we want to use ggplot2 for it. If we want to do so, we need to take 2 steps:

1. Install the package ggplot2 using install.packages("ggplot2")
2. Load the package ggplot2 using library(ggplot2) or require(ggplot2)

Recoding Variables.

Frequency tables show you how often a given value occurs. To look at a frequency table of the data in R, use the function table(). The top row of the output is the value, and the bottom row is the frequency of the value.

We easily can make graphs to visualize our data with `barplot()`.

```
# Assign the frequency of the mtcars variable "am" to a variable called "height"
height <- table(mtcars$am)

# Create a barplot of "height"
barplot(height)
```

```
# vector of bar heights
height <- table(mtcars$am)

# Make a vector of the names of the bars called "barnames"
barnames <- c("automatic", "manual")

# Label the y axis "number of cars" and label the bars using barnames
barplot(height, ylab = "number of cars", names.arg = barnames)
```

You can make histograms with the `hist()` function.

```
# Make a histogram of the carb variable from the mtcars data set. Set the title to "Carburetors"
hist(mtcars$carb, main = "Carburetors")
```

```
# arguments to change the y-axis scale to 0 - 20, label the x-axis and colour the bars red
hist(mtcars$carb, main = "Carburetors", ylim=c(0, 20), xlab = "Number of Carburetors", col = "red")
```

```
# Calculate the mean miles per gallon
mean(mtcars$mpg)

# Calculate the median miles per gallon
median(mtcars$mpg)
```

```
# Produce a sorted frequency table of `carb` from `mtcars`
sort(table(mtcars$carb), decreasing = TRUE)
```

The range of a variable is the difference between the highest and lowest value.
We can find these values using max() and min() on the variables of our choice.

You can calculate the quartiles in your data set using the function quantile(). The output of quantile() gives you the lowest value, first quartile, second quartile, third quartile and highest value. 25% of your data lies below the first quartile value, 50% lies below the second quartile, and 75% lies below the third quartile value

To better visualise your data's quartiles you can create a boxplot using the function boxplot()
Similarly, you can calculate the interquartile range manually by subtracting the value of the third quartile from the value of the first quartile, or we can use the function IQR() on your variable of interest

```
# Make a boxplot of qsec
boxplot(mtcars$qsec)

# Calculate the interquartile range of qsec
IQR(mtcars$qsec)
```

In the boxplot you created you can see a circle above the boxplot. This indicates an outlier. We can calculate an outlier as a value 1.5 * IQR above the third quartile, or 1.5 * IQR below the first quartile.

```
IQR(mtcars$qsec)

quantile(mtcars$qsec)

# What is the threshold value for an outlier below the first quartile?
18.9 + 2.0075*1.5

# What is the threshold value for an outlier above the third quartile?
16.8925 - 2.0075*1.5
```

We can also measure the spread of data through the standard deviation. You can calculate these using the function sd(), which takes a vector of the variable in question as its first argument.

```
# Find the IQR of horsepower
IQR(mtcars$hp)

# Find the standard deviation of horsepower
sd(mtcars$hp)

# Find the IQR of miles per gallon
IQR(mtcars$mpg)

# Find the standard deviation of miles per gallon
sd(mtcars$mpg)
```

Mean, median and mode are all measures of the average. In a perfect normal distribution the mean, median and mode values are identical, but when the data is skewed this changes.

We can calculate the z-score for a given value (X) as (X - mean) / standard deviation. In R you can do this with a whole variable at once by putting the variable name in the place of X

```
# Calculate the z-scores of mpg
(mtcars$mpg - mean(mtcars$mpg))/sd(mtcars$mpg)
```

Z-scores 1, 2, 3: 68%, 95%, 98%.


```
chocolate = c(2, 4, 1.5, 2, 3)
chocolate_mean = mean(chocolate) # => 2.5
chocolate_sd = sd(chocolate) # => 1

happiness = c(7, 3, 8, 8, 6)
happiness_mean = mean(happiness) # => 6.4
happiness_sd = sd(happiness) # => 2.073644

x = data.frame(chocolate, happiness)
cor(x, method = "pearson")
```

```
# Plot height and weight of the "women" dataset. Make the title "Heights and Weight
plot(women$weight, women$height, main = "Heights and Weights")
```

Making a Contingency Table

We can make a contingency table of this data using the table() function. While previously you may have used this with one variable, this time you will use it with two. The first variable used with table() will appear in the rows, while the second variable will appear in the columns.

Saved in your console is a dataset called smoking, which contains data about amount of tobacco smoked per day in a sample of 88 students. The student variable says whether a student is in high school, or university, and the tobacco variable indicates how many grams of tobacco are smoked per day.

```
# Make a contingency table of tobacco consumption and education
table(smoking$tobacco, smoking$student)
```

```
           high school university
 0-9g            17         14
 10-19g          16         15
 20-29g          11         15
```

round(12.6734, digits = 2) would return the value 12.67

```
# What percentage of high school students smoke 0-9g of tobacco?
round(17*100/(17+16+11), digits = 1)

# Of the students who smoke the most, what percentage are in university?
round(15*100/(15 + 11), digits = 1)
```

We can calculate the correlation in R using the function cor(), which takes your two variables as it's first argument.

When we draw a line through our data, we measure error as the sum of the difference between the observation and the line. We usually square this so that positive and negative residuals don't cancel each other out. The line that gives us the least error is our regression line.

```
# predicted values of y according to line 1
y1 <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# predicted values of y according to line 2
y2 <- c(2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

# actual values of y
y <- c(3, 2, 1, 4, 5, 10, 8, 7, 6, 9)

# calculate the squared error of line 1
sum((y1 - y) ^ 2)

# calculate the squared error of line 2
sum((y2 - y) ^ 2)
```

The regression equation is Y = a + bx, where a is the intercept and b is the slope of the line.

We can find the regression coefficients for our data using the lm() function, which takes our model as the first argument: first the y variable, followed by a ~ symbol, then the x variable. For instance: lm(y ~ x)

```
# Our data
money <- c(1,2,3,4,5,6,7,8,9,10)
prosocial <- c(3, 2, 1, 4, 5, 10, 8, 7, 6,9)
# Find the regression coefficients
lm(prosocial ~ money)
```

```
# Your plot
plot(money, prosocial, xlab = "Money", ylab = "Prosocial Behavior")
# Store your regression coefficients in a variable called "line"
line <- lm(prosocial ~ money)

# Use "line" to tell abline() to make a line on your graph
abline(line)
```

```
# Your plot
plot(money, prosocial, xlab = "Money", ylab = "Prosocial Behavior")
# Your regression line
line <- lm(prosocial ~ money)
abline(line)
# Add a line that shows the mean of the dependent variable
abline(mean(prosocial), 0)
```

These are the two lines you plotted in the last assignment. One line shows the mean, and one shows the regression line. Clearly, there is less error when we use the regression line compared to the mean line. This reduction in error from using the regression line compared to the mean line tells us how well the independent variable (money) predicts the dependent variable (prosocial behaviour).

Let's try to put it all together. You've conducted a study looking at how much money people have (dependent variable) and their education level (independent variable). Let's check some different things in your data!

Probability mass and density functions

```
# the data frame
data <- data.frame(outcome = 0:5, probs = c(0.1, 0.2, 0.3, 0.2, 0.1, 0.1))

# make a histogram of the probability distribution
barplot(data$probs, names.arg=data$outcome)
```

```
# simulating data
set.seed(11225)
data <- rnorm(10000)

# check for documentation of the dnorm function
help(dnorm)

# calculate the density of data and store it in the variable density
density <- dnorm(data)

# make a plot with as x variable data and as y variable density
plot(data, density)
```

The cumulative probability distribution

```
# probability that x is smaller or equal to two
prob <- probability_distribution$probs[1] + probability_distribution$probs[2] + probability_distribution$probs[3]

# probability that x is 0, smaller or equal to one,
# smaller or equal to two, and smaller or equal to three
cumsum(probability_distribution$probs)
```

```
# calculate the expected probability value and assign it to the variable expected_score
expected_score <- sum(data$outcome * data$probs)

# print the variable expected_score
expected_score
```

Variance

```
# the mean of the probability mass function
expected_score <- sum(data$outcome * data$probs)

# calculate the variance and store it in a variable called variance
variance <- sum(mapply(function(x, p) (x - expected_score)^2*p, data$outcome, data$probs))

# calculate the standard deviation and store it in a variable called std
std <- sqrt(variance)
```

```
# probability of a woman having a hair length of less than 20 centimeters
round(pnorm(20, mean = 25, sd = 5, lower.tail = TRUE), 2)
```

```
# 85th percentile of female hair length
round(qnorm(0.85, mean = 25, sd = 5), 2)
```

A special form of the normal probability distribution is the standard normal distribution, also known as the z - distribution. A z distribution has a mean of 0 and a standard deviation of 1. Often you can transform variables to z values. You can transform the values of a variable to z-scores by subtracting the mean, and dividing this by the standard deviation. If you perform this transformation on the values of a data set, your transformed data set will ave a mean of 0 and a standard deviation of 1.

The binomial distribution

The binomial distribution is important for discrete variables. There are a few conditions that need to be met before you can consider a random variable to binomially distributed:

There is a phenomenon or trial with two possible outcomes and a constant probability of success - this is called a Bernoulli trial
All trials are independent

Other ingredients that are essential to a binomial distribution is that we need to observe a certain number of trials, let's call this n, and we count the number of successes in which we are interested, let's call this x. Useful summary statistics for a binomial distribution are the same as for the normal distribution: the mean and the standard deviation.

The mean is calculated by multiplying the number of trials n by the probability of a success denoted by p. The standard deviation of a binomial distribution is calculated by the following formula: sqrt(n*p*(1-p))

```
# calculate the mean and store it in the variable mean_chance
mean_chance = 0.2*25

# calculate the standard deviation and store it in the variable std_chance
std_chance = sqrt(25*0.2*(1-0.2))
```

Sampling from the population

the male beard length (in millimeters) of hipsters in Scandinavia

If we were interested in estimating the average male beard length of hipsters in Scandinavia, in R we can use the sample() function to sample from the population. For instance, to sample 50 inhabitants from our Scandinavian male hipster population which is included in the variable scandinavia_data, we could do the following: sample(scandinavia_data, size = 50). This command collects a simple random sample of size 50. If we didn't have access to the entire male hipster Scandinavian population, working with these 50 inhabitants would be considerably simpler than having to go through the entire Scandinavian male hipster population.

```
# variable scandinavia_data contains the beard lengths of scandinavian male population
set.seed(11225)
first_sample <- sample(scandinavia_data, size = 100)
mean(first_sample)
```

Every time some operation has to be repeated a specific number of times, a for loop may come in handy.

```
# initialize an empty vector
new_number <- NULL

# run an operation 10 times.
# The ith position of new number will be set to i
# at the end of the loop, the vector new_number is printed
for (i in 1:10){
  new_number[i] <- i
}

print(new_number)
```

```
# set the seed such that you will get the same sample as in the solution code
set.seed(11225)

# empty vector sample means
sample_means <- NULL

# take 200 samples from scandinavia_data
for (i in 1:500){
  samp <- sample(scandinavia_data, 200)
  sample_means[i] <- mean(samp)
}

# calculate the population mean, that is, the mean of scandinavia_data and print it
mean(scandinavia_data)

# calculate the mean of the sample means, that is, sample_means
mean(sample_means)
```

```
# standard deviation of the population
population_sd <- sd(scandinavia_data)
population_sd

# standard deviation of the sampling distribution
sampling_sd = population_sd/sqrt(200)
sampling_sd
```

The central limit theorem

"Provided that the sample size is sufficiently large, the sampling distribution of the sample mean is approximately normally distributed even if the variable of interest is not normally distributed in the population"

In this exercise we will take a look at a new population of simulated household income of citizens in the United States. The data is stored in a variable called household_income. This population is right skewed. We will take a 1000 samples of n = 200 from this population and calculate the sample mean each time. You will see that the sampling distribution, just as the central limit theorem states, is normally distributed.

```
# empty vector sample means
sample_means <- NULL

# take 200 samples from scandinavia_data
for (i in 1:1000){
  samp <- sample(household_income, 200)
  sample_means[i] <- mean(samp)
}

# make a histogram of household_income
hist(household_income)

# make a histogram of sample_means
hist(sample_means)
```

Recall the concept of Z scores from the lectures. Z scores are standardized scores how far a parameter is removed from its mean. A Z score with value 2 means that an observation is 2 standard deviations away from its population mean.

To illustrate the concept of the Z score, let's go back to our scandinavia_data dataset. In this population of male hipsters from Scandinavia, the average beard length is 25. The standard deviation in the population is 3.47. Suppose we had a hipster with a beard length of 32mm, this would be unusual for this population and thus would have a rather high Z score.

```
# z score of hipster with a beard of 32 millimeter
z_score <- (32-25)/3.47

# print the variable z_score to the console
z_score
```

Z scores can be easily translated to probabilities. There are multiple ways to do so:

Look up the z score in a table
Calculate the probability using R

In R we can use the pnorm() function to calculate the probability of obtaining a given score or a more extreme score in the population. Basically this calculate an area under the bell curve. The function pnorm() has several parameters you can include such as:

q: The observation for which you want to calculate the probability
mean: The population mean
sd: The population standard deviation
lower.tail: Indicates whether you want to calculate the area under the curve left of your observations or right of your observations

```
# calculate the area under the curve left of the observation
pnorm(2.02, lower.tail = TRUE)

# calculate the area under the curve right of the observation
pnorm(2.02, lower.tail = FALSE)
```

So far we have calculated the probabilities of observations using mean and standard deviation values from the population. However, we can also calculate these observation probabilities using mean and standard deviation values from the sample. For instance, we could have a question along the lines of what is the probability that the sample mean of the beard length of 50 Scandinavian hipsters is larger or equal to 26 millimeters. Because in this example we are talking about a specific sample from the population, we make use of the sampling distribution and not the population distribution.

Because we make use of the sampling distribution, we are now using the standard deviation of the sampling distribution which is calculated using the formula σ/n‾√σ/n.

```
# calculate the population mean
population_mean <- mean(scandinavia_data)

# calculate the population standard deviation
population_sd <- sd(scandinavia_data)

# calculate the standard deviation of the sampling distribution and put it in a variable sampling_sd
sampling_sd <- population_sd/sqrt(50)

# calculate the Z score and put in a variable called z_score
z_score = (26 - population_mean)/sampling_sd

# cumulative probability calculation. Don't forget to set lower.tail to FALSE
pnorm(z_score, lower.tail = FALSE)
```

You may notice that this distribution of sample means is much narrower than the distribution of observations of individual hipsters. How would you interpret the red area?

Confidence Interval with known SD

```
# Assign the sample mean to object "m"
m <- mean(samp)

# Assign the standard deviation to object "s"
s <- sd(samp)

# Calculate the upper confidence interval
m + 1.96*s/sqrt(300)

# Calculate the lower confidence interval
m - 1.96*s/sqrt(300)
```

T-scores come from T-distributions, which help us account for error that occurs when we sample from a population. We use a different T-distribution to calculate cumulative probabilites depending on our degrees of freedom.

Lets say we conducted another study on how often people get angry when they're driving (known as 'road rage') using a sample of 200 people chosen at random, saved in your console as rrage. Let's calculate the 95% confidence interval for where the population mean lies.

This time we must use a slightly different formula: sample mean +/- t value * standard error. The standard error is calculated as the population standard deviation, divided by the square root of the sample size. The T-score for a df of 199 is 1.9720.


In the last question we demonstrated how 95% of a population fall between 1.96 standard deviations above and below the population mean.
Let's pretend we have psychic knowledge that the standard deviation of sadness in the world is 8, but we need to find out what the mean is. We take a sample of 300 people. Let's estimate where the population mean is likely to lie using this sample.

If you remember, the formula for calculating the confidence interval is the sample mean +/- 1.96 * standard deviation. In this case, the standard deviation is the population standard deviation, divided by the square root of the sample size.

Calculating a Confidence Interval Without The Population Standard Deviation

Unfortunately in reality we usually don't know a population standard deviation, and thus must rely on sample standard deviations and T-scores. T-scores come from T-distributions, which help us account for error that occurs when we sample from a population. We use a different T-distribution to calculate cumulative probabilites depending on our degrees of freedom.

Lets say we conducted another study on how often people get angry when they're driving (known as 'road rage') using a sample of 200 people chosen at random, saved in your console as rrage. Let's calculate the 95% confidence interval for where the population mean lies.

This time we must use a slightly different formula: sample mean +/- t value * standard error. The standard error is calculated as the population standard deviation, divided by the square root of the sample size. The T-score for a df of 199 is 1.9720.

```
# Assign the sample mean to object "m"
m <- mean(rrage)

# Assign the sample standard error to object "s"
s <- sd(rrage)/sqrt(200)

# Calculate the upper 95% confidence interval
m + 1.972*s

# Calculate the lower 95% confidence interval
m - 1.972*s
```

Calculating A Confidence Interval for a Proportion I

Instead of measuring road rage as a continuous variable, you ask a sample to simply answer "yes" or "no" to the question "do you have road rage?". The outcome is saved in your console as roadrage. Let's find what proportion of your sample do have road rage.

```
# Make p the proportion of the sample with road rage
p <- table(roadrage)[2]/length(roadrage)
```

```
# Make p the proportion of the sample with road rage
p <- 70 / 200
# Find the standard error of p
se <- sqrt(p*(1-p)/200)
```

```
# Make p the proportion of the sample with road rage
p <- 70 / 200
# Find the standard error of p
se <- sqrt( (p * (1 - p)) / 200)
# Calculate the upper level of the confidence interval
p + 1.96*se
# Calculate the lower level of the confidence interval
p - 1.96*se
```

Your road rage study suggested that a proportion of 0.375 of your sample felt that they had road rage. The 95% confidence interval was from 0.308 to 0.442. What does this mean?

```
# Make p the proportion of the sample with road rage
p <- 75 / 200
# Find the standard error of p
se <- sqrt( (p * (1 - p)) / 200)
# Calculate the upper level of the 95% confidence interval
p + 1.96 * se
# Calculate the lower level of the 95% confidence interval
p - 1.96 * se
# Report the range of the 95% confidence interval
(p + 1.96 * se) - (p - 1.96 * se)

# Report the range of the 99% confidence interval
(p + 2.58 * se) - (p - 2.58 * se)

# Which has the widest range?
99
```

Let's do the same thing again with your original study that looked at how often people get angry when they're driving. The data from this study was from a sample of 200, and the results are saved in your console as rrage if you need them. We left you the code from where you calculated the 95% confidence interval. Now let's try finding the 90% confidence interval (corresponding to a T score of 1.6525), and comparing what happens when we use these different intervals.


Sample Size II

You're interested in looking at how many days in the week students drink alcohol, and need to know what kind of sample size to use. You know that to find this out, you need a Z-score, a margin of error and a standard deviation. Let's try to establish the standard deviation first. You expect that about 95% of people will consume an alcoholic drink between 1 and 6 days in the week.

Significance testing recap

From the lectures you may recall the concept of a hypothesis. Often in quantitative social science research, you will deal with a null hypothesis (H0) and an alternative hypothesis (H1). The way we do hypothesis testing in most of social science research is that we assume that the null hypothesis is true and that we look at the probability of our data under the null hypothesis. If this probability is very small, we reject the null hypothesis and at least temporarily accept the alternative hypothesis. Usually we take a significance level, denoted by the αα parameter, of 0.05 or 0.01. We then compare the p value that we find to the significance level against which we testing.

Given that we have tested against a significance level of 0.05 and found a p value of 0.03, do we accept the null hypothesis or the alternative hypothesis? What does a p value of 0.03 mean?

Significance testing: one-sided versus two-sided

```
# calculate the value of cut_off
cut_off <- round(qnorm(0.95, mean = 25, sd = 0.55), 2)

# print the value of cut_off to the console
cut_off
```

Significance testing: one-sided versus two-sided (2)

```
# calculate the value of the variable lower_cut_off
lower_cut_off <- qnorm(0.025, mean = 25, sd = 0.55)

# calculate the value of the variable upper_cut_off
upper_cut_off <- qnorm(0.975, mean = 25, sd = 0.55)

# print lower_cut_off to the console
lower_cut_off

# print upper_cut_off to the console
upper_cut_off
```

In the last exercises we saw that there are different cut-off values for one-sided and two-tailed hypothesis tests. You saw that in order to reject the null hypothesis when performing a two-tailed hypothesis, you would need to pass a higher threshold. In this exercise and the exercise to come, we will calculate probabilities based on sample means.

```
# calculate the z score and assign it to a variable called z_value
z_value <- round((25.95 - 25)/(3.5/sqrt(40)), 2)

# calculate the corresponding p value and store it in the variable called p_value
p_value <- round(pnorm(z_value, lower.tail = FALSE), 2)

# print p_value to the console
p_value
```

Hypothesis testing and the binomial distribution

So now we know some background on hypothesis testing and the difference between one-sided and two-sided testing, let's apply this knowledge to one of the most common distributions: the binomial distribution. To recap, the binomial distribution deals with discrete random variables and it gives probabilities for counts with binary data.

Let's go back to an example we worked with in earlier labs: the exam of 25 multiple choice questions. Is each question has 5 options, it would make logical sense that the probability of guessing 1 question correctly is 0.2. Now suppose we have a student who answered 12 out of 25 correctly and we believe that this student did better than merely guessing. What could be our corresponding hypotheses?

H0:p=0.20,H1:p>0.20

So now we know our hypotheses, let's actually test them. To test hypotheses and calculate p values, we can use the function pbinom(). Looks familiar, doesn't it? Imagine we want to test the hypothesis that a student who scored 18 out of 25 questions did better than randomly guessing, we can calculate the area under the curve, that is, pbinom(17, size = 25, prob = 0.20). While this formula calculates the area under the curve for values below 17 and equal to 17, we need to know the area ABOVE 17. Because the total probability of all possible scores occuring is 1, we can subtract the probability of scores less than or equal to 17 from the total area of 1, and the remaining value will be the probability of a score that is equal to or larger than 18.

```
#' calculate the probability of answering 12 ore more questions correctly given
#' that the student is merely guessing and store this in the variable p_value
p_value <- round((1 - pbinom(11, size = 25, prob = 0.20)), 2)

# print the probability calculated above to the console
p_value

# assign either accepted or rejected to the variable conclusion
conclusion <- "rejected"
```

In the last exercise, we did a hypothesis test by calculating the p value by using the pbinom() function. However, a more widely used way to do so is to calculate the mean (the expected probability) of our distribution and its standard deviation and to verify how many standard deviations the observed probability is removed from the expected probability (the z score). Because we usually test our hypothesis using a sample, we work with the sampling distribution instead of the population distribution. This means that we use the standard error, rather than the standard deviation. Recall that the formula for the standard error for a binomial distribution was the following: sqrt(p(1-p)/n)

https://stats.stackexchange.com/questions/29641/standard-error-for-the-mean-of-a-sample-of-binomial-random-variables

It's easy to get two binomial distributions confused:

distribution of number of successes
distribution of the proportion of successes

```
# calculate the mean (expected probability) and assign it to a variable called average
average <- 0.2

# calculate the standard error and assign it to a variable called se
se <- round(sqrt(average*(1-average)/25), 2)

# calculate the z value and assign it to a variable z_value
z_value <- round((12/25 - 0.2)/se, 2)

# calculate the p value and store it in a variable p_value
p_value <- round(pnorm(z_value, lower.tail = FALSE), 2)

# print p_value to the console
p_value
```

The t distribution

Often when comparing means of continuous variables we use a t distribution instead of the normal distribution. The main reason to use the t distribution here is because we often have to deal with small samples.

Now image the following example of height: They say that Dutch people are among the tallest in the world with an average male height of 185 centimeters with a standard deviation of 5 centimers. We take a sample of 50 males from this population and find an average height of 186.5 centimeters which is above the population mean. Imagine we want to do a one-sided hypothesis test where we check whether the population mean of Dutch male height is larger than 185 and we use a significance level of 0.05. There are several things we can do now and 1 thing that we must do.

Firstly, we need to calculate the degrees of freedom which refers to the amount of independent samples in the set of data, which is equal to the sample size - 1. Thus, the degrees of freedom here is 50−1=4950−1=49. Secondly, we could either calculate the associated p value or, alternatively, we could calculate the critical cut-off value. The critical cut-off value in this case is the 95th percentile as we are doing a one-sided hypothesis test.

```
# calculate the critical cut off value and store it in a variable called cut_off
cut_off <- round(qt(0.95, 49), 2)

# print cut_off to the console
cut_off
```

Using our example where we had a sample of 50 males with a mean height of 186.5 and a population standard deviation of 5 and population mean of 185, calculate the associated standard error, round this value to two digits and store it in the variable se.

```
# calculate the standard error and store it in the variable se
se <- round(5/sqrt(50), 2)

# calculate the t value and store it in a variable called t_value
t_value <- round((186.5 - 185)/se, 2)

# calculate the p value and store it in a variable called p_value
p_value <- round(pt(t_value, 49, lower.tail = FALSE), 2)

# print p_value to the console
p_value
```

Do you remember how to calculate confidence intervals? If not, let's shortly recap this. You can calculate a confidence interval, say a 95% confidence interval, by taking the mean and adding and subtracting its standard error multiplied by the given t value or z value. Usually confidence intervals are expressed as a two-sided range as we will also do in this exercise.

A 95% confidence intervals can be interpreted as that we are 95% confident that this interval will contain our population statistic. Take our last example where we found a standard error of 0.71, a population mean of 185, and a sample mean of 186.5. As the sample size was 50, our relevant degrees of freedom were 49.

Desired Confidence Interval	Z Score
90% 95% 99%	1.645 1.96 2.576

```
# calculate the t value and store it in the variable t_value
t_value <- qt(0.975, 49)

(186.5-185)/0.71

#' calculate a 95% confidence interval as a vector with two values and store it in a
#' a variable called conf_interval
conf_interval = c(round(186.5 - 0.71*t_value, 2), round(186.5 + 0.71*t_value, 2))

# print conf_interval to the console
conf_interval
```

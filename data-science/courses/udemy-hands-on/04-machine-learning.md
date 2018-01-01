# Chapter 4 - Machine Learning with Python

## Supervised vs. Unsupervised Learning, and Train/Test

Machine learning is algorithms that can learn from data and make predictions
(linear regression fits this definition).

With unsupervised learning the model has no predefined correct answers to learn from.
An example would be clustering of objects into 2 different sets where you don't
know ahead of time what the sets should be (shape, color size etc.). You may
get surprising results and you may find classifications that you didn't even know
about it. Unknown groups of users or movies etc. may emerge.

With supervised learning you have a set of answers for the model to learn from.
As an example you can predict car prices based on car attributes. If you have enough
data you can split it into a training (i.e. 80%) and testing set (i.e 20%). This allows
us to test the model on unseen data. You can use the root mean squared error for evaluation.

You can tune models and measure errors with the train/test approach.
You can also use train/test to avoid overfitting. The train and test data sets
need to be large enough and the selection needs to be random.

Train/test is not infallible. Overfitting can still happen. You can do K-fold cross validation
which means you split your data into K random segments and reserve one segment for testing.
Train each of the K-1 segments and measure against the test set. Take the average of the K-1
r-squared scores.

"R-squared is a statistical measure of how close the data are to the fitted regression line. It is also known as the coefficient of determination, or the coefficient of multiple determination for multiple regression. ... 100% indicates that the model explains all the variability of the response data around its mean"

## Using Train/Test to Prevent Overfitting a Polynomial Regression

Regression is a form of supervised machine learning. Remember to shuffle the data before you split it
so that the selection is random (there are library functions to select train/test data).
Look at the shape of the train/test data to get a feeling for what it's like.

## Bayesian Methods: Concepts

You can use Bayes theorem to build a spam classifier. Bayes theorem is:

```
P(A|B) = P(A)*P(B|A)/P(B)
```

Probability of email being spam if it contains the word "free":

```
P(Spam|Free) = P(Spam)*P(Free|Spam)/P(Free)
```

## [Activity] Implementing a Spam Classifier with Naive Bayes

## K-Means Clustering

Unsupervised learning where you want to create clusters. We split the data into K groups.
Uses only the positions of each data point. Can uncover interesting groupings. Examples:
where do millionaires live, what genres for music/movies fall out of the data? Create your
own stereotypes from demographic data.

## [Activity] Clustering people based on income and age

## Measuring Entropy

## [Activity] Install GraphViz

## Decision Trees: Concepts

## [Activity] Decision Trees: Predicting Hiring Decisions

## Ensemble Learning

## Support Vector Machines (SVM) Overview

## [Activity] Using SVM to cluster people using scikit-learn

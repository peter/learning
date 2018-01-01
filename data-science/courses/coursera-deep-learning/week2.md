# Week 2 - Neural Networks Basics

## Binary Classification

This week we will use logistic regression to make the ideas easier to understand.
Suppose we want to classify an image as either a cat (1) or not a cat (0).

If the image is 64x64 pixels the computer will have three matrices for red,
green, blue (0-255). We arrange the pixels in a single x vector with dimension
64*64*3 = 12288. This means the number of features (nx) is 12288.

Having the feature vectors as columns as columns instead of rows will make
the implementation easier.

```
y - the output label {0, 1}
nx - number of features
x - vector with dimension nx
X - input feature matrix where the x vectors are columns, shape: (nx, m)
(x,y) - labeled training example
Y - the output matrix, shape (1, m)
```

## Logistic Regression

Algorithm used for binary classification problems. Given x we are looking for
a prediction of y, i.e. the probability that y is 1 - P(y=1|x).

```
w - coefficients, nx dimension vector
b - offset
y (hat) = sigmoid(wT*x + b)
sigmoid(z) = 1 / (1 + e^-z) - 0.5 for z = 0, 0 if z is small and 1 if z is large
```

## Logistic Regression Cost Function

We of course want to minimize the error in our predictions so we want the prediction
y (hat) to be as close to y as possible.

One possible loss function is the squared error. However this makes the optimization
problem non-convex so there may be multiple local optima. Alternative loss function:

```
L(yh, y) = -(y*log(yh) + (1-y)*log(1 - yh))
```

If y=1 then you want log(yh) to be as large as possible, i.e. yh as large as possible.
If y=0 then you want log(1-yh) to be as large as possible, i.e. yh as small as possible.

The loss function is the error for a single training example. The cost function
will be the average of loss function values across all examples.

Logistic regression can be viewed as a very small neural network.

## Gradient Descent

We want to find the w, b that minimize the cost function J(w, b).

## Derivatives

## More Derivative Examples

## Computation graph

## Derivatives with a Computation Graph

## Logistic Regression Gradient Descent

## Gradient Descent on m Examples

## Vectorization

## More Vectorization Examples

## Vectorizing Logistic Regression

## Vectorizing Logistic Regressions Gradient Output

## Broadcasting in Python

## On python/numpy vectors

## iPython Notebooks

## Explanation of the cost function

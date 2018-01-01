# Week 2. Supervised Machine Learning

## Introduction

In the previous module, you saw a basic sample of supervised machine learning using a k-nearest neighbor classifier, classifying different types of fruit based on their various physical properties.

Machine learning algorithms of this type are called supervised learning algorithms because they use labeled examples in the training set to learn how to predict the labels for new, previously unseen examples.

Learning objectives:

* Learn to do supervised machine learning in Python with scikit-learn
* Learn general principles of supervised machine learning like overfitting

Feature representation means taking a real thing (like a fruit) and converting
it to numbers that the computer can understand. We use the terms instance, sample, example interchangeably. The X matrix holds the feature values. The label is the target value (y) in classification. In regression the target value is a continuous value.

The train/test approach means that we reserve a part of the data set (25%)
for testing, so that we have `X_train, X_test, y_train, y_test`.

An example of binary classification is credit card fraud detection.

Fruit recognition is an example of a multi class classification. The
fruit can only be of one type.

Multi label classification is for example deciding categories/topics for a
web page.

An example of a regression problem is price predictions.

We will spend most of our time with classification. The algorithms we'll
look at are K-Nearest Neighbors and Linear model fit with least squares.

* KNN. Makes few assumptions about structure of data. Gives accurate but
  potentially unstable predictions.
* Linear models. Make strong assumptions about the structure of the data
  and give stable but potentially inaccurate predictions.

With increasing model complexity the training accuracy will increase but
at some point the test accuracy will start to decrease and we are overfitting
and the model doesn't generalize well.

## Generalization, Overfitting, and Underfitting

You can always memorize the training data and have 100% training accuracy.
We make the assumption that the train set has the same properties as the
data that we are trying to predict. Overfitting typically happens when an
overly complex model is applied to an insufficient amount of training data.
The model can't see the global trends and patterns. Understanding and avoiding
overfitting may be the most important thing to learn in supervised machine learning.

Of course, that's not what happens in the real world. What we actually want from a supervised machine learning algorithm is the ability to predict a class or target value correctly on a test set of future examples that haven't been seen before.

This ability to perform well on a held out test set is the algorithms ability to generalize.

How do we know that our trained supervised model will generalize well? In other words, perform well on an unseen test set. Well, typically machine learning makes an important assumption that the future test set has the same properties, or, more technically, as drawn from the same underlying distribution as the training set.

This means that if we observe our model has good accuracy on the training set, and the training set and test sets are similar, we can also expect that it will do well on the test set. Unfortunately, sometimes this doesn't happen due to an important problem known as 'overfitting'. Informally, overfitting typically occurs when we try to fit a complex model with an inadequate amount of training data.

And overfitting model uses its ability to capture complex patterns by being great at predicting lots and lots of specific data samples or areas of local variation in the training set. But it often misses seeing global patterns in the training set that would help it generalize well on the unseen test set. It can't see these more global patterns because, intuitively, there's not enough data to constrain the model to respect these global trends.

Example of overfitting - using polynomial with too many degrees.

Example of overfitting - KNN with too high K value.

## Datasets

The synthetic dataset we'll use, for illustration purposes are typically low dimensional examples. Because they only use a small number of features, typically one or two. This makes them easy to explain and visualize.

Many real world datasets, on the other hand have a higher dimensional feature space. In other words they have dozens, hundreds, or even thousands, or millions of features. So some of the intuition we gain from looking at low dimensional examples doesn't always translate to high dimensional datasets, and we'll discuss that a bit more later.

For example, high dimensional data sets in some sense have most of their data in corners with lots of empty space and that's kind of difficult to visualize. You can use `from sklearn.dataset import make_regression` to generate
data for a scatter plot.

The color of each point shows the classification. Are the points linearly seperable? You can use the function
`make_classification`.

Features: width, height, mass, color
Classes: apple, mandarin, orange, lemon

## K-Nearest Neighbors: Classification and Regression

Let's recall that, for classification, the k-Nearest Neighbor Classifier simply memorizes the entire training set. And then to classify a new instance does 3 steps.

First, it finds the k-Nearest most similar instances to the new instance in the training set.

Then it gets the labels of those training instances. And then it predicts the label of the new instance as a function of the nearby training labels typically by a simple majority vote.

So the k-Nearest Neighbor's Classifier with k = 1, you can see that the decision boundaries that derived from that prediction are quite jagged and have high variance. This is an example of a model, classification model, it has high model complexity. And in fact, you can see that the one nearest neighbors classifier is over-fitting the training data in this case. It's trying to get correct predictions for every single training point while ignoring the general this trend between the two classes

And here is what happens when we increase k from 1 to 11. Now the classifier must combine the votes of the 11 nearest points, not just 1. So single training data points no longer have as dramatic an influence on the prediction. The result is a much smoother decision boundary, which represents a model with lower model complexity where the decision boundary has much less variance. Actually if we increased k even higher to be the total number of points in the training set, the result would be a single decision region where all predictions would be the most frequent class in the training data.

Starting on the left when k = 1, the regression model fits the training data perfectly with a r-squared score of 1.0. But it's very bad at predicting the target values for new data samples, as reflected in the r-squared test score of only 0.155. Finally in this series, the model with k = 15 has the best test set performance, with an r-squared score of 0.485. Increasing k much further however to k = 55, results in both the training and test set scores dropping back down to lower levels, as the model now starts to under-fit. In other words, it's too simple to do well, even on the training data.

The R^2 (0-1) score is called the coefficient of determination. The 0 value
represents the mean value.

KNN can be a baseline against which you compare the performance of other algorithms. The KNN approach has problems if you have a very high number of features. The main parameters of KNN are N and the metric (euclidian).

## Linear Regression: Least-Squares

b is the intercept and w is the slope.

Ordinary least squares (OLS).

```
y = b + w1*x1 + ... + wn*xn
```

In learning we optimize the objective function and minimize the loss function.

```python
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X_R1, y_R1, random_state = 0)
linreg = LinearRegression().fit(X_train, y_train)
linreg.intercept_
linreg.coef_
linreg.score(X_train, y_train)
linreg.score(X_test, y_test)
```

## Linear Regression: Ridge, Lasso, and Polynomial Regression

Ridge regression uses the same least-squares criterion, but with one difference. During the training phase, it adds a penalty for feature weights, the WI values that are too large as shown in the equation here. You'll see that large weights means mathematically that the sum of their squared values is large.

This addition of a penalty term to a learning algorithm's objective function is called Regularisation. Regularisation is an extremely important concept in machine learning. It's a way to prevent overfitting, and thus, improve the likely generalization performance of a model, by restricting the models possible parameter settings.

Ridge regression adds to the OLS error the sum of squares of the w coefficients so
it favors those being small. The w sum of sqares is multiplied by a weight called alpha. The default setting for alpha is 1.0 and a setting of 0 represents OLS.

```python
from sklearn.linear_model import Ridge
```

For Ridge to work well we need to normalize the feature values so that the penalty
is applied more fairly. MinMax scaling is (x-xmin)/(xmax - xmin).

```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
```

Do not fit the scaler using any part of the test data.

There is usually an intermediate model complexity that balances under and over fitting.

You can also use Lasso regression with an L1 penalty which is the sum of the absolute
values of the w coefficients. The results are noticably different and sparse solution
that is easier to interpret.

The alpha value is the regularization parameter.

Polynomial feature transformation:

```
(x0, x1) -> (x0, x1, x0^2, x0*x1, x1^2)
```

And in effect, adding these extra polynomial features allows us a much richer set of complex functions that we can use to fit to the data. So you can think of this intuitively as allowing polynomials to be fit to the training data instead of simply a straight line, but using the same least-squares criterion that minimizes mean squared error. We'll see later that this approach of adding new features like polynomial features is also very effective with classification. And we'll look at this kind of transformation again in kernelized support vector machines. When we add these new polynomial features, we're essentially adding to the model's ability to capture interactions between the different variables by adding them as features to the linear model. For example, it may be that housing prices vary as a quadratic function of both the lat size that a house sits on, and the amount of taxes paid on the property as a theoretical example. A simple linear model could not capture this nonlinear relationship, but by adding nonlinear features like polynomials to the linear regression model, we can capture this nonlinearity. Or generally, we can use other types of nonlinear feature transformations beyond just polynomials. This is beyond the scope of this course but technically these are called nonlinear basis functions for regression, and are widely used.

Of course, one side effect of adding lots of new features especially when we're taking every possible combination of K variables, is that these more complex models have the potential for overfitting. So in practice, polynomial regression is often done with a regularized learning method like ridge regression.

## Logistic Regression

We're now going to look at a second supervised learning method that in spite of being called a regression measure, is actually used for classification and it’s called logistic regression.

Logistic regression can be seen as a kind of generalized linear model.

However, unlike ordinary linear regression, in it's most basic form logistic repressions target value is a binary variable instead of a continuous value.

There are flavors of logistic regression that can also be used in cases where the target value to be predicted is a multi class categorical variable, not just binary. But for now we'll focus on the simple binary case of logistic regression.

Linear regression predicts a real valued output y based on a weighted sum of input variables or features xi, plus a constant b term.

```
y = b + w1*x1 + ... wn*xn
```

The logistic function is a non linear s-shaped function. This is applied to
the linear function output to produce y - between 0 and 1, interpreted as the
probability the input belongs to the positive class given its input features x.

Probability of passing an exam (y, positive, 0 or 1) based on number of study hours x.

"Logistic functions model resource limited exponential growth."

It can be important to normalize all features so they are on the same scale.

Apple/not-apple classification.

The C-parameter - higher values correspond to overfitting. The default value is 1.

"L1-norm loss function is also known as least absolute deviations (LAD)"

"L2-norm loss function is also known as least squares error (LSE)"

"The method of least absolute deviations finds applications in many areas, due to its robustness compared to the least squares method. Least absolute deviations is robust in that it is resistant to outliers in the data. This may be helpful in studies where outliers may be safely and effectively ignored. If it is important to pay attention to any and all outliers, the method of least squares is a better choice."

http://www.chioka.in/differences-between-l1-and-l2-as-loss-function-and-regularization

"Sparsity refers to that only very few entries in a matrix (or vector) is non-zero. L1-norm has the property of producing many coefficients with zero values or very small values with few large coefficients."

## Linear Classifiers: Support Vector Machines

Let's look at how linear models are also used for classification, starting with binary classification.

This approach to prediction uses the same linear functional form as we saw for regression. But instead of predicting a continuous target value, we take the output of the linear function and apply the sign function to produce a binary output with two possible values, corresponding to the two possible class labels.

If the target value is greater than zero, the function returns plus one and if it's less than zero, the function returns minus one. Here's a specific example.

## Kernelized Support Vector Machines

We saw earlier how linear support vector machines served as effective classifiers for some datasets, by finding a decision boundary with maximum margin between the classes.

Linear support vector machines worked well for simpler kinds of classification problems, where the classes were linearly separable or close to linearly separable like this example on the left.

But with real data, many classification problems aren't this easy.

Basically, kernelized support vector machines, which I'll just call SVMs, can provide more complex models that can go beyond linear decision boundaries.

In essence, one way to think about what kernelized SVMs do, is they take the original input data space and transform it to a new higher dimensional feature space, where it becomes much easier to classify the transform to data using a linear classifier.

There are lots of different possible transformations we could apply to data. And the different kernels available for the kernelized SVM correspond to different transformations. Here we're going to focus mainly on what's called the radial basis function kernel, which we'll abbreviate as RBF.
We'll also look briefly at a polynomial kernel.

A kernel is a similarity measure between data points.

http://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html

Intuitively, the gamma parameter defines how far the influence of a single training example reaches, with low values meaning ‘far’ and high values meaning ‘close’.

The C parameter trades off misclassification of training examples against simplicity of the decision surface. A low C makes the decision surface smooth, while a high C aims at classifying all training examples correctly by giving the model freedom to select more samples as support vectors.

The C parameter tells the SVM optimization how much you want to avoid misclassifying each training example. For large values of C, the optimization will choose a smaller-margin hyperplane if that hyperplane does a better job of getting all the training points classified correctly. Conversely, a very small value of C will cause the optimizer to look for a larger-margin separating hyperplane, even if that hyperplane misclassifies more points. For very tiny values of C, you should get misclassified examples, often even if your training data is linearly separable

## Cross Validation

So far we've seen a number of supervised learning methods, and when applying you to these methods we followed a consistent series of steps. First, partitioning the data set into training and test sets using the Train/Test split function. Then, calling the Fit Method on the training set to estimate the model. And finally, applying the model by using the Predict Method to estimate a target value for the new data instances, or by using the Score Method to evaluate the trained model's performance on the test set. Let's remember that the reason we divided the original data into training and test sets was to use the test set as a way to estimate how well the model trained on the training data would generalize to new previously unseen data.

Well, you may have noticed for example by choosing different values for the random state seed parameter in the Train/Test split function, when you're working on some examples or assignments, that the accuracy score you get from running a classifier can vary quite a bit just by chance depending on the specific samples that happen to end up in the training set. Cross-validation basically gives more stable and reliable estimates of how the classifiers likely to perform on average by running multiple different training test splits and then averaging the results, instead of relying entirely on a single particular training set.

The most common type of cross-validation is k-fold cross-validation most commonly with K set to 5 or 10.

For example, to do five-fold cross-validation, the original dataset is partitioned into five parts of equal or close to equal size. Each of these parts is called a "fold". Then a series of five models is trained one per fold. The first model: Model one, is trained using folds 2 through 5 as the training set and evaluated using fold 1 as the test set. The second model: Model 2, is trained using Folds 1, 3, 4, and 5 as the training set, and evaluated using Fold 2 as the test set, and so on.

It's typical to then compute the mean of all the accuracy scores across the folds and report the mean cross-validation score as a measure of how accurate we can expect the model to be on average.

One benefit of computing the accuracy of a model on multiple splits instead of a single split, is that it gives us potentially useful information about how sensitive the model is to the nature of the specific training set.

if we perform k-fold cross-validation and we don't compute the fold results in parallel, it'll take about k times as long to get the accuracy scores as it would with just one Train/Test split.

Stratified folding is a technique that tries to preserve the proportion of labels/classes
in the full data set.

## Decision Trees

Decision trees are a popular supervised learning method that like many other learning methods we've seen, can be used for both regression and classification. Decision trees are easy to use and understand and are often a good exploratory method if you're interested in getting a better idea about what the influential features are in your dataset.

Basically, decision trees learn a series of explicit if then rules on feature values that result in a decision that predicts the target value. Here's a simple example. Suppose we're playing a game where one person is thinking of one of several possible objects so let's say, an automobile, a bus, an airplane, a bird, an elephant and a dog. A second person has to guess the identity of that thing by asking as few yes or no questions as possible up to a limit of no more than say, 10 questions. Suppose the first person secretly thinks of an automobile. So one of the first questions the second person might ask is, "Is it alive?" Intuitively, we know that this type of broad question is much more informative and helps eliminate a larger set of possibilities early on, compared to asking a more specific question right away like, "does it have orange fur with black stripes?" The more specific questions might be useful later once we've narrowed the class of things down to particular animals or vehicles, for example. If we think of the property of being alive as a binary feature of an object and the property of having orange fur with black stripes as another feature, we can say that the is a live feature is more informative at an early stage of guessing and thus would appear higher in our tree of questions.

We can generalize this idea of finding a set of rules that can learn to categorize an object into the correct category to many other classification tasks. For example, we're going to look at a classification task next that involves finding rules that can predict what species a particular flower is, based on measurements of certain parts of the flower. Rather than try to figure out these rules manually for every task, there are supervised algorithms that can learn them for us in a way that gets to an accurate decision quickly, which we'll look at now. Let's start by looking at a famous dataset in machine learning called the iris dataset

For continous data the binary questions becomes a check of whether the value above or below a threshold. An informative split separates the classes/labels well. There a number of criteria
used to evaluate the split, one is called information gain (change in information entropy).

When used for regression the predicted value is the mean value of the target values in the leaf node.

We can control model complexity with the `max_depth` and `max_leaf_nodes` parameters.

You can use `plot_decision_tree` function in the course material to visualize decision trees (uses graphviz).

Feature importance is a number between 0 and 1 and measures how accurately the feature
predicts the target value. The sum of all feature importances is 1. You can extract
the feature importances with the `feature_importances_` attribute. The most important
features will be at the top of the tree. A low value in importance doesn't necessarily
mean that the feature doesn't correlate with the target but it may correlate with other
features and thus not provide much additional information and therefore end up far down
in the tree.

http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html

## Assignment

In this assignment you'll explore the relationship between model complexity and generalization performance, by adjusting key parameters of various supervised learning models. Part 1 of this assignment will look at regression and Part 2 will look at classification.

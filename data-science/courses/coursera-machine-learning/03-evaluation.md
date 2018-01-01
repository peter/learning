# Week 3. Evaluation

## Learning Objectives

* Understand why accuracy alone can be an inadequate metric for getting a more complete picture of a classifier's performance
* Understand the motivation and definition of a variety of important evaluation metrics in machine learning and how to interpret the results of using a given evaluation metric
* Optimize a machine learning algorithm using a specific evaluation metric appropriate for a given task

## Model Evaluation and Selection

Iterative process of machine learning: Represent -> Train -> Evaluate -> Refine

Accuracy of a model may not be sufficient since all errors may not have an equal
cost to the business or project. Overall goal may be revenue, user satisfaction,
or survival rates (in medicine). Accuracy is defined as the total ratio of correct predictions.

Suppose you have a binary classification problem with 1000 examples where only
one in a thousand is positive. This is called an unbalanced classification scenario.

In particular, let's assume that we have an e-commerce application. Where for every 1,000 randomly sampled product items, one of them is relevant to a user's need and the other 999 are not relevant.
And after you've finished the development, you measure its accuracy on the test set to be 99.9%. At first, that might seem to be amazingly good, right? That's incredibly close to perfect. But let's compare that to a dummy classifier that always just predicts the most likely class, namely, the not relevant class. In other words, no matter what the actual instance is, the dummy classifier will always predict that an item is not relevant. So if we have a test set that has 1,000 items, on average 999 of them will be not relevant anyway. So our dummy classifier will correctly predict the not relevant label for all of those 999 items. And so the accuracy of the dummy classifier is also going to be 99.9%. So in reality our own classifier's performance isn't impressive at all. It's no better than just always predicting The majority class without even looking at the data.

Binary prediction outcomes are shown in the confusion matrix:

TN (True Negative), FP (False Positive)
FN (False Negative), TP (True Negative)

There is one true outcome per row and one predicted outcome per column. Success
cases are along the diagonal. For a multi class classification the matrix
would have as many rows and columns as classes.

## Basic Evaluation Metrics

There is a classic tradeoff between precision and recall:

```
Precision (0-1) = TP/(TP + FP)
Recall (0-1) = TP/(TP + FN)
```

Examples of recall oriented tasks: tumor detection (cost of false negative high)
Examples of precision oriented task: search engine, document classification (cost of false positive high)

The F1 score combines precision and recall in a harmonic mean:

```
F1 = 2*Precision*Recall/(Precision + Recall)
```

The F Beta score allows a beta weight towards recall or precision in the combined score.

The scores are available in `sklearn.metrics`.

## Precision-Recall and ROC Curves

You can plot recall (y-axis) against precision (x-axis) for given models/parameters.

The ROC curve shows true positive rate (y-axis) against false positive rate (x-axis).
The ideal point is in the upper left corner. The diagonal represents a random guess
for a binary classification and this serves as a baseline. The model curve should
be above the diagonal. We can measure the area under the ROC curve, AUC, and we
want this area to approach 1.

http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html

* micro precision: Calculate metrics globally by counting the total true positives, false negatives and false positives.
* macro precision: Calculate metrics for each label, and find their unweighted mean. This does not take label imbalance into account.

Grid Search: http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html

## Regression Evaluation

For regression evaluation R^2 is mostly adequate. There are alternatives such
as median absolute error that is less sensitive to outliers. You should think
about the cost of different types of errors.

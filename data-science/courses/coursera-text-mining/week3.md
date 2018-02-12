# Week 3 - Classification of Text

## Text Classification (Supervised Learning of Text)

Problem - figuring out which topic a text relates to (i.e. nephrology, neurology, podiatry)

Spelling correction is contextual, i.e. "weather" and "whether".

In supervised learning you have a training phase where the model learns from
labeled instances. Each instance has a set of features X and the model learns an
input-output mapping X->y. As part of the testing phase there is also validation
(i.e. hold out data) that can be used to tune model parameters.

There is also an inference phase where you test/evaulate the trained model.

Questions to ask in supervised learning:

* What are the features and how to you represent them?
* What is the classification model?
* What are the model parameters?

## Identifying Features from Text

Text features can be pulled in at different granularities. The most common construct
is the words. English has around 40 thousand unique words.

How do you handle stop words, upper case / lower case (normalization)?
How do you handle stemming and lemmatization?
How do you handle synonyms (groups of words)?

"White House" is different from "white house".

## Naive Bayes Classifiers

Suppose you want to classify search queries and you get the query "Python".
Does it refer to the snake (Zoology), or the programming language (Computer Science),
or Monty Python (Entertainment). Suppose the query is "Python download".
Most common case: zoology.

```
P(y=CS|"Python") = P(y=CS) * P("Python" | y=CS) / P("Python")
```

## Support Vector Machines

Let's think about classifying a text as nephrology, neurology, podiatry.
Let's think about sentiment analysis for a review of a movie. You could
then relate words to positive reviews.

Let's suppose there are only two dimensions x1 and x2 and we have instances
in a plot and we are looking for a decision boundary that separates one class
from another (in a binary classification problem). Overfitting here means the
decision boundary is complex and words very well for training data but does not
generalize well to test data. Using a line as decision boundary is very sensitive
to small changes and outliers in the training data. What we use is a maximal
margin classifier.

"In addition to performing linear classification, SVMs can efficiently perform a non-linear classification using what is called the kernel trick, implicitly mapping their inputs into high-dimensional feature spaces."

## Learning Text Classifiers in Python

NLTK interfaces with scikit-learn.

```python
from sklearn import naive_bayes
nb = naive_bayes.MultinomialNB()
nb.fit(X_train, y_train)
predicted_labels = nb.predict(X_test)
metrics.f1_score(test_labels, predicted_labels, average='micro')
```

"The F1 score is the harmonic average of the precision and recall, where an F1 score reaches its best value at 1 (perfect precision and recall) and worst at 0."

"The harmonic mean is one of the three Pythagorean means. For all positive data sets containing at least one pair of nonequal values, the harmonic mean is always the least of the three means,[1] while the arithmetic mean is always the greatest of the three and the geometric mean is always in between."

* [F1 Score](https://en.wikipedia.org/wiki/F1_score)

Support Vector Machine:

```python
from sklearn import svm
m = svm.SVC(kernel='linear', C=0.1)
m.fit(X_train, y_train)
predicted_labels = m.predict(X_test)
```

Model selection:

```python
from klearn import model_selection
X_train, X_test, y_train, y_test = model_selection.test_split(
  train_data, train_labels, test_size=0.2, random_state=0)
```

You are missing out on 20% of data for training with an 80/20 split.
An alternative is to do a five-fold cross validation (each of the five folds are used
once for testing):

```python
predicted_labels = model_selection.cross_val_predict(m, train_data, train_labels, cv=5)
```

```python
from nltk.classify import NaiveBayesClassifier
classifier = NaiveBayesClassifier.train(train_set)
classifier.classify(unlabeled_instance)
classifier.classify_many(unlabeled_instances)
nltk.classify.util.accuracy(classifier, test_set)

from nltk.classify import SklearnClassifier
```

# Week 1. Fundamentals of Machine Learning - Intro to SciKit Learn

## Learning Objectives

* Understand basic machine learning concepts and workflow
* Distinguish between different types of machine learning tasks, based on examples of how they are applied to real-world problems
* Understand how a basic classification algorithm (k-nearest neighbors) learns and makes predictions
* Build and evaluate a basic k-nearest neighbors classifier on an example dataset using Python and scikit-learn

## Introduction

"In a lot of cases when a computing problem needs to be solved, for example, storing and retrieving data from a database, the way we often address it is to write a program that manually specifies a series of programming steps that need to be run to solve that particular problem.

This works great for the vast number of computer science problems that are out there. However, not all problems lend themselves to being solved effectively by writing a handcrafted program or set of rules.

For example, how would you write down a set of rules in a programming language for accurately converting human speech to text? A process known as speech recognition which is now available on millions of smart phones or used in customer support systems all over the world.

Given how a subtle and complex human speech is with the huge variety of different pronunciations, vocabulary, accents, and so forth.

Writing a set of program rules by hand that could recognize portions of an audio signal and decide which words were in the signal and so forth would be a gargantuan task.

And even then, it would still likely be inflexible and not very robust at recognizing different types of speech.

Moreover, if we needed to customize the system so it could recognize new words or other features that we hadn't encoded in our existing rules, we'd have to write a whole new set of rules, which would be a prohibitively difficult task.

Machine Learning, on the other hand, gives us the technology that allows us to automatically learn these complex rules efficiently from labelled examples, called, training data, in a way that is much more accurate and flexible than attempting to program all the rules by hand."

"So the basic problem of machine learning is to explore how computers can program themselves to perform a task, and to improve their performance automatically as they gain more experience."

Example applications:

* Spam protection
* Fraud detection (credit cards)
* Recommendations (movies, music, ads, shopping etc.)
* Image recognition
* Speech recognition
* Search engines
* Reasearch in economics in optimal markets etc.
* Research in psychology in human learning

Machine Learning draws heavily on statistics and computer science.

"Think about how quickly a commercial search engine can match your query against billions of web pages and almost instantly return a set of useful results. That's an ideal illustration of the power of combining statistical methods with computer science."

"Over 85% of handwritten mail is sorted automatically with very high accuracy by the United States Postal Service."

"there is a very exciting trend happening where ready to use machine learning algorithms for speech recognition, language translation, text classifications and many other tasks, are now being offered as web based services on cloud computing platforms"

## Key Concepts in Machine Learning

Machine learning has two main parts:

### Supervised Learning

The goal is to predict an output variable associated with a given input.

If the output is a category of finite possibilities (i.e. fraudulent, not fraudulent)
we call this a classification problem and the function that we learn is called
the classifier.

If the output is a real valued number (i.e. how many seconds it takes a car to
accelerate to 100 km/h) then we call the problem a regression problem and what
we are learning is a regression function.

The input data table is denoted with X and the target value is Y (labels).
The training examples (correct answers) are used to train the algorithm.

There are many algorithms to choose from.

You split your data into train/test sets.

### Unsupervised Learning

There is only input data, there is no given output (labels).

* Finding clusters of similar users
* Visualizing structure or producing summaries
* Anamoly and outlier detection, detecting abnormal behaviour (intrusion detection etc.)

### Basic Workflow

1. Representation. Definition of the problem. Feature representation. Algorithm/classifier selection.
2. Evaluation. What criterion distinguishes good/bad classifier? Accuracy.
3. Optimization. Search for settings/parameters that give the best classifier (i.e. k values for k nearest neighbour).

## Python Tools

* [scikit-learn](http://scikit-learn.org) - Built on NumPy, SciPy, and matplotlib
* [scipy](https://www.scipy.org/scipylib/index.html)
* [numpy](http://www.numpy.org/) - multidimensional arrays
* [pandas](http://pandas.pydata.org) - data frames for tabular data (spreadsheet type data)
* [matplotlib pyplot](https://matplotlib.org/api/pyplot_api.html) - MATLAB-like plotting framework

```python
ipython
%pylab
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

x = np.arange(0, 5, 0.1);
y = np.sin(x)
plt.plot(x, y)
```

You can use [nbopen](https://github.com/takluyver/nbopen) to open iPyhton notebooks
from the terminal. Install python with [anaconda](https://www.anaconda.com/download/#macos) and put `/anaconda/bin` first in your PATH (Linux/Mac).

## Example Problem

The dataset we're going to use is a small, very simple, example dataset derived from one originally created by Dr. Iain Murray at the University of Edinburgh for the task of training a classifier to distinguish between different types of fruit.

So to create the original dataset, Dr. Murray went to a nearby store, bought a few dozen oranges, lemons, and apples of different varieties, and recorded their measurements in a table. So he sat down and he looked at the height and the width, estimated their mass, and so forth.

rotten orange detection use ultraviolet light that can detect interior decay

So, looking at this data frame, we can see that it contains 59 rows corresponding to 59 different pieces of fruit

So to create training and test sets from a input dataset, Scikit-learn provides a handy function that will do this split for us, called, not surprisingly, train test split.

This function randomly shuffles the dataset and splits off a certain percentage of the input samples for use as a training set, and then puts the remaining samples into a different variable for use as a test set. So in this example, we're using a 75-25% split of training versus test data.

## Examining the Data

In general, if you're thinking about applying machine learning to a data set, it's a really good first step to actually look at the data set first, maybe using some simple visualization methods.

First, it's helpful to simply get a sense for what's actually in the data set. because it may be that in inspecting the features of each object, you might get a better idea of what type of cleaning or preprocessing still needs to be done to the data. And of the range of values or the distribution of values that is typical for each attribute or each feature.

For example, you might discover that the data set you got has a single column with person's name that still needs to be split into two separate first and last name columns. For example, if you're using the name as one of the prediction feature, that might be important. Second, you might notice missing or noisy data. Or maybe some specific inconsistencies, such as the wrong data type being used for a column. Incorrect or inconsistent units of measurement for a particular column, particular feature. Or maybe you'll notice that there aren't enough examples of a particular labeled class.

And finally, it might turn out that for your data set, your problem is actually solvable without machine learning.

the first visualization tool we'll use is called a feature pair plot. So this plot shows all possible pairs of features and produces a scatter plot for each pair, showing how the features are correlated to each other or not.

Just by looking at this pair plot, we can already see that some pairs of features, like the height and color score in the top right corner here, are good for separating out different classes of fruit. And this suggests that a classifier that was trained using those features could likely learn to classify the various fruit types reasonably well.

## K-Nearest Neighbors Classification

Now that we've gotten a sense for what's in our data set, as a simple example to get started, we're going to use this data set to train a classifier that will automatically identify any future pieces of fruit that might come our way. Based on the features available to the classifier such as the object's color, size and mass. To do this, we'll use a popular and easy to understand type of machine learning algorithm known as k-nearest neighbors or k-NN. The K-Nearest Neighbors algorithm can be used for classification and regression. Though, here we'll focus for the time being on using it for classification. k-NN classifiers are an example of what's called instance based or memory based supervised learning. What this means is that instance based learning methods work by memorizing the labeled examples that they see in the training set. And then they use those memorized examples to classify new objects later.

So, because this is a k-nearest neighbor classifier, and we are looking at the case where k = 1, we can see that the class boundaries here, the decision boundaries.

For larger values of K, the areas assigned to different classes are smoother and not as fragmented and more robust to noise in the individual points. But possibly with some mistakes, more mistakes in individual points. This is an example of what's known as the bias variance tradeoff. And we'll look at that phenomenon and its implications in more depth in next week's class.

* Value of k (number of neighbours)
* Distance metric (Euclidian)
* Weighting of neighbours
* Method for aggregating classes

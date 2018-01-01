# Week 1 - Introduction to deep learning

## Learning Objectives

* Understand the major trends driving the rise of deep learning.
* Be able to explain how deep learning is applied to supervised learning.
* Understand what are the major categories of models (such as CNNs and RNNs), and when they should be applied.
* Be able to recognize the basics of when deep learning will (or will not) work well.

## What is a Neural Network

Let's say you want to fit a function to predict housing prices with the size
of the house. You can plot the price on the y-axis and the size on the x-axis
and try to fit a line to the points. This is a simple example of a Neural Network:

```
size -> (neuron) -> price
```

The price linear function has a minimum of zero and is a [ReLu function](https://en.wikipedia.org/wiki/Rectifier_(neural_networks)):

```
f(x) = max(0, x)
```

You can also imagine that `size` and `number of bedrooms` predicts family size, and that
`zip code` predicts walkability, and that `wealth` predicts school qualities, and that
these three intermediate features in turn predict the price. Let x be the four inputs
and y be the price. Instead of
assuming or specifying what the intermediate features are (`family size`, `walkability`, `school qualities`) we will let these be neurons that can depend on all four input features.
Neural networks are remarkably good at figuring out functions that map from x to y.

## Supervised Learning with Neural Networks

In supervised learning you have some input x and you want to learn the function
to some output y. Applications:

* Real estate pricing (Standard NN)
* Online advertising (Standard NN). The most lucrative application of neural networks today is in
online advertising - figuring out which ads to show to users (this has a direct impact on the bottom line).
* Image tagging (CNN)
* Speech recognition (RNN)
* Machien translation (RNN)
* Autonomous driving

Types of NN:

* Standard NN
* CNN - Convolutional Neural Network
* RNN - Recurrant Neural Network

Types of data:

* Structured. Data in databases.
* Unstructured. Audio, images, natural language text.

Neural networks enables computers to understand unstructured better than what was
possible just a few years ago.

The basic ideas of NN have been around for decades.

## Why is Deep Learning Taking Off?

Deep learning is taking off now since we now have the amount of data and the
computing power that is needed to make deep learning perform well.

Traditional ML techniques such as SVM have more diminishing returns in performance
as a function of the amount of data.

To get better performance you can use more data and use a large neural network
(a lot of hidden units). So scale has been driving the development of Deep Learning.

By amount of data (labeled m) we refer to the size of labeled data (x, y).
In the small data set region the engineering of features is more important for
performance.

There has also been a lot of algorithmic innovation, for examples in making
neural networks function. For example switching from a
[sigmoid function](https://en.wikipedia.org/wiki/Sigmoid_function) to a ReLu
function.

The process of training a Neural Network is very iterative (idea - code - experiment).
This process is much faster and more efficient if training your network takes 2 minutes
rather than a month.

Innovation in hardware like GPUs has helped this progress.

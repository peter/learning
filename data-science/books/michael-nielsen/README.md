# Neural Networks and Deep Learning - Michael Nielsen

## Introduction

"Neural networks are one of the most beautiful programming paradigms ever invented. In the conventional approach to programming, we tell the computer what to do, breaking big problems up into many small, precisely defined tasks that the computer can easily perform. By contrast, in a neural network we don't tell the computer how to solve our problem. Instead, it learns from observational data, figuring out its own solution to the problem at hand."

"Automatically learning from data sounds promising. However, until 2006 we didn't know how to train neural networks to surpass more traditional approaches, except for a few specialized problems. What changed in 2006 was the discovery of techniques for learning in so-called deep neural networks. These techniques are now known as deep learning. They've been developed further, and today deep neural networks and deep learning achieve outstanding performance on many important problems in computer vision, speech recognition, and natural language processing. They're being deployed on a large scale by companies such as Google, Microsoft, and Facebook."

"One conviction underlying the book is that it's better to obtain a solid understanding of the core principles of neural networks and deep learning"

"This means the book is emphatically not a tutorial in how to use some particular neural network library"

"We'll learn the core principles behind neural networks and deep learning by attacking a concrete problem: the problem of teaching a computer to recognize handwritten digits."

## Using neural nets to recognize handwritten digits

http://neuralnetworksanddeeplearning.com/chap1.html

"we humans are stupendously, astoundingly good at making sense of what our eyes show us. But nearly all that work is done unconsciously. And so we don't usually appreciate how tough a problem our visual systems solve."

"In each hemisphere of our brain, humans have a primary visual cortex, also known as V1, containing 140 million neurons, with tens of billions of connections between them. And yet human vision involves not just V1, but an entire series of visual cortices - V2, V3, V4, and V5 - doing progressively more complex image processing."

"Simple intuitions about how we recognize shapes - "a 9 has a loop at the top, and a vertical stroke in the bottom right" - turn out to be not so simple to express algorithmically. When you try to make such rules precise, you quickly get lost in a morass of exceptions and caveats and special cases. It seems hopeless."

"The program is just 74 lines long, and uses no special neural network libraries. But this short program can recognize digits with an accuracy over 96 percent, without human intervention. Furthermore, in later chapters we'll develop ideas which can improve accuracy to over 99 percent. In fact, the best commercial neural networks are now so good that they are used by banks to process cheques, and by post offices to recognize addresses."

### Perceptrons

"The neuron's output, 0 or 1, is determined by whether the weighted sum(wj*xj) is less than or greater than some threshold value."

"That's the basic mathematical model. A way you can think about the perceptron is that it's a device that makes decisions by weighing up evidence."

"the first column of perceptrons - what we'll call the first layer of perceptrons - is making three very simple decisions, by weighing the input evidence. What about the perceptrons in the second layer? Each of those perceptrons is making a decision by weighing up the results from the first layer of decision-making. In this way a perceptron in the second layer can make a decision at a more complex and more abstract level than perceptrons in the first layer. And even more complex decisions can be made by the perceptron in the third layer. In this way, a many-layer network of perceptrons can engage in sophisticated decision making."

Alternative formulation with bias:

```
output: 0 if w*x + b <= 0
output: 1 if w*x + b > 0
```

"For a perceptron with a really big bias, it's extremely easy for the perceptron to output a 11. But if the bias is very negative, then it's difficult for the perceptron to output a 1"

A perceptron can also implement a NAND gate if you have weights w1=-2 and w2=-2 and bias 3, you then get:

```
(0, 0) -> 1
(0, 1) -> 1
(1, 0) -> 1
(1, 1) -> 0
```

"The NAND example shows that we can use perceptrons to compute simple logical functions. In fact, we can use networks of perceptrons to compute any logical function at all. The reason is that the NAND gate is universal for computation, that is, we can build any computation up out of NAND gates."

### Sigmoid Neurons

"To see how learning might work, suppose we make a small change in some weight (or bias) in the network. What we'd like is for this small change in weight to cause only a small corresponding change in the output from the network. As we'll see in a moment, this property will make learning possible."

"For example, suppose the network was mistakenly classifying an image as an "8" when it should be a "9". We could figure out how to make a small change in the weights and biases so the network gets a little closer to classifying the image as a "9". And then we'd repeat this, changing the weights and biases over and over to produce better and better output. The network would be learning."

"The problem is that this isn't what happens when our network contains perceptrons. In fact, a small change in the weights or bias of any single perceptron in the network can sometimes cause the output of that perceptron to completely flip, say from 00 to 11. That flip may then cause the behaviour of the rest of the network to completely change in some very complicated way."

"Sigmoid neurons are similar to perceptrons, but modified so that small changes in their weights and bias cause only a small change in their output. That's the crucial fact which will allow a network of sigmoid neurons to learn."

### Gradient Descent

"An idea called stochastic gradient descent can be used to speed up learning. The idea is to estimate the gradient ∇C∇C by computing ∇Cx∇Cx for a small sample of randomly chosen training inputs. By averaging over this small sample it turns out that we can quickly get a good estimate of the true gradient ∇C∇C, and this helps speed up gradient descent, and thus learning"

### Implementation

"once we've trained a network it can be run very quickly indeed, on almost any computing platform. For example, once we've learned a good set of weights and biases for a network, it can easily be ported to run in Javascript in a web browser, or as a native app on a mobile device."

"In general, debugging a neural network can be challenging. This is especially true when the initial choice of hyper-parameters produces results no better than random noise."

"The lesson to take away from this is that debugging a neural network is not trivial, and, just as for ordinary programming, there is an art to it."


```
import network
import mnist_loader
import os
path = os.path.expanduser('~/src/vendor/neural-networks-and-deep-learning/data/mnist.pkl.gz')
training_data, validation_data, test_data = mnist_loader.load_data_wrapper(path)

type(training_data) # => list
len(training_data) # => 50000
type(training_data[0]) # => tuple
len(training_data[0]) # => 2
type(training_data[0][0]) # =>  numpy.ndarray
len(training_data[0][0]) # => 784 (input)
training_data[0][0].shape # => (784, 1)
type(training_data[0][1]) # =>  numpy.ndarray
len(training_data[0][1]) # => 10 (output)
training_data[0][1].shape # => (10, 1)

test_data[0][0].shape # => (784, 1)
test_data[0][1] # => 7

net = Network([784, 30, 10])
net.train(training_data, 30, 10, 3.0, test_data=test_data)
```

## Resources

* [Book Homepage](http://neuralnetworksanddeeplearning.com)
* [Source Code - Python 2](https://github.com/mnielsen/neural-networks-and-deep-learning)
* [Source Code - Python 3](https://github.com/MichalDanielDobrzanski/DeepLearningPython35)

# Basic Statistics Week 3 - Probability & Randomness

## 3.1 Probability & Randomness

"Before we can understand probability we first have to understand another concept: randomness. The first video explains this concept. It also shows that even though randomness is everywhere around us, humans are nonetheless bad in assessing it."

"Once we understand randomness we can define probability as a way to quantify randomness. The second video explains how this quantification can be accomplished by experiments which record the relative frequency that certain events of interest occur. It follows that probabilities are always larger or equal to zero and smaller or equal to one; and also that the sum of the probabilities for all possible events equals one. Due to the very nature of random events, the experiments may have to continue for a while before the relative frequencies represent the probabilities accurately, but the law of large numbers dictates that it will do so eventually."

"Importantly, whether something is random is not just a property of that phenomenon, but very much also a consequence of our knowledge about it. "

"On one hand, we see all sorts of patterns in what is really random data. There's a word for it, apophenia. And on the other hand, we are unable to make up random data ourselves. "

Random patterns have clusters.

"Another example of over interpreting randomness is the so called gambler's fallacy, the false idea that a random phenomenon can be predicted from a series of preceding random phenomena."

Summary:

* Randomness is not an intrinsic property
* Humans are not good at assessing randomness (over interpretation of randomness - apophenia)

Persistence beats the odds.

The law of large numbers relies on independence, i.e. outcomes are not related.

Suppose there are four sea shells on the beach with equal probability. Suppose you collect 20 shells and look at the propertions. Each probability
is between 0 and 1 and the sum of all probabilities is always 1. Picking a shell is an independent trial.

In reality there is usually interdependence between random events.

* Probability is a way to quantify randomness

## 3.2 Sample space, events & tree diagrams

"The first video explains that all the possible outcomes for the experiment form the so-called sample space, and that elementary or combined outcomes in the experiment are called events. It shows how all events can be organised in a tree-diagram, which helps to understand how events relate to each other. At the same time it provides a clear structure to quantify the probabilities relating to each of these events. The various probability calculations that can be conducted with support of a tree-diagram are further explained in the second video."

## 3.3 Probability & Sets

The selection of ice cream and soft drink in the line to an ice-cream stand are random independent events in a tree. The leaves in the tree represent the sample space. A node in the tree is an event. Assume probability of 0.5 for selecting ice cream and soft drink. At each level of depth in the tree the sum of probabilities is 1 (0.5, 0.25, 0.125)

* Sample space - collection of all possible outcomes for a random phenomenon
* Event - subset of the sample space. Each event has a probability.

Quantify the probability with experiment or make plausible assumptions.

A sample space is an example of a set. Events that do not share any outcomes are called disjoint or mutually exclusive. Multiple events that together fill up the sample space are called collectively or jointly exhaustive.

The probability of the union of several events is the sum of the probabilities of the separate events minus the probability of the intersection among the events.

A set is a collection of distinct items.

The complement of an event is the outcome that the event does not happen.

The Venn diagram of two coin toss (tail/head).

Disjoint events have zero intersection.

For independent events the intersection is the product.

Picking three shells at random, Q/R. Describe: experiment, trial, outcome, event, random variable. Each pick up of a shell is a trial with an outcome. The combinations of outcomes are events. The random variable is the type of shell. The sample space is all possible outcomes. An event could be picking up two or more R shells and its complement is one or zero R shells. The event first shell is R and last shell is R are not disjoint so they overlap. What is the probability of picking up at least two Q shells if Q is 1/3 and R 2/2 probability?

A Union is sum of parts without double counting (subtract intersection, i.e. joint probability).

## 3.4 Conditional probability & Independence

"This lecture introduces quite a few new concepts again: joint probabilities, marginal probabilities and subsequently also conditional probabilities and independence between events or random variables. Finally, the relationship between conditional probabilities in two directions, Bayes' law, is explained."

"Conditional probability is the probability of an event, given that another event occurs"

"Mathematically, the conditional probability of A given B equals the joint probability of A and B, divided by the (marginal) probability of event B."

Gender (M/F) and activity on the beach (resting, playing, swimming). Each person is a case in your data set. The contingency table has gender as rows and activity as columns and totals in the row/column margins. The joint probability is the intersection of gender and activity in each cell. The cells are disjoint, i.e. mutually exclusive, and exhaustive. Each person is put in exactly one cell.

P(A | B) - probability of A given B

P(A | B) = P(A and B) / P(B)

Bayes works for both independent and non-independent events:

P(A | B) = P(B | A)P(A) / P(B)

Two events are independent if P(A | B) = P(A)

* Sample space - all possible outcomes for a random phenomenon
* Event - a subset of the sample space

Disjoint events are mutually exclusive and intersection P(A and B) = 0. The opposite of an event is called the complement.
Collectively exhaustive events fill up the whole sample space and have probability 1.

Venn diagrams are useful for understanding these concepts.

For independent events the intersection is `P(A)*P(B)`.

The marginal probability of an outcome for a variable is the probability for that outcome
without regard for any other variables. They are in the margins of the contingency table.

Gender (male, female) and activity at the beach (resting, playing, swimming).

The terminology includes "experiment", "trial", "event", "outcome", "random variable"

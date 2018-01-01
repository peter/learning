# Week 1 (Functional Programming Principles in Scala)

## 1.1 Programming Paradigms

"The primary objective is to teach you functional programming from first principles"

"you can combine the two paradigms (OO and FP), and it's one of Scala's strengths, that it provides a gradual migration path from a more concise travel-light language to full-functional programming. But in this course we're not going to be gradual, we're going to take a clean break. I'd like to, you to suspend for the time being most of what you know about programming and look at programs with fresh eyes"

Imperative programming:

* Modifying mutable variables with assignments
* Control structures like if-then-else, loops, break, continue, return

John Backus: "Can programming be liberated from the von Neumann style"

In programming we need high level abstractions.

Mutation can destroy useful laws.

In a restricted sense FP means programming without mutation and imperative control structures. In a wider sense FP means focusing on functions and functions being first class values.

Recommended classic reading: [SICP](https://mitpress.mit.edu/sicp)

## 1.2 Elements of Programming

"Every non-trivial language provides primitive expressions that represents the simplest elements of the language. And then some ways to combine expressions and ways to abstract expressions. Abstraction means that we introduce a name for an expression and then further on we can reference the expression by its name."

"This scheme of expression evaluation is called the substitution model. The idea underlying this model is that all evaluation does is reduce an expression to a value. And that reduction can be expressed by a sequence of simple rewriting steps that rewrite the expression term itself until it is a value, very similar to what you would do in algebraic simplification."

"the substitution model, can be applied only to expressions that do not have a side effect."

"Does every expression reduce to a value in a finite number of steps? In fact, the answer is no."

Two different evaluation strategies are call by name and call by value.

## 1.3 Evaluation Strategies and Termination

* [Call by value](https://www.coursera.org/learn/progfun1/lecture/eervR/lecture-1-3-evaluation-strategies-and-termination) - follows the substituation model where function arguments are evaluated before the function body executes.
* Call by name - evaluation of the function arguments are delayed up until the point where they are references and needed in the evaluation of the function body

Call by name and call by value will produce the same results if the evaluations terminate.

In practice call by value is more efficient as it avoids re-computation of function arguments.

## 1.4 Conditionals and Value Definitions

[Video](https://www.coursera.org/learn/progfun1/lecture/f6IQm/lecture-1-4-conditionals-and-value-definitions)

## 1.5 Example: square roots with Newton's method

## 1.6 Blocks and Lexical Scope

## 1.7 Tail Recursion

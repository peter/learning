# Glossary of Terms in Functional Programming and Mathematics

[Functional Programming](https://en.wikipedia.org/wiki/Functional_programming):

"In computer science, functional programming is a programming paradigm—a style of building the structure and elements of computer programs—that treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data. It is a declarative programming paradigm, which means programming is done with expressions[1] or declarations[2] instead of statements. In functional code, the output value of a function depends only on the arguments that are passed to the function, so calling a function f twice with the same value for an argument x will produce the same result f(x) each time; this is in contrast to procedures depending on a local or global state, which may produce different results at different times when called with the same arguments but a different program state. Eliminating side effects, i.e. changes in state that do not depend on the function inputs, can make it much easier to understand and predict the behavior of a program, which is one of the key motivations for the development of functional programming."

## [Algebra](#algebra) [[W](https://en.wikipedia.org/wiki/Algebra)]

"Algebra (from Arabic "al-jabr" meaning "reunion of broken parts"[1]) is one of the broad parts of mathematics, together with number theory, geometry and analysis. In its most general form, algebra is the study of mathematical symbols and the rules for manipulating these symbols;[2] it is a unifying thread of almost all of mathematics"

"algebra is the study of generalizations of arithmetic operations"

"As a single word with an article or in plural, "an algebra" or "algebras" denotes a specific mathematical structure, whose precise definition depends on the author. Usually the structure has an addition, multiplication, and a scalar multiplication (see Algebra over a field). When some authors use the term "algebra", they make a subset of the following additional assumptions: associative, commutative, unital, and/or finite-dimensional."

## [Applicative Functor](#applicative-functor) [[W]()]

"In functional programming, specifically Haskell, an applicative functor is a structure that is like a monad (return, fmap, join) without join, or like a functor with return and fmap. Applicative functors are the programming equivalent of lax monoidal functors with tensorial strength in category theory. In Haskell, applicative functors are implemented in the Applicative type class."

## [Associativity](#associativity) [[W](https://en.wikipedia.org/wiki/Associative_property)]

"In mathematics, the associative property is a property of some binary operations."

```
(2 + 3) + 4 = 2 + (3 + 4) = 9
2 * (3 * 4) = (2 * 3) * 4 = 24
```

""addition and multiplication of real numbers are associative operations"."

## [Calculus](#calculus) [[W](https://en.wikipedia.org/wiki/Calculus)]

"Calculus (from Latin calculus, literally "small pebble used for counting on an abacus")[1] is the mathematical study of continuous change, in the same way that geometry is the study of shape and algebra is the study of generalizations of arithmetic operations."

## [Catamorphism](#catamorphism) [[W](https://en.wikipedia.org/wiki/Catamorphism)]

"In category theory, the concept of catamorphism (from the Greek: κατά "downwards" and μορφή "form, shape") denotes the unique homomorphism from an initial algebra into some other algebra."

## [Category Theory](#category-theory) [[W](https://en.wikipedia.org/wiki/Category_theory)]

"Category theory[1] formalizes mathematical structure and its concepts in terms of a labeled directed graph called a category, whose nodes are called objects whose labelled directed vertices are called arrows (or morphisms). A category has two basic properties: the ability to compose the arrows associatively and the existence of an identity arrow for each object. The language of category theory has been used to formalize concepts of other high-level abstractions such as sets, rings, and groups."

## [Commutativity](#commutativity) [[W](https://en.wikipedia.org/wiki/Commutative_property)]

"In mathematics, a binary operation is commutative if changing the order of the operands does not change the result. It is a fundamental property of many binary operations, and many mathematical proofs depend on it"

"The name is needed because there are operations, such as division and subtraction, that do not have it"

## [Functor](#functor) [[W](https://en.wikipedia.org/wiki/Functor)]

"In mathematics, a functor is a type of mapping between categories arising in category theory. Functors can be thought of as homomorphisms between categories."

## [Homomorphism](#homomorphism) [[W](https://en.wikipedia.org/wiki/Homomorphism)]

"In algebra, a homomorphism is a structure-preserving map between two algebraic structures of the same type (such as two groups, two rings, or two vector spaces). The word homomorphism comes from the ancient Greek language: ὁμός (homos) meaning "same" and μορφή (morphe) meaning "form" or "shape".

Homomorphisms of vector spaces are also called linear maps, and their study is the object of linear algebra."

## [Isomorphism](#isomorphism) [[W](https://en.wikipedia.org/wiki/Isomorphism)]

"In mathematics, an isomorphism (from the Ancient Greek: ἴσος isos "equal", and μορφή morphe "form" or "shape") is a homomorphism or morphism (i.e. a mathematical mapping) that admits an inverse.[note 1] Two mathematical objects are isomorphic if an isomorphism exists between them."

## [Monad](#monad) [[W](https://en.wikipedia.org/wiki/Monad_(functional_programming))]

"In functional programming, a monad is a design pattern that defines how functions, actions, inputs, and outputs can be used together to build generic types,[1] with the following organization:

1. Define a data type, and how values of that data type are combined.
2. Create functions that use the data type, and compose them together into actions, following the rules defined in the first step.
"

"For example, the simple Maybe monad encapsulates variables which may have a null value, representing an option type, and automatically ensures that null values are not passed as arguments to functions that cannot handle them, serving as an alternative programming technique to throwing and catching exceptions when null values arise"

"The monad represents computations with a sequential structure: a monad defines what it means to chain operations together. This enables the programmer to build pipelines that process data in a series of steps (i.e. a series of actions applied to the data), in which each action is decorated with the additional processing rules provided by the monad.[2] A monad is defined by a return operator that creates values, and a bind operator used to link the actions in the pipeline; this definition must follow a set of axioms called monad laws, which are needed for the composition of actions in the pipeline to work properly.

Monads allow a programming style where programs are written by putting together highly composable parts, combining in flexible ways the possible actions that can work on a particular type of data. As such, monads have been described as "programmable semicolons"; a semicolon is the operator used to chain together individual statements in many imperative programming languages,[2] thus the expression implies that extra code will be executed between the actions in the pipeline. Monads have also been explained with a physical metaphor as assembly lines, where a conveyor belt transports data between functional units that transform it one step at a time.[3]

Purely functional programs can use monads to structure procedures that include sequenced operations like those found in structured programming.[4][5] Many common programming concepts can be described in terms of a monad structure without losing the beneficial property of referential transparency, including side effects such as input/output, variable assignment, exception handling, parsing, nondeterminism, concurrency, continuations, or domain-specific languages. This allows these concepts to be defined in a purely functional manner, without major extensions to the language's semantics. Languages like Haskell provide monads in the standard core, allowing programmers to reuse large parts of their formal definition and apply in many different libraries the same interfaces for combining functions.[6]

The name and concept comes from category theory, where monads are one particular kind of functor"

## [Unital](#unital) [[W](https://en.wikipedia.org/wiki/Algebra_over_a_field#Unital_algebra)]

"An algebra is unital or unitary if it has a unit or identity element I with Ix = x = xI for all x in the algebra."

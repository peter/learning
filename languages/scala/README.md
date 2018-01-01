# Learning Scala

Notes in learning the Scala programming language

* [Glossary of Terms in Functional Programming and Mathematics](FUNCTIONAL_GLOSSARY.md)

* [Notes from Functional Programming Principles in Scala (Coursera)](course/README.md)

## Features

* The name Scala refers to the ability to scale from simple scripts to large systems
* Scala started out as a research project in combining object oriented and functional programming
* Scala allows you to program in an imperative style but encourages a functional style - using immutable objects, and methods without side effects.
* Scala runs on the JVM and is interoperable with Java code
* Almost everything in Scala is an expression (rather than a statement)
* Everything is an object
* Scala doesn’t require Semicolons at the end of lines
* Scala doesn't require explicit returns from functions

## Questions

* Understanding the object keyword and companion classes

## Tour

```scala
println("Hello World")

val msg = "Hello World"
msg = "foobar" // => error: reassignment to val
println(msg)

def max(x: Int, y: Int): Int = {
  if (x > y) x
  else y
}
max(3, 8) // => 8
def max2(x: Int, y: Int): Int = if (x > y) x else y
max2(3, 8) // => 8

// Scalas Unit is similar to void in Java. Methods with a return type of
// Unit are only executed for their side effects.
def greet() = println("Hello World") // => greet: ()Unit
greet()
greet
```

In `hello.scala`:

```scala
println(s"Hello ${args(0)}!")
```

From the command line:

```
scala src/hello.scala world
```

```
scala src/printargs.scala scala is fun
```

```scala
object HelloWorld extends App {
  println("Hello World!")
}
```

```scala
object HelloWorld {
  def main(args: Array[String]) {
    println("Hello World!")
  }
}
```

In Scala, the main or entry point method is defined in an object. An object can be made executable by either extending the type App or by adding a method def main(args: Array[String]).

## Naming Conventions

```scala
class MyClass
object MyObject
package com.novell.coolness
def myFairMethod = ...

// doesn't change state, call as birthdate
def birthdate = firstName

// updates our internal state, call as age()
def age() = {
  _age = updateAge(birthdate)
  _age
}

val myValue = ...

// Type Parameters
class Map[Key, Value] {
  def get(key: Key): Value
  def put(key: Key, value: Value): Unit
}

val ThisIsMyConstant = 3.14
```

See [Naming Conventions](https://docs.scala-lang.org/style/naming-conventions.html) for details.

## Strings

You can do [Strings interpolation](http://docs.scala-lang.org/overviews/core/string-interpolation.html) by prefixing double quoted string literals with s

```scala
"foobar".exists { _.isUpper } // => false
"foobar".map { _.toUpper } // => FOOBAR
"foobar" map { _.toUpper } exists { _.isUpper } // => true
"Hello, " + "World"
```

## Array

A scala Array is a mutable sequence of objects of the same type.

```scala
val greetStrings = new Array[String](3)
greetStrings(0) = "Hello"
greetStrings(1) = ", "
greetStrings(2) = "World"
greetStrings.mkString("") // => "Hello, World"
```

Array short syntax that uses the apply method of the
Array companion object:

```scala
val numNames = Array("zero", "one", "two")
```

## List

An immutable sequence of objects. You do concatenation
with `:::` and prepend an element with the cons operator `::`.
Lists prepend in constant time but appending takes linear
time and is done with the `:+` operator.

```scala
val oneTwo = List(1, 2)
val threeFour = List(3, 4)
val oneTwoThreeFour = oneTwo ::: threeFour
2 :: threeFour // => List(2, 3, 4)
(threeFour :+ 5) // => List(3, 4, 5)
```

Useful List methods:

```scala
threeFour.first
threeFour.head
threeFour.tail
threeFour.reverse // => List(4, 3)
threeFour.count { _ > 3 } // => 1
threeFour.drop(1) // => List(4)
threeFour.take(1) // => List(3)
threeFour.exists { _ > 4 }
threeFour.foreach(print)

threeFour.filter { _ > 3 }
threeFour.map { n => n * n }
threeFour.reduce { _ + _ } // => 7
threeFour.reduce { _ max _ }
threeFour.fold(20) { _ + _ } // => 27
```

The empty list is `Nil` or `List()`:

```scala
val fourFiveSix = 4 :: 5 :: 6 :: Nil
```

## Tuple

Tuples are immutable sequences that contain objects of different types. The maximum Tuple size is 22.

```scala
val pair = (99, "Luftballons")
pair._1
pair._2
val (first, second) = pair
```

## Set

Sets are immutable by default by mutable sets are available
in `scala.collection.mutable`.

## Map

There are mutable maps in `scala.collection.mutable` and immutable maps in `scala.collection.immutable`.

Mutable map:

```scala
import scala.collection.mutable.Map
val treasureMap = Map[Int, String]() // Factory method
treasureMap += (1 -> "Go to island") // Adds tuple to map
treasureMap += (2 -> "Find big X on ground")
treasureMap += (3 -> "Dig")
treasureMap(2)
```

Immutable map:

```scala
val romanNumeral = Map(
  1 -> "I", 2 -> "II", 3 -> "III", 4 -> "IV", 5 -> "V"
)
romanNumeral(5) // => "V"
romanNumeral(6) // => java.util.NoSuchElementException: key not found: 6
```

## Collections

At the top of the collections hierarchy is `Traversable` with the `foreach` method. From
the `foreach` method Traversable can support
methods such as `+`, `map`, `flatMap` etc.

## Extractors

An Extractor in Scala is an object with an unapply method. The purpose of the unapply method
is to take apart a value. Often a dual method
called apply is provided but this is not required.

```scala
object Email {
  def apply(user: String, domain: String) = user + "@" + domain
  def unapply(str: String): Option[(String, String)] = {
    val parts = str split "@"
    if (parts.length == 2) Some(parts(0), parts(1)) else None
  }
}

Email("peter", "marklunds.com") // => "peter@marklunds.com"
"peter@marklunds.com" match {
  case Email(user, domain) => (user, domain)
}
Email.unapply(Email.apply("peter", "marklunds.com")) // => Some((peter,marklunds.com))
```

Use `unapplySeq` to extract a variable number of parts:

```scala
object Domain {
  def unapplySeq(whole: String): Option[Seq[String]] =
    Some(whole.split("\\.").reverse)
}

"foo.acm.org" match {
  case Domain("org", "acm", _*) => println("acm domain")
}
```

## Classes

Classes in Scala are very similar to classes in Java. They are templates containing fields and methods. Like in Java, classes can be instantiated using the new construct, there can be many “instances” (or “objects”) of the same class.

Classes in Scala cannot have static members. You can use objects to achieve similar functionality as with static members in Java.


```scala
class MyClass(index: Int, name: String)
val myInstance1 = new MyClass(5, "foobar")
val myInstance2 = new MyClass(index = 5, name = "foobar")

class ChecksumAccumulator {
  var sum = 0 // public
  private var secret = "foo"

  def add(b: Byte): Unit = {
    sum += b
  }

  def checksum(): Int = ~(sum & 0xFF) + 1
}
val acc = new ChecksumAccumulator
acc.sum // => 0
acc.sum = 1
acc.add(3)
acc.checksum

class Rational(n: Int, d: Int) {
  require(d != 0) // Throws IllegalArgumentException if d == 0
  val numer: Int = n
  val denom: Int = d

  def this(n: Int) = this(n, 1) // Auxiliary constructor

  override def toString = n + "/" + d

  // We could also use + as the name of this method
  def add(that: Rational): Rational =
    new Rational(
      numer * that.denom + that.numer * denom,
      denom * that.denom
    )

  def lessThan(that: Rational) =
    this.numer * that.denom < that.numer * this.denom

  def max(that: Rational) =
    if (this.lessThan(that)) that else this

  def * (that: Rational): Rational =
    new Rational(numer * that.numer, denom * that.denom)

  def * (i: Int): Rational =
    new Rational(numer * i, denom)
}
val oneHalf = new Rational(1, 2)
val twoThirds = new Rational(2, 3)
oneHalf add twoThirds
oneHalf * oneHalf
oneHalf * 2
```

At the top of the Scala class hierarchy is `Any` (with ==, !=, equals, ##, hashCode, and toString methods).

## Object

An `object` definition in Scala is like a class, but it only has a single instance. It is not possible to create instances of objects using new, instead you can just access the members (methods or fields) of an object using its name.

## Implicit Conversions

In order to make `2*oneHalf` work we can use an implicit conversion:

```scala
implicit def intToRational(x: Int) = new Rational(x)

2 * oneHalf
```

Implicit type conversions trigger when the compiler encounters a type mismatch/error. Implicit type conversions can be applied both to the receiver of a method call and to the arguments. Implicits enable
client programmers to use existing types (i.e. Int) as if they
were instances of a new type (i.e. Rational). If
multiple implicit conversions can be applied then
if possible the more type specific (where one type is the subtype of the other) conversion will be chosen. Otherwise there is ambiguity and an error is raised.

## Case Classes

```scala
case class MyCaseClass(index: Int, name: String)
val myInstance1 = new MyCaseClass(5, "foobar")
val myInstance2 = new MyCaseClass(index = 5, name = "foobar")
myInstance2.index // => 5
myInstance2.name = "bla" // => error: reassignment to val
```

Case classes support pattern matching.

```scala
expr match {
  case BinOp(op, left, right) =>
    println(expr + " is a binary operation")
  case _ => println("It's something else")
}

def describe(x: Any) = x match {
  case 5 => "five"
  case true => "true"
  case "hello" => "hi"
  case Nil => "empty list"
  case _ => "something else"
}
```

## Singleton Objects

Classes in Scala cannot have static members, instead Scala has singleton objects.
When a singleton object shares the same name as a class it is called that class's
compantion object and they must be defined in the same file.

```scala
import scala.collection.mutable.Map
object ChecksumAccumulator {
    private val cache = Map[String, Int]()
}
```

## A Scala Application

To run a Scala program you must supply the name of a standalone singleton object with
a main method that takes an Array[String] parameter and has a result of Unit.

```scala
object MyApp {
  def main(args: Array[String]) {
    // TODO write app
  }
}
```

You can also make your application object extend the `Application` trait and then
you can skip the main method if you don't need command line args.

## Type Parameterization

Type parameterization allows you to write generic classes and traits, i.e. `Set[T]`.

```scala
class SlowAppendQueue[T](elems: List[T]) {
  def head = elems.head
  def tail = new SlowAppendQueue(elems.tail)
  def enqueue(x: T) = new SlowAppendQueue(elems ::: List(x))
}
```

Classes and traits that take type parameters are generic. The List definition `List[+T]` is
covariant because of the + which means that you can assign `List[Int]` to a variable of `List[Any]`

## Default Imports

Scala implicitly imports packages java.lang, scala, and members of the singleton object
Predef (assert, println etc.).

## Built-in Control Structures

All control structures (`if`, `while`, `for`, `try`, `match`) return a value.

You can use `if` instead of the ternary operator.

```scala
println(if (!args.isEmpty) args(0) else "default.txt")
```

Re-assignment to vars returns a Unit value so you can't usefully have them in if statements.

```scala
val files = (new java.io.File(".")).listFiles
def grep(pattern: String) =
  for (file <- files // generator syntax
     if file.isFile if file.getName.endsWith(".scala")
     line <- fileLines(file)
     if line.trim.matches(pattern)) println(file + ": " + line.trim)

for (file <- files) yield file // => Array[java.io.File] = ...

for (i <- 1 to 4)
  println(i)
```

There is no `break` or `continue` in Scala.

## For Expressions

```scala
case class Person(
  name: String,
  isMale: Boolean,
  children: Person*
)
val lara = Person("Lara", false)
val bob = Person("Bob", true)
val persons = List(
  lara,
  bob,
  Person("Julie", false, lara, bob)
)

// NOTE: we use withFilter to only traverse once
persons.withFilter { !_.isMale }.
  flatMap { p => p.children.map (c => (p.name, c.name)) }

for {
  p <- persons
  if !p.isMale
  c <- p.children
} yield (p.name, c.name)

for {
  p <- persons            // generator
  n = p.name              // definition
  if (n.startsWith("L")) // filter
} yield n

// Authors who have written at least two books
for {
  b1 <- books
  b2 <- books
  if b1 != b2
  a1 <- b1.authors
  a2 <- b2.authors
  if a1 == a2
} yield a1
```

For expressions work on data types that implement the `map`, `flatMap`, and `withFilter` methods.

## Exceptions

You handle exceptions with `try-catch` blocks like in Java but unlike in Java
exceptions are unchecked.

## Match Expressions

```scala
val firstArg = if (args.length > 0) args(0) else ""
val friend =
  firstArg match {
    case "salt" => "pepper"
    case "chips" => "salsa"
    case _ => "huh?"
  }
```

## Character Literals

```scala
'A'
'\101' // Octal Unicode A
'\u0041' // Four hex digits Unicode A
```

## Symbol Literals

```scala
'foobar
'foobar.name // => "foobar"
```

## Boolean Literals

```scala
true
false
```

## Object Equality

Using the `==` operator checks if the left operand is `null` and otherwise invokes the equals method (value equality rather than reference equality like in Java).

## Methods

If a method takes only one parameter you can call it without a dot or without parentheses.

## Operators

`2 + 2` is syntactic sugar for `(2).+(2)`. If an infix operator
ends with a colon then the method is invoked on the right
operand instead of the left, so `1 :: List(2)` means
`List(2).::(1)`.

## apply and update

`greetStrings(i)` gets transformed to `greetStrings.apply(i)`.
`greetStrings(i) = 0`

## Option

TODO

## Either

TODO

## Traits

Traits encapsulate method and field definitions that can be mixed in to classes.

Traits are like interfaces in Java, but they can also contain concrete members, i.e. method implementations or field definitions.

## Scala Collections API

TODO

## require

The `require` function throws `IllegalArgumentException` if a condition is not
met. Here is [an example](https://stackoverflow.com/questions/26140757/what-to-choose-between-require-and-assert-in-scala) with assert and require:

```scala
def fac(i: Int) = {
  require(i >= 0, "i must be non negative") //this is for correct input

  @tailrec def loop(k: Int, result: Long = 1): Long = {
    assert(result == 1 || result >= k)   //this is only for verification

    if(k > 0) loop(k - 1, result * k) else result
  }

  loop(i)
}
```

## Functions and Closures

Besides methods Scala offers functions within functions (local functions),
function literals, and function values.

```scala
val incr = (x: Int) => x + 1

// Partial function application with _
def sum(a: Int, b: Int) = a + b
val add2 = sum(2, _: Int)
add2(2)
```

Functions can not only access bound variables (arguments) but also free variables
from the scope where it is defined, i.e. be closures.

## Repeated function parameters

```scala
def echo(args: String*) = // args will be of type Array[String]
  for (arg <- args) println(arg)
echo("foo", "bar", "baz")
```

## Named Arguments

```scala
def speed(distance: Float, time: Float): Float =
  distance / time
speed(100, 10) // positional arguments
speed(distance = 100, time = 10) // named arguments
```

## Default Parameter Values

```scala
def printTime(out: java.io.PrintStream = Console.out, divisor: Int = 1) =
  out.println("time = " + System.currentTimeMillis() / divisor)
printTime()
printTime(divisor = 10)
```

## Recursion

Tail recursive function that will be converted into a loop by the compiler:

```scala
def approximate(guess: Double): Double =
  if (isGoodEnough(guess)) guess
  else approximate(improve(guess))
```

## Control Abstraction

Higher order functions are functions that take other functions as arguments:

```scala
def filesMatching(query: String, matcher: (String, String) => Boolean) = {
  val files = (new java.io.File(".")).listFiles
  for (file <- files if matcher(file.getName, query)) yield file
}
filesMatching(".md", _.endsWith(_))
filesMatching(".md", _.contains(_))
filesMatching(""".*\.md.*""", _.matches(_))
```

## Curried Functions

```scala
def curriedSum(x: Int)(y: Int) = x + y
curriedSum(2)(3)
curriedSum(2)_
(curriedSum(2)_)(3)
```

## Regular Expressions

```scala
import scala.util.matching.Regex
new Regex("""(-)?(\d+)(\.\d*)?""") // decimal
"""(-)?(\d+)(\.\d*)?""".r // decimal
```

Important Regex methods: `findFirstIn`, `findAllIn`, `findPrefixOf`.

```scala
"/api-dev/bla/partner/bla".matches(""".*api-dev.*partner.*""") // => true
```

```scala
val EmailPattern = """(\w+)@([\w\.]+)""".r
EmailPattern.findFirstIn("foo@example.com").isEmpty // => false
EmailPattern.findFirstIn("foo").isEmpty // => true
```

## Pipelining

```scala
import scalaz.syntax.id._
"foobar" |> { _.reverse } |> { _.toUpperCase }
```

## Call by Name vs Call by Value

* [Call by value](https://www.coursera.org/learn/progfun1/lecture/eervR/lecture-1-3-evaluation-strategies-and-termination) - follows the substituation model where function arguments are evaluated
  before the function body executes.
* Call by name - evaluation of the function arguments are delayed up until the point where
  they are references and needed in the evaluation of the function body

Call by name and call by value will produce the same results if the evaluations terminate.

Example of call by value:

```scala
def loop: Boolean = loop
def first(x: Int, y: Boolean) = x

first(1, loop) // doesn't terminate
```

Example of call by name:

```scala
def loop: Boolean = loop
def first(x: Int, y: => Boolean) = x

first(1, loop) // => 1
```

In practice call by value is more efficient as it avoids re-computation of function arguments.

Difference between def and val:

```scala
def loop: Boolean = loop
def x = loop // by name, ok
val x = loop // by value, doesn't terminate
```

## Square Root with Newtons Method

To calculate square root of x:

* Pick an initial estimate y, i.e. 1
* Repatedly improve estimate by taking mean of y and x/y
* Terminate when the absolute (or relative) error is less than certain amount, i.e. 0.001

```scala

def sqrt(value: Double) = {
  def abs(x: Double) = if (x < 0) -x else x

  def sqrtIter(guess: Double, x: Double): Double =
    if (isGoodEnough(guess, x)) guess
    else sqrtIter(improve(guess, x), x)

  def isGoodEnough(guess: Double, x: Double) =
    abs(guess * guess - x) / x < 0.001

  def improve(guess: Double, x: Double) =
    (guess + x / guess) / 2

  sqrtIter(1.0, value)
}
```

A block in Scala (enclosed in curly braces) can appear anywhere an expression can and it returns its last evaluated expression. Definitions inside a block are only visible inside
the block. Definitions outside the block are visible inside the block as long as they are
not shadowed.

Recursive functions need explicit return types.

## Recursion

Tail recursive functions have an iterative process. One can require that a function
is tail recursive with the `@tailrec` annotation.

Clarity trumps efficiency so don't go out of your way to achieve tail recursion if your
input data doesn't demand it.

## Style Guide

* Avoid Casts and Type Tests - never use isInstanceOf or asInstanceOf
* Indentation - two spaces
* Line Length and Whitespace
* Use local Values to simplify complex Expressions. When writing code in functional style, methods are often implemented as a combination of function calls. If such a combined expression grows too big, the code might become hard to understand. In such cases it is better to store some arguments in a local value before passing them to the function. Make sure that the local value has a meaningful name.
* Choose meaningful Names for Methods and Values
* Avoid using explicit returns in functions
* Avoid mutable local Variables

## Resources

* [Programming in Scala (Book)](https://www.amazon.com/Programming-Scala-Comprehensive-Step-Step/dp/0981531644)
* [Scala Cheat Sheet](https://github.com/lampepfl/progfun-wiki/blob/gh-pages/CheatSheet.md)
* [Functional Programming Principles in Scala (Course)](https://www.coursera.org/learn/progfun1)
* [Scala Standard Library API Doc](http://www.scala-lang.org/api/current/)
* [Best Scala courses, videos & books in 2017](https://reactdom.com/blog/scala-books)
* [Twitter Scala School](http://twitter.github.io/scala_school/)
* [Tour of Scala](http://docs.scala-lang.org/tour/tour-of-scala.html)
* [Glossary of Scala and FP Terms](http://docs.scala-lang.org/glossary/)

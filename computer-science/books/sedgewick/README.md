# Algorithms (Sedgewick)

## 1. Fundamentals

### 1.1 Basic Programming Model

"The term algorithm is used in computer science to describe
a finite, deterministic, and effective problem-solving method suitable for implementation
as a computer program."

"We can define an algorithm by describing a procedure for solving a problem in a
natural language, or by writing a computer program that implements the procedure,
as shown at right for Euclid’s algorithm for finding the greatest common divisor of
two numbers, a variant of which was devised
over 2,300 years ago."

```java
public static int gcd(int p, int q) {
  if (q == 0) return p;
  int r = p % q;
  return gcd(q, r);
}
```

### 1.3 Bags, Queues, and Stacks

API - each container data type (`Bag`, `Queue`, `Stack`) has an empty constructor, a method for adding (`add`, `enqueue`, `push`), an optional removal method (`dequeue`, `pop`), `isEmpty`, and `size`.

The container types use generics to be able to hold any type of data.

```java
Stack<String> stack = new Stack<String>();
stack.push("Test");
String next = stack.pop();

Queue<Date> queue = new Queue<Date>();
queue.enqueue(new Date(12, 31, 1999));
Date next = queue.dequeue();
```

Collections should also be iterable:

```java
Queue<Transaction> collection = new Queue<Transaction>();
for (Transaction t : collection) {
  StdOut.println(t);
}
```

A linked list is a recursive data structure that is either empty (null) or a
reference to a node having a generic item and a reference to a linked list.

Traversal of linked list:

```java
for (Node x = first; x != null; x = x.next) {
  // Process x.item.
}
```

### 1.4 Analysis of Algorithms

* How long will my program take?
* Why does my program run out of memory?

The scientific method: observe - hypothesize - predict - verify.

"One of the key tenets of the scientific method is that the experiments we design must be reproducible, so that others can convince themselves of the validity of the hypothesis. Hypotheses must also be falsifiable, so that we can know for sure when a given hypothesis is wrong (and thus needs revision). As Einstein famously is reported to have said (“No amount of experimentation can ever prove me right; a single experiment can prove me wrong”), we can never know for sure that any hypothesis is absolutely correct; we can only validate that it is consistent with our observations."

We use Javas `currentTimeMillis()` to measure elapsed time.

```java
public class Stopwatch {
  private final long start;
  public Stopwatch() {
    start = System.currentTimeMillis();
  }
  public double elapsedTime() {
    return (System.currentTimeMillis() - start) / 1000.0;
  }
}
```

In the early days of computer science, D. E. Knuth postulated that, despite all of the complicating factors in understanding the running times of our programs, it is possible, in principle, to build a mathematical model to describe the running time of any program. Knuth’s basic insight is simple: the total running time of a program is determined by two primary factors:

* The cost of executing each statement
* The frequency of execution of each statement

Rate of growth:

* Constant (most Java operations)
* Logarithmic (i.e. Binary search, base of logarithm not relevant). Barely slower than constant time (ln(1K) ~ 7, ln(1M) ~ 14, ln(1G) ~ 21, ln (1T) ~ 27)
* Linear - proportial to N
* Linearithmic - N log N (merge sort, quick sort)
* Quadratic (i.e. nested loops, insertion sort)
* Cubic (i.e. three nested loops, ThreeSum)
* Exponential - 2^N. Very slow but vast class of problems need such algorithms.

We can optimize a 2-sum problem (find pairs of numbers in array that sum to 0) by first doing a search and then inside the loop doing a binary search, this yields N log N.

"The idea of a lower bound on the order of growth of the worst-case running time for all possible algorithms to solve a problem is a very powerful one"

Strategy:

* First find a brute-force solution
* Examine algorithmic improvements
* Run experiments to validate performance

"A famous rule of thumb known as Moore’s Law implies that you can expect to have a
computer with about double the speed and double the memory 18 months from now,
or a computer with about 10 times the speed and 10 times the memory in about 5 years."

"One of the first assumptions that we made in order to
determine the order of growth of the program’s running time of a program was that the
running time should be relatively insensitive to the inputs. When that is not the case, we
may get inconsistent results or be unable to validate our hypotheses."

"To determine the memory usage of an object,
we add the amount of memory used by each instance
variable to the overhead associated with each object,
typically 16 bytes. The overhead includes a reference to
the object’s class, garbage collection information, and
synchronization information. Moreover, the memory
usage is typically padded to be a multiple of 8 bytes
(machine words, on a 64-bit machine). For example,
an Integer object uses 24 bytes (16 bytes of overhead,
4 bytes for its int instance variable, and 4 bytes of
padding)."

### 1.5 Case Study: Union Find

"An efficient algorithm can be as simple to code as an inefficient one."

Dynamic connectivity We start with the following problem specification: The
input is a sequence of pairs of integers, where each integer represents an object of some
type and we are to interpret the pair p q as meaning “p is connected to q.” We assume
that “is connected to” is an equivalence relation, which means that it is:

* Reflexive : p is connected to p.
* Symmetric : If p is connected to q, then q is connected to p.
* Transitive : If p is connected to q and q is connected to r, then p is connected to r.

## Resources

* [Book Homepage](https://algs4.cs.princeton.edu/home)
* [Book Source Code](https://github.com/kevin-wayne/algs4)

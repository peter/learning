# Week 2

## Counting Inversions

## Strassens Subcubic Matrix Multiplication Algorithm

## Algorithm for Closest Pair (Optional)

## The Master Method

### Integer multiplication example.

We are looking for the worst case number of operations as a function of the input size N.

* There is a base case when there is no further recursion (constant running time, T(1) <= constant).
* Work done in recursive calls
* Work done outside recursive calls

Without Gauss elimination: T(n) <= 4T(n/2) + O(n)

### Formal Statement

Requires the subproblem/recursive data size to be the same (half/half).

Base Case - constant

There are a recursive calls and b is the factor by which the data shrinks, i.e 2, d is the exponent in summing/merging time. T(n) <= aT(n/b) + O(n^d)

If T(n) <= a*T(n/b) + O(n^d) then:

T(n) = O(n^d*log(n)) if a = b^d (Case 1)
T(n) = O(n^d) if a < b^d (Case 2)
T(n) = O(n^(logb(a))) if a > b^d (Case 3)

The logarithms with different bases differ only by a constant factor in big O.
However, when the logarithm is in the exponent then the logarithmic base does matter.

### Merge Sort Example

a = 2
b = 2
d = 1

Case 1.

O(NlogN)

### Binary Search Example

a = 1
b = 2
d = 0

Like lookup in a phone book.

Case 1

O(logN)

### Multiplication Example

Without Gauss:

a = 4
b = 2
d = 1

Case 3. O(n^log2(4)) = O(n^2)

With Gauss:

a = 3
b = 2
d = 1

Case 3. O(n^log2(3))

### Straussen Matrix multiplication

a = 7
b = 2
d = 2

Case 3. O(N^log2(7)) ~ O(N^2.81)

### Case 2 Example

a = 2
b = 2
d = 2

Case 2. O(N^2)

## Proof 1

At each level j 0,1,...,logb(n) there are a^j subproblems of size n/b^j.

Total work at level j. Sum up over all levels to get total work:

```
Upper bound at level j:
a^j + c*(n/b^j)^d = c*n^d*(a/b^d)^j

Total:
c*n^d * sum[0..logb(n)](a/b^d)^j
```

a - rate of subproblem prolification (RSP, evil, root of slowness, creates more subproblems)
b^d - rate of work shrinkage (RWS, good, per subproblem)

If RSP < RWS then the amount of work decreases at increasing levels j

There is a battle of forces between a (good) and b^d (evil).

1. RSP = RWS => n^d*log(n)
2. RSP < RWS => n^d
3. RSP > RWS => O(#leaves)

## Resources

* [Master Theorem (analysis of algorithms)](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)) "In the analysis of algorithms, the master theorem for divide-and-conquer recurrences provides an asymptotic analysis (using Big O notation) for recurrence relations of types that occur in the analysis of many divide and conquer algorithms. The approach was first presented by Jon Bentley, Dorothea Haken, and James B. Saxe in 1980, where it was described as a "unifying method" for solving such recurrences.[1] The name "master theorem" was popularized by the widely used algorithms textbook Introduction to Algorithms by Cormen"

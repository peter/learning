# Week 1

Introduction; "big-oh" notation and asymptotic analysis.

## 1. Introduction

### Why Study Algorithms?

An algorithm is a set of rules (a procedure or recipe) for solving a computational problem. Examples are sorting numbers, finding the shortest path in a network, task scheduling etc.

Algorithms is a fundamental subject in computer science. Networking, cryptography, graphics, databases etc. rely on algorithms.

Search engines use a tapestry of algorithms.

The design and analysis of algorithms is fun! It requires precision and creativity and can be frustrating at time.

### Integer Multiplication

1234 * 5678.

The rate of growth is N^2 for size N numbers.

"As, as an algorithm designer you should adopt as your Mantra the question, can we  do better?"

### Karatsuba Multiplication

Later we will learn a toolbox for designing Divide and Conquer algorithms.

The algorithm design is far richer than you may expect - there is a dazzling array of options.

```
x = ab
y = cd

x = 10^n/2*a + b
y = 10^n/2*c + d
x*y = (10^n/2*a + b) * (10^n/2*c + d) = 10^n*ac + 10^n/2*(ad + bc) + bd
```

We have broken down the multiplication into several multiplications of smaller numbers. We can recursively compute ac, ad, bc, bd and then calculate the top level result.

The base case where recursion stops is that the two number to multiply archive one digit each.

We can refine the recursive approach by doing a trick to reduce four recursive calls to three: `ac`, `bd`, `(a + b)*(c + d)`. From this
we can then derive `ad + bc` (with Gauss's trick):

```
(a + b) * (c + d) = ac + ad + bc + bd
```

### Merge Sort

Merge sort was known to von Neumann in 1945 but it's still used frequently
in practice in libraries. Merge sort is perhaps the most transparent application of the Divide-and-Conquer algorithm.

Simpler sorting approaches include insertion sort, selection sort, and bubble sort O(N^2).

The algorithm will call itself on smaller and smaller arrays.

Example:

```
5 4 1 8 7 2 6 3 -> 1 2 3 4 5 6 7 8
```

Split the array in half and recurse on each. When you get the result
merge the results. The base case is an array with zero or one elements.
The merge is done by traversing the two arrays in parallel and picking
the smallest (for ascending order) first. There is a special case
where all elements in one array is smaller than those in the other array.

How many operations/instructions does merge sort yield as a function of
the size of the input N. The number of operations in the merge is roughly
`4m + 2` which is less than `6m`.

The upper bound of merge sort in total is `6nlog(n) + 6n`

```
ln(10^3) ~ 7
ln(10^6) ~ 14
ln(10^9) ~ 21
ln(10^12) ~ 28
ln(10^15) ~ 35
```

The algorithm forms a binary tree. Let's call the root node level 0.
The level number at the leaves is then `log2(n)` and this is the number
of levels of recursion. At level `j` there are `2^j` sub problems of size `n/2^j`. The total number of operations at level j:

```
2^j * 6 * (n/2^j) = 6n
```

### Principles for Analysis of Algorithms

* Use worst case analysis (as opposed to average time analysis or benchmarks) and make no assumptions about the input.
* Don't worry about constant factors (that are implementation dependent)
* Use asymptotic analysis - when N tends to infinity. The growth of N will dominate over constant factors. It's the rate of growth that we are interested in.

"That said, I'm not saying you should be completely ignorant of constant factors when you implement algorithms. It's still good to have a general sense of what these constant factors are so for example in highly tuned versions of Merge Sort which you'll find in many programming libraries. In fact, because of the difference in constant factors, the algorithm will actually switch from Merge Sort over to insertion sort, once the problem size drops below some particular threshold, say seven elements, or something like that."

The holy grail is usually a linear time algorithm and nlog(n) is close to that.

## 2. Asymptotic Analysis

We are looking for analysis that hits a sweet spot in high level reasoning about algorithm performance. It should be coarse enough to
suppress implementation details but sharp enough for useful comparisons.

*The high level idea is to suppress constant factors and lower order terms*



## Resources

* [Comparison of sorting algorithms](https://brilliant.org/wiki/sorting-algorithms)
* [Merge Sort](https://en.wikipedia.org/wiki/Merge_sort): "Most implementations produce a stable sort, which means that the implementation preserves the input order of equal elements in the sorted output."
* [Quick Sort - O(n log n)](https://en.wikipedia.org/wiki/Quicksort): "In efficient implementations it is not a stable sort, meaning that the relative order of equal sort items is not preserved. Quicksort can operate in-place on an array, requiring small additional amounts of memory to perform the sorting."

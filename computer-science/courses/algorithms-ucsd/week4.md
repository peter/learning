# Week 4

In this module you will learn about a powerful algorithmic technique called Divide and Conquer. Based on this technique, you will see how to search huge databases millions of times faster than using naïve linear search. You will even learn that the standard way to multiply numbers (that you learned in the grade school) is far from the being the fastest! We will then apply the divide-and-conquer technique to design two efficient algorithms (merge sort and quick sort) for sorting huge lists, a problem that finds many applications in practice. Finally, we will show that these two algorithms are optimal, that is, no algorithm can sort faster!

## Master Theorem

T(n) = aT(n/b) + O(n^d)
a - number of subdivisions per level
b - fraction of size of each subdivision
d - exponent in work
a > 0, b > 1, d > 0

O(n^d) if d > logb(a)
O(n^d*log(n)) if d = logb(a)
O(n^logb(a)) if d < logb(a)

a = 8
b = 2
d = 2
log2(a) = 3 > d

a = 1
b = 2
d = 0
log2(a) = 0 = d

a = 3
b = 2
d = 1

log2(3) ~ 1.5 > d

Worst case running time of quick sort is O(n^2) if the array is already sorted.
What is the running time of the Partition procedure? O(n)
What is the amount of additional memory that regular Quick Sort uses (besides the array being sorted) in the worst case? O(logn)

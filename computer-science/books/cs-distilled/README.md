# Computer Science Distilled

Notes from the book Computer Science Distilled.

"Computer science is not about machines in the same way that astronomy is not about telescopes" - Dijkstra

Computers need us to break down problems into chunks they can crunch.

## Flowcharts

Example: Wikipedia edition process

* State and instruction steps in rectangles (i.e. Edit page)
* Decision steps in diamonds (i.e. do you agree with the change?)
* Connect sequential steps with arrows
* Mark the start and end of the process

## Math

N Factorial is the number of ways N items can be ordered (permutations). If r of the items
are identical then the number of orderings should be divided by r factorial.

"n choose m" - the number of ways you can select m from n regardless of order.

# Complexity

The first person to find a non-exponential algorithm to an NP-complete problem
gets a million dollars from the Clay Mathematics Institute. Factorial time
algorithms are even worse than exponential time.



## Appendix

### Numerical Basis

Information can be expressed as numbers. Number systems are based
on sums of digits. Each digit in position i is multiplied by d (the number base)
to the power of i. Examples:

```
# Hexadecimal base 16
10E1 -> 4096+0+224+16=4321

# Binary base 2
1000011100001 -> 4096+128+64+32+1=43321
```

### Gauss' Trick

The story goes that Gauss was asked by his elementary school teacher
to sum numbers from 1 to 100 (a [geometric series](http://mathworld.wolfram.com/GeometricSeries.html)).

```
(1 + 100) + (2 + 99) + (3 + 98) ... = 100*101/2 = 5050
n*(n+1)/2
```

## Resources

* [Computer Science Distilled on Amazon](https://www.amazon.com/Computer-Science-Distilled-Computational-Problems/dp/0997316020)

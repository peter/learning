# Week 2

Daniel Kane

## Why Study Algorithms

Some problems are too simple and require simple traversal. Some problems are too
difficult and require AI (natural language processing, recognizing objects in images).

Algorithmic problems (sweet spot) - not clear how to solve, brute force is too slow.

AI problems are hard to state/define.

The optimal routing problem (traveling salesman) is an example of a problem
that is easy to state precisely but difficult to solve.

## Computing Runtime

Implementation dependent: programming language, compiler, OS, hardware (memory size, CPU speed, number of cores) etc.

You may not know which OS and hardware etc. your algorithm will run on.

Instead we want to figure out how the runtime scales/grows with the input size.

## Asymptotic Notation

Ignore the constant factors. As the input size n goes to infinity all constant
factors become irrelevant.

```
        n, nlog(n), n^2, 2^n
n=20:   1s, 1s,    1s,     1s
n=50    1s, 1s,    1s,     13 days
n=10^6  1s, 1s,    17 min, ...
n=10^9  1s, 30s,   30 years, ...
```

We write f(n)=O(g(n)) to express the fact that f(n) grows no faster than g(n): there exist constants N and c>0 so that for all n≥N, f(n)≤c⋅g(n)

## Logarithms

```
log(n^k) = klog(n)
log(nm) = log(n) + log(m)
n^log(b) = b^log(n)
log[a](n)*log[b](a) = log[b](n)
```

Change of logarithm base (base does not affect big-O):

```
log[b](x) = log[d](x) / log[d](b)
```

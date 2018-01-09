# Week 3

The QuickSort algorithm and its analysis; probability review.

## Overview

QUICKSORT - THE ALGORITHM (Part V). One of the greatest algorithms ever, and our first example of a randomized algorithm. These lectures go over the pseudocode --- the high-level approach, how to partition an array around a pivot element in linear time with minimal extra storage, and the ramifications of different pivot choices --- and explain how the algorithm works.

PROBABILITY REVIEW (Part VII). This first of these videos reviews the concepts from discrete probability that are necessary for the QuickSort analysis --- sample spaces, events, random variables, expectation, and linearity of expectation. The second video covers just two topics, although quite tricky ones! (Namely, conditional probability and independence.) You need to review these two topics (via this video or some other source, as you wish) before studying the analysis of the randomized contraction algorithm in Week 4.

HOMEWORK: This week's quiz will help you understand QuickSort and probability more deeply. Programming Assignment #3 asks you to implement QuickSort and compute the number of comparisons that it makes for three different pivot rules.

SUGGESTED READING FOR WEEK 3: Algorithms Illuminated (Part 1), Chapter 5 and Appendix B.

## Quicksort: Introduction

* A greatest hit algorithm
* Prevalence in practice
* O(nlog(n)) in place (needs less memory than merge sort, does repeated swaps)

Key idea: partitioning around a pivot

How do you pick the pivot?

Re-arrange every item left/right of the pivot so that all items to the left
are smaller than the pivot and all items to the right are greater. This means
the pivot is in the right place for sorting but the left/right items are not
sorted among themselves.

Algorithm discovered by Tony Hoare 1961. Won Turing award in 1980.

Assume pivot is the first element. If it's not, swap pivot with first element as a pre-processing step to this algorithm.

## Quicksort: Partitioning around a Pivot

The pivot element winds up in the right position. Then you recurse on the left side and on the right side.

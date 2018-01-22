# Week 5

## The Change Problem

The greedy algorithm is to always pick the largest coin that is less than the remaining amount but this will not always yield an optimal solution (i.e not minimize the number of coins used):

```
40 = 25 + 10 + 5
40 = 20 + 20
```

You can try to change 9 with 6, 5, and 1 with a recursive program, but it will not complete in a lifetime...

## String Comparison / Edit Distance

Pavel Pevzner

Alignment game: remove symbols to maximize points.

* Remove 1st symbol from both strings - 1 point if they match, 0 otherwize
* Remove 1st symbol from one of the strings - 0 points

```
A T G T T A T A
A T C G T C C
+1
  +1

A T - G T T A T A
A T C G T - C - C

Alignment score:

match: +1
mismatch: -my
indel: -sigma
```

Common subsequence: longest common subsequence of these strings. Corresponds to
maximizing the alignment score with my=sigma=0.

Edit distance: minimum number of operations to transform one string to another.
This corresponds to maximizing the alignment score.

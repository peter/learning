# Week 4

Part VIII --- LINEAR-TIME SELECTION (Required). These lectures study the problem of computing the ith smallest element of an input array (e.g., the median). It's easy to solve this problem in O(n log n) time using sorting, but we can do better! The required material goes over a super-practical randomized algorithm, very much in the spirit of QuickSort, that has *linear* expected running time. Don't forget that it takes linear time just to read the input! The analysis is somewhat different than what we studied for QuickSort, but is equally slick. Basically, there's a cool way to think about the progress the algorithm makes in terms of a simple coin-flipping experiment. Linearity of expectation (yes, it's back...) seals the deal.

Part VIII --- LINEAR-TIME SELECTION (Optional). I couldn't resist covering some advanced related material. The first is an algorithm that has more Turing Award-winning authors than any other algorithm that I know of. It is a deterministic (i.e., no randomization allowed) linear-time algorithm for the Selection problem, based on an ingenious "median-of-medians" idea for guaranteeing good pivot choices. (There are some accompanying lectures notes for this part, available for download underneath each video.) The second optional topic answers the question "can we do better?" for sorting, unfortunately in the negative. That is, a counting argument shows that there is no "comparison-based" sorting algorithm (like MergeSort, QuickSort, or HeapSort) with worst-case running time better than n log n.

Part IX --- GRAPHS AND THE CONTRACTION ALGORITHM. The second set of lectures for this week is a segue from randomized algorithms to graph algorithms. We first review graphs and the most standard ways of representing them (most commonly, by adjacency lists). We then consider the random contraction algorithm, discovered by Karger "only" 20ish years ago (while a PhD student here at Stanford). This algorithm solves the minimum cut problem --- given an undirected graph, separate the vertices into two non-empty groups to minimize the number of "crossing edges". Such problems come up when reasoning about, for example, physical networks, social networks, and images. This algorithm was perhaps the first strong evidence that graph problems could be added to the long list of "killer applications" of random sampling. Don't tune out before the final plot twist --- a simple but useful trick for transforming an algorithm that almost always fails into one that almost always succeeds.

HOMEWORK: Problem Set #4 has five questions about the randomized selection algorithm, cuts in graphs, and the contraction algorithm. Programming Assignment #4 asks you to implement the contraction algorithm and use it to compute the min cut of the graph that we provide.

SUGGESTED READINGS FOR WEEK 4: Algorithms Illuminated (Part 1), Chapter 6.

## Randomized Selection

No sort can have better time than O(n*log(n)). We are going to look at the problem of selecting the i:th smallest
entry (order statistic) out of an input of n numbers. The first order statistic is the minimum, the n:th order statistic is the maximum. When n is odd then the median n/2 order statistic is the middle element. If n is even
we can just pick the lower of the two middle elements. A possible solution is to use quick sort and then pick the i:th
element. However, with a randomized selection algorithm similar to quick sort with random pivot we can achieve O(N).

Selection is fundamentally easier than sorting.

## Graphs and the Contraction Algorithm for Minimum Cuts

What is a graph?

* Vertex - node
* Edge - connects to vertices. There can be a direction (directed graph with from/to - head/tail) or not (undirected graph). We accept duplicates of vertex connections.

Applications:

* Finding network bottlenecks/weaknesses
* Community detection in social networks
* Image segmentation (You have an edge between two pixels if they are neighboring - an edge graph). Compare colors to figure out if pixels are from the same object.

More: road networks, the web, dependency analysis

A graph with n vertices and no parallel edges that is fully connected will have between `n-1` and `n(n-1)/2` (n choose 2) edges.

Sparse vs dense graphs. Some algorithms are better suited for one or the other type.

n - number of vertices
m - number of edges

m is at least O(n) and at most O(n^2).

The adjacency matrix A has Aij = 1 (or a weight, or +1 or -1 for direction) if there is an edge between i and j.
Space requirement is n^2 which is wasteful for sparse graphs.

Adjancency list. Space requirement is m + n.

Which is better? Which operations do you need and is your graph sparse or dense? We will be focusing on adjancency lists. The number of vertices of the web is roughly 10^10. Number of atoms in the universe is around 10^80.

## Random Contraction Algorithm

Devised in the early 90:ies. Uses random sampling. There is a main loop that descreases the number of vertices
by one. Choose an edge (u, v) among the remaining ones at random. Merge/contract u and v into a single vertex.
Remove self loops. Return cut represented by final 2 vertices.

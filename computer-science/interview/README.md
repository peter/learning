# Cracking the Coding Interview

## Data Structures

* How to implement
* When to use (pros/cons)

* Linked lists
* Stacks
* Queues
* Trees
* [Tries](https://en.wikipedia.org/wiki/Trie)
* Graphs
* Vectors
* Heaps
* Hashtables

## Algorithms

* Implementation
* Space vs Time complexity

* Quick Sort
* Merge Sort
* Tree insert/find
* Binary search
* Breadth-first search
* Depth-first search

Bit manipulation

## Binary Search Trees

https://en.wikipedia.org/wiki/Binary_search_tree

"Binary search trees keep their keys in sorted order, so that lookup and other operations can use the principle of binary search: when looking for a key in a tree (or a place to insert a new key), they traverse the tree from root to leaf, making comparisons to keys stored in the nodes of the tree and deciding, on the basis of the comparison, to continue searching in the left or right subtrees. On average, this means that each comparison allows the operations to skip about half of the tree"

```python
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value # information that is being stored in the tree
        self.left = left   # the left child (subtree)
        self.right = right # the right child (subtree)

    def __str__(self):
        return node.value
```

"There are two primary ways to traverse, or iterate through, a tree: depth-first and breadth-first. In the depth-first method, the left subtree is searched first, then the right subtree is searched. In the breadth-first method, the search progresses through the nodes at each height level of the tree, or in other words, the root node first, then level 1 nodes, then level 2 nodes, and so forth."

## Sorting Algorithms

"Comparison sorts are usually more straightforward to implement than integer sorts, but comparison sorts are limited by a lower bound of n*log(n), meaning that, on average, comparison sorts cannot be faster than n*log(n)"

"There is only one permutation of a list that is sorted, but n! possible lists, so the chances that the input is already sorted is very unlikely, and on average, the list will not be very sorted."

"Integer sorts determine for each element​  how many elements are less than . If there are  elements that are less than , then  will be placed in the  slot"

## Hash Table

https://en.wikipedia.org/wiki/Hash_table

In computing, a hash table (hash map) is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

Ideally, the hash function will assign each key to a unique bucket, but most hash table designs employ an imperfect hash function, which might cause hash collisions where the hash function generates the same index for more than one key. Such collisions must be accommodated in some way.

A hash function is any function that can be used to map data of arbitrary size to data of fixed size. The values returned by a hash function are called hash values, hash codes, digests, or simply hashes. One use is a data structure called a hash table, widely used in computer software for rapid data lookup. Hash functions accelerate table or database lookup by detecting duplicated records in a large file. An example is finding similar stretches in DNA sequences. They are also useful in cryptography. A cryptographic hash function allows one to easily verify that some input data maps to a given hash value, but if the input data is unknown, it is deliberately difficult to reconstruct it (or equivalent alternatives) by knowing the stored hash value. This is used for assuring integrity of transmitted data, and is the building block for HMACs, which provide message authentication.

https://en.wikipedia.org/wiki/Hash_function

```python
def limit_consecutives(input_str, limit=1):
    if limit == 0:
        return ''
    result = ''
    consecutive_count = 1
    previous = None
    for c in input_str:
        if c == previous:
            if consecutive_count < limit:
                result += c
                consecutive_count += 1
        else:
            result += c
            consecutive_count = 1
        previous = c
    return result
```

```java

public  class Stack<T> {
    private T[] elements;
    private int size = 0;

    public Stack(int capacity) {
        elements = new Object[capacity];
    }

    public void push(T elem) {
        if (size == capacity) {
          T[] newElements = new Object[2*capacity];
          // TODO: copy elements
          elements = newElements;          
        }
        elements[size++] = elem;
    }

    public T pop() {
        T result = elements[--size];
        elements[size + 1] = null;
        return result;
    }
}
```

## Resources

* [Gayle L McDowell - Cracking The Coding Interview](https://www.youtube.com/watch?v=rEJzOhC5ZtQ&feature=youtu.be)
* [Binary Search Trees](https://brilliant.org/wiki/binary-search-trees)
* [Sorting Algorithms](https://brilliant.org/wiki/sorting-algorithms)

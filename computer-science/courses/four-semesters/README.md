# Four Semesters of Computer Science in 5 Hours

## Big O and Recursion

"Big O is the way we analyze how efficient algorithms (or code in this case) without getting too mired in the details."

## Sorting

### Bubble Sort

"[Bubble Sort](https://en.wikipedia.org/wiki/Bubble_sort) is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed"

Inefficient - O(n^2)

### Insertion Sort

Good for arrays that are somewhat sorted. Worst case is as inefficient as Bubble sort.

### Merge Sort

Efficient (useful)! Divide and conquer. It's a stable sort. Take the whole list, recursively
divide it down in two halves until you are down to the base case which is a sorted list with one item.
On the way up you will merge sorted lists together.

The input of merge is two sorted lists that should be merged. Compare each element in the lists and take the smallest and proceed through the list with two different indexes (shift smallest from the two lists into a result).

Stable sort means elements that are identical/equivalent by sort have order preserved. Quicksort is not stable. In case of sorting numbers, stability of course makes no difference.

"its worst-case running time is O(n log n). It is also easily applied to lists, not only arrays, as it only requires sequential access, not random access. However, it has additional O(n) space complexity, and involves a large number of copies in simple implementations."

### Median Values

Problem: given two sorted arrays return the median element of the two arrays.

Naive solution: concat arrays and sort and then get the middle one.

Better solution: use merge from merge sort and abort when you have the middle element.

### Quicksort

"Quicksort is a divide and conquer algorithm which relies on a partition operation: to partition an array an element called a pivot is selected. All elements smaller than the pivot are moved before it and all greater elements are moved after it. This can be done efficiently in linear time and in-place. The lesser and greater sublists are then recursively sorted."

"The basic gist is that you take the last element in the list and call that the pivot. Everything that's smaller than the pivot gets put into a "left" list and everything that's greater get's put in a "right" list. You then call quick sort on the left and right lists independently (hence the recursion.) After those two sorts come back, you concatenate the sorted left list, the pivot, and then the right list (in that order.) The base case is when you have a list of length 1 or 0, where you just return the list given to you."

Variations on quicksort are about how to choose the pivot. The most popular strategy is Quicksort 3 which picks the middle value between the first, the middle, and the last item.

Takes less memory than mergesort.

If you get a sorted list and always pick the last item as pivot then you get O(n^2).
Comparing everything to everything is what we are trying to avoid.

* Base case: list with one element or less can be returned as it's already sorted.
* Pick the pivot, now iterate through the list, if the item is smaller than the pivot then put it in the left list, otherwise put it in the right one
* Return [...quickSort(left), ...pivot, ...quickSort(right)]

## Data Structure Interfaces

Black box abstraction.

### Set

Unordered and unique values.

Operations: add, remove, contains, and toList

Useful for deduplication.

ES6 has Set natively.

### Map

A collection of keys with associated values, i.e. a dictionary.
The keys must be unique. Lookup is O(1).

### Stack

Last in, first out (LIFO).

Operations: push, pop. The optional operation peek just returns the last value.

An example of a stack is the call stack in a programming language. When a function
is invoked it gets pushed onto the call stack and when it returns it gets popped from
the stack.

### Queue

First in, first out (FIFO).

Operations: enqueue, dequeue. Opeationally: peek.

There are also priority queues where each item gets assigned a priority.

## Implementing Data Structures

### Array List

An allocated indexed piece of memory. Index lookup is efficient.

Deleting items is expensive since everything after the deleted item has to be shifted.

Optimized for get, not optimized for delete and insert.

When allocating memory you allocate blocks.

### Linked List

The head is a pointer to the first item. Each item has a value and a next pointer. The
last element has a null next pointer. The tail is a pointer to the last item. Getting a value
by index is very expensive if index is large. Delete and insertion is cheap.

### Binary Search Tree

Binary Search Trees (BST) way to store information that makes lookup fast. It's a middle ground between Array List and Linked List. Every value in the tree to the left is less than the value and every value
in the tree to the right is greater. Every node has zero, one, or two children. When you add a value
you traverse the tree from the top and make left/right decisions at each step. Logarithmic search time.

### AVL Tree

"AVL tree are the answer to the problem that BST have: BST can easily get out of balance. Even if it's not the worst case scenario of ascending or descending lists being added, even a random distribution on numbers on a BST is going to pretty heavy in places. There are several ways to balance these trees and we're going to tackle one of them: AVL trees"

The AVL tree should stay as flat as possible. The tree being balanced means that number of levels
to the left of a node should be the same as to the right.

## Resources

* [Wikipedia: Sorting Algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm)
* [Binary Search](https://en.wikipedia.org/wiki/Binary_search_algorithm)
* [Book/PDF: Introduction to Algorithms - Cormen (MIT)](http://io.acad.athabascau.ca/~oscar/ebook/algorithms.pdf)
* [Course Homepage](https://frontendmasters.com/courses/computer-science)
* [Course Material](http://btholt.github.io/four-semesters-of-cs/)

# Functional Programming Principles in Scala

## Assignment 1

### Pascal’s Triangle

"The numbers at the edge of the triangle are all 1, and each number inside the triangle is the sum of the two numbers above it. Write a function that computes the elements of Pascal’s triangle by means of a recursive process."

"Do this exercise by implementing the pascal function in Main.scala, which takes a column c and a row r, counting from 0 and returns the number at that spot in the triangle. For example, pascal(0,2)=1,pascal(1,2)=2 and pascal(1,3)=3."

### Parentheses Balancing

"Write a recursive function which verifies the balancing of parentheses in a string, which we represent as a List[Char] not a String. For example, the function should return true for the following strings:

(if (zero? x) max (/ 1 x))
I told him (that it’s not (yet) done). (But he wasn’t listening)
The function should return false for the following strings:

:-)
())(

The last example shows that it’s not enough to verify that a string contains the same number of opening and closing parentheses."

### Counting Change

"Write a recursive function that counts how many different ways you can make change for an amount, given a list of coin denominations. For example, there are 3 ways to give change for 4 if you have coins with denomination 1 and 2: 1+1+1+1, 1+1+2, 2+2."

"Once again, you can make use of functions isEmpty, head and tail on the list of integers coins."

"Hint: Think of the degenerate cases. How many ways can you give change for 0 CHF(swiss money)? How many ways can you give change for >0 CHF, if you have no coins?"

## Resources

* [Assignment 1 - Recursion](https://www.coursera.org/learn/progfun1/programming/Ey6Jf/recursion)

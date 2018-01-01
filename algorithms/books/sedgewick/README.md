# Algorithms (Sedgewick)

## 1. Fundamentals

### 1.1 Basic Programming Model

"The term algorithm is used in computer science to describe
a finite, deterministic, and effective problem-solving method suitable for implementation
as a computer program."

"We can define an algorithm by describing a procedure for solving a problem in a
natural language, or by writing a computer program that implements the procedure,
as shown at right for Euclid’s algorithm for finding the greatest common divisor of
two numbers, a variant of which was devised
over 2,300 years ago."

```java
public static int gcd(int p, int q) {
  if (q == 0) return p;
  int r = p % q;
  return gcd(q, r);
}
```

### 1.3 Bags, Queues, and Stacks

API - each container data type (`Bag`, `Queue`, `Stack`) has an empty constructor, a method for adding (`add`, `enqueue`, `push`), an optional removal method (`dequeue`, `pop`), `isEmpty`, and `size`.

The container types use generics to be able to hold any type of data.

```java
Stack<String> stack = new Stack<String>();
stack.push("Test");
String next = stack.pop();

Queue<Date> queue = new Queue<Date>();
queue.enqueue(new Date(12, 31, 1999));
Date next = queue.dequeue();
```

Collections should also be iterable:

```java
Queue<Transaction> collection = new Queue<Transaction>();
for (Transaction t : collection) {
  StdOut.println(t);
}
```

Dijkstra’s Two-Stack Algorithm for Expression Evaluation:

```java
public class Evaluate
  {
    public static void main(String[] args)
    {
      Stack<String> ops = new Stack<String>();
      Stack<Double> vals = new Stack<Double>();
      while (!StdIn.isEmpty())
      { // Read token, push if operator.
        String s = StdIn.readString();
        if (s.equals("(")) ;
        else if (s.equals("+")) ops.push(s);
        else if (s.equals("-")) ops.push(s);
        else if (s.equals("*")) ops.push(s);
        else if (s.equals("/")) ops.push(s);
        else if (s.equals("sqrt")) ops.push(s);
        else if (s.equals(")"))
        { // Pop, evaluate, and push result if token is ")".
          String op = ops.pop();
          double v = vals.pop();
          if (op.equals("+")) v = vals.pop() + v;
          else if (op.equals("-")) v = vals.pop() - v;
          else if (op.equals("*")) v = vals.pop() * v;
          else if (op.equals("/")) v = vals.pop() / v;
          else if (op.equals("sqrt")) v = Math.sqrt(v);
          vals.push(v);
        } // Token not operator or paren: push double value.
        else vals.push(Double.parseDouble(s));
      }
    StdOut.println(vals.pop());
  }
}
```

```
export CLASSPATH=$CLASSPATH:lib/algs4.jar:classes
javac -d classes src/Evaluate.java
java Evaluate
( 1 + 1 )
ctrl-D
```

## Resources

* [Book Homepage](https://algs4.cs.princeton.edu/home)
* [Book Source Code](https://algs4.cs.princeton.edu/code/)

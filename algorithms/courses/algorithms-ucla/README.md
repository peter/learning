# Algorithmic Toolbox (Coursera)

## Week 1

### Maximum Pairwise Addition

Given a sequence of non-negative integers a0,…,an−1, find the maximum pairwise product, that is, the largest integer that can be obtained by multiplying two different elements from the sequence (or, more formally, max0≤i≠j≤n−1aiaj). Different elements here mean ai and aj with i≠j (it can be the case that ai=aj).

A brute force quadratic time solution may time out:

"This is because our program performs about n2 steps on a sequence of length n. For the maximal possible value n=200,000=2⋅10^5, the number of steps is about 10,000,000,000=10^10. This is too much. Recall that modern machines can perform roughly 10^9 basic operations per second (this depends on a machine of course, but 10^9 is a reasonable average estimate)"

Improvement, find the two largest numbers (linear time):

```c
long long MaxPairwiseProductFast(const vector<int>& numbers) {
  int n = numbers.size();

  int max_index1 = -1;
  for (int i = 0; i < n; ++i)
    if ((max_index1 == -1) || (numbers[i] > numbers[max_index1]))
      max_index1 = i;

  int max_index2 = -1;
  for (int j = 0; j < n; ++j)
    if ((numbers[j] != numbers[max_index1]) && ((max_index2 == -1) || (numbers[j] > numbers[max_index2])))
      max_index2 = j;

  return ((long long)(numbers[max_index1])) * numbers[max_index2];
}
```

Now, you decide to check how long does it take your program to process a large dataset. For this, you pass an array of size 200,000=2⋅105 filled in by zeroes to your new function.

### Stress Testing

* A few small manual tests.
* A test for each possible type of answer (smallest answer, biggest answer, answer doesn't exist, etc.)
* Test for time/memory limit: generate a test with the largest possible size of input ("max test"), run your program, measure time and memory consumption.

Tests for corner cases:

* Smallest possible "n": the length of the input sequence or string, the number of queries, etc.
* Equal numbers, equal letters in the string, more generally, equal objects in the input. Any two objects that are not restricted to be different in the problem statement can be equal.
* Largest numbers in the input allowed by the problem statement - for example, to test for integer overflow.
* Degenerate cases like empty set, three points on one line, a tree which consists of just one chain of nodes.

A stress test consists of four parts:

1. The solution you want to test.
2. A different, possibly trivial and very slow, but easy to implement and obviously correct solution to the problem.
3. A test generator.
4. An infinite loop in which a new test is generated, it is fed into both solutions, then the results are compared, and if they differ, the test and both answers are output, and the program stops, otherwise the loop repeats.

```c
while (true) {
  int n = rand() % 10 + 2;
  cerr << n << "\n";
  vector<int> a;
  for (int i = 0; i < n; ++i) {
    a.push_back(rand() % 100000);
  }
  for (int i = 0; i < n; ++i) {
    cerr << a[i] << ' ';
  }
  cerr << "\n";
  long long res1 = MaxPairwiseProduct(a);
  long long res2 = MaxPairwiseProductFast(a);
  if (res1 != res2) {
    cerr << "Wrong answer: " << res1 << ' ' << res2 << "\n";
    break;
  }
  else {
    cerr << "OK\n";
  }
}
```

"Test on the examples from the problem statement. Then make a few other small tests, solve them manually and check that your program outputs the correct answer. Generate a big input and launch your program to check that it works fast enough and doesn't consume too much memory. Test for corner cases: smallest allowed values and largest allowed values of all input parameters, equal numbers in the input, very long strings, etc. Then make a stress test. After all these tests passed, submit the solution."

## Resources

* [Course Home](https://www.coursera.org/learn/algorithmic-toolbox/home/welcome)

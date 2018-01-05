# Language Comparison

## Hello World

Java:

```java
public class Hello {
  public static void main(String[] args) {
    System.out.println("Hello World!");
  }
}
```

Python:

```python
print('Hello World!')
```

## Split String

Java:

```java
String numberString = "1,2,3,4,5";
int[] numbers = Arrays.stream(numberString.split(",")).mapToInt(Integer::parseInt).toArray();
```

Python:

```python
numberString = '1,2,3,4,5'
numbers = [int(n) for n in numberString.split(',')]
```

Ruby:

```ruby
"1,2,3,4,5".split(",").map(&:to_i)
```

Kotlin:

```kotlin
val numberString = "1,2,3,4,5"
val numbers = numberString.split(",").map { it.toInt() }
```

Clojure:

```clojure
(require '[clojure.string :as str])
(map #(Integer/parseInt %) (str/split "1,2,3,4,5" #","))
; Alternative:
(map read-string (str/split "1,2,3,4,5" #","))
```

## Join List

Java:

```java
List<Integer> numbers = Arrays.asList(4, 8, 15, 16, 23, 42);
String numberString = numbers.stream()
                        .map(Object::toString)
                        .collect(Collectors.joining( "," ));
```

Python:

```python
numbers = [4, 8, 15, 16, 23, 42]
numberString = ",".join([str(n) for n in numbers])
```

Kotlin

```kotlin
val numbers = listOf(4, 8, 15, 16, 23, 42)
val numberString = numbers.joinToString(",")
```

## Get n:th value from list/array or default

Python

```
my_list = [1, 2, 3]
my_list[3] if len(my_list) > 3 else 'default-value'
```

Ruby:

```ruby
my_list = [1, 2, 3]
my_list[3] || 'default-value'
```

## Interpolate String

Java:

```java
String.format("a=%s b=%s c=%s", a, b, c)
```

Python:

```python
# Python 3.6 (https://www.python.org/dev/peps/pep-0498):
f"a={a} b={b} c={c}"

# Older versions:
"a={} b={} c={}".format(a, b, c)
```

Kotlin:

```kotlin
"a=$a b=$b c=$c"
```

## Match Regex

Python:

```python
import re
re.match(r'^([1-9][0-9]*|[0-9])$', my_string)
```

## Extract Substring with Regex

Python:

```python
import re
re.match(r'^(.+)_bar$', 'foo_bar').group(1) # => 'foo'
```


## Copy/Clone List or Dictionary

Python:

```python
import copy
new_list_shallow = copy.copy(old_list)
new_list_deep = copy.deepcopy(old_list)

# Alternative shallow copy:
new_list_shallow = list(old_list)
```

## For loop with index

Python:

```python
my_list = [3, 2, 1]
for i, item in enumerate(my_list):
    print(i, item)
```

## Dynamic Function Invocation

Python:

```python
import sys

def current_module():
    return sys.modules[__name__]

def lookup_function(name):
    return getattr(current_module(), name)

def my_function():
  return 'foobar'

lookup_function('my_function')() # => 'foobar'
```

Ruby:

```ruby
def my_function
  'foobar'
end

self.send('my_function') # => 'foobar'
```

## Dynamic Listing of Functions and Variables in Module

Python:

```python
import sys

def current_module():
    return sys.modules[__name__]

dir(current_module())

# Alternative:
import inspect
inspect.getmembers(current_module())
```

* [inspect module](https://docs.python.org/3/library/inspect.html)

## Elapsed Time

Python:

```python
import time
start_time = time.time() # floating point seconds since epoch
# Code here
elapsed_seconds = time.time() - start_time
```

* [timeit module](https://docs.python.org/3/library/timeit.html)
* [python decorator for profiling functions](https://stackoverflow.com/questions/3620943/measuring-elapsed-time-with-the-time-module)

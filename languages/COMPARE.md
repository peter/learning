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

Clojure:

```clojure
(println "Hello World!")
```

Elixir:

```elixir
IO.puts "Hello World"
```

JavaScript:

```javascript
console.log('Hello World!')
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

JavaScript:

```javascript
"1,2,3,4,5".split(",").map(n => parseInt(n))
```

Clojure:

```clojure
(require '[clojure.string :as str])
(map #(Integer/parseInt %) (str/split "1,2,3,4,5" #","))
; Alternative:
(map read-string (str/split "1,2,3,4,5" #","))
```

Elixir:

```elixir
"1,2,3,4,5" |> String.split(",") |> Enum.map(&String.to_integer/1)
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
numberString = ", ".join([str(n) for n in numbers])
```

JavaScript:

```javascript
const numbers = [4, 8, 15, 16, 23, 42]
const numberString = numbers.join(", ")
```

Clojure:

```clojure
(require '[clojure.string :as str])
(let [numbers [4, 8, 15, 16, 23, 42]
      number-string (str/join ", " numbers)])
```

Elixir:

```elixir
Enum.join([4, 8, 15, 16, 23, 42], ", ")
```

Kotlin

```kotlin
val numbers = listOf(4, 8, 15, 16, 23, 42)
val numberString = numbers.joinToString(",")
```

## Truth

Java: only `true` and `false` are valid in a boolean context, there is no concept of truthy/falsy

Ruby: only `nil` and `false` are falsy

Python: treats `None`, `False`, `0`, and empty sequences such as `""`, `[]`, `{}`, `()` as falsy. If `bool(value)` returns `False` then the value is falsy. Python will invoke `__bool__` or `__len__` to figure out the boolean value.

JavaScript: treats `false`, `null`, `undefined`, `0`, `NaN`, `""` (empty string) as falsy. Empty arrays and objects are truthy.

Clojure: only `nil` and `false` are falsy

## Equality

Java: you need to use/implement the `equals` method for value based equality. The `==` operator is identity based.

Ruby: you can use `==` for value based equality checks of arrays and maps

Python: you can use `==` for value based equality checks of arrays and maps

JavaScript: you can *not* use `==`for value based equality checks of objects and arrays

Clojure: provides value based equality via the `=` operator for primitive data types and built in composite data types such as vector, map, set etc. Due to immutability equality checks are fast.

## Immutability

Java: strings are immutable

JavaScript: strings are immutable

Python: strings are immutable

Ruby: strings are mutable

## Initialize Variable with Default if Null

Ruby:

```
my_var ||= 'some-default-value'
```

Python:

```python
my_var = 'some-default-value' if my_var is None else my_var

# Alternative 1:
if my_var is None:
  my_var = 'some-default-value'

# Alternative 2:
my_var = vars().get('my_var', 'some-default-value')
```

## Anomymous Functions

Python:

```python
foo = lambda n: n*n
foo(3) # => 9
# NOTE: Python lambdas are single line only
```

JavaScript:

```javascript
const foo = (n) => n*n
foo(3)
```

Clojure:

```clojure
(let [foo #(* % %)]
  (foo 3))
; Alternative syntax with argument names
(let [foo (fn [n] (* n n))]
  (foo 3))
```

## Conditional with Assignmemt

Clojure:

```clojure
(defn get-data [] "the-data")

(if-let [data (get-data)]
  (println data))
```

Ruby:

```ruby
def get_data
  "the-data"
end

if data = get_data
  puts data
end
```

Java: not possible

JavaScript: not possible

Python: not possible

## Single Line Conditional

Java:

```java
public static void foobar(Integer n) {
  if (n == null) return;
}
```

JavaScript:

```javascript
function foobar(n) {
  if (n == null) throw new Error("n cannot be null or undefined")
}
```

Ruby:

```ruby
def get_data
  "the-data"
end

def should_get_data?
  true
end

get_data if should_get_data?
```

JavaScript:

```javascript
function getData() {
  return 'the-data'
}
function shouldGetData() {
  return true
}
if (shouldGetData()) getData()
```

Clojure:

```clojure
(defn get-data[] "the-data")
(defn should-get-data?[] true)
(if (should-get-data?) (get-data)) ; => "the-data"
```

Python: not possible

## Ternary operator

JavaScript:

```javascript
const foo = n % 2 == 0 ? 'even' : 'odd'
```

Python:

```python
# NOTE: Python doesn't have the ternary operator
foo = 'even' if n % 2 == 0 else 'odd'
```

Clojure:

```clojure
(def n 10)
(let [foo (if (= (mod n 2) 0) "even" "odd")]
     (println foo)) ; => "even"

; Alternative:
(let [foo (if (even? n) "even" "odd")]
     (println foo)) ; => "even"
```

## Get n:th value from list/array or default

Python

```python
my_list = [1, 2, 3]
my_list[3] if len(my_list) > 3 else 'default-value'

def nth(items, index, default=None):
  return items[index] if len(items) > index else default

nth([1, 2, 3], 3) # => None
nth([1, 2, 3], 3, 'default value') # => 'default value'
```

JavaScript:

```javascript
const myList = [1, 2, 3]
myList[3] || 'default-value'
```

Ruby:

```ruby
my_list = [1, 2, 3]
my_list[3] || 'default-value'
```

Clojure:

```clojure
(let [my-list [1, 2, 3]]
  (nth my-list 3 "default-value")) ; => "default-value"
```

## Partial Function Application and Currying

Python:

```python
from functools import partial
basetwo = partial(int, base=2)
basetwo('10010')
```

Clojure:

```clojure
(defn add [a b] (+ a b))
(map (partial add 2) [3 5]) ; => [5, 7]
```

JavaScript:

```javascript
function add(a, b) {
  return a + b
}
[3, 5].map(add.bind(null, 2))
```

## String Interpolation

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

JavaScript:

```javascript
`a=${a} b=${b} c=${c}`
```

Kotlin:

```kotlin
"a=$a b=$b c=$c"
```

Clojure:

```clojure
(str "a=" a " b=" b " c=" c)
```

Elixir:

```elixir
"a=#{a} b=#{b} c=#{c}"
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

## Read a File

Python:

```python
# Using the [open context manager](http://docs.python-guide.org/en/latest/writing/structure):
with open('README.md') as f:
    data = f.read()

# Read one integer per line:
with open('my-data-file.txt') as f:
    a = [int(x) for x in f]

# Alternative 1:
data = open('README.md').read()

# Alternative 2:
data = open('README.md').readlines()
def chomp(line):
  return line.rstrip('\r\n')
data = [chomp(l) for l in open('README.md').readlines() if chomp(l)]
```

Clojure:

```
(slurp "README.md")
```

## Write a File

Clojure:

```
(spit "/tmp/foobar" "this is the data")
(slurp "/tmp/foobar") ; => "this is the data"
```

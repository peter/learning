# Language Comparison

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
val numbers: List<Int> = numberString.split(",").map { it..trim().toInt() }
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

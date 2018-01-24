# Strings

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

## Immutability

Java: strings are immutable

JavaScript: strings are immutable

Python: strings are immutable

Ruby: strings are mutable

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

## Parsing Strings

Python:

```python
def parse_boolean(value):
    if isinstance(value, str):
        return value.lower() in ['t', 'true', '1']
    else:
        return value

def valid_int(value):
    if isinstance(value, str) and re.match('^([1-9][0-9]*|[0-9])$', value):
        return True
    else:
        return isinstance(value, int)
```

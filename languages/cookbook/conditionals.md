# Conditionals

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

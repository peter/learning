# Truth

Java: only `true` and `false` are valid in a boolean context, there is no concept of truthy/falsy

Ruby: only `nil` and `false` are falsy

Python: treats `None`, `False`, `0`, and empty sequences such as `""`, `[]`, `{}`, `()` as falsy. If `bool(value)` returns `False` then the value is falsy. Python will invoke `__bool__` or `__len__` to figure out the boolean value.

JavaScript: treats `false`, `null`, `undefined`, `0`, `NaN`, `""` (empty string) as falsy. Empty arrays and objects are truthy.

Clojure: only `nil` and `false` are falsy

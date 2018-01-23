# Equality

Java: you need to use/implement the `equals` method for value based equality. The `==` operator is identity based.

Ruby: you can use `==` for value based equality checks of arrays and maps

Python: you can use `==` for value based equality checks of arrays and maps

JavaScript: you can *not* use `==`for value based equality checks of objects and arrays

Clojure: provides value based equality via the `=` operator for primitive data types and built in composite data types such as vector, map, set etc. Due to immutability equality checks are fast.

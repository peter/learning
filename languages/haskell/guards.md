# Guards

Defining functions based on predicates.

```haskell
absolute x = if (x < 0) then (-x) else x

absolute x
  | x < 0 = -x
  | otherwise = x
```

```haskell
mylength l =
  [] -> 0
  (x:xs) = 1 + mylength xs
```

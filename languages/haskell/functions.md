# Functions

## Conditional Functions

One definition per case:

```haskell
length [] = 0
length x:xs = 1 + length xs
```

With if statement:

```haskell
length lst =
  if lst == []
    then 0
    else let x:xs = lst in 1 + length xs
```

With guards:

```haskell
length lst
  | lst == [] = 0
  | otherwise = let x:xs = lst in 1 + length xs
```

With a where clause on a single line (prefix with let in the REPL):

```haskell
f = f' where f' 1 = 0; f' x = x + f' (x-1)
```

An if statement also works as a one-liner in the REPL:

```haskell
let length lst = if lst == [] then 0 else let x:xs = lst in 1 + length xs
```

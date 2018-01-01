# Lists

Two approaches to working with lists:

* Using recursion to traverse the list structure
* Use the standard list processing functions

The latter approach is preferred.

A list is built from the empty list [] and the function cons :: a -> [a] -> [a]. The (:) operator is equivalent to cons. Every list is either [] or (x : xs) for some head x and some tail xs.

Map is a special case of fold.

## Recursive definition of length

```haskell
length :: [a] -> Int
length [] = 0                  -- base case
length (x:xs) = 1 + length xs  -- recursion/induction case
```

## Recursive definition of filter

```haskell
filter :: (a -> Bool) -> [a] -> [a]
filter pred []     = []
filter pred (x:xs)
  | pred x         = x : filter pred xs
  | otherwise      = filter pred xs
```

## Recursive definition of map

```haskell
map :: (a -> b) -> [a] -> [b]
map _ [] = []
map f (x:xs) = f x : map f xs
```

## Function Composition

```haskell
(.) :: (b->c) -> (a->b) -> a -> c
(f . g) x = f (g x)
```

## Composition of maps

```haskell
map f (map g xs) = map (f . g) xs
```

Example:

```haskell
map ((+5) . (*3)) [1..10]
```

## Folding

An iteration over a list to produce a singleton value is called fold. By convention the list type is b and the singleton value type is a. You can fold from the left with `foldl` and from the right with `foldr`.

```haskell
foldl :: (a -> b -> a) -> a -> [b] -> a
foldr :: (a -> b -> b) -> b -> [a] -> b
```

```haskell
foldl :: Foldable t => (b -> a -> b) -> b -> t a -> b
```

Examples:

```haskell
sum      = foldr (+) 0
product  = foldr (*) 1

-- With foldr, the accumulator is the second argument:
foldr (\item acc -> item : acc) [] [1] -- > [1]

-- With foldl, the accumulator is the first:
foldl (\acc item -> item : acc) [] [1] -- > [1]
```

(This is sometimes called “point free” style because you’re programming solely with the functions; the data isn’t mentioned directly.)

See maps_folds.hs for more example code.

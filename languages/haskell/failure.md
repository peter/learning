# Failure

Example: dividing to integers and the divisor is zero.

We can use `Maybe` from the `Prelude` library to deal with errors
or exceptional cases.

```haskell
data Maybe a = Nothing | Just a
  deriving (Eq, Ord)
```

```haskell
-- Find the max value in an Int list
maxhelper :: Int -> [Int] -> Int
maxhelper x [] = x
maxhelper x [y:ys] = maxhelper
  (if x>y then x else y) ys

maxfromlist :: [Int] -> Maybe Int
maxfromlist [] = Nothing
maxfromlist (x:xs) = Just (maxhelper x xs)
```

We can use `fmap` to apply a function to a value inside a Maybe:

```haskell
let inc = (1+)
:type inc -- > inc :: Num a => a -> a
fmap inc (Just 1) -- > Just 2
fmap inc Nothing -- > Nothing
```

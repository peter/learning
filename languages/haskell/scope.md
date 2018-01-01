# Scope

Scoping is about limiting the region of the program in which a name exists and can be used.

A let expression provides local scope.

```haskell
let x = 2
    y = 3
in x+y
```

```haskell
journeycost :: Float -> Float -> Float
journeycost miles fuelcostperlitre =
  let milespergallen = 35
      litrespergallen = 4.55
      gallons = miles/milespergallon
  in (gallons*litrespergallon*fuelcostperlitre)
```

Haskell is the Swiss army knife of programming languages, there are lots of ways of doing things. You can also use `where`:

```haskell
squareplusone :: Int -> Int
squareplusone x = xsquared + §
  where xsquared = x * x
```

# Case Expressions

```haskell
data Pet = Cat | Dog | Fish

hello :: Pet -> String
hello x =
  case x of
    Cat -> "meeow"
    Dog -> "woof"
    Fish -> "bubble"
```

```haskell
data Pet = Cat | Dog | Fish | Parrot String
hello :: Pet -> String
hello x =
  case x of
    Cat -> "meeow"
    Dog -> "woof"
    Fish -> "bubble"
    Parrot name -> "pretty" ++ name
```

Using a catch all (else/otherwise) clause:

```haskell
hello :: Pet -> String
hello x =
  case x of
    Parrot name -> "pretty" ++ name
    _ -> "grunt"
```

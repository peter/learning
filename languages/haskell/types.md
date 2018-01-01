# Types

Types are a set of values that are related. They usually correspond to the valid input or output of a function.

User defined types are custom data types for a program.

A finite set of alternative values:

```haskell
data SimpleNum = One | Two | Many deriving Show
:t One -- > One :: SimpleNum

let convert 1 = One
    convert 2 = Two
    convert _ = Many

map convert [1..5]
```

Number of runs scored, number of players out. Product data type. `Score` is a type constructor that takes a string and two integers:

```haskell
data CricketScore = Score [Char] Int Int deriving Show
let x = Score "New Zealand" 350 4
:t x -- > CricketScore
```

Haskell types are algebraic data types.

## Grow a Tree

In Computer Science trees grow upside-down. The root is at the top and the leaves are at the bottom.

Binary trees are used for sorting. Here is a tree of integer values:

```haskell
data Tree = Leaf | Node Int Tree Tree deriving Show
let l = Node 3 Leaf Leaf
:t l -- > Tree

treeDepth :: Tree -> Int
treeDepth Leaf = 0
treeDepth (Node _ left right) =
  1 + max (treeDepth left) (treeDepth right)

isSortedTree :: Tree -> Int -> Int -> Bool
isSortedTree Leaf _ _ = True
isSortedTree (Node x left right) minVal maxVal =
  let leftSorted = isSortedTree left minVal x
      rightSorted = isSortedTree right x maxVal
  in x >= minVal && x < maxVal && leftSorted && rightSorted
```

## Type Classes

Number types: Int, Float, Integer (high precision). Many arithmetic functions can be applied to any number like type.

```haskell
:t (+) -- > :: Num a => a
:t (==) -- > :: Eq a => a -> a -> Bool
:t (<) -- > :: Ord a => a -> a -> Bool
:t show -- > :: Show a => a -> String
:t read -- > :: Read a => String -> a

read "True" :: Bool -- > True
```

A type class is a family of similar types. Other type classes: Show,

```haskell
data SimpleNum = One | Two | Many deriving (Show, Read, Eq)
One == One -- > True
One == Two -- > False
```

Type classes were one of the early innovations of Haskell. Type classes are like interfaces in OO and enable operator overloading.

Simon Peyton Jones was a lead designer of Haskell and Glasgow was an epicenter of Haskell. Haskell is very unusual in being designed by a group. Haskell has been very influential and has become a thought leader. Lazy means let's proctrastinate as much as possible.

# Haskell Course with Adam at Magine

[Course material](https://docs.google.com/document/d/1AsuBaiBv_35PLi2cqnacM8gQeT_Q04evtZWo1N49Sr8/edit#heading=h.jss03mrmx3oq)

[99 questions/1 to 10](https://wiki.haskell.org/99_questions/1_to_10)

## Getting Started

```
brew install haskell-stack
stack --version # 1.5.1
stack setup # sandbox
stack runghc hello.hs
stack ghci hello.hs
main
:r # reload
:l # filename to load
:q # quit
```

https://www.youtube.com/watch?v=ybba5tcOeEY&index=2&list=PLbgaMIhjbmEm_51-HWv9BQUXcmHYtl4sw

[LYAH - Starting Out](http://learnyouahaskell.com/starting-out)

```
2 + 15
49 * 100
1892 - 1472
5 / 2
(50 * 100) - 4999

True && False
False || True
not False
not (True && True)

5 == 5
5 /= 4
"hello" == "hello"
5 == True -- No instance for (Num Bool) arising from the literal ‘5’
-- "You can't compare apples and oranges"
:t (==) -- (==) :: Eq a => a -> a -> Bool
"hello" == ['h', 'e', 'l', 'l', 'o'] -- True

-- Above are infix function but most are prefix:
succ 8
min 9 10
max 100 101

-- Function application (calling a function by putting a space after it and then typing out the parameters) has the highest precedence
succ 9 + max 5 4 + 1
(succ 9) + (max 5 4) + 1

succ 9 * 10
succ (9 * 10)

-- If a function takes two parameters, we can also call it as an infix function by surrounding it with backticks
div 92 10
92 `div` 10

doubleMe x = x + x
-- doubleMe :: Num a => a -> a

doubleSmallNumber x = if x > 100  
                      then x  
                      else x*2

doubleSmallNumber' x = (if x > 100 then x else x*2) + 1

-- We usually use ' to either denote a strict version of a function (one that isn't lazy) or a slightly modified version of a function or a variable

myFunction = "foobar"
-- myFunction :: [Char]

-- We can use the let keyword to define a name right in GHCI
-- In Haskell, lists are a homogenous data structure
let lostNumbers = [4,8,15,16,23,42]

[1,2,3,4] ++ [9,10,11,12]
"hello" ++ " " ++ "world"
['w','o'] ++ ['o','t']

-- When you put together two lists (even if you append a singleton list to a list, for instance: [1,2,3] ++ [4]), internally, Haskell has to walk through the whole list on the left side of ++
-- However, putting something at the beginning of a list using the : operator (also called the cons operator) is instantaneous.
'A':" SMALL CAT"
5:[1,2,3,4,5]
[1,2,3] == 1:2:3:[] -- True

-- Get element out of list by index with !!
"Steve Buscemi" !! 6
[9.4,33.2,96.2,11.2,23.25] !! 1

let myList = [1,2,3,4,5]
head myList -- 1
tail myList -- [2,3,4,5]
last myList -- 5
init myList -- [1,2,3,4]
head [] -- Exception
length myList
null myList -- False
null [] -- True
reverse myList
take 3 myList
drop 3 myList
minimum myList
maximum myList
sum myList
product myList

-- elem takes a thing and a list of things and tells us if that thing is an element of the list. It's usually called as an infix function because it's easier to read that way.
4 `elem` [3,4,5,6]
:t elem -- :: (Eq a, Foldable t) => a -> t a -> Bool

[1..20]
['a'..'z']
[2,4..20] -- [2,4,6,8,10,12,14,16,18,20]
[3,6..20] -- [3,6,9,12,15,18]

take 10 (cycle [1,2,3])
take 10 (repeat 5)

-- If you've ever taken a course in mathematics, you've probably run into set comprehensions. They're normally used for building more specific sets out of general sets
--  The part before the pipe is called the output function, x is the variable, N is the input set and x <= 10 is the predicate.
[x*2 | x <- [1..10], x*2 >= 12]
[x | x <- [50..100], x `mod` 7 == 3]

-- In some ways, tuples are like lists. Tuples, however, are used when you know exactly how many values you want to combine and its type depends on how many components it has and the types of the components

fst (8,11)
fst ("Wow", False)
snd (8,11)
snd ("Wow", False)

zip [1,2,3,4,5] [5,5,5,5,5]
zip [1 .. 5] ["one", "two", "three", "four", "five"]

let triangles = [ (a,b,c) | c <- [1..10], b <- [1..10], a <- [1..10] ]
```

Hoogle search for function signatures against all packages.

```
ghci test.hs
:reload

:type add1
-- add1 :: Num a => a -> a

:t (+)
-- (+) :: Num a => a -> a -> a

:t (+) :: Int -> Int -> Int
```

## Tutorial

A technique for getting help from compiler with `_` - the compiler will tell you what is missing:

```
map _ [1, 2, 3]
```

Recommended Book:

[Programming in Haskell 2nd Edition](https://www.amazon.com/Programming-Haskell-Graham-Hutton-ebook/dp/B01JGMEA3U/ref=mt_kindle?_encoding=UTF8&me=)

Recommended Course:

[CIS 194: Introduction to Haskell](http://www.seas.upenn.edu/~cis194/fall16/)

YouTube instructions:

[Haskell-1-1](https://www.youtube.com/watch?v=N6sOMGYsvFA)

[Write Yourself a Scheme in 48 Hours](file:///Users/peter/Downloads/Write_Yourself_a_Scheme_in_48_Hours.pdf)

## Types

```
Char
[Char]
Integer
Int
Float
Double
Bool
List []
Maybe (Just x, Nothing)
```

There is no null type. You have to use Maybe.

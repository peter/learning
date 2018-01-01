# Learning Haskell

## Properties/Features

* A function is a relation between a set of possible inputs and a set of possible outputs
* Types are a way of categorizing values
* Functions are curried
* Functions can't begin with uppercase letters
* Some functions are infix operators. To apply such a function in prefix form you must wrap it in parentheses, i.e. (+).
* Anonymous function syntax in Haskell uses a backslash to represent a lambda, i.e. \x -> x
* The $ operator means "evaluate everything to the right of me first", i.e. (2^) $ 2 + 2 means (2^) (2 + 2)
* Whitespace is significant.
* To define a named function in the REPL (ghci) you need to use let, i.e. let triple x = x * 2
* Strings are arrays of chars and literals use double quotes. Char literals use single quotes.
* You can check the type of an expression in the ghci REPL with :t
* Everything is an expression (there are no statements). All expressions evaluate to a result.
* Parentheses are used for grouping, like in mathematics. If you don't need parentheses for grouping they are optional. Operators have precedence similar to other languages.
* Function application happens by writing the function name followed by arguments separated by spaces.
  Function application has the highest precedence.
* Assignment - equations give names to values. A name can be given a value only once, i.e. variables are constants.
  Values are immutable - we never destroy old values, only compute new ones. The garbage collector will collect old
  values that are not used.
* The mechanism for executing imperative programs is to run through a series of statements.
  The mechanism for executing a functional program is reduction, i.e. converting an expression to a simpler form.
  It can be proven that the result does not depend on the reduction path, i.e. correctness does not depend on
  order of execution. This means the compiler can change the order freely to improve performance without affecting
  the result and expressions can be evaluated in parallel. Functions in Haskell is side-effect free and the
  same input will always yield the same output, i.e. they are pure and independent of the state of the world.
* Elements in lists are evaluated lazily, i.e. when they are needed.
* Many of the built in functions in Haskell are defined in the Prelude standard library.
* Relational operators test the relation between values, i.e. == tests whether two values of the same type are equal
* In a if statement the test value must evaluate to a Bool and then and else clauses must be of the same type
* Input and output (I/O) operations are impure. They influence and interact with the ‘outside world’. Output operations return the empty IO value, i.e. IO (). We know from a function’s type whether it is involved with I/O. You sequence IO actions with `do` and ordering is significant there. Order of function evaluation in pure code doesn't matter. The `do` notation is only syntactic sugar, underneath it is rewritten as a chain of function calls.
* The identity function is `id`

## Reduction of Simple Expressions

```haskell
(3+4) * (15-9)
-- >
7 * (15-9)
-- >
7 * 6
-- >
42
```

## What you need to dive in

As explained in [Learn You a Haskell](http://learnyouahaskell.com/introduction#what-you-need) you need to install Haskell on your platform and you can then invoke `ghci` REPL and you can load code in myfunctions.hs with `:l myfunctions` and subsequently invoke `:r` to reload.

Invoke `:set +m` in ghci to enable multiline entry.

## Starting Out

You can try this code out in `ghci`:

Arithmetic:

```haskell
2 + 15 -- > 17
(+) 2 15 -- > 17
49 * 100
1892 - 1472
5 / 2
(50 * 100) - 4999
```

Equality

```haskell
42 == 42 -- > True :: Bool
1 /= 2 -- (not equal) > True :: Bool
"foo" /= "bar" -- > True :: Bool
True /= False -- > True
True == 1 -- > Exception: No instance for (Num Bool)...
```

Comparison:

```haskell
9 < 10 -- > True
[1,2,3] < [1,2,3,4] -- > True
"Aardvark" < "Aaronic" -- > True
```

Boolean expressions:

```haskell
True && False
False || True
not False  
not (True && True)
-- Folding boolean operator over a list:
and [False, True, False, True] -- > False
```

```haskell
5 == 5
5 /= 4
"hello" == "hello"
```

Assignment - equations give names to values

```haskell
answer = 42
```

Function invocation/application, precedence and grouping:

```haskell
succ 8
min 9 10  
min 3.4 3.2  
max 100 101
succ 9 + max 5 4 + 1
(succ 9) + (max 5 4) + 1
succ 9 + max 5 (4 + 1)

abs 5
abs (-5)

sqrt 9+7
sqrt (9+7)

min (max 3 4) 5
```

The expression `abs -5` yields an error as it is interpreted as `abs - 5`.

Function definition:

```haskell
doubleMe x = x + x
```

Let - declaring values (variables) in functions:

```haskell
let lostNumbers = [4,8,15,16,23,42]

fnWithLet :: Num a => a -> a
fnWithLet x =
  let y = x * 2
      z = x^2
  in 2 * y * z

roots a b c =
  let
    det2 = b*b - 4*a*c
    det = sqrt det2
    root1=(-b+det)/2/a
    root2=(-b-det)/2/a
  in
    [root1, root2]
```

In ghci:

```haskell
let x = 5; y = 6 in x * y -- 30
```

In code:

```haskell
mult1 = x * y
  where x = 5
        y = 6
```

Using `where`:

```haskell
mult1 = x * y
  where x = 5
        y = 6

printInc n = print plusTwo
  where plusTwo = n + 2
```

Conditionals with if:

```haskell
max x y =
  if x > y
    then x
    else y

-- The then and else values must have the same type
if True then "foo" else 5 -- > Exception No instance for (Num [Char])
```



Conditionals with case:

```haskell
data Color = Red | Blue | Yellow
color = set_color
action = case color of
  Red -> action1
  Blue -> action2
  Yellow -> action3
```

Hash Map:

```haskell
set :: Data.Map.Map String Integer
set = Data.Map.empty
set' = insert "Answer" 42 set
```

You should break up long lines with 100 chars or more by indenting following lines:

```haskell
x = 10 * 5 + y

x = 10
    * 5 + y
```

Also, lines should not start with space. All declarations in a module must start in the same column.

Lambdas:

```haskell
(\x -> x) 0 -- 0
(\x -> x * 2) 3 -- 6
let square = \x -> x ^ 2
square 10 -- 100
\x y -> x*x + y*y
sumprod = \x y -> [x + y, x * y]

-- Equivalent defintions:
f x = x + 1
f = \x -> x+1
```

Arrays and concatenation:

```haskell
[1,2,3,4] ++ [9,10,11,12]  
[1,2,3,4,9,10,11,12]  
"hello" ++ " " ++ "world"  
"hello world"  
['w','o'] ++ ['o','t']  
```

The dollar ($) operator:

```haskell
(2^) $ (+2) $ 3*2
```

Checking type of expression:

```haskell
:t 'f'
-- 'f' :: Char
:t (+)
-- (+) :: Num a => a -> a -> a
:t True
-- True :: Bool  
:t "HELLO!"  
-- "HELLO!" :: [Char]  
:t (True, 'a')  
-- (True, 'a') :: (Bool, Char)  
:t 4 == 5  
-- 4 == 5 :: Bool  
```

Getting info on functions and operators (some functions are operators):

```haskell
:info (*)
-- infixl 7 *
```

The `*` operator is left associative with precedence 7 (higher is applied first, between 0 and 9). Left associative means that a * b * c is equivalent to (a * b) * c.

Useful built in list functions:

```haskell
head [5,4,3,2,1]
tail [5,4,3,2,1]
last [5,4,3,2,1]
init [5,4,3,2,1]
```

Invoking head, tail, last and init on the empty list [] throws an exception.
You are usually better off with pattern matching than with using head or tail.

```haskell
length [5,4,3,2,1]
null [1,2,3]
null []
reverse [5,4,3,2,1]
take 3 [5,4,3,2,1]
drop 3 [8,4,2,1,5,6]
minimum [8,4,2,1,5,6]
maximum [1,9,2,3,4]
sum [5,2,1,6,3,2,5,7]
elem 4 [3,4,5,6]
take 10 (cycle [1,2,3])
take 10 (repeat 5)
zip [5,3,2,6,2,7,2,5,4,6,6] ["im","a","turtle"]
zip [1..] ["apple", "orange", "cherry", "mango"]
id 1
mod 15 12
1 + (rem 23 7)
```

Infix function invocation:

```haskell
4 `elem` [3,4,5,6]
```

Prefix operator invocation:

```haskell
(+) 100 1
(+1) 100
```

If the function is not commutative then the ordering matters:

```haskell
(1/) 2 -- 0.5
(/1) 2 -- 2.0
```

A list comprehension is a high level notion for specifying the computation of a list.
List comprehensions and ranges:

```haskell
[x*2 | x <- [1..10]]
[x*2 | x <- [1..10], x*2 >= 12]
[ x | x <- [50..100], x `mod` 7 == 3]
boomBangs xs = [ if x < 10 then "BOOM!" else "BANG!" | x <- xs, odd x]
boomBangs [7..13]
removeNonUppercase st = [ c | c <- st, c `elem` ['A'..'Z']]
[[a,b] | a <- [10,11,12] , b <- [20,21]]
-- > [[10,20],[10,21],[11,20],[11,21],[12,20],[12,21]]
```

Tuples:

```haskell
fst (8,11)
fst ("Wow", False)
snd (8,11)
snd ("Wow", False)
let triangles = [ (a,b,c) | c <- [1..10], b <- [1..10], a <- [1..10] ]
```

Type declarations for functions:

```haskell
removeNonUppercase :: [Char] -> [Char]  
removeNonUppercase st = [ c | c <- st, c `elem` ['A'..'Z']]

addThree :: Int -> Int -> Int -> Int  
addThree x y z = x + y + z

factorial :: Integer -> Integer  
factorial n = product [1..n]
```

Type variables

```haskell
:t head  
-- head :: [a] -> a
:t fst  
-- fst :: (a, b) -> a  
```

Type classes (such as Eq, Ord, Show, Read, Enum, Num):

```haskell
:t (==)  
-- (==) :: (Eq a) => a -> a -> Bool

:t (>)  
-- (>) :: (Ord a) => a -> a -> Bool

show 3
read "5" :: Int
read "5" :: Float
read (show 3) :: Float
```

Higher order functions

```haskell
map (\x -> 2 * x + 1) [1..10]
map (\i -> xor (fst i) (snd i)) [(x,y) | x<-[False, True], y<-[False, True]]
filter (<5) [3,9,2,12,6,4] -- > [3,2,4]
foldl (\acc elt -> elt:acc) "" "Reversing a string" -- > "gnirts a gnisreveR"
foldr (\elt acc -> acc ++ [elt]) "" "Reversing a string" -- > "gnirts a gnisreveR"

sum = foldr (+) 0
prod = foldl (*) 1

-- Equivalent:
sum = foldl (+) 0
sum = \xs -> foldl (+) 0 xs

gen_add_n = \n ->
    \x -> x+n
```

Lazy evaluation in lists:

```haskell
answer = 42
yourlist = [7, answer+1, 7*8]
yourlist -- > [7, 43, 56]

[1..] -- > list of all positive numbers
```

Accessing element at certain index in list:

```haskell
[5,3,8,7]  !! 2    -- > 8
```

Checking if element is part of list:

```haskell
elem 1 [1,2,3] -- > True
4 `elem` [1,2,3] -- > False
```

Getting the length of a list:

```haskell
length ["this", "is", "a", "list"] -- > 4
```

Adding an element to a list with the (:) cons operator:

```haskell
23 : [48, 41, 44] -- > [23,48,41,44]
```

If the index is too large or negative then undefined is returned.

Sequences:

```haskell
[0..5]
-- > [0,1,2,3,4,5]
['a'..'z']
-- > "abcdefghijklmnopqrstuvwxyz"
[1.1,1.2 .. 2.0]
```

The zip function is used to combine a pair of lists into a list of pairs:

```haskell
zip [1,2,3] [3,2,1,0] -- > [(1,3),(2,2),(3,1)]
-- :: Num a => [(a, Char)]
zip [1,2,3] ['a','b','c'] -- > [(1,'a'),(2,'b'),(3,'c')]
zip3 "ab" "cd" "ef" -- > [('a','c','e'),('b','d','f')]
zipWith (+) [1,2] [3,4] -- > [4,6]
zipWith max [1,2,3] [0,2,4] -- > [1,2,4]
zipWith (\x y -> (x,y)) [1,2,3] "abc" -- > [(1,'a'),(2,'b'),(3,'c')]
```

You can zip two lists of different types

## IO

Haskell programs use the IO monad to interact with the world. When a function is using IO its type must contain IO. Using `getLine` and `putStrLn`:

```haskell
:type getLine -- > :: IO String
:type putStrLn -- > :: String -> IO ()

putStrLn "hello world" -- > hello world :: IO ()
-- Sequence IO operations with the do construct.
-- Values are bound with the <-, = won't work.
do { putStrLn "what is your name?"; x <- getLine; putStrLn ("hello " ++ x) }

do { putStrLn "what is your name?"; n<-getLine; let nUpper = map toUpper n in putStrLn ("HELLO" ++ nUpper) }

read "42" :: Int
show 42

putStrLn 42 -- > Exception: No instance for (Num String)
putStrLn (show 42)
print 42 -- > same as putStrLn and show
```

Order of evaluation doesn't matter in pure code:

```haskell
let a = reverse "winston"
    b = reverse "churchill"
in "sir" ++ a ++ " " ++ b
```

## Resources

* [Book: Learn You a Haskell](http://learnyouahaskell.com)
* [Book: Real World Haskell](http://book.realworldhaskell.org/read/)
* [Book: Haskell Programming from First Principles (haskellbook.com)](http://haskellbook.com)
* [Book: Programming in Haskell (Second Edition, Kindle)](https://www.amazon.com/Programming-Haskell-Graham-Hutton-ebook/dp/B01JGMEA3U/ref=mt_kindle?_encoding=UTF8&me=)
* [Course: Functional Programming in Haskell](https://www.futurelearn.com/courses/functional-programming-haskell)
* [Try Haskell in your browser](https://www.haskellmooc.co.uk)

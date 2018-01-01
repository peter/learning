# Learning Elm

## Features

* Every element in a list must have the same type.
* Significant whitespace
* Uses structure equality rather than reference equality so that (3, 4) == (3, 4) is true. You can only compare values of the same type.
* If statements always have an else, and the branches must be the same type.
* Code is organized into modules
* Parenthesis are used for tuples and for precedence
* Has type inference, union types, and generics (type variables). Types are always uppercase. Read x : T as x has type T. Functions have types too.
* Has pattern matching in the case statement
* Has function argument destructuring
* Has auto currying (partially apply a function by passing only some of its arguments)

## Strengths

* Pragmatic and simple
* Convention over configuration
* Developer and beginner friendly with very good developer ergonomics. Compiler is very helpful.
* Great tooling
* Draws on strengths of functional programming, static type checking, and Haskell
* Draws of many of the best ideas in frameworks like React and reactive programming. Also borrows async ideas from Erlang.

## Examples

```elm
["the", "quick", "brown", "fox"]
[1, 2, 3, 4, 5]
```

Appending lists and strings (Appendable things can be combined with a ++ b)

```elm
"Hello " ++ "world!" -- "Hello world!"
[1..5] ++ [6..10] == [1..10] -- True
```

```elm
List.head [1..5] -- Just 1
List.tail [1..5] -- Just [2, 3, 4, 5]
List.head [] -- Nothing
```

Tuples: fixed length, heterogeneous:

```elm
("elm", 42)
```

Records:

```elm
{ x = 3, y = 7 }
{ x = 3, y = 7 }.x -- 3
.y { x = 3, y = 7 } -- 7
person = {name = "peter"}
{ person | name = "George" }
{ particle | position = particle.position + particle.velocity }
```

Control flow:

```elm
n = 5
if n < 0 then
  "n is negative"
else if n > 0 then
  "n is positive"
else
  "n is zero"
```

```elm
case aList of
  [] -> "matches the empty list"
  [x]-> "matches a list of exactly one item, " ++ toString x
  x::xs -> "matches a list of at least one item whose head is " ++ toString x
```

You can pattern match in function definitions when there's only one case (single argument tuple):

```elm
area (width, height) =
  width * height

area (6, 7) -- 42
```

```elm
volume {width, height, depth} =
  let
    area = width * height
  in
    area * depth

volume { width = 3, height = 2, depth = 7 } -- 42
```

Functions can be recursive:

```elm
fib n = if n < 2 then 1 else fib (n - 1) + fib (n - 2)
List.map fib [0..8] -- [1, 1, 2, 3, 5, 8, 13, 21, 34]
```

Type signature for functions:

```elm
double : Int -> Int
double x = x * 2

List.map : (a -> b) -> List a -> List b
```

Type signature for records:

```elm
origin : { x : Float, y : Float, z : Float }
origin =
  { x = 0, y = 0, z = 0 }
```

Type alias:

```elm
type alias Point3D =
  { x : Float, y : Float, z : Float }
otherOrigin : Point3D
otherOrigin =
  Point3D 0 0 0
origin == otherOrigin -- True
```

Union types with tags:

```elm
type Direction =
  North | South | East | West

type IntTree =
  Leaf | Node Int IntTree IntTree
```

Union types (and type aliases) can use type variables:

```elm
type Tree a =
  Leaf | Node a (Tree a) (Tree a)

leftmostElement : Tree a -> Maybe a
leftmostElement tree =
  case tree of
    Leaf -> Nothing
    Node x Leaf _ -> Just x
    Node _ subtree _ -> leftmostElement subtree
```

Modules export everything by default

```elm
module Name where
module Name (MyType, myValue) where -- exports MyType and myValue

-- Imports the Dict module and the Dict type, so your annotations don't have to
-- say Dict.Dict. You can still use Dict.insert.
import Dict exposing (Dict)

import Graphics.Collage as C
```

Lists:

```elm
[1..4]
[1,2,3,4]
1 :: [2,3,4]
1 :: 2 :: 3 :: 4 :: []
```

Tooling

```sh
elm make MyFile.elm

# The reactor is a server that compiles and runs your files.
# Click the wrench next to file names to enter the time-travelling debugger!
elm reactor

elm repl

elm package install evancz/elm-html
```

elm-format

## Resources

* [Course: Elm for Beginners](http://courses.knowthen.com/courses/elm-for-beginners)
* [Elm Conf](https://www.elm-conf.us)
* [create-elm-app](https://www.npmjs.com/package/create-elm-app)
* [Heroku buildpack and TODOMVC app](https://github.com/HappyAndHarmless/heroku-buildpack-elm)
* [Book: Elm in Action](https://www.manning.com/books/elm-in-action)
* [Learn X in Y Minutes](https://learnxinyminutes.com/docs/elm/)
* [Elm Syntax](http://elm-lang.org/docs/syntax)
* [Union Types](http://guide.elm-lang.org/types/union_types.html)
* [Video: Richard Feldman - Introduction to Elm (March 2016)](https://www.youtube.com/watch?v=zBHB9i8e3Kc)
* [Video: Confident Frontend with Elm (Jack Franklin) - Full Stack Fest 2016](https://www.youtube.com/watch?v=rDQ22Yg3Fms)
* [Video: Adventures in Elm](https://www.youtube.com/watch?v=cgXhMc8M4X4)
* [Video: "Beyond Hello World and Todo Lists" by Ossi Hanhinen ](https://www.youtube.com/watch?v=vpc80c5iC6k)
* [HTML to Elm (Tool)](http://mbylstra.github.io/html-to-elm/)
* [Learning FP the hard way: Experiences on the Elm language](https://gist.github.com/ohanhi/0d3d83cf3f0d7bbea9db)
* [Learning Elm - Lucas Reis](http://lucasmreis.github.io/blog/learning-elm-part-1/)
* [Elm: Concurrent FRP for Functional GUIs](http://elm-lang.org/papers/concurrent-frp.pdf)
* [Building a simple admin interface using elm](https://jazmit.github.io/2015/06/17/elm-admin-interface.html)

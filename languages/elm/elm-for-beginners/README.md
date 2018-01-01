# Course: Elm for Beginners

Course notes

## Hello World

```
elm package install elm-lang/html
```

```elm
module Main exposing (..)

import Html


main =
    Html.text "Hello World"
```

```
elm reactor
```

## Functions

```elm
module main exposing (..)

import Html

add a b =
  a + b

result =
  add 1 2

main =
  Html.text result
```

* The pipe operator is `|>`.
* Anonymous functions use Haskell syntax with a backslash
* Elm ensures that functions are pure, i.e. do not modify state (the outside world)
* You can use let-in blocks like in Haskell

```elm
List.map ((+) 2) [1, 2, 3]
List.map (\n -> n + 2) [1, 2, 3]
```

You can create your own infix functions (use sparingly). All functions with names with only non-alphanumeric characters are considered infix by Elm:

```elm
(~+) a b =
  a + b + 0.1
1 ~+ 2 -- > 3.1
(~+) 1 2 -- > 3.1
```

Like in Haskell, you can invoke prefix functions as infix functions with backticks:

```elm
add a b =
  a + b

1 `add` 2
```

Functions are curried.

It's worthwhile looking through the [Basics functions]() in the core package.

The default imports in Elm are:

```elm
import Basics exposing (..)
import Debug
import List exposing ( List, (::) )
import Maybe exposing ( Maybe( Just, Nothing ) )
import Result exposing ( Result( Ok, Err ) )
import Platform exposing ( Program )
import Platform.Cmd exposing ( Cmd, (!) )
import Platform.Sub exposing ( Sub )
```

## Static Type System

Types are inferred so you don't need to declare them but it is often a good idea to do so anyway. The static type system in Elm makes runtime exceptions very rare.

The role of the Elm compiler is to help you fix bugs at compile time.

## Elm Types

```elm
"a string" -- > String
'c' -- > Char
True
False
["Joe", "Adam"] --> List String
("pie", 3.14) --> ( String, Float )
```

Records are like objects in JavaScript but you cannot ask for a field that does not exist and a record field will never be undefined or null. You also can't create recursive records.

```elm
person = {name = "James", age = 42} -- > : { name : String, age : number }
person.name -- > "James"
.name person --> "James"
person.foobar -- > TYPE MISMATCH error
olderPerson = { person | age = 43}
person.age -- > 42 : number
olderPerson.age -- > 43 : number
```

Union types are enumerations:

```elm
type Action = AddPlayer | Score
action = AddPlayer
```

You can add additional information via type constructors:

```elm
-- AddPlayer: name of player
-- Score: who scored (player ID), how many points?
type Action = AddPlayer String | Score Int Int
msg = AddPlayer "James"
```

You can use pattern matching to switch on union types:

```elm
case msg of
  AddPlayer name -> "TODO: add player " ++ name
  Score playerId points -> "TODO: score " ++ (toString playerId) ++ " " ++ (toString points)
```

Using `Maybe` allows us to avoid null related errors. Tony Hoare calls his invention of the null value a "billion-dollar mistake". Elm does not allow null values. A Maybe is a union type:

```elm
type Maybe a = Just a | Nothing
```

```elm
first = List.head [] -- > Nothing
case first of
  Just val -> val
  Nothing -> "Empty"
```

When you use Maybe in Elm the compiler ensures you have dealt with the empty/null case.

You can deal with computations that may fail with a `Result`:

```elm
type Result error value = Ok value | Err error
```

```elm
import Date
someDate = Date.fromString "01/01/1974"
case someDate of
  Ok val -> "Legit date"
  Err err -> err
someDate = Date.fromString "Not a date" -- > Err "Unable to parse..."
```

You can use `Maybe.map` to transform the value in a Maybe.

## Type Annotations

Type annotations are optional in Elm but type annotations disambiguate the type signature of
a function and serve as documentation.

```elm
type alias Item =
  {name: String,
   price: Float,
   qty: number,
   discounted: Bool}

cart : List Item
cart =
  [ {name = "Lemon", price = 0.5, qty = 1, discounted = False}
    {name = "Apple", price = 1.0, qty = 5, discounted = False}
    {name = "Pear", price = 1.25, qty = 10, discounted = False}
  ]

-- fiveOrMoreDiscount item =
--   if item.qty >= 5 then
--     { item
--         | price = item.price * 0.8
--         , discounted = True
--     }
--   else
--     item

discount : number -> Float -> Item -> Item
discount minQty discPct item =
  if not item.discounted && item.qty >= minQty then
    { item
        | price = item.price * (1.0 - discPct)
        , discounted = True
    }
  else
    item

newCart : List Item
newCart =
  List.map ((discount 10 0.3) >> (discount 5 0.2)) cart

main : Html.Html msg
main =
  Html.text (toString newCart)
```

Writing type annotations first can help you think about your functions and write better functions.
If you are unsure about what the type annotation should be you can start with the inferred types.

## Planning the Scorekeeper App

Three sections in an Elm app:

* Model (state)
* Update (behavior)
* View (UI)

```elm
type alias Player = {
  id: Int
  , name: String
  , points: Int
}

type alias Play = {
  id: Int
  , playerId: Int
  , name: String
  , points: Int
}

type alias Model = {
  players: List Player
  , playerName: String
  , playerId: Maybe Int
  , plays: List Play
}

type Msg = Edit | Score | Input | Save | Cancel | DeletePlay
```

We should break our app up into a hierarchy of components.

* main view
  * player section
    * player list header
    * player list
      * player
    * point total
  * player form
  * play section
    * play list header
    * play list
      * play

TODO: create functions for each of the above.

## Using a Build Process

There is a starter environment in the directory "05 scorekeeper-starter".

## Building the Scorekeeper App

Adding to a list:

```elm
1 :: [2, 3]
[1] ++ [2, 3]
```

Lists are singly linked lists.

## Resources

* [Elm Syntax](http://elm-lang.org/docs/syntax)
* [Elm for Beginners](http://courses.knowthen.com/courses/elm-for-beginners)
* [Course Github Repo](https://github.com/knowthen/elm)
* [Elm Packages](http://package.elm-lang.org/)

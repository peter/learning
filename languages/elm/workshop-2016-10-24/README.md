# Elm Workshop 2016-10-24

Meet the Elm programming language:

* Domain specific language targeting UI in the browser (HTML, CSS, JavaScript)
* Purely functional (pure functions and immutable data)
* Statically typed with few runtime exceptions
* Uses a virtual DOM approach to generating HTML (like React.js)
* The basic Elm architecture is Model - Update - View.
* Released by Evan Czaplicki in 2012

## Developer Setup

See [Developer Setup Instructions](https://github.com/knowthen/elm/blob/master/DEVSETUP.md) by James Moore
for the [Elm For Beginners course](http://courses.knowthen.com/p/elm-for-beginners).

## Short Language Intro

Types

```elm
-- Basic types
"Hello " ++ "world!"
123
3.14
True
False

-- Lists, variable length, heterogeneous
["the", "quick", "brown", "fox"]
[1, 2, 3, 4, 5]

-- Tuples, fixed length, heterogeneous
-- : (String, number)
("elm", 42)

-- Records
{x = 3, y = 7}
peter = {name = "Peter"} -- > { name : String }
peter.name -- > "Peter"
george = { peter | name = "George" }
george.name -- > "George"
```

Functions:

```elm
double : Int -> Int
double x = x * 2

myList = [3, 5, 8]

List.map double myList -- > [6,10,16]

-- map/filter/reduce and anonymous functions (lambdas):
List.map (\n -> n * 2) myList -- > [6,10,16]
List.filter (\n -> n % 2 == 0) myList --> 8
List.foldl (+) 0 myList -- > 16

add a b = a + b

-- Forward pipe operator
add 1 2 |> add 3 -- > 6

-- Left function composition:
List.map (double << (add 3)) myList -- > [12,16,22]
-- Right function composition:
List.map (double >> (add 3)) myList -- > [9,13,19]

-- Argument destructuring and let/in:
volume {width, height, depth} =
  let
    area = width * height
  in
    area * depth

volume { width = 3, height = 2, depth = 7 } -- 42
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

## Creating the Scorekeeper app

Take a look at the [wireframe](scorekeeper-wireframe.png) to see what we'll be building.

### Model


```elm
type alias Model =
  { players : List Player
  , playerName : String
  , playerId : Maybe Int
  , plays : List Play
 }

type alias Player =
  { id : Int
  , name : String
}

type alias Play =
  { id: Int
  , playerId : Int
  , name : String
  , points : Int}
```

TODO: initial model

### Update

What can be done in our app?

* Edit
* Score
* Input
* Save
* Cancel
* DeletePlay

TODO: Message union type

TODO: update function

### View

UI hierarchy:

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

TODO: create functions for each of the components above

### Build Process

You can copy the needed files from the [scorekeeper dir](https://github.com/peter/learning-elm/tree/master/workshop-2016-10-24/scorekeeper) in this repo.

Install dependencies:

```
npm install
```

Install the gulp build tool:

```
npm install gulp -g
```

Gulp will compile Elm to JavaScript for us and start a Node.js http server.

Start the server:

```
gulp
```

### Building the App

We can follow along with the [lectures here](http://courses.knowthen.com/courses/elm-for-beginners/lectures/1254149)

If you get stuck along the way, you can take a look at the completed solution in this repo under [elm-for-beginners/scorekeeper](https://github.com/peter/learning-elm/tree/master/elm-for-beginners/scorekeeper).

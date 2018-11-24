# Reason

## Introduction and Selling Pitch

"Reason lets you write simple, fast and quality type safe code
while leveraging both the JavaScript & OCaml ecosystems."

"ReasonML is a new object-functional programming language created at Facebook. In essence, it is a new C-like syntax for the programming language OCaml. The new syntax is intended to make interoperation with JavaScript and adoption by JavaScript programmers easier. Additionally, it removes idiosyncrasies of OCaml’s syntax."

"Compilation to JavaScript is fast."

## Installation

```
npm install -g bs-platform
```

## REPL

Install the `refmt` and `rtop` tools:

```
npm install -g reason-cli@latest-macos
```

Start a REPL:

```
rtop
```

## Editor

Visual Studio Code with the
[reason-vscode](https://marketplace.visualstudio.com/items?itemName=jaredly.reason-vscode) extension.

## Create Basic Project

```
bsb -init reason-basic-project -theme basic-reason
cd reason-basic-project
yarn build # or npm run build, for npm
node src/Demo.bs.js
```

## Create React App

```
bsb -init reason-react-app -theme react
cd reason-react-app && yarn install && yarn start
# in another tab
yarn run webpack
```

## Tutorial and Basic Syntax

```Reason
type schoolPerson = Teacher | Director | Student(string);

let greeting = person =>
  switch (person) {
  | Teacher => "Hey Professor!"
  | Director => "Hello Director."
  | Student("Richard") => "Still here Ricky?"
  | Student(anyOtherName) => "Hey, " ++ anyOtherName ++ "."
  };
```

```Reason
/* Let binding - immutable */
let x = 5

/* Let binding - mutable */
let x = ref(5)
x := x^ + 1

/* Strings must use double quotes */
"Hello world!"
"hello " ++ "world"
/* Characters use single quotes */
'a'

/* Booleans */
true
false
!true

/* Boolean operators */
|| && <= >= < >

/* Value equality (deep, recursive, no type coerction) */
==
!=

/* Reference equality */
===
!==

/* Numbers */
3
3.14
3 + 4
3.0 +. 4.5
5 mod 3

/* Records (do not compile to plain JS objects) */
type point = {x: int, mutable y: int}
{x: 30, y: 20}
point.x
point.y = 30;
{...point, x: 30}

/* Arrays, Tuples, Lists */
[|1, 2, 3|]
myArray[1] = 10
(1, "Bob", true)
[1, 2, 3]

/* null */
let possiblyNullValue1 = None;
let possiblyNullValue2: option(string) = Some("Hello@");

switch (possiblyNullValue2) {
| None => print_endline("Nothing to see here.")
| Some(message) => print_endline(message)
};

/* Functions */
(arg) => retVal
let named = (arg) => ...
add(4, add(5, 6))

let myFun = (x, y) => {
  let doubleX = x + x
  let doubleY = y + y
  doubleX + doubleY
}

/* Conditionals/Branching */
if (a) {b} else {c}
a ? b : c
switch

/* Destructuring */
let {a, b} = data
let [|a, b|] = data
let {a: aa, b: bb} = data

/* Loops */
for (i in 0 to 10) {...}
for (i in 10 downto 0) {...}
while (true) {...}

/* Blocks */
let res = {
  let x = 23;
  let y = 34;
  x + y
};

/* Creating new scopes with code blocks */
let x = "hello";
print_string(x); /* hello */
{ /* A */
    let x = "tmp";
    print_string(x); /* tmp */
};  /* B */
print_string(x); /* hello */

/* Expressions */
let myBool = true;
let myBoolStr = if (myBool) "yes" else "no";
let abcabc = {
  let abc = "abc"
  abc ++ abc
};

/* Unit type (not an element of any other type) */
();

/* Everything is camel-cased in ReasonML */

/* ReasonML does not prevent you from redefining variables (shadowing, useful in the REPL) */

/* Currying - automatic and built in */
```

## Pattern Matching

TODO

http://reasonmlhub.com/exploring-reasonml/ch_pattern-matching.html

## Functions

TODO

http://reasonmlhub.com/exploring-reasonml/ch_functions.html

## Modules

TODO

http://reasonmlhub.com/exploring-reasonml/ch_basic-modules.html

## Variant Types

TODO

http://reasonmlhub.com/exploring-reasonml/ch_variants.html

## Polymorphic Variant Types

TODO

http://reasonmlhub.com/exploring-reasonml/ch_polymorphic-variants.html

## Lists

http://reasonmlhub.com/exploring-reasonml/ch_lists.html

## Arrays

http://reasonmlhub.com/exploring-reasonml/ch_arrays.html

## Records

http://reasonmlhub.com/exploring-reasonml/ch_records.html

## Functors

http://reasonmlhub.com/exploring-reasonml/ch_functors.html

## Ad-Hoc Polymorphism

"ReasonML does not currently support ad hoc polymorphism where the same operation is implemented differently depending on the types of the parameters. Haskell, another functional programming language supports ad hoc polymorphism via type classes. ReasonML may eventually support it via the similar modular implicits.

ReasonML not supporting ad hoc polymorphism means that most operators such as + (int addition), +. (float addition) and ++ (string concatenation) only support a single type. Therefore, it is your responsibility to convert operands to proper types. On the plus side, ReasonML will warn you at compile time if you forget to do so. That’s a benefit of static typing."

## Resources

* [Reason Homepage](https://reasonml.github.io)
* [ReasonML Standard Library Docs](https://reasonml.github.io/api/index)
* [ReasonReact Homepage](https://reasonml.github.io/reason-react/en)
* [Reason/Ocaml Syntax Comparison](https://reasonml.github.io/docs/en/comparison-to-ocaml)
* [esy - Simple workflow for native Reason and OCaml](https://esy.sh)
* [Exploring ReasonML and functional programming - Axel Rauschmayer (Book)](http://reasonmlhub.com/exploring-reasonml/)
* [Reason Syntax Cheatsheet](https://reasonml.github.io/docs/en/syntax-cheatsheet)
* [Awesome ReasonML - List of Resources](https://github.com/vramana/awesome-reasonml)
* [reason-cli (REPL)](https://github.com/reasonml/reason-cli)
* [Discussion on Semicolons in Reason](https://github.com/facebook/reason/issues/1613)

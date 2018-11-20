# Learning F#

## Language Evaluation

* REPL
* Ability to read and understand code
* Ability to work with json and rest apis and databases
* Deployment (Azure, AWS, Heroku, GCP etc.)
* Momentum

## REPL

Start the F# interactive REPL with `fsharpi`.

## Tutorial

* Curly braces are not used to delimit blocks of code. Instead, indentation is used (Python is similar this way).
* Whitespace is used to separate parameters rather than commas.

```F#
printf "Hello World"

printf "hello %s" "World"

// The "let" keyword defines an (immutable) value
let myInt = 5
let myFloat = 3.14
let myString = "hello"	//note that no types needed

let twoToFive = [2;3;4;5]
let oneToFive = 1 :: twoToFive
let zeroToFive = [0;1] @ twoToFive

// The "let" keyword also defines a named function.
let square x = x * x
square 3
let add x y = x + y
add 2 3

let evens list =
   let isEven x = x%2 = 0
   List.filter isEven list
evens oneToFive

let sumOfSquaresTo100 =
   List.sum (List.map square [1..100])

let sumOfSquaresTo100piped =
   [1..100] |> List.map square |> List.sum

let sumOfSquaresTo100withFun =
   [1..100] |> List.map (fun x->x*x) |> List.sum

// Match..with.. is a supercharged case/switch statement.
let simplePatternMatch =
   let x = "a"
   match x with
    | "a" -> printfn "x is a"
    | "b" -> printfn "x is b"
    | _ -> printfn "x is something else"

// Some(..) and None are roughly analogous to Nullable wrappers
let validValue = Some(99)
let invalidValue = None

let optionPatternMatch input =
   match input with
    | Some i -> printfn "input is an int=%d" i
    | None -> printfn "input is missing"

optionPatternMatch validValue
optionPatternMatch invalidValue

let twoTuple = 1,2
let threeTuple = "a",2,true

type Person = {First:string; Last:string}
let person1 = {First="john"; Last="Doe"}
```

## Currying

```F#
let add a b = a + b
let add1 = add 1 // => (int -> int)
add1 2 // => 3
```

[Read more about currying](https://fsharpforfunandprofit.com/posts/currying)

## The >=> Operator (i.e. The Kleisli or Fish Operator)

From [StackOverflow](https://stackoverflow.com/questions/30110964/what-f-sorcery-is-this):

"That's the Kleisli composition operator for monads. It allows you to compose functions with signatures like 'a -> M<'b> and 'b -> M<'c'> where M is monadic: in your case the Result<'t> from the linked article.

>=> is really just a function composition, but >> wouldn't work here since the return type of the first function isn't the argument of the second one - it is wrapped in a Result<'t> and needs to be unwrapped, which is exactly what >=> implementation does."

See [Railway oriented programming](https://fsharpforfunandprofit.com/posts/recipe-part2/).

## Resources

* [F# syntax in 60 seconds](https://fsharpforfunandprofit.com/posts/fsharp-in-60-seconds/)
* [F# for fun and profit (Video)](https://fsharpforfunandprofit.com/video/)
* [Get Programming with F# (Book)](https://www.manning.com/books/get-programming-with-f-sharp)
* [Why you should use F# - Phillip Carter (Video)](https://youtu.be/Mu39vtwKWpg)

* [PDC 2008 An Introduction to Microsoft F# - Luca Bolognese](https://www.youtube.com/watch?v=Dfnr05mgGzE&feature=youtu.be)

* [Eight reasons to learn F#](https://medium.com/real-world-fsharp/eight-reasons-to-learn-f-fcb2bef64d7a)

* [Low overhead type definitions | F# for fun and profit](https://fsharpforfunandprofit.com/posts/conciseness-type-definitions/)
* [Currying](https://fsharpforfunandprofit.com/posts/currying)

* [REST API with MongoDB and F# on .NET Core (and Giraffe)](https://medium.com/@leocavalcante/rest-api-with-mongodb-and-f-on-net-core-605a2336f264)
* [Giraffe Example App](https://github.com/cartermp/GiraffeSample)

* [F# Guide](https://docs.microsoft.com/en-us/dotnet/fsharp)
* [F# Style Guide](https://docs.microsoft.com/en-us/dotnet/fsharp/style-guide/)

* [ASP.NET Core (Wikipedia)](https://en.wikipedia.org/wiki/ASP.NET_Core)
* [ASP.NET Core (Homepage)](https://www.asp.net/core/overview/aspnet-vnext)
* [.NET Core vs JVM](https://www.quora.com/Is-Microsoft-winning-the-programming-language-framework-wars-by-launching-Net-Core)
* [Get started with F# with the .NET Core CLI](https://docs.microsoft.com/en-us/dotnet/fsharp/get-started/get-started-command-line)
* [Visual Studio Code Keyboard Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)

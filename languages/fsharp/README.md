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

let x = 50
if x.GetType() = typeof<int> then "is int" else "is not int" // => "is int"

let mutable x = 100
x <- 200

// The "let" keyword also defines a named function.
let square x = x * x
square 3
let add x y = x + y
add 2 3

// parameterless functions take unit as their argument
let sayHello() =
    "hello"

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

let twoItems = ("apple", "dog")
fst twoItems // => "apple"
snd twoItems // => "dog"

let items = ("apple", "dog", "Mustang")
let fruit, animal, car = items

type Person = {First:string; Last:string}
let person1 = {First="john"; Last="Doe"}

let isEven x =
    if x % 2 = 0 then
        "it's even!"
    else
        "it's odd!"

let isApple x =
    match x with
    | "apple" -> true
    | _ -> false

let getDinnerIf x =
    let name, foodChoice = x

    if foodChoice = "veggies" || foodChoice ="fish" ||
       foodChoice = "chicken" then
        sprintf "%s doesn't want red meat" name
    else
        sprintf "%s wants 'em some %s" name foodChoice

let getDinner x =
    match x with
    | (name, "veggies")
    | (name, "fish")
    | (name, "chicken") -> sprintf "%s doesn't want red meat" name
    | (name, foodChoice) -> sprintf "%s wants 'em some %s" name foodChoice

let list = ["apple"; "pear"; "grape"; "peach"]
list.Head
list.Tail
list.Length

let result =
    [0..5]
    |> List.filter isEven
    |> List.map square

// arrays are mutable
let fruits = [| "apple"; "pear"; "peach"|]
fruits.[0]
fruits.[1] <- "peach"

// you can create arrays with comprehensions
let numbers =
    [| for i in 0..10 do
           if i % 2 = 0 then yield i |]

let translate score =
    match score with
    | 5 -> "Great"
    | 4 -> "Good"
    | 3 -> "Decent"
    | 2 -> "Bad"
    | 1 -> "Awful"
    | _ -> "Unknown"

// mutable class
type Person2(name:string) =
    let mutable internalName = name

    member this.Name
        with get() = internalName
        and set(value) = internalName <- value

    member this.Speak() =
        "Hi my name is " + this.Name

let person = new Person2("Shaun")
let firstPhrase = person.Speak()
person.Name <- "Shaun of the Dead"
let secondPhrase = person.Speak()
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

* [Type Extensions](https://docs.microsoft.com/en-us/dotnet/fsharp/language-reference/type-extensions)

* [PDC 2008 An Introduction to Microsoft F# - Luca Bolognese](https://www.youtube.com/watch?v=Dfnr05mgGzE&feature=youtu.be)

* [Eight reasons to learn F#](https://medium.com/real-world-fsharp/eight-reasons-to-learn-f-fcb2bef64d7a)

* [Low overhead type definitions | F# for fun and profit](https://fsharpforfunandprofit.com/posts/conciseness-type-definitions/)
* [Currying](https://fsharpforfunandprofit.com/posts/currying)

* [REST API with MongoDB and F# on .NET Core (and Giraffe)](https://medium.com/@leocavalcante/rest-api-with-mongodb-and-f-on-net-core-605a2336f264)
* [Giraffe Example App](https://github.com/cartermp/GiraffeSample)
* [Azure Functions in F# (For Real)](https://spin.atomicobject.com/2018/05/17/azure-functions-f-sharp/)
* [Build your first Web API with F#, Giraffe and host it on Azure Cloud](https://koukia.ca/build-your-first-web-api-with-f-giraffe-and-host-it-on-azure-cloud-1d9dc07dc248)

* [Saturn Web Framework](https://github.com/SaturnFramework/Saturn)
* [FSharp.Data.GraphQL](https://github.com/fsprojects/FSharp.Data.GraphQL)

* [Training With Tomas Petricek at fsharpWorks](http://tomasp.net)
* [F# Workshop - Course Material](https://www.fsharpworkshop.com)
* [F# Koans](https://github.com/ChrisMarinos/FSharpKoans)
* [F# Koans Snippts](http://fssnip.net/bG)

* [Why Isn’t F# the King of .NET?](https://hackernoon.com/why-isnt-f-the-king-of-net-2a9a1963e087)

* [F# Programming Wikibook](https://en.wikibooks.org/wiki/F_Sharp_Programming/Print_version)

* [F# Guide](https://docs.microsoft.com/en-us/dotnet/fsharp)
* [F# Style Guide](https://docs.microsoft.com/en-us/dotnet/fsharp/style-guide/)

* [ASP.NET Core (Wikipedia)](https://en.wikipedia.org/wiki/ASP.NET_Core)
* [ASP.NET Core (Homepage)](https://www.asp.net/core/overview/aspnet-vnext)
* [.NET Core vs JVM](https://www.quora.com/Is-Microsoft-winning-the-programming-language-framework-wars-by-launching-Net-Core)
* [Get started with F# with the .NET Core CLI](https://docs.microsoft.com/en-us/dotnet/fsharp/get-started/get-started-command-line)
* [Visual Studio Code Keyboard Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)

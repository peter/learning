# Erlang

Erlang is a language designed to support the building of large fault-tolerant systems.

## Language Features and Philosophy

* Language goals are fault tolerance, distributed programming, concurrency and scalability
* Concurrency Oriented
* Systems are built on a hierarchy of isolated and supervised processes
* Processes communicate with message passing and have no shared state
* Processes are very lightweight and cheap to create in time and space
* Fault isolation is the key to system fault tolerance
* Use the same programming model if you are running on one computer as on a hundred computers
* Individual processes are allowed to crash (fail fast) and restart in a pristine state when errors occur
* Allow modules to be hot reloaded in production without system restart
* Dynamically typed
* Functional. Recursion is the only looping construct. Everything is an expression that returns a value.
* Data structures are immutable
* Variables are only assigned once (like constants)
* There are no global variables
* Variables start with uppercase letter
* Atoms start with lowercase letter and are names representing themselves (like symbols or keywords in other languages)

## Processes

In Erlang processes are the basic unit of abstraction:

* Everything is process
* Processes are isolated
* Processes only communicate via messages
* Processes have unique identifiers, Pids
* If you have the name of a process you can send it a message
* Error handling is non-local. It needs to be non-local since if a computer fails it needs to be handled somewhere else.
* Processes do what they are supposed to do or fail fast

## Modules

Example Erlang module:

```erlang
-module(math).
-export([areas/1]).
-import(lists, [map/2]).

areas(L) ->
  lists:sum(
             map(
                  fun(I) -> area(I) end,
                  L)).

area({square, X}) ->
  X*X;
area({rectangle, X, Y}) ->
  X*Y.
```

```
erl
c(math).
math:areas([{reactangle,12,4}, {square,6}]).
```

## Data Structures

* Integers
* Atoms. Starts with a lowercase letter and are constants with their own name as value.
* Floats
* References. Created with make_ref()
* Binaries. Sequence of bytes.
* Pids. References to Erlang processes
* Ports. Communication with outside world.
* Funs. Function closures. Created with fun() -> ... end
* Tuples. Container of fixed number of values.
* Lists. Sequence of variable number of values. First element is accessed at constant time. A list has a head and tail. [D1 | [D2 | ... | [Dn | []]]].
* Strings. Byte sequences (ASCII). The string "cat" is short for [97, 99, 116]
* Records. Associates a tag with each element in a tuple for named access. A pre-compiler converts records to tuples.

## Atoms

You can enclose an atom in single quotes to have it contain other characters than alphanumeric, underscore and @. Atoms are not garbage collected so you should not create too many of them. The following atoms are
reserved words:

```
after and andalso band begin bnot bor bsl bsr bxor
case catch cond div end fun if let not of
or orelse query receive rem try when xor
```

## Boolean Operators

```
true and false.
false or true.
not false.
not (true and true).
```

Note: the `and` and `or` operators will evaluate both their operands. If you want short-cut
operators use `andalso` and `orelse`.

## Variables

Variable names start with an uppercase letter. Variables are either unbound,
i.e. have no value, or bound, i.e. have a value. Once a variable can only be
bound once (they can only be assigned to once). You can use underscore (_) as
variable name (placeholder) when you don't need to use the value.

```erlang
X = 5
X1 = X + 10
```

## Numbers

```erlang
2 + 15.
% => 17
5 / 2.
% => 2.5
5 div 2.
% => 2
5 rem 2.
% => 1
```

## Boolean Operators

```erlang
true and false.
% => false
false or true.
% => true
not false.
% => true
not (true and true).
% => false
```

## Equality

```erlang
5 =:= 5.
% => true
1 =/= 0.
% => true
```

## Tuples

```erlang
Point = {3, 4}.
{X, Y} = Point.
X.
Y.
{X1, _} = Point.
X1.
{X2, Y2} = {5, 6, 7}.
% => ** exception error: no match of right hand side value {5,6,7}
```

A "tagged tuple":

```erlang
PreciseTemperature = {celsius, 23.213}.
{kelvin, T} = PreciseTemperature.
% => ** exception error: no match of right hand side value {celsius,23.213}
```

## Lists

```erlang
[1, 2, 3, {numbers,[4,5,6]}, 5.34, atom].
[97, 98, 99].
% => "abc"
[1,2,3] ++ [4,5].
[2,4,2] -- [2,4].
hd([1,2,3,4]).
% => 1
tl([1,2,3,4]).
% => [2, 3, 4]
List = [2,3,4].
NewList = [1|List].
% => [1, 2, 3, 4]
[1 | []].
% => [1]
[2 | [1 | []]].
% => [2,1]
[3 | [2 | [1 | []]]].
% => [3,2,1]
```

## List Comprehensions

"List comprehensions in Erlang are about building sets from other sets"

```erlang
[2*N || N <- [1,2,3,4]].
[X || X <- [1,2,3,4,5,6,7,8,9,10], X rem 2 =:= 0].
% => [2,4,6,8,10]
RestaurantMenu = [{steak, 5.99}, {beer, 3.99}, {poutine, 3.50}, {kitten, 20.99}, {water, 0.00}].
[{Item, Price*1.07} || {Item, Price} <- RestaurantMenu, Price >= 3, Price =< 10].
```

## Bit Syntax

Erlang "makes dealing with raw binary data fun and easy (no, really), which was necessary for the telecom applications it was created to help with"

```erlang
Color = 16#F09A29.
Pixel = <<Color:24>>.
```

## Modules

"Modules are a bunch of functions regrouped in a single file, under a single name. Additionally, all functions in Erlang must be defined in modules."

Build in functions like `hd` and `tl` belong in the erlang module and don't need
the module prefix when they are invoked.

```erlang
erlang:element(2, {a,b,c}).
% => b
element(2, {a,b,c}).
% => b
lists:seq(1,4).
% => [1,2,3,4]
seq(1,4).
% => ** exception error: undefined shell command seq/2
```

Example module:

```erlang
-module(useless).

-export([add/2]).

add(A,B) ->
  A + B.

%% Shows greetings.
%% io:format/1 is the standard function used to output text.
hello() ->
  io:format("Hello, world!~n").

greet_and_add_two(X) ->
  hello(),
  add(X,2)
```

In the `erl` shell:

```
cd("/path/to/where/you/saved/the-module/")
c(useless)
useless:add(7,2).
```

Keep modules cohesive and avoid circular dependencies.

## Pattern Matching

```erlang
{P, abcd} = {123, abcd}.
[H|T] = "cat".
```

A function without pattern matching:

```erlang
function greet(Gender,Name)
  if Gender == male then
    print("Hello, Mr. %s!", Name)
  else if Gender == female then
    print("Hello, Mrs. %s!", Name)
  else
    print("Hello, %s!", Name)
end
```

A function with pattern matching and function clauses:

```erlang
greet(male, Name) ->
  io:format("Hello, Mr. ~s!", [Name]);
greet(female, Name) ->
  io:format("Hello, Mrs. ~s!", [Name]);
greet(_, Name) ->
  io:format("Hello, ~s!", [Name]).
```

Examples of pattern matching:

```erlang
head([H|_]) -> H.

second([_,X|_]) -> X.

same(X,X) ->
  true;
same(_,_) ->
  false.
```

Validation of args:

```erlang
valid_time({Date = {Y,M,D}, Time = {H,Min,S}}) ->
  io:format("The Date tuple (~p) says today is: ~p/~p/~p,~n",[Date,Y,M,D]),
  io:format("The time tuple (~p) indicates: ~p:~p:~p.~n", [Time,H,Min,S]);
valid_time(_) ->
  io:format("Stop feeding me wrong data!~n").
```

## Guards

```erlang
wrong_age(X) when X < 16; X > 104 ->
  true;
wrong_age(_) ->
  false.
```

## If

```erlang
help_me(Animal) ->
  Talk = if Animal == cat  -> "meow";
            Animal == beef -> "mooo";
            Animal == dog  -> "bark";
            Animal == tree -> "bark";
            true -> "fgdadfgna"
          end,
  {Animal, "says " ++ Talk ++ "!"}.
```

## Case

```erlang
beach(Temperature) ->
  case Temperature of
    {celsius, N} when N >= 20, N =< 45 ->
      'favorable';
    {kelvin, N} when N >= 293, N =< 318 ->
      'scientifically favorable';
    {fahrenheit, N} when N >= 68, N =< 113 ->
      'favorable in the US';
    _ ->
      'avoid beach'
  end.
```

## Type Test BIFs

```
is_atom/1           is_binary/1        
is_bitstring/1      is_boolean/1        is_builtin/3       
is_float/1          is_function/1       is_function/2      
is_integer/1        is_list/1           is_number/1        
is_pid/1            is_port/1           is_record/2        
is_record/3         is_reference/1      is_tuple/1
```

## Comments

Comments begin with the character % and extend to the end of the line.

## Functions

* A function has one or more clauses separated by semicolons
* A clause has a head followed by a separator -> followed by a body
* A function head is an atom followed by a parenthesized set of patterns followed by an optional guard. The guard if present is introduced with the when keyword.
* A function body consists of a sequence of comma-separated expressions. The value of the body is the value of the last expression.

```erlang
factorial(0) -> 1;
factorial(N) -> N * factorial(N-1).

member(H, [H|T]) -> true;
member(H, [_|T]) -> member(H, T);
member(H, []) -> false.
```

```erlang
c(functions).
functions:member(3, [2, 4, 3]).
% -> true
functions:member(1, [2, 4, 3]).
% -> false
functions:member(dog, [cat,man,dog,ape]).
% -> true
```

## Recursion

"functional programming languages usually do not offer looping constructs like for and while. Instead, functional programmers rely on a silly concept named recursion"

A function is tail recursive if the last calls in the function body are calls to other functions in the system.

Tail recursive functions can run in loops and are called iterative.

```erlang
factorial2(N) -> factorial2_t(N, 1).
factorial2_t(0, Acc) -> Acc;
factorial2_t(N, Acc) -> factorial2_t(N-1, N*Acc).
```

Without tail recursion:

```erlang
len([]) -> 0;
len([_|T]) -> 1 + len(T).
```

With tail recursion:

```erlang
tail_len(L) -> tail_len(L, 0).

tail_len([], Acc) -> Acc;
tail_len([_|T], Acc) -> tail_len(T, Acc + 1)
```

## Types and Safety

"To make it short, while most languages and type systems aim to make a program error-free, Erlang uses a strategy where it is assumed that errors will happen anyway and makes sure to cover these cases"

## Resources

* [Erlang Home](http://www.erlang.org)
* [Making reliable distributed systems in the presence of software errors (Armstrong PHD Thesis)](http://erlang.org/download/armstrong_thesis_2003.pdf)
* [Learn You Some Erlang for Great Good!](http://learnyousomeerlang.com)

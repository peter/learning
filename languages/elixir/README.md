# Learning Elixir

## What is Elixir?

Elixir is a general purpose programming language:

* Typing: Dynamic
* Paradigm: Functional
* Virtual Machine: Erlang (BEAM)
* Distributed, fault-tolerant, soft real-time, optimized for zero-downtime applications

Features:

* Everything is an expression
* Compiles to Erlang bytecode
* Erlang functions can call Elixir functions and vice versa without runtime impact
* Shared nothing actor concurrency model. All Elixir code runs inside lightweight threads of execution (processes) that are isolated and exchange information via messages.
* Pattern matching is used extensively
* The pipe operator (|>) is used to pass data between functions
* Parenthesis are optional when invoking a function with one or more arguments (like in Ruby). Zero argument functions that are not qualified by a module need parenthesis when invoked.
* Functions are identified by name and arity
* When defining a function with the same name and arity multiple times, each such definition is called a clause
* Emphasis on recursion and higher order functions
* Lazy and async collections with streams
* Meta programming with macros
* Polymorphism via protocols (like in Clojure)
* Support for Python like doc strings
* UTF-8 Support

## Erlang

[Notes on Erlang](topics/erlang/README.md)

Examples of calling an [Erlang functions](http://erlang.org/doc/search/) from Elixir:

```elixir
:crypto.md5("Using crypto from Erlang OTP")
:os.getenv("PATH")
:timer.sleep(500)
:random.uniform
```

## Interactive Elixir (REPL)

Elixir ships with a REPL callex `iex` - Elixirs interactive shell. You can
autocomplete commands in the shell with tab.

```
iex
h # help about using Interactive Elixir
h IO # help about IO module
h IO.puts # help about IO.puts function
IO. # hit tab key to see all functions available in the IO module
c "lib/misc.ex" # compiles/runs "hello.exs" file

```

You can also start iex with a script:

```
iex lib/misc.ex
```

## Running Elixir Scripts

"In addition to the Elixir file extension .ex, Elixir also supports .exs files for scripting. Elixir treats both files exactly the same way, the only difference is in intention. .ex files are meant to be compiled while .exs files are used for scripting."

```bash
elixir lib/hello_world.exs
```

Interactively (REPL):

```
iex
c "lib/hello_world.exs"
```

## Basic Data Types

The following all evaluate to true:

```elixir
is_integer(3)
is_number(3)
is_float(5.3)
is_number(5.3)
is_atom(:im_an_atom)
is_boolean(false)
is_binary("hello")
is_function(fn(n) -> n * n end)
is_list([2, "foo", true])
is_tuple({:foo, 5, true})
is_map(%{:foo => 1, :bar => 2})
```

## Modules

```elixir
defmodule ExampleModule do
  def some_fun do
    IO.puts("some fun")
  end

  def some_fun(list) when is_list(list) do
    IO.inspect list
  end

  defmodule Util do
    def do_something do
      :ok
    end
  end

  defp private_function do
    :secret
  end
end

ExampleModule.some_fun
ExampleModule.Util.do_something
```

## Functions

Anonymous functions:

```elixir
sum = fn(a, b) -> a + b end
sum.(4, 3)
#=> 7

square = fn(x) -> x * x end
Enum.map [1, 2, 3, 4], square

my_fn = &(&1 * &1)
my_fn.(3) # => 9

Enum.map [1, 2, 3, 4], &(&1 * 2)

List.foldl [1, 2, 3, 4], 0, &(&1 + &2)
```

Guards:

```elixir
def sum(a, b) when is_integer(a) and is_integer(b) do
  a + b
end

def sum(a, b) when is_list(a) and is_list(b) do
  a ++ b
end

def sum(a, b) when is_binary(a) and is_binary(b) do
  a <> b
end
```

Default values:

```elixir
def mul_by(x, n \\ 2) do
  x * n
end
mul_by 4, 3 #=> 12
mul_by 4    #=> 8
```

First-class named functions:

```elixir
defmodule Math do
  def square(x) do
    x * x
  end
end

Enum.map [1, 2, 3], &Math.square/1
```

## Function Clauses, Recursion, and Pattern Matching

```elixir
defmodule Example do
  def loop_through([h | t]) do
    IO.inspect h
    loop_through t
  end

  def loop_through([]), do: :ok
end

Example.loop_through([:a, :b, :c])
```

```elixir
defmodule Example do
  def sum(list) do
    _sum(list, 0)
  end

  defp _sum([], result), do: result
  defp _sum([h | t], result) do
    _sum(t, h + result)
  end
end

Example.sum([1, 2, 3, 4, 5]) # => 15
```

```elixir
defmodule NotTailRecursive do
  def factorial(0), do: 1
  def factorial(n), do: n * factorial(n-1)
end

NotTailRecursive.factorial(5)
#=> 120

defmodule TailRecursive do
  def factorial(n), do: _factorial(n, 1)
  def _factorial(1, acc), do: acc
  def _factorial(n, acc), do: _factorial(n-1, n*acc)
end

TailRecursive.factorial(5)
#=> 120
```

## Control Flow

The `case` construct provides control flow based purely on pattern matching.

```elixir
case {x, y} do
  {:a, :b} -> :ok
  {:b, :c} -> :good
  other -> other
end
```

There is also `cond` and `if`:

```elixir
test_fun = fn(x) ->
  cond do
    x > 10 ->
      :greater_than_ten
    x < 10 and x > 0 ->
      :less_than_ten_positive
    x < 0 or x === 0 ->
      :zero_or_negative
    true ->
      :exactly_ten
  end
end

if x > 10 do
  :greater_than_ten
else
  :not_greater_than_ten
end

x = 7
if x > 10, do: "x greater than 10", else: "x less than or equal to 10"
```

## Equality

```elixir
4 == 4.0 #=> true
4 === 4.0 #=> false
4 != 4.0 #=> false
4 !== 4.0 #=> true

[1, 2, %{foo: 3}] === [1, 2, %{foo: 3}]
#=> true
[1, 2, %{foo: 3}] === [1, 2, %{foo: 4}]
#=> false
```

## Lists

```elixir
my_list = [:a, :b, :c]
hd my_list # head
#=> :a
tl my_list # tail
#=> [:b, :c]
length my_list
#=> 3
```

Kernel functions:

* tl/1
* hd/1
* length/1

## The Enum Module

The [Enum Module](https://hexdocs.pm/elixir/Enum.html#content) has tons of useful
functions many of which will be familiar from other languages.

* `map`
* `filter`
* `reduce`

Look at the [Stream module](https://hexdocs.pm/elixir/Stream.html) for a lazy more performance alternative to the eager Enum module. If you chain several Enum.map/Enum.filter calls together on a large sequence of data you will be traversing
that sequence multiple times. By changing to Stream you will be traversing it once instead.

```elixir
stream = 1..3
  |> Stream.map(&IO.inspect(&1))
  |> Stream.map(&(&1 * 2))
  |> Stream.map(&IO.inspect(&1))
Enum.to_list(stream)
```

## Keyword Lists

Elixir offers a literal syntax for creating a list of two-item tuples where the first item in the tuple is an atom and calls them keyword lists:

```elixir
kw = [another_key: 20, key: 10]
kw[:another_key] # => 20
```

## Maps

```elixir
map = %{:key => 0}
map = %{map | :key => 1}
%{:key => value} = map
value === 1
```

Some useful Kernel functions for maps:

* [get_in/2](https://hexdocs.pm/elixir/Kernel.html#get_in/2)
* [put_in/3](https://hexdocs.pm/elixir/Kernel.html#put_in/3)
* [update_in/3](https://hexdocs.pm/elixir/Kernel.html#update_in/3)
* [get_and_update_in/3](https://hexdocs.pm/elixir/Kernel.html#get_and_update_in/3)

## Boolean Operators

* `&&`
* `and` - requires first argument to be a boolean
* `or` - requires first argument to be a boolean
* `||`
* `not`

## List Comprehensions

```elixir
for n <- [1,2,3,4,5], rem(n,2) == 1, do: n*n
```

## Sending and Receiving Messages

```elixir
pid = Kernel.self

send pid, {:hello}

receive do
  {:hello} -> :ok
  other -> other
after
  10 -> :timeout
end
```

## Spawning Processes


```elixir
for num <- 1..1000, do: spawn fn -> IO.puts "#{num * 2}" end
```

```elixir
defmodule SpawnBasic do
  def greet do
    IO.puts "Hello"
  end
end

SpawnBasic.greet Hello
pid = spawn(SpawnBasic, :greet, [])
Process.alive? pid
```

```elixir
defmodule Greeter do
  def greet do
    receive do
      {sender, msg} ->
        send sender, {:ok, "Hello #{msg}"}
        greet()
    end
  end
end

pid = spawn(Greeter, :greet, [])

send pid, {self(), "World!"}

receive do
  {:ok, msg} -> IO.puts(msg)
  after 500 ->
    IO.puts "No message from Greeter, giving up"
end

receive do
  {:ok, msg} -> IO.puts(msg)
  after 500 ->
    IO.puts "No message from Greeter, giving up"
end
```

## Linking Processes

"When a process reaches its end, by default it exits with reason :normal"

The default behaviour of linked processes is that if a process dies then so
does its linked process. We can change this by trapping the exit:

```elixir
defmodule LinkExample do
  def sad_function do
    :timer.sleep 500
    exit(:boom)
  end

  def run do
    Process.flag(:trap_exit, true)
    spawn_link(LinkExample, :sad_function, [])
    receive do
      msg ->
        IO.puts "Received msg: #{inspect(msg)}"
      after 1000 ->
        IO.puts "No message received"
    end
  end
end

LinkExample.run
```

See also [spawn_monitor/1](https://hexdocs.pm/elixir/Kernel.html#spawn_monitor/1)

## The Task Module

The [Task module](https://hexdocs.pm/elixir/Task.html#content) offers "conveniences for spawning and awaiting tasks" via the `async` and `await` functions. Tasks can
be supervised.

```elixir
defmodule Parallel do
  def pmap(collection, func) do
    collection
    |> Enum.map(&(Task.async(fn -> func.(&1) end)))
    |> Enum.map(&Task.await/1)
  end
end

result = Parallel.pmap 1..1000, &(&1 * &1)
```

## OTP

OTP (Open Telecom Platform) is a set of genric implemetations
of common design patterns such as discovery, failure detection
and monitoring, hot code swapping, node failover, data storage, and releases.

In OTP, every process is a supervisor or a worker. An application is a tree
of processes. Supervisors manage the workers, i.e. start, stop, and monitor them.

The most common restart strategies are: one_for_one and one_for_all.

Children are stopped in reverse start order.

You can use `mix new --sup` to create a new OTP application.

## OTP: GenServer

Basic GenServer example:

```elixir
defmodule Greeting do
  use GenServer

  def init(initial_data) do
    {:ok, %{greeting: initial_data}}
  end

  def handle_call({:get}, _from, state) do
    {:reply, Map.get(state, :greeting), state}
  end

  def handle_call({:set, greeting}, _from, state) do
    new_state = Map.put(state, :greeting, greeting)
    {:reply, new_state, new_state}
  end
end

{:ok, pid} = GenServer.start_link(Greeting, "Hello")
Process.alive? pid                                  
#=> true
GenServer.call(pid, {:get})
#=> "Hello"
GenServer.call(pid, {:set, "Foobar"})
GenServer.call(pid, {:get})          
#=> "Foobar"
```

You can give the GenServer process a name when you start it but this name needs to
be unique, you can't start a process with a certain name twice:

```elixir
GenServer.start_link(__MODULE__, %{}, name: :name_of_my_server)
```

Another basic example:

```elixir
defmodule Counter do
  use GenServer

  def handle_call(:next, _from, count) do
    {:reply, count, count + 1}
  end
end

{:ok, pid} = GenServer.start_link(Counter, 100)
GenServer.call(pid, :next)
```

## alias, require, import, use

[Elixir Lang: alias, require, and import](http://elixir-lang.org/getting-started/alias-require-and-import.html)

## Observer

```
:observer.start
```

## Coding Convensions

* Two column indentation with spaces (not tabs)

## Resources

* [Wikipedia: Elixir](https://en.wikipedia.org/wiki/Elixir_(programming_language))
* [Elixir Lang](http://elixir-lang.org)
* [Elixir Lang: Crash Course](http://elixir-lang.org/crash-course.html)
* [Elixir Lang: Naming Conventions](https://hexdocs.pm/elixir/naming-conventions.html#content)
* [Elixir Lang: Typespecs](https://hexdocs.pm/elixir/typespecs.html#content)
* [Elixir Lang: Documentation](https://hexdocs.pm/elixir/writing-documentation.html#content)
* [Elixir Lang: Documentation (PDF)](https://media.readthedocs.org/pdf/elixir-lang/latest/elixir-lang.pdf)

* [Book: Programming Elixir (Dave Thomas)](https://pragprog.com/book/elixir/programming-elixir)
* [Book: Elixir in Action (Sasa Juric)](https://www.manning.com/books/elixir-in-action)

* [Source Code: OTP app example with GenServer](https://github.com/omgneering/elhex_delivery)
* [Video: Elixir GenServer Basics](https://www.youtube.com/watch?v=zC7TcrRi46Q&feature=youtu.be)
* [Video: Elixir Tutorial - Derek Banas](https://www.youtube.com/watch?v=pBNOavRoNL0)

* [Course: The Complete Elixir and Phoenix Bootcamp](https://www.udemy.com/the-complete-elixir-and-phoenix-bootcamp-and-tutorial)
* [Source Code: The Complete Elixir and Phoenix Bootcamp](https://github.com/StephenGrider/ElixirCode)

defmodule Misc do
  def question do
    name = IO.gets("What is your name?") |> String.trim
    IO.puts "Hello #{name}"
  end

  def hello_world do
    IO.puts("Hello World")
  end
end

# Python Programming for Beginners

The target audience of this course is people (adults or children) who have never programmed before. In this course we will be writing a few simple Python programs. The goal is to:

* Teach fundamental programming constructs, concepts and terminology
* Give a hands on taste of what programming is like, i.e. the workflow of programming and the tooling. You should be able to use the IDE, do debugging and independently be able to search for solutions to problems

## Tooling

The pre-requisites for the course is access to the Python interpreter and an editor/IDE for working with your code:

* Download and install Python from [Python.org](https://www.python.org/)
* Download and install [Visual Studio Code](https://code.visualstudio.com/)

As an alternative to installing Python on your computer you can also code Python directly in your web browser using services like [Github Codespaces](https://github.com/features/codespaces), [replit](https://replit.com/) etc.

## Programming Assignments

### 1. Printing to the Screen

Write a program that outputs (prints) "Hello World!" on the screen.

### 2. Taking User Input

Write a program that asks the user for their name (i.e. "What is your name?") and then prints a
greeting with the name back to the user. Here is what an example of how the program might work:

* The program prints: "What is your name?"
* The user enters "Joe"
* The program prints "Hello Joe!"

### 3.a Looping

Write a program that prints "Hello World!" a hundred times.

### 3.b Looping

Write a program that prints the numbers between 0 and 99 with one number on each line.

### 3.c Looping, Type Conversion, and User Input

Write a program that asks the user "How many times?" to which the user answers with a number and hits enter. The program will then output "Hello World!" as many times as the user has entered. Here is an example of the flow:

* The program prints "How many times?"
* The user enteres the number "5"
* The program prints "Hello World!" five times

## Python Programming Constructs

### Printing Text to the Screen

### Taking User Input

### Variables and Data Types

"How would we keep track of the player’s points within our program? Using a variable. A variable is a named value that we can access and change. Variables hold the data within our programs."

"Variables are a fundamental part of programming: they enable you to track values by assigning names to them. Once we’ve made a variable, we can access and change its value throughout our program."

Variable names are case sensitive and must start with an underscore or a letter.

```python
x = 1          # int
y = 2.5        # float
name = 'John'  # str
is_cool = True # bool

print(x, y, name, is_cool)

print(type(x))
print(type(y))

# Basic math
sum = x + y

# Casting
x_string = str(x)

# Equality
5 == '5' # => False
str(5) == '5' # => True
5 == int('5') # => True
```

## Strings

```python
# String concatenation and variable interpolation in f-strings.
name = 'Joe'
age = 25

print('Hello, my name is ' + name + ' and I am ' + str(age) + ' years old')

print(f'Hello, my name is {name} and I am {age} years old')

# Useful string methods
s = 'hello world'
s.upper()
s.lower()
s.capitalize()
s.startswith('hello')
s.endswith('world')
s.split()
s.isnumeric()

import re
re.findall(r'\w', s)
re.search(r'o w', s)
re.sub(r'\s', '_', s) # => hello_world
```

### Type Conversion

### Control Flow (If-Statements)

### Data Structures - Lists and Dictionaries

### Comments

### Files

### JSON Data

### Looping

### Functions

## Concepts in Software Development

Those concepts are for orientation and are really beyond the scope of this course:

* The importance of knowing the user and use cases you are building for. Balance the program being too specific (ie hard coded) vs too generic (ie too configurable, dynamic or over engineered)
* Agile vs waterfall - the value of starting small and using fast feedback loops and small increments
* Cohesion and coupling - decomposing
* Abstraction and Encapsulation
* Mutability
* DRY
* The REPL
* Testing - unit testing vs end-to-end testing
* The importance and difficulty of naming things well
* Refactoring
* Static typing
* Caching
* Databases
* Object orientation
* Functional programming

## Resources

* [Python 3 Language Reference](https://docs.python.org/3/reference/index.html)
* [Googles Python Class](https://developers.google.com/edu/python)

# Write Command Line Scripts with Python

## Install Python 3

You can check the availability of Python 3 on your system:

```sh
python3 --version
```

To install Python 3:

```sh
brew install python3
```

## Using sys.argv and sys.stdin

```python
#!/usr/bin/env python3
# URL encode a string
#
# echo "foo bar" | urlencode
# urlencode "foo bar"

import urllib.parse
import sys

def first_arg_or_stdin():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return sys.stdin.read().rstrip("\r\n")

def urlencode(value):
    return urllib.parse.quote_plus(value)

if __name__ == "__main__":
    print(urlencode(first_arg_or_stdin()))
```

## Read From Stdin or Files

A common pattern with Unix commands is the ability to read from files given as arguments or from `stdin` (usually via a pipe). Here is an example of doing that in Python:

```python
#!/usr/bin/env python3

import argparse
import fileinput

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('files', metavar='FILE', nargs='*', help='files to read, if empty, stdin is used')
    args = parser.parse_args()

    # If you would call fileinput.input() without files it would try to process all arguments.
    # We pass '-' as only file when argparse got no files which will cause fileinput to read from stdin
    for line in fileinput.input(files=args.files):
        print(line)
```

Example usage:

```sh
stdin file1.txt file2.txt
cat file1.txt | stdin
```

## Using argparse

```python
#!/usr/bin/env python3
#
# Basic sed/awk/grep replacement in Python.
#
# Examples:
#
# Get first character:
# echo 'foobar' | extract --index 0
#
# Split lines:
# extract --split --sep \\n "$(ps)"
# ps | extract --split --sep \\n
#
# Get second line:
# ps | extract --split --sep \\n --index 1
#
# Get second and third line:
# ps | extract --split --sep \\n --from 1 --to 3
#
# Get last line:
# ps | extract --split --sep \\n --from -1
#
# Get first column (process ID) in first row matching pattern "npm.*start":
# ps | extract --split --sep \\n --filter 'node.*start' --index 0 | extract --split --index 0
#
# Replace all occurence of one word with another
# ps|extract --split --sep \\n --replace node python
#
# Replace entire text to extract a word
# ps|extract --split --sep \\n --from 1 --replace '^.*ttys(\d+).*$' '\1'
#
# Evaluate python code:
# ps|extract --split --sep \\n --from 1 --eval '"yes" if "bash" in data else "no"'
# ps|extract --split --sep \\n --from 1 --eval 'data.upper()'

import argparse
import sys
import re

def arg_parser():
    parser = argparse.ArgumentParser(description='Describe structure of JSON document')
    parser.add_argument('--split', action='store_true', help='whether to split the input')
    parser.add_argument('--sep', default=' ', help='separator to split by')
    parser.add_argument('--index', type=int, default=None, help='index to return when using split')
    parser.add_argument('--from', type=int, default=None, help='start index to return when using split')
    parser.add_argument('--to', type=int, default=None, help='end index (exclusive) to return when using split')
    parser.add_argument('--filter', help='regex pattern to filter by when using split')
    parser.add_argument('--replace', nargs='*', help='from and to regex patterns for replacing parts or all of the text')
    parser.add_argument('--eval', help='eval python code on data variable')
    parser.add_argument('text', nargs='?', help='text to select data from (can come from stdin)')
    return parser

def apply(transform, data):
        if isinstance(data, list):
            return [transform(i) for i in data]
        else:
            return transform(data)

def extract(args):
    result = args['text']
    if args['split']:
        result = [i.strip() for i in args['text'].split(args['sep']) if i.strip()]

    if args['filter'] and isinstance(result, list):
        result = [i for i in result if re.search(args['filter'], i)]

    if args['index'] != None:
        result = result[args['index']]
    elif args['from'] != None or args['to'] != None:
        result = result[args['from']:args['to']]

    if args['replace']:
        def do_replace(data):
            from_pattern, to_pattern = args['replace']
            return re.sub(from_pattern, to_pattern, data)
        result = apply(do_replace, result)

    if args['eval']:
        def do_eval(data):
            return eval(args['eval'])
        result = apply(do_eval, result)

    if args['split'] and isinstance(result, list):
        result = [i for i in result if i]
        result = args['sep'].join(result)

    return result

if __name__ == "__main__":
    args = vars(arg_parser().parse_args())
    if not args['text']:
        args['text'] = sys.stdin.read().rstrip("\r\n")
    if args['sep'] == '\\n':
        args['sep'] = "\n"
    print(extract(args))
```

## Expsoing Python Functions with Python Fire

The [Python Fire](https://github.com/google/python-fire) library offers a powerful and easy way to expose Python functions on the command line:

```python
#!/usr/bin/env python3

import fire

class Calculator(object):
  """A simple calculator class."""

  def add(self, a, b):
    return a + b

  def double(self, number):
    return 2 * number

if __name__ == '__main__':
  fire.Fire(Calculator)
```

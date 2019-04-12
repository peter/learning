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

## Basic Example

```python
#!/usr/bin/env python3
# URL encode a string
#
# echo "foo bar" | urlencode
# urlencode "foo bar"

import urllib.parse
from util import first_arg_or_stdin
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

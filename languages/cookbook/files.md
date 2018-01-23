# Files/IO

## Read a File

Python:

```python
# Using the [open context manager](http://docs.python-guide.org/en/latest/writing/structure):
with open('README.md') as f:
    data = f.read()

# Read one integer per line:
with open('my-data-file.txt') as f:
    a = [int(x) for x in f]

# Alternative 1:
data = open('README.md').read()

# Alternative 2:
data = open('README.md').readlines()
def chomp(line):
  return line.rstrip('\r\n')
data = [chomp(l) for l in open('README.md').readlines() if chomp(l)]
```

Clojure:

```
(slurp "README.md")
```

## Write a File

Python:

```python
with open('/tmp/test.txt', 'w') as f:
  f.write('Hello World')
```

Clojure:

```
(spit "/tmp/foobar" "this is the data")
(slurp "/tmp/foobar") ; => "this is the data"
```

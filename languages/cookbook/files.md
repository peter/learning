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

## Check if File Exists

Python:

```python
import os
path = 'README.md'
os.path.exists(path)
os.path.isfile(path)
os.path.isdir(path)
```

## Stat a File

Python:

```
import os
path = 'README.md'
os.stat(path)
```

## Recursively get Files in a Directory

Python:

```python
import glob
for filename in glob.iglob('**/*.py', recursive=True):
  print filename

paths = list(glob.iglob('**/*.py', recursive=True))
```

## Dealing with Tilde (~) in Path

Python:

```
import os
path = '~/.bashrc'
os.path.exists(path) # => False
os.path.exists(os.path.expanduser(path)) # => True
```

## Create a Directory

Python:

```python
def makedirs(name):
    import os, errno
    try:
        os.makedirs(name)
    except OSError as ex:
        if ex.errno == errno.EEXIST and os.path.isdir(name):            
            pass # ignore existing directory
        else:            
            raise # a different error happened
```

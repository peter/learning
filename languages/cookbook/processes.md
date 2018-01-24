# Processes

## Get Environment Variable

Python:

```python
import os
def env(name):
    return os.environ.get(name)
```

## Config Overridden by Environment Variables

Python:

```python
import os
default_config = {
    'email': 'foobar@example.com',
    'password': '123',
}
config = {k: os.environ.get(k.upper(), v) for k, v in default_config.items()}
```

## Exiting a Process

Python:

```python
SUCCESS_EXIT_CODE = 0
FAILURE_EXIT_CODE = 1
exit(0)
```

## Invoking External Programs (Shelling Out)

Python (see [subprocess](https://docs.python.org/3/library/subprocess.html#module-subprocess)):

```python
from subprocess import call
call(["ls", "-l"])
run("exit 1", shell=True, check=True)
```

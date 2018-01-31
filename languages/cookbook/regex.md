# Regular Expressions

## Match Regex

Python:

```python
import re
re.match(r'^([1-9][0-9]*|[0-9])$', my_string)
```

## Extract Substring with Regex

Python:

```python
import re
re.match(r'^(.+)_bar$', 'foo_bar').group(1) # => 'foo'
# This function only extracts subgroups, not the entire match which is in match.group(0)
def extract(pattern, string):
    match = re.match(pattern, string)
    return match.groups() if match else ()
```

## Named Regex Capture Groups

Python:

```python
m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
m.group('first_name') # => 'Malcolm'
m.group('last_name') # => 'Reynolds'
```

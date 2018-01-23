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
```

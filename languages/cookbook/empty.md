# Empty/Missing

## Check for Empty/Blank/Null

Python:

```python
def blank(value):
    return ((value is None) or
            (type(value) in {str, tuple, list, dict, set} and len(value) == 0))

def present(value):
    return not blank(value)
```

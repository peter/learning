# Empty/Missing

## Check for Empty/Blank/Null

Python:

```python
def blank(value):
    return ((value is None) or
            (type(value) in {str, tuple, list, dict, set} and len(value) == 0))

def present(value):
    return not blank(value)

# Drop keys from dictionary/sequence with empty/null values
def compact(collection):
    if isinstance(collection, dict):
        return {k: v for k, v in collection.items() if present(v)}
    else:
        return [v for v in collection if present(v)]
```

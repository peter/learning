# Copying and Cloning

## Copy/Clone List or Dictionary

Python:

```python
import copy
new_list_shallow = copy.copy(old_list)
new_list_deep = copy.deepcopy(old_list)

# Alternative shallow copy:
new_list_shallow = list(old_list)
```

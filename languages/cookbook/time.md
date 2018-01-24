# Dates and Time

## Parsing a Datetime String

Python:

```python
# See: https://docs.python.org/3.6/library/datetime.html#strftime-strptime-behavior
# Default is to parse ISO datetime to second precision
from datetime import datetime
def parse_datetime(date_str, format = '%Y-%m-%dT%H:%M:%S', limit = 19):
    date_str = date_str[:limit] if limit else date_str
    return datetime.strptime(date_str, format)
```

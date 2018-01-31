# Dates and Time

## Parsing a Datetime String

Python:

```python
from datetime import datetime

# See: https://docs.python.org/3.6/library/datetime.html#strftime-strptime-behavior
# Default is to parse ISO datetime to second precision
def parse_datetime(date_str, format = '%Y-%m-%dT%H:%M:%S', limit = 19):
    date_str = date_str[:limit] if limit else date_str
    return datetime.strptime(date_str, format)

def from_iso_date(date_str):
  return datetime.strptime(date_str, '%Y-%m-%d')

def to_iso_date(date):
  return datetime.strftime(date, '%Y-%m-%d')
```

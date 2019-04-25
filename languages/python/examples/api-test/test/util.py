import copy
import re
from functools import reduce
import secrets
from datetime import datetime

def deep_get(dictionary, keys, default=None):
    if not isinstance(dictionary, dict):
        return default
    path = keys.split('.') if isinstance(keys, str) else keys
    result = dictionary
    def valid_index(key, _list):
        return valid_int(key) and int(key) >= 0
    for key in path:
        if isinstance(result, dict) and key in result:
            result = result[key]
        elif isinstance(result, list) and valid_index(key, result):
            result = result[int(key)] if int(key) < len(result) else None
        elif isinstance(result, list) and len(result) > 0:
            result = list(map(lambda v: v.get(key, None) if isinstance(v, dict) else None,
                              result))
        else:
            result = default
            break
    return copy.deepcopy(result)

def deep_set(dictionary, keys, value):
    if dictionary is None:
        dictionary = {}
    path = keys.split('.')
    result = copy.deepcopy(dictionary)
    nested_dict = result
    for i, key in enumerate(path):
        if i == (len(path) - 1):
            nested_dict[key] = value
        else:
            if not key in nested_dict or not isinstance(nested_dict[key], dict):
                nested_dict[key] = {}
            nested_dict = nested_dict[key]
    return result

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

def digest(length=16):
    return secrets.token_urlsafe(length)

def parse_boolean(value):
    if isinstance(value, str):
        return value.lower() in ['t', 'true', '1']
    else:
        return value

def valid_int(value):
    if isinstance(value, str) and re.match('^([1-9][0-9]*|[0-9])$', value):
        return True
    else:
        return isinstance(value, int)

# See: https://docs.python.org/3.6/library/datetime.html#strftime-strptime-behavior
# Default is to parse ISO datetime to second precision
def parse_datetime(date_str, format = '%Y-%m-%dT%H:%M:%S', limit = 19):
    date_str = date_str[:limit] if limit else date_str
    return datetime.strptime(date_str, format)

def now():
    return datetime.today()

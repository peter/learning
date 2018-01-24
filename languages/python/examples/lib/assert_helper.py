import json

def pretty_json(value):
  return json.dumps(value, indent=4, sort_keys=True)

def assert_equal(actual, expected, message=None):
    if (message):
        print('assert', message)
    try:
        assert actual == expected
    except:
        print('assert', message, 'failure actual:', pretty_json(actual))
        print('assert', message, 'failure expected:', pretty_json(expected))
        raise

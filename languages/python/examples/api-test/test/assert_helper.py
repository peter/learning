from test.json import pretty_json

def assert_equal(actual, expected, message=None, debug_info=None):
    if (message):
        print('assert', message)
    try:
        assert actual == expected
    except:
        print('assert', message, 'failure actual:', pretty_json(actual))
        print('assert', message, 'failure expected:', pretty_json(expected))
        print(f'debug_info={debug_info}')
        raise

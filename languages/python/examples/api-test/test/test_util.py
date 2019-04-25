import test.util as u

def test_deep_get():
    assert u.deep_get(None, 'foo.bar') is None
    assert u.deep_get({'foo': 1}, 'foo') == 1
    assert u.deep_get({'foo': 1}, 'foo.bar.baz') is None
    assert u.deep_get({'foo': 1}, 'bar') is None
    assert u.deep_get({'foo': 1}, 'bar', 'default-value') == 'default-value'
    assert u.deep_get({'foo': {'bar': 1}}, 'foo.bar') == 1
    assert u.deep_get({'foo': {'bar': 1}}, 'foo.baz') is None

def test_deep_get_array_index():
    assert u.deep_get({'foo': {'bar': [1]}}, 'foo.bar') == [1]
    assert u.deep_get({'foo': {'bar': [1]}}, 'foo.bar.0') == 1
    assert u.deep_get({'foo': {'bar': [1]}}, 'foo.bar.1') is None
    assert u.deep_get({'foo': {'bar': [{'baz': 1}]}}, 'foo.bar.0.baz') == 1
    assert u.deep_get({'foo': {'bar': [{'baz': 1}]}}, 'foo.bar.1.baz') is None

def test_deep_get_list_keys():
    assert u.deep_get({'foo': {'bar': 1}}, ['foo', 'bar']) == 1
    assert u.deep_get({'foo': {'bar': [1]}}, ['foo', 'bar', '0']) == 1
    assert u.deep_get({'foo': {'bar': [1]}}, ['foo', 'bar', 0]) == 1

def test_deep_get_array_map():
    assert u.deep_get({'foo': {'bar': [{'baz': 1}]}}, 'foo.bar') == [{'baz': 1}]
    assert u.deep_get({'foo': {'bar': [{'baz': 1}]}}, 'foo.bar.baz') == [1]
    assert u.deep_get({'foo': {'bar': [{'baz': 1}]}}, 'foo.bar.baz.bla') == [None]
    assert u.deep_get({'foo': {'bar': [1]}}, 'foo.bar.baz') == [None]

def test_deep_set():
    assert u.deep_set(None, 'foo.bar', 1) == {'foo': {'bar': 1}}
    assert u.deep_set({}, 'foo.bar', 1) == {'foo': {'bar': 1}}
    assert u.deep_set({'foo': 2}, 'foo.bar', 1) == {'foo': {'bar': 1}}
    assert u.deep_set({'foo': {'bar': 2}}, 'foo.bar', 1) == {'foo': {'bar': 1}}
    assert u.deep_set({'foo': {'bar': 2, 'baz': 1}, 'bla': 0}, 'foo.bar', 1) == {'foo': {'bar': 1, 'baz': 1}, 'bla': 0}
    assert u.deep_set({'foo': {'bar': 1}}, 'foo.baz', 0) == {'foo': {'bar': 1, 'baz': 0}}

def test_blank_and_resent():
    for value in [None, '', [], {}, set(), tuple()]:
        assert u.blank(value)
        assert not u.present(value)
    for value in [1, 'foo', ['foo'], {'foo': 1}, set('foo'), tuple('foo')]:
        assert not u.blank(value)
        assert u.present(value)

def test_compact():
    assert u.compact({}) == {}
    assert u.compact({'foo': 1}) == {'foo': 1}
    assert u.compact({'foo': 1, 'bar': None, 'baz': [], 'bla': ''}) == {'foo': 1}

def test_parse_boolean():
    assert u.parse_boolean(True) == True
    assert u.parse_boolean(False) == False
    assert u.parse_boolean({'foo': 1}) == {'foo': 1}
    for value in ['f', 'false', 'False', '0']:
        assert u.parse_boolean(value) == False
    for value in ['t', 'true', 'TRUE', '1']:
        assert u.parse_boolean(value) == True

def test_valid_int():
    assert u.valid_int(3) == True
    assert u.valid_int('0') == True
    assert u.valid_int('9') == True
    assert u.valid_int('123') == True
    assert u.valid_int('0123') == False
    assert u.valid_int('1.23') == False
    assert u.valid_int('123a') == False
    assert u.valid_int('foobar') == False
    assert u.valid_int(None) == False

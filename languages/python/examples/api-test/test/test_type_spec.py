import pytest
from test.type_spec import typeSpec
import test.type_spec as t

class Data:
    def __init__(self, data):
        self.data = data

class MyNumber:
  def __init__(self, n):
    self.n = n
  def __add__(self, other):
    return MyNumber(self.n + other.n)
  def type_check(my_number):
    return t.type_check(my_number.n, int)

def Number(v):
    return t.type_check(v, t.AnyOf(int, float))

def Positive(v):
    if v < 0:
        return 'must be positive'

class CallableNumber:
    def __call__(self, v):
        return t.type_check(v, int)

def GreaterThanZero(v):
    if v <= 0:
        return 'must be greater than zero'

@typeSpec(Number, t.AllOf(Number, GreaterThanZero), Number)
def div(a, b):
    return a / b

def test_compact():
    assert t.compact({'foo': 1, 'bar': None}) == {'foo': 1}
    assert t.compact({}) == {}

def test_TypeOf():
    assert t.TypeOf(5)(2) == None
    assert t.TypeOf(5)('foo') == "must be of type int"

def test_Maybe():
    assert t.Maybe(int)(5) == None
    assert t.Maybe(int)(None) == None
    assert t.Maybe(int)(2.3) == "must be of type int"

def test_Enum():
    assert t.Enum('bar', 'baz')('bar') == None
    assert t.Enum('bar', 'baz')('baz') == None
    assert t.Enum('bar', 'baz')('bla') == 'must be one of bar, baz'
    assert t.Enum('bar', 'baz')(None) == 'must be one of bar, baz'

def test_NoneCheck():
    assert t.NoneCheck(None) == None
    assert t.NoneCheck('foo') == 'must be None'
    assert t.NoneCheck(5) == 'must be None'

def test_List():
    assert t.List([])([]) == None
    assert t.List([])(['foo']) == None

    assert t.List([])(None) == 'must be of type list'
    assert t.List([])(5) == 'must be of type list'
    assert t.List([])({}) == 'must be of type list'

    assert t.List([str])(['foo']) == None
    assert t.List([str])(['foo', 'bar']) == None
    assert t.List([str])([3]) == "list index 0 is invalid - must be of type str"
    assert t.List([str])(['foo', 3]) == "list index 1 is invalid - must be of type str"

    assert t.List([t.Maybe(float)])([3.3, None, 5.2]) == None
    assert t.List([t.Maybe(float)])([3.3, None, 5]) == "list index 2 is invalid - must be of type float"

    assert t.List([str, int, t.Maybe(float)])(['foo', 1, 3.4]) == None
    assert t.List([str, int, t.Maybe(float)])(['foo', 1, None]) == None
    assert t.List([str, int, t.Maybe(float)])(['foo', 1, 3.4, 5]) == 'list has length 4 but must be 3'
    assert t.List([str, int, t.Maybe(float)])(['foo', 1.3, None]) == "list index 1 is invalid - must be of type int"

def test_Dict():
    assert t.Dict({})({}) == None
    assert t.Dict({})({'foo': 1}) == None

    assert t.Dict({})(None) == 'must be of type dict'
    assert t.Dict({})(3) == 'must be of type dict'
    assert t.Dict({})([]) == 'must be of type dict'

    assert t.Dict({'foo': str, 'bar': int})({'foo': 'foo', 'bar': 5}) == None
    assert t.Dict({'foo': str, 'bar': int})({'foo': 'foo', 'bar': 5, 'baz': 'bla'}) == None

    assert t.Dict({'foo': str, 'bar': int})({'foo': 'foo', 'bar': 'bar'}) == "{'bar': 'must be of type int'}"
    assert t.Dict({'foo': str, 'bar': int})({'foo': 'foo'}) == "{'bar': 'must be of type int'}"

    assert t.Dict({'foo': t.Maybe(str), 'bar': int})({'bar': 5}) == None
    assert t.Dict({'foo': t.Maybe(str), 'bar': int})({'foo': None, 'bar': 5}) == None

    assert t.Dict({'foo': str, 'bar': [{'n': int}]})({'foo': 'foo', 'bar': [{'n': 3}]}) == None

def test_AnyOf():
    assert t.AnyOf(int, str)(5) == None
    assert t.AnyOf(int, str)('foo') == None
    assert t.AnyOf(int, str)(2.3) == "must be one of these types: int, str"

    assert t.AnyOf(t.Maybe(int), str)(5) == None
    assert t.AnyOf(t.Maybe(int), str)(None) == None
    assert t.AnyOf(t.Maybe(int), str)('foo') == None
    assert t.AnyOf(t.Maybe(int), str)({}) == "must be one of these types: Maybe(int), str"

def test_AllOf():
    assert t.AllOf(Number, Positive)(0) == None
    assert t.AllOf(Number, Positive)(1) == None
    assert t.AllOf(Number, Positive)(1.5) == None
    assert t.AllOf(Number, Positive)('foobar') == "must be one of these types: int, float"
    assert t.AllOf(Number, Positive)(-3) == 'must be positive'

def test_type_check_type():
    assert t.type_check(5, int) == None
    assert t.type_check('foobar', int) == 'must be of type int'

    assert t.type_check(True, bool) == None
    assert t.type_check(False, bool) == None
    assert t.type_check(5, bool) == 'must be of type bool'

    assert t.type_check(Data(5), Data) == None
    assert t.type_check('foobar', Data) == 'must be of type test.test_type_spec.Data'

def test_type_check_custom_check():
    assert t.type_check(MyNumber(5), MyNumber) == None
    assert t.type_check(MyNumber(5.3), MyNumber) == 'must be of type int'

def test_type_check_none():
    assert t.type_check(None, None) == None
    assert t.type_check(5, None) == 'must be None'

def test_type_check_dict():
    assert t.type_check({}, {}) == None
    assert t.type_check([], {}) == 'must be of type dict'
    assert t.type_check({'foo': 1}, {}) == None
    assert t.type_check({'foo': 1}, {'foo': int}) == None
    assert t.type_check({'foo': 1.3}, {'foo': int}) == "{'foo': 'must be of type int'}"

def test_type_check_list():
    assert t.type_check([], []) == None
    assert t.type_check({}, []) == 'must be of type list'
    assert t.type_check([3], []) == None
    assert t.type_check([3], [int]) == None
    assert t.type_check([3, 4, 5], [int]) == None
    assert t.type_check([3, 4, 5.2], [int]) == 'list index 2 is invalid - must be of type int'

def test_type_check_callable():
    assert t.type_check(5, Positive) == None
    assert t.type_check(5.9, Positive) == None
    assert t.type_check(-5, Positive) == 'must be positive'

    assert t.type_check(5, CallableNumber()) == None
    assert t.type_check(5.5, CallableNumber()) == 'must be of type int'

def test_type_check_predicate():
    even = lambda n: n % 2 == 0
    assert t.type_check(6, even) == None
    assert t.type_check(5, even) == 'must be of type test_type_check_predicate.<locals>.<lambda>'

def test_type_check_example():
    assert t.type_check(5, 1) == None
    assert t.type_check(5, 1.3) == 'must be of type float'
    assert t.type_check('foo', 'bar') == None
    assert t.type_check(MyNumber(3), MyNumber(5)) == None
    assert t.type_check(3, MyNumber(5)) == 'must be of type test.test_type_spec.MyNumber'

def test_typeSpec():
    div(3, 4)
    div(1, 1)
    with pytest.raises(ValueError, message='must be greater than zero'):
        div(1, 0)
    with pytest.raises(ValueError, message='must be of type Number'):
        div('1', 1)

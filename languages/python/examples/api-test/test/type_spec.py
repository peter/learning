# This modules provides pre/post conditions for python functions via the @typeSpec decorator

import re
from functools import reduce

def compact(d):
    return {k: v for k, v in d.items() if v != None}

def type_str(t):
    result = str(t)
    match = re.match(r'<function (\S+)', result)
    if match:
        return match.group(1)
    match = re.match(r'<class \'(\S+)\'', result)
    if match:
        return match.group(1)
    return result

def TypeOf(example):
    example_type = type(example)
    def check(v):
        if not isinstance(v, example_type):
            return 'must be of type {}'.format(type_str(example_type))
    return check

class Maybe:
    def __init__(self, optional_type):
        self.optional_type = optional_type
    def __call__(self, v):
        if v == None:
            return None
        else:
            return type_check(v, self.optional_type)
    def __repr__(self):
        return 'Maybe({})'.format(type_str(self.optional_type))

def Enum(*allowed_values):
    def check(v):
        if not v in set(allowed_values):
            return 'must be one of {}'.format(', '.join(allowed_values))
    return check

def NoneCheck(v):
    if v == None:
        return None
    else:
        return 'must be None'

def List(list_spec):
    def check(v):
        if not isinstance(v, list):
            return 'must be of type list'
        if len(list_spec) == 1:
            item_type = list_spec[0]
            for i, iv in enumerate(v):
                error_message = type_check(iv, item_type)
                if error_message:
                    return 'list index {} is invalid - {}'.format(i, error_message)
        elif len(list_spec) > 1:
            if len(list_spec) != len(v):
                return 'list has length {} but must be {}'.format(len(v), len(list_spec))
            for i, iv in enumerate(v):
                error_message = type_check(iv, list_spec[i])
                if error_message:
                    return 'list index {} is invalid - {}'.format(i, error_message)
    return check

def Dict(dict_spec):
    def check(v):
        if not isinstance(v, dict):
            return 'must be of type dict'
        errors = compact({k: type_check(v.get(k, None), t) for k, t in dict_spec.items()})
        return str(errors) if len(errors) > 0 else None
    return check

def AnyOf(*allowed_types):
    def check(v):
        for allowed_type in allowed_types:
            result = type_check(v, allowed_type)
            if result == None:
                return result
        return 'must be one of these types: {}'.format(', '.join(map(type_str, allowed_types)))
    return check

def AllOf(*required_types):
    def check(v):
        for required_type in required_types:
            result = type_check(v, required_type)
            if result != None:
                return result
    return check

def type_check(v, required_type):
    def check_callable(v, callable_type):
        result = callable_type(v)
        error_message = 'must be of type {}'.format(type_str(callable_type)) if result == False else result
        if result != True and error_message:
            return error_message
    if type(required_type) == type:
        callable_type = getattr(required_type, 'type_check', None)
        if not isinstance(v, required_type):
            return 'must be of type {}'.format(type_str(required_type))
        elif callable_type:
            return check_callable(v, callable_type)
    elif required_type == None:
        return check_callable(v, NoneCheck)
    elif type(required_type) == list:
        return check_callable(v, List(required_type))
    elif type(required_type) == dict:
        return check_callable(v, Dict(required_type))
    elif callable(required_type):
        return check_callable(v, required_type)
    else:
        return check_callable(v, TypeOf(required_type))

def assert_type(v, required_type, message = ''):
    error_message = type_check(v, required_type)
    if error_message:
        raise ValueError(message + error_message)

class typeSpec(object):
    def __init__(self, *signature):
        if len(signature) < 1:
            raise ValueError('Signature is empty')
        self.arg_types = signature[:-1]
        self.return_type = signature[-1]

    def __call__(self, f):
        def with_type_check(*args, **kwargs):
            for i, arg in enumerate(args):
                assert_type(arg, self.arg_types[i], message='typeSpec: arg {} with value {} of type {} is invalid - '.format(i, arg, type(arg)))
            result = f(*args, **kwargs)
            assert_type(result, self.return_type, message='typeSpec: return type with value {} of type {} is invalid - '.format(result, type(result)))
            return result
        return with_type_check

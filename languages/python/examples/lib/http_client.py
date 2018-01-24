import requests
import json
import test.config as config
from test.assert_helper import assert_equal
from test.util import compact
from test.json import pretty_json

def print_response_body(response):
    print('response body:')
    try:
        print(pretty_json(response.json()))
    except:
        print(response.text)

def check_status_code(response, valid_codes={200, 204, 404}):
    message = 'status_code in %s, actual %s' % (valid_codes, response.status_code)
    if response.status_code not in valid_codes:
        print('Invalid response', response.status_code, response.reason)
        print_response_body(response)
    assert_equal(response.status_code in valid_codes, True, message)

def header_str(headers):
    return ' '.join(["'%s':'%s'" % (k, v) for k, v in headers.items()])

def get(url, params={}, headers={}, valid_codes={200, 404}):
    headers = compact(headers)
    print("\nhttp get '%s' %s " % (url, header_str(headers)))
    response = requests.get(url, params=params, headers=headers)
    check_status_code(response, valid_codes)
    if config.boolean('LOG_RESPONSE'):
        print_response_body(response)
    return response

def post(url, data, headers={}, valid_codes={200, 204, 201}):
    headers = compact(headers)
    print("\necho '%s' | http post '%s' %s " % (json.dumps(data), url, header_str(headers)))
    response = requests.post(url, json=data, headers=headers)
    check_status_code(response, valid_codes)
    return response

def put(url, data, headers={}, valid_codes={200, 204}):
    headers = compact(headers)
    print("\necho '%s' | http put '%s' %s " % (json.dumps(data), url, header_str(headers)))
    response = requests.put(url, json=data, headers=headers)
    check_status_code(response, valid_codes)
    return response

def patch(url, data, headers={}, valid_codes={200, 204}):
    headers = compact(headers)
    print("\necho '%s' | http patch '%s' %s " % (json.dumps(data), url, header_str(headers)))
    response = requests.patch(url, json=data, headers=headers)
    check_status_code(response, valid_codes)
    return response

def delete(url, headers={}, valid_codes={200, 204}):
    headers = compact(headers)
    print("\nhttp delete '%s' %s " % (url, header_str(headers)))
    response = requests.delete(url, headers=headers)
    check_status_code(response, valid_codes)
    return response

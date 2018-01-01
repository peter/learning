# First start api.py in a separate terminal and then run the tests:
#
# BASE_URL=http://localhost:5000 python -m pytest -s -vv test_api.py

import os
import sys
import uuid
import requests

BASE_URL = os.getenv('BASE_URL')

def uuid_hex():
    return uuid.uuid4().hex

def merge(dict1, dict2):
    return {**dict1, **dict2}

item = {'id': uuid_hex(), 'name': 'test item'}
updated_item = merge(item, {'name': 'test item updated'})

def test_happy_path_crud():
    list_url = BASE_URL + '/items'
    get_url = BASE_URL + '/items/' + item['id']

    response = requests.get(get_url)
    assert response.status_code == 404

    response = requests.post(list_url, json={'item': item})
    assert response.status_code == 200
    assert response.json()['item'] == item

    response = requests.get(get_url)
    assert response.status_code == 200
    assert response.json()['item'] == item

    response = requests.get(list_url)
    assert response.status_code == 200
    assert item in response.json()['items']

    response = requests.put(get_url, json={'item': updated_item})
    assert response.status_code == 200

    response = requests.get(get_url)
    assert response.status_code == 200
    assert response.json()['item'] == updated_item

    response = requests.delete(get_url)
    assert response.status_code == 200

    response = requests.get(get_url)
    assert response.status_code == 404

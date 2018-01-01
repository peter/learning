# Usage:
#
# Starting the API:
#
# pip install Flask
# FLASK_APP=api.py flask run
#
# Invoking the API:
#
# create:
# echo '{"item": {"id": 123, "name": "some name"}}' | http POST http://127.0.0.1:5000/items
#
# get:
# http http://127.0.0.1:5000/items/123
#
# list:
# http http://127.0.0.1:5000/items
#
# update:
# echo '{"item": {"name": "new name"}}' | http PUT http://127.0.0.1:5000/items/123
#
# delete:
# http DELETE http://127.0.0.1:5000/items/123

from flask import Flask, jsonify, request

app = Flask(__name__)

DB = {'items': []}

def request_item():
    return request.get_json() and request.get_json().get('item', {})

def find(f, seq):
  for item in seq:
    if f(item):
      return item
  return None

def get_item(id):
    return find(lambda i: i['id'] == id, DB['items'])

def create_item(item):
    DB['items'].append(item)
    return item

def update_item(item):
    DB['items'] = [item if item['id'] == i['id'] else i for i in DB['items']]
    return item

def delete_item(item):
    DB['items'].remove(item)

def validate_item(item):
    # TODO
    return None

@app.route('/items', methods=['GET'])
def list():
    return jsonify({'items': DB['items']})

@app.route('/items/<id>', methods=['GET'])
def get(id):
    item = get_item(id)
    if item:
        return jsonify({'item': item})
    else:
        return ('Could not find item', 404)

@app.route('/items', methods=['POST'])
def create():
    item = request_item()
    errors = validate_item(item)
    if not errors:
        created_item = create_item(item)
        return jsonify({'item': created_item})
    else:
        return (jsonify({'errors': errors}), 422)

@app.route('/items/<id>', methods = ['PUT'])
def update(id):
    updated_item = request_item()
    item = get_item(id)
    if item and updated_item['id'] == id:
        errors = validate_item(item)
        if not errors:
            updated_item = update_item(updated_item)
            return jsonify({'item': updated_item})
        else:
            return (jsonify({'errors': errors}), 422)
    else:
        return ('Could not find item', 404)

@app.route('/items/<id>', methods = ['DELETE'])
def delete(id):
    item = get_item(id)
    if item:
        delete_item(item)
        return (jsonify({}), 200)
    else:
        return ('Could not find item', 404)

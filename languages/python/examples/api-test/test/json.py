import json

def pretty_json(value):
  return json.dumps(value, indent=4, sort_keys=True)

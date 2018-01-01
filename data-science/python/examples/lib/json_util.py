import json

def generate(obj):
    return json.dumps(obj)

def parse(json_str):
    return json.loads(json_str)

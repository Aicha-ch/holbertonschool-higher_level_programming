#!/usr/bin/python3
import json
"""returning the JSON representation of an object"""


def to_json_string(my_obj):
    json_str = json.dumps(my_obj)
    return json_str


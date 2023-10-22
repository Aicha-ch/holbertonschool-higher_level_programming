#!/usr/bin/python3
"""import json module"""

import json


def save_to_json_file(my_obj, filename):
    """get the JSON-formatted string"""
    json_str = json.dumps(my_obj)
    """Write the JSON string to a text file"""
    with open(filename, "w") as file:
        file.write(json_str)

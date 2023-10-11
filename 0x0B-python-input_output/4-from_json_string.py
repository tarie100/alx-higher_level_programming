#!/usr/bin/python3
"""define func"""


def from_json_string(my_str):
    """iport json"""
    import json
    """returns py data struct. rep by json"""
    return json.loads(my_str)

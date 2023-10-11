#!/usr/bin/python3
"""define func"""


def load_from_json_file(filename):
    """import json"""
    import json
    """creates object"""
    with open(filename) as f_file:
        """returns object"""
        json.load(f_file)

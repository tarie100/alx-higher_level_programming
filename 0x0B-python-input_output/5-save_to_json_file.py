#!/usr/bin/python3
"""define func"""
def save_to_json_file(my_obj, filename):
    """import json"""
    import json
    with open(filename, "w", encoding="utf-8") as n_file:
        """opens file and writes object"""
        json.dump(my_obj, n_file)

#!/usr/bin/python3
"""define func"""
import json


def load_from_json_file(filename):
    """creates object"""
    with open(filename) as f_file:
        """returns object"""
        json.load(f_file)

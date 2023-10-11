#!/usr/bin/python3
"""defining file reader"""


def read_file(filename=""):
    """rep function"""
    with open(filename, encoding="utf-8") as my_file:
        """open file with utf8 encoder"""
        print(my_file.read, end="")

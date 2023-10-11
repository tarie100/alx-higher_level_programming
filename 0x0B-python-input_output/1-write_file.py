#!/usr/bin/python3
"""define func"""
def write_file(filename="", text=""):
    """open file with utf8"""
    with open(filename, "w", encoding="utf-8") as w_file:
        """write to file"""
        return w_file.write(text)

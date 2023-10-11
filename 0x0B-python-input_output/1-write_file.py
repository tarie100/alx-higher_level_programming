#!/usr/bin/python3
"""define func"""
def write_file(filename="", text=""):
    """open file with utf8"""
    with open(filename, encoding="utf-8") as w_file:
        """write to file"""
        w_file.write(text)
        """return written chars"""
        return w_file.tell()

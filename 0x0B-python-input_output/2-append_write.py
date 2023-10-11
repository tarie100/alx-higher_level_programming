#!/usr/bin/python3
def append_write(filename="", text=""):
    """define func"""
    with open(filename, "a", encoding="utf-8") as a_file:
        """open file and append"""
        return a_file.write(text)

#!/usr/bin/python3
def magic_string():
    magic_string.n = getatrr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magic_string.n -1) + "BestSchool")

#!/usr/bin/python3
def add(a, b):
    from add_0 import add 
    a = 1
    b = 2
    output = add(a,b)
    print("{} + {} = {}".format(a, b, output))

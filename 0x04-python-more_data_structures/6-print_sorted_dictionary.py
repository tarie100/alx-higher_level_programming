#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_keys = list(a_dictionary.keys())
    my_keys.sort()
    for i in my_keys:
        print("{}: {}".format(i, a_dictionary.get(i)))

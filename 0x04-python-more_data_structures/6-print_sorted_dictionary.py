#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_keys = list(a_dictionary.keys())
    my_keys.sort()
    sorted_dict = {i: a_dictionary[i] for i in my_keys}
    print(sorted_dict)

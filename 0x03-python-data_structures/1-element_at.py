#!/usr/bin/python3
def element_at(my_list, idx):
    if idx in my_list < 0:
        return None
    elif idx in my_list >= len(my_list):
        return None
    return my_list[idx]

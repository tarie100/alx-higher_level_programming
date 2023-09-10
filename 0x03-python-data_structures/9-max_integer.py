#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == "":
        return None
    max_value = my_list[0]
    for num in range(len(my_list[1:])):
        if my_list[num] > max_value:
            max_value = my_list[num]
    print(max_value)

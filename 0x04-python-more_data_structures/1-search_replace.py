#!/usr/bin/python3
def search_replace(my_list, search, replace):
    count_dict = {}
    new_list = []
    for item in my_list:
        if item in count_dict:
            new_list.append('rep')
        else:
            count_dict[item] = 1
            new_list.append(replace)
    print(my_list)
    print(new_list)

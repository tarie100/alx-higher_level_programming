#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_nums = set()
    total = 0
    for num in my_list:
        if num not in uniq_nums:
            total += uniq_nums.add(num)
    return total

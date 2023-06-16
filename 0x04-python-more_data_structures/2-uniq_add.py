#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set()
    for num in my_list:
        if num not in new_list:
            new_list.add(num)
    total = sum(new_list)

    return total

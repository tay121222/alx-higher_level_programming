#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = set()

    for element in set_1:
        if element in set_2:
            new_list.add(element)
    return new_list

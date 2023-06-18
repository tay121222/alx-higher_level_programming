#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    big_val = 0
    for key in a_dictionary:
        if int(a_dictionary[key]) > big_val:
            big_val = int(a_dictionary[key])
    return big_val

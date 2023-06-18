#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None

    big_val = 0
    big_key = None
    for key in a_dictionary:
        if a_dictionary[key] is not None and int(a_dictionary[key]) > big_val:
            big_val = int(a_dictionary[key])
            big_key = key
    return big_key

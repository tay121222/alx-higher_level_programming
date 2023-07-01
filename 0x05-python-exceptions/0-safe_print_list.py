#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for members in my_list:
            print(members, end="")
            i += 1
            if i == x:
                break
        print()
        return i
    except:
        return i

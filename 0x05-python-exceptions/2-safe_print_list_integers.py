#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            try:
                if type(my_list[i]) == int:
                    print("{:d}".format(my_list[i]), end="")
                    count += 1
            except (ValueError, IndexError):
                continue
        print()
        return count
    except (TypeError, IndexError):
        return count

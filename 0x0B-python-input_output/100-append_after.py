#!/usr/bin/python3
"""contains function that inserts a
line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """contains function that inserts a
    line of text to a file
    """
    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()

    with open(filename, 'w', encoding="utf-8") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.writeline(new_string + '\n')

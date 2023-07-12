#!/usr/bin/python3
"""contains function that inserts a
line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """contains function that inserts a
    line of text to a file
    """
    new_str =""
    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            new_str += line
            if search_string in line:
                new_str += new_string

    with open(filename, 'w', encoding="utf-8") as file:
        file.write(new_str)

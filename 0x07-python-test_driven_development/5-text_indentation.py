#!/usr/bin/python3
"""contains function that prints a text with 2 new lines"""


def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")

    for char in ".:?":
        text = (char + "\n\n").join(
            [line.strip(" ") for line in text.split(char)])
    print("{}".format(text), end="")

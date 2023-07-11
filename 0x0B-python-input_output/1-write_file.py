#!/usr/bin/python3
"""Contains function that writes a string to a text file"""


def write_file(filename="", text=""):
    """writes a string to a text file (TF8)"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

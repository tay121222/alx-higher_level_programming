#!/usr/bin/bash
"""contains function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        readlines = file.read()
        print(readlines, end="")

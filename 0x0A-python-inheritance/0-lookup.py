#!/usr/bin/python3
"""returns the list of available attributes"""


def lookup(obj):
    """funlist ttributes and methods of an object"""
    list_attrib = dir(obj)
    return list_attrib

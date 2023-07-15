#!/usr/bin/python3
"""Contains function that adds a new attribute
to an object if it’s possible"""


def add_attribute(obj, attr, value):
    if not hasattr(obj, '__dict__') and not hasattr(
            obj, '__slots__'
            ):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)

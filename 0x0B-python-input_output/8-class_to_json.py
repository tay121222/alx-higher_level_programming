#!/usr/bin/python3
"""function that returns the dictionary
description with simple data structure
"""


def class_to_json(obj):
    """returns the dictionary descrip. with simple data structure"""
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    else:
        return {}

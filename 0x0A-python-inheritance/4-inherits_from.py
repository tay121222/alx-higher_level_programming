#!/usr/bin/python3
"""function that returns True 
if the object is an instance of a class
"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class

#!/usr/bin/python3
"""contains class Student that defines a student"""


class Student:
    """class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializing variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation
        of a Student instance based on attributes
        passed to it
        """
        obj_list = self.__dict__
        new_list = dict()
        if type(attrs) is list and all(type(a) is str for a in attrs):
            for a in attrs:
                if a in obj_list:
                    new_list.update({a: self.__dict__[a]})
            return new_list
        return self.__dict__.copy()

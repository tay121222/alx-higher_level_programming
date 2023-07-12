#!/usr/bin/python3
"""contains class Student that defines a student"""


class Student:
    """class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializing variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation
        of a Student instance
        """
        return self.__dict__.copy()

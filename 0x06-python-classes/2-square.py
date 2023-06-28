#!/usr/bin/python3
"""
My first square
"""


class Square:
    """
    This class represents a square
    """
    __size = None

    def __init__(self, size=0):
        """ Initializing method """

        if type(size) != int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

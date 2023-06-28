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

        self.__size = 0

    @property
    def size(self):
        """ size property """
        return self.__size

    @size.setter
    def size(self, value):
        """
        type and value checks to ensure that the assigned value is an integer
        """

        if type(value) != int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Clculate area of the square
        """

        return self.__size ** 2

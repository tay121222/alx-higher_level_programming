#!/usr/bin/python3
"""Defines a Rectangle"""


class Rectangle:
    """Rectangle class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        """Method for retrieving the width"""
        return self._width

    @width.setter
    def width(self, value):
        """Setting the width of the rec."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Method for retrieving the height"""
        return self._height

    @height.setter
    def height(self, value):
        """Setting the height of the rec."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """ Returns rectangle area"""
        return self._width * self._height

    def perimeter(self):
        """Returns rectangle perimeter"""
        if self._width == 0 or self._height == 0:
            return 0
        return (self._width + self._height) * 2

    def __str__(self):
        """ print the rectangle with the character # """
        if self._width == 0 or self._height == 0:
            return ""
        return (("#" * self._width + "\n") * self._height)[:-1]

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle(" + str(self._width) + ", " + str(self._height) + ")"

    def __del__(self):
        """Print the message Bye rectangle"""
        print("Bye rectangle...")

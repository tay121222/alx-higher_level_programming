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

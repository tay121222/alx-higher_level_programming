#!/usr/bin/python3
"""Defines a Rectangle"""


class Rectangle:
    """Rectangle class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Method for retrieving the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the width of the rec."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method for retrieving the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the height of the rec."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

#!/usr/bin/python3
"""Contains Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """Returns an area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns string rep of a rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

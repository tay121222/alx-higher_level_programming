#!/usr/bin/python3
"""Defines a Rectangle"""


class Rectangle:
    """Rectangle class that defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height
        self.number_of_instances += 1

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
        return (
                (
                    str(self.print_symbol) * self._width + "\n"
                    ) * self._height
                )[:-1]

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle(" + str(self._width) + ", " + str(self._height) + ")"

    def __del__(self):
        """Print the message Bye rectangle"""
        self.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Rec with the bigger area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance"""
        return cls(size, size)

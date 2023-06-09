#!/usr/bin/python3
"""
My first square
"""


class Square:
    """
    This class represents a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializing method
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        size property
        """
        return self.__size

    @property
    def position(self):
        """
        Gets the postion of the store
        """
        return self.__position

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

    @position.setter
    def postion(self, value):
        """
        Sets the position of the square
        """
        if type(value) != tuple or len(value) != 2:
            raise TyperError("position must be a tuple of 2 positive integers")
        for num in value:
            if type(num) != int or num < 0:
                raise ValueError("position must contain 2 positive integers")

        self.__position = value

    def area(self):
        """
        Calculate area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """ Print square using '#' char """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns a string rep of a square
        """
        s_rep = ""
        if self.__size == 0:
            return s_rep
        else:
            for _ in range(self.__position[1]):
                s_rep += "\n"
            for _ in range(self.__size):
                s_rep += " " * self.__position[0] + "#" * self.__size + "\n"
            return s_rep.rstrip("\n")

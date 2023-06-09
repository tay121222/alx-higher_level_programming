#!/usr/bin/python3
""" Python class that does same as Python bytecode """

import math


class MagicClass:
    """ Represent a Circle """

    def __init__(self, radius=0):
        """ Initialize a MagicClass """

        self.__radius = 0
        if type(radius) != int and type(radius) != float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ Calculate the area of the MagicClass """
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """ Calculate the circumference of the MagicClass """
        return 2 * math.pi * self.__radius

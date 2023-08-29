#!/usr/bin/python3
"""docstring module"""
import math


class MagicClass:
    """ the class magicClass"""

    def __init__(self, radius=0):
        """ initialises docstring """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """initializes another docstring"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """another docstring"""
        return 2 * math.pi * self.__radius

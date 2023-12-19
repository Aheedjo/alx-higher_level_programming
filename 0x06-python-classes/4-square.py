#!/usr/bin/python3
"""This module contains a Square class"""

class Square:
    """A square class"""
    def __init__(self, size=0):
        """
        Initialize a square with size.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """A property that returns the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Find area of square"""
        return self.__size * self.__size

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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        return self.__size * self.__size

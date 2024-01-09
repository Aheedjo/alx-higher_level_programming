#!/usr/bin/python3
"""This module contains a Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that defines square objects"""

    def __init__(self, size):
        """Initialize square

        Args:
            size (int): The size of the sq
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size


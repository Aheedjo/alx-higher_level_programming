#!/usr/bin/python3
"""This module contains a sqaure class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that defines square objects"""

    def __init__(self, size):
        """
        Desc:
            Constructor for new squares

        Args:
            size (int): The size of the sq
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ print str repr"""
        return f"[Square] {self.__size}/{self.__size}"


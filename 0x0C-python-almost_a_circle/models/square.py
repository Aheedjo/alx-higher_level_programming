#!/usr/bin/python3
"""This module contains the Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines the rectangle object"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of square
            x (int): The x coordinate of the sq
            y (int): The y coordinate of the sq
            id (int): The id of the sq
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Override str representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """size getter method
        return:
            size sq
        """
        return self.width

    @size.setter
    def size(self, value):
        """width and height setter method
        args:
            value: size value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attrs"""
        if args:
            keys = ["id", "size", "x", "y"]
            for key, arg in zip(keys, args):
                setattr(self, key, arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dict repr of a Square"""
        keys = ["id", "x", "size", "y"]
        return {key: getattr(self, key) for key in keys}


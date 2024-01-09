#!/usr/bin/python3
"""This module contains a BaseGeometry class"""


class BaseGeometry:
    """This class will the the blueprint for its instances"""
    def area(self):
        """A function yet to be implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Desc:
            A method that validates value

        Args:
            value (int): The value to be validated
            name (str): name of the parameter

        Raises:
            TypeError: If name is not an integer
            ValueError: If name < 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


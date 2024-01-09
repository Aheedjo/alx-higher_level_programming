#!/usr/bin/python3
"""This module contains a Rectangle class that inherits from BaseGeo"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A cls that defines the rect instance"""
    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """A method to find area of obj"""
        return self.__height * self.__width

    def __str__(self):
        """ print str repr"""
        return f"[Rectangle] {self.__width}/{self.__height}"


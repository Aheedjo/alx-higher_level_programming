#!/usr/bin/python3
"""This module contains Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """This class defines rectangle objects"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializatin of variables"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """print a graphical repr of rectangle with '#'"""
        for row in range(self.y):
            print()
        for row in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def __str__(self):
        """Override str representation"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} " \
            f"- {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Update the attrs"""
        if args:
            keys = ["id", "width", "height", "x", "y"]
            for key, arg in zip(keys, args):
                setattr(self, key, arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dict repr of Rectangle"""
        keys = ["x", "y", "id", "height", "width"]
        return {key: getattr(self, key) for key in keys}


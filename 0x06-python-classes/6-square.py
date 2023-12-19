#!/usr/bin/python3
"""A python module that contains a sqaure class"""


class Square:
    """A square class"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square with size.

        Args:
            size (int): The size of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """A property that returns the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        A function that sets the value of size

        Args:
            value (int): the size of the sq

        Raises:
            TypeError: if the value is not int
            ValueError: if the size <= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """A property that retrieves the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        A function that sets the value of position

        Args:
            value (tuple): the position of the sq

        Raises:
            TypeError: if the value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """A function that prints the sq"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def area(self):
        """Find area of square"""
        return self.__size * self.__size


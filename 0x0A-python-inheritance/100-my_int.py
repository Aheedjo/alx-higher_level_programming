#!/usr/bin/python3
"""This module contains a MyInt class"""


class MyInt(int):
    """This class defines a custom int obj"""

    def __eq__(self, value):
        """Override == opeartor with != operator"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == operator"""
        return self.real == value


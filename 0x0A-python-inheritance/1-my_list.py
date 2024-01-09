#!/usr/bin/python3
"""This module contains a MyList class"""


class MyList(list):
    """A class that defines a list based on the builtin list class"""
    def print_sorted(self):
        """A method that prints a sorted version of a list"""
        sorted_list = sorted(self)
        print(sorted_list)


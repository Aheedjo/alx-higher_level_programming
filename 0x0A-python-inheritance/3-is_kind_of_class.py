#!/usr/bin/python3
"""This module contains a function that returns true if an object is an
instance of a specified class"""


def is_kind_of_class(obj, a_class):
    """
    Desc:
        check if an obj is exactly an instance of a class

    Args:
        obj (any): Object
        a_class (type): the class to be matched

    Returns:
        bool: True if match, otherwise false
    """
    return isinstance(obj, a_class)


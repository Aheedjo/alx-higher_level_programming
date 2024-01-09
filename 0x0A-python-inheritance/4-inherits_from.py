#!/usr/bin/python3
"""This module contains a function that returns true if an object is an
instance of a specified class"""


def inherits_from(obj, a_class):
    """
    Desc:
        check if an object is an instance of a class that inherited
        from a_class

    Args:
        obj (any): Object
        a_class (type): the class to be matched

    Returns:
        bool: True if match, otherwise false
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class


#!/usr/bin/python3
"""This module contains a functin add_attribute"""


def add_attribute(obj, att, value):
    """
    Desc:
        a function that adds a new attr to an object
    Args:
        obj (any): The object to add an attribute to
        att (str): The name of the attribute to add to obj
        value (any): The value of att
    Raises:
        TypeError: If the obj can't have a new attr
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)


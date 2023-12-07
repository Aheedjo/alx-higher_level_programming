#!/usr/bin/python3

"""
Desc:
    This function replaces or adds key/value in a dictionary.

Args:
    a_dictionary (dict): dictionary to be processed
    key: the key of the object to be replaced
    value: the value of the object to be replaced

Returns:
    dict: the resulting dict
"""


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return (a_dictionary)

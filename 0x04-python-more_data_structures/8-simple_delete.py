#!/usr/bin/python3

"""
Desc:
     A function that deletes a key in a dictionary.

Args:
    a_dictionary (dict): The dictionary to be processed
    key (str): key to be deleted

Returns:
    bool: New processed dict
"""


def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key):
        del a_dictionary[key]
    return (a_dictionary)

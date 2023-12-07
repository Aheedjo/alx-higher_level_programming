#!/usr/bin/python3

"""
Desc:
    a function that prints a dictionary by ordered keys.

Args:
    a_dictionary (dict): the dict to be processed

Returns:
    None
"""


def print_sorted_dictionary(a_dictionary):
    keys_view = list(a_dictionary.keys())
    sorted_view = sorted(keys_view)

    for i in range(len(sorted_view)):
        print(f"{sorted_view[i]}: {a_dictionary[sorted_view[i]]}")

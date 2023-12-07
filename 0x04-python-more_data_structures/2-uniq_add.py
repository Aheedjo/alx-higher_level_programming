#!/usr/bin/python3

"""
Desc:
     a function that adds all unique integers in a list.

Args:
    my_list (list): the list to be processed

Returns:
    bool: result of the summation of all unique elements
"""


def uniq_add(my_list=[]):
    new_set = set(my_list)
    result = 0
    for i in new_set:
        result += i

    return result

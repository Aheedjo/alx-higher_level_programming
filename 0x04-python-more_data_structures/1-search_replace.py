#!/usr/bin/python3

"""
Desc:
        a function that replaces all occurrences of an element by in a new list

Args:
    my_list (list): the list to be processed
    search: element to be searched for
    replace: element to be put in place of search

Returns:
    list: the processed list
"""


def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return new_list

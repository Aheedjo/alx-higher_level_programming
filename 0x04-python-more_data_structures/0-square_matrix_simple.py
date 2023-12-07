#!/usr/bin/python3

"""
Desc:
    a function that computes the square value of all ints of a matrix.

Args:
    matrix (list): 2d array

Returns:
    list: the resulting matrix
"""


def square_matrix_simple(matrix=[]):
    if matrix:
        result = []
        for array in matrix:
            list_array = []
            for element in array:
                list_array.append(element ** 2)
            result.append(list_array)
        return result

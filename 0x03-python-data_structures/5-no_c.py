#!/usr/bin/python3

def no_c(my_string):
    if my_string:
        result = ""
        for char in my_string:
            if char != 'c' and char != 'C':
                result += char
        return result
    return ""

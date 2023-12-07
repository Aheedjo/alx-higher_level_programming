#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:

        num = 0
        den = 0

        for tup in my_list:
            num += tup[0] * tup[1]
            den += tup[1]

        return (num / den)
    return 0

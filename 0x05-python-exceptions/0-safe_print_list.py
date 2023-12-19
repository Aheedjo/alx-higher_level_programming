#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for element in my_list[:x]:
            print(element, end="")
            count += 1
            el = my_list[count]
        return x
    except IndexError:
        return count
    finally:
        print()

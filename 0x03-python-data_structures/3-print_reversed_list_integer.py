#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    size = len(my_list)
    if (size != 0):
        while (size > 0):
            size = size - 1
            print("{:d}".format(my_list[size]))

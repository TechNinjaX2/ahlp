#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    size = len(my_list)
    if (idx > size):
        return my_list
    elif (idx < 0):
        return my_list
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list

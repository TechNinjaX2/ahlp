#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    size = len(my_list)
    if (idx > size - 1):
        return my_list
    elif (idx < 0):
        return my_list
    else:
        my_list[idx] = element
        return my_list

#!/usr/bin/python3
def no_c(my_string):
    idx = 0
    for i in my_string:
        if (i == 'C'):
            continue
        elif (i == 'c'):
            continue
        else:
            my_string[idx] = i
            idx = idx + 1
    return my_string

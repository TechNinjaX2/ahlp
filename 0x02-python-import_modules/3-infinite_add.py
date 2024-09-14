#!/usr/bin/python3
import sys
if __name__ == '__main__':
    index = 0
    array = {}
    for i in sys.argv:
        if (index == 0):
            index = index + 1
            continue
        else:
            array[index - 1] = i
            index = index + 1
    a = 0
    index = 0
    while (index != len(array)):
        a = a + int(array[index])
        index = index + 1
    print("{}".format(a))

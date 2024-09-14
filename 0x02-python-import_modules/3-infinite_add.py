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
            print("{}".format(array[index - 1]))
            index = index + 1
    a = 0
    index = 0
    for j in array[index]:
        print(f"{array[index]}")
        a = a + int(array[index])
        index = index + 1
    print("{}".format(array[2]))
    print("{}".format(a))

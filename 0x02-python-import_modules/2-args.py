#!/usr/bin/python3
import sys
if __name__ == '__main__':
    args = len(sys.argv)
    if (args == 1):
        print("0 arguments.")
    elif (args == 2):
        print("1 argument:")
        index = 0
        for i in sys.argv:
            if (index == 0):
                index = index + 1
                continue
            else:
                print("{}: {}".format(index, i))
    else:
        print("{} arguments:".format(args - 1))
        index = 0
        for i in sys.argv:
            if (index == 0):
                index = index + 1
                continue
            else:
                print("{}: {}".format(index, i))
                index = index + 1

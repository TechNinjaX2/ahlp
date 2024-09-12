#!/usr/bin/python3
def uppercase(str):
    for i in str:
        j = ord(i)
        if (j >= 97):
            if (j <= 123):
                k = j - 32
                print("{}".format(chr(k)), end="")
        else:
            print("{}".format(i), end="")
    print("")

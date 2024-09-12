#!/usr/bin/python3
def islower(c):
    if (ord(c) <= 127):
        if (ord(c) >= 97):
            return True
    else:
        return False

#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1, 10):
        if ((i * 10 + j) >= (j * 10 + i)):
            continue
        elif (i * 10 + j == 89):
            print(f"{i * 10 + j}")
        else:
            print(f"{i * 10 + j:02d}, ", end="")

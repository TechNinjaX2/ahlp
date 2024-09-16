#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    if (matrix == "\0"):
        print("")
    i = 0
    while (i < 3):
        j = 0
        while (j < 2):
            print("{} ".format(matrix[i][j]), end="")
            j = j + 1
        print("{}".format(matrix[i][j]))
        i = i + 1

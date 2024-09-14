#!/usr/bin/python3
import calculator_1 as calc
import sys
if __name__ == '__main__':
    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = sys.argv[1]
        b = sys.argv[3]
        if (sys.argv[2] == "+"):
            print("{} + {} = {}".format(a, b, calc.add(int(a), int(b))))
        elif (sys.argv[2] == "-"):
            print("{} - {} = {}".format(a, b, calc.sub(int(a), int(b))))
        elif (sys.argv[2] == "*"):
            print("{} * {} = {}".format(a, b, calc.mul(int(a), int(b))))
        elif (sys.argv[2] == "/"):
            print("{} / {} = {}".format(a, b, calc.div(int(a), int(b))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

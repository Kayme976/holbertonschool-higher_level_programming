#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
if __name__ == "__main__":
    if (add):
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    if (sub):
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    if (mul):
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    if (div):
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

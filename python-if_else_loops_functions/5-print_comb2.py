#!/usr/bin/python3
for k in range(100):
    if k == 99:
        print("{}".format(k))
    else:
        print("{:02d}, ".format(k), end='')

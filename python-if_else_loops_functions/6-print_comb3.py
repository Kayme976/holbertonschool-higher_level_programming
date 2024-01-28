#!/usr/bin/python3
k = 0
while (k < 9):
    a = 1 + k
    while (a < 10):
        if k == 8 and a == 9:
            print("{}{}".format(k, a))
        else:
            print("{}{}".format(k, a), end=',')
        a = a + 1
    k = k + 1

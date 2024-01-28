#!/usr/bin/python3
k = 0
while (k < 9):
    a = 1 + k
while (j < 10):
    for inc in range(num + 1, 10):
        if num == 8 and inc == 9:
            print("{}{}".format(num, inc))
        else:
            print("{}{}".format(num, inc), end=',')
        a = a + 1
    k = k + 1

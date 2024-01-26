#!/usr/bin/python3
for a in range(10):
    for inc in range(a + 1, 10):
        if a == 8 and inc == 9:
            print("{}{}".format(a, inc))
        else:
            print("{}{}".format(a, inc), end=',')

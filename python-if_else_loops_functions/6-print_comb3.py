#!/usr/bin/python3
for num in range(10):
    for inc in range(num + 1, 10):
        if num == 8 and inc == 9:
            print("{}{}".format(num, inc))
        else:
            print("{}{}".format(num, inc), end=',')

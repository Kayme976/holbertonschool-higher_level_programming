#!/usr/bin/python3
k = 0
while (i < 9):
    a = 1 + i
    while (j < 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{},".format(i, j), end='')
        j = j + 1
    i = i + 1

#!/usr/bin/python3
def uppercase(str):
    res = ""
    for char in str:
        j = ord(char)
        if 97 <= j <= 122:
            res += chr(j - 32)
        else:
            res += char
            print("{}".format(res))

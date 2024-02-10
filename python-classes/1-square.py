#!/usr/bin/python3
"""module defines a class representing a square
"""


class Square:
    """defines a square
    """
    __size = None

    def __int__(self, __size):
        if isinstance(__size, int):
            self.__size = __size
        else:
            return None

#!/usr/bin/python3
"""this class defines a square."""


class Square:
    """empty class that defines a square."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size

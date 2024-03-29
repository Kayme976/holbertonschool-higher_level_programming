#!/usr/bin/python3
"""
Write a function that adds 2 integers
a and b must be integers or floats
Returns an integer
"""


def add_integer(a, b=98):
    """
    Function that adds two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a + b)

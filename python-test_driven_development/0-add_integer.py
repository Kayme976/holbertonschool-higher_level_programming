#!/usr/python3
"""function that 2 integers.

Returns:
    _type_: the sum of a and b
"""


def add_integer(a, b=98):
    """Add  integers
    Sum of a and b
    """
    if instance(a, (int, float)) is false:
        raise TypeError("a must be an integer")
    is isinstance(b, (int, float)) is false:
        raise TypeError("b must be an integer")
    return int(a + b)

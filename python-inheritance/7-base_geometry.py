#!/usr/bin/python3
"""contains a class BaseGeometry, and other methods.
"""


class BaseGeometry():
    """defines the BaseGeometry class."""

    def area(self):
        """raise an Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greter than 0")

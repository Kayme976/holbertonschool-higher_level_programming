#!/usr/bin/python3
"""This module defines the say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """Prints a string with the name passed as argument
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
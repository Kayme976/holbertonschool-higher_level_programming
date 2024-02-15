#!/usr/bin/python3
"""defines an inherited list class MyList."""


class MyList(list):
    """implements sorted printing for built in list class."""

    def print_sorted(self):
        """print a list in sorted ascending order."""
        print(sorted(self))

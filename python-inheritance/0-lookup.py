#!/usr/bin/python3
"""defines an object attribute lookup function."""



def lookup(obj):
    """return a lis of an object's available attributes."""
    return (dir(obj))

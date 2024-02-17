#!/usr/bin/python3
"""rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class rectangle(BaseGeometry):
    """a class rectangle that inherits form BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

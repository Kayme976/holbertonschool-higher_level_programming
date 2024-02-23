#!/usr/bin/python3
"""Module for Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle width, height, x, y and id"""

        self.width = width
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.height = height
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.x = x
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.y = y
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)

    @property
    def width(self):
        """Get the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the horizontal position of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the horizontal position of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the vertical position of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the vertical position of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of a rectangle"""
        return self.__width*self.__height

    def display(self):
        """Prints a rectangle pattern with '#'"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" "*self.x, end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Return the rectangle description."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute"""

        for _ in args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]

        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'width' in kwargs:
            self.__width = kwargs['width']
        if 'height' in kwargs:
            self.__height = kwargs['height']
        if 'x' in kwargs:
            self.__x = kwargs['x']
        if 'y' in kwargs:
            self.__y = kwargs['y']

    def to_dictionary(self):
        """Return a dictionnary representation of a rectangle"""
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}

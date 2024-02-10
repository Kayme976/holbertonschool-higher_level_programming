#!/usr/bin/python3
"""square module

this module includes a class that defines a square and its size,
checks the validity of the value supplied, and provides getter and
seeter methods for manipulating them. it also includes a method
for calculating the area of the square, and another method for
displaying the square.
"""



class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Sets the necessary attributes for the Square object.

        Args:
            size (int): the size of one edge of the square.
            position (tuple): the coordinates of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """Get or set the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2 and \
                isinstance(value[0], int) and isinstance(value[1], int) and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the # character on stdout."""
        if self.__size > 0:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print()

#!/usr/bin/python3
"""importing rectangle for Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square that inherits of Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialiaze a square size."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the square description."""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width))

    @property
    def size(self):
        """Get the size of a square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the square size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute"""

        for _ in args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'size' in kwargs:
            self.size = kwargs['size']
        if 'x' in kwargs:
            self.x = kwargs['x']
        if 'y' in kwargs:
            self.y = kwargs['y']

    def to_dictionary(self):
        """Return a dictionnary representation of a rectangle"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

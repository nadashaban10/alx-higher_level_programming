#!/usr/bin/python3

"""Define a class """


class Square:

    def __init__(self, size=0):
        """Initialize a new square."""
        self._size = size  # Private instance attribute

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Calculate and return the current area of the square."""
        return self.size * self.size

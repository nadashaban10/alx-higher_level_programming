#!/usr/bin/python3

"""Define a class """


class Square:

    def __init__(self, size=0):
        """Initialize a new square."""
        self.__size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current area of the square."""
        return self.__size * self.__size

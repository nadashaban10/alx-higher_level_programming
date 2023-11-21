#!/usr/bin/python3

"""Define a class"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new one.

        Args:
            size (int): the size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """Return a square of area"""
            return (self.__size * self.__size)

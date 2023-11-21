#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(i < 0 for i in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """prints a # using size of"""

        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
                print("")

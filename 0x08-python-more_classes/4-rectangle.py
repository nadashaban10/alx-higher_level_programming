#!/usr/bin/python3

"""
Defines a class Rectangle
"""


class Rectangle:
    """Representation of Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes the width rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for priv instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the private instance attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter fot height priv inst"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError(" height must be >= 0")
        self.__height = value

    def area(self):
        """return the Area of rectanagle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        p = 2 * (self.__width + self.__height)
        return p

    def __str__(self):
        """return printed square based or h and w"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_printed = ""
        for i in range(self.height):
            for j in range(self.width):
                rectangle_printed = rectangle_printed + "#"
            rectangle_printed = rectangle_printed + "\n"
        return rectangle_printed

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

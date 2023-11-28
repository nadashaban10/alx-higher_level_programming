#!/usr/bin/python3

"""
Defines a class Rectangle
"""


class Rectangle:
    """Representation of Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the width rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
            return rect_2

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
        if self.width == 0 or self.height == 0:
            return ""

        rectangle_p = ""
        for i in range(self.height):
            for j in range(self.width):
                rectangle_p += Rectangle.print_symbol
            if i != self.height - 1:
                rectangle_p += "\n"

        return rectangle_p

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message for every deletion of a Rectangle.
    """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

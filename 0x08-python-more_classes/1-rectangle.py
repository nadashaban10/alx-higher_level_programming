#!/usr/bin/python3

"""
Define a Regtangle class with W and H
"""


class Rectangle:
    """Rrpresentation of Rectanagle class"""


def __init__(self, width=0, height=0):
    """initialzes the width rectangle"""
    self.width = width

    @property
    def width(self):
        """getter for priv instance"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")
        self__.width = value

        @property
        def height(self):
            """getter fot height priv inst"""
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError(" height must be >= 0")

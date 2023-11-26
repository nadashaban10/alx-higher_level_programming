#!/usr/bin/python3
"""define add_integer function."""


def add_integer(a, b=98):

    """Args: a,b integer or float numbers
    Return: sumtion of two integer
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """

    if (not isinstance(a, int) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return result

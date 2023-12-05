#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        '''function that raise exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validate the int values'''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name}must be greater than 0")

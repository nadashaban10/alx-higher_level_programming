#!/usr/bin/python3
""" define a class with a priv atrr """
class Square:
    """ represent the square """

    def __init__(self, size):
        """ initialize the Sqaure with size
            Args:
            size(int): priv attr size 
        """

        self.__size = size

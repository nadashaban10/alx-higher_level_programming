#!/usr/bin/python3

"""this is module that prints my name , with 2 str given"""
def say_my_name(first_name, last_name=""):
    """ funtion prints with 2 parameter


    Args:
        first_name: fisrt name to print.
        last_name: last name to print.

    Return:
        void , full name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}" .format(first_name, last_name))

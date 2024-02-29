#!/usr/bin/python3
""" Test function find_peak """


def find_peak(list_of_integers):
    """ Test function find_peak """
    if not list_of_integers:
        return None
    return max(list_of_integers)

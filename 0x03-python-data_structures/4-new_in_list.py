#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    range_list = len(my_list) - 1
    if idx < 0:
        return my_list.copy()
    if idx > range_list:
        return my_list.copy()
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
        return my_list

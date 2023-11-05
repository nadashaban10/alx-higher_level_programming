#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    x = len(my_list)
    if idx < 0:
        return " none"
    if idx > x - 1:
        return "none"
    else:
        my_list[idx] = element
        return my_list

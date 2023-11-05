#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    range_list = len(my_list) - 1
    if idx < 0:
        return my_list.copy()
    if idx > range_list:
        return my_list.copy()
    else:
        my_list[idx] = element
        return my_list
    

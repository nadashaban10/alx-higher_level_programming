#!/usr/bin/python3
def element_at(my_list, idx):
    x = len(my_list)
    if idx < 0:
        return " none"
    if idx > x - 1:
        return 'none'
    else:
        return my_list[idx]

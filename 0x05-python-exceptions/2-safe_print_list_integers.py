#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    printed_element = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed_element = printed_element + 1
        except (ValueError, TypeError):
            continue
    print("")
    return (printed_element)

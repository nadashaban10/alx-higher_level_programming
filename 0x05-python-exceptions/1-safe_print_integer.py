#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)) + "\n")
        return True
    except (ValueError, IndexError):
        return False

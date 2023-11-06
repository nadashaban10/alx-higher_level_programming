#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for cln in row:
            print("{:d}" .format(cln), end=" " if cln != row[-1] else "")
        print()

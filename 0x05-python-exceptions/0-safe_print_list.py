#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num_printed = 0
        for i, element in enumerate(my_list):
            if i < x:
                print(element, end=" ")
                num_printed += 1
            else:
                break
        print()
        return num_printed
    except Exception as e:
        print("Error occurred:", e)
        return 0

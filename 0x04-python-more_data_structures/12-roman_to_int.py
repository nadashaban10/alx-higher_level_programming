#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_value = 0
    i = 0

    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_dict[roman_string[i:i + 2]] > roman_dict[roman_string[i]]:
            int_value -= roman_dict[roman_string[i:i + 2]]
            i += 2
        else:
            int_value += roman_dict[roman_string[i]]
            i += 1

    
    if int_value < 1 or int_value > 3999:
        return 0

    return int_value

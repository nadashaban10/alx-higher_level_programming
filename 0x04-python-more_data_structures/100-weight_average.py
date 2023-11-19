#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total_score = 0
    total_weight = 0
    for tupl  in my_list:
        total_score += tupl[0] * tupl[1]
        total_weight += tupl[1]
        av = total_score / total_weight
        return av

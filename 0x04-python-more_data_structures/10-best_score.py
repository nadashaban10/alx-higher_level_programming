#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        list_dic = list(a_dictionary.keys())
        max_value = 0
        leader = ""
        for i in list_dic:
            if a_dictionary[i] > max_value:
                max_value = a_dictionary[i]
                leader = i
        return leader

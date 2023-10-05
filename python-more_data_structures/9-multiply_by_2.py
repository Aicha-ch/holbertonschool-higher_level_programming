#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for key, value in a_dictionary.items():
        if value % 2 == 0:
            new_dic[key] = value
    return (new_dic)

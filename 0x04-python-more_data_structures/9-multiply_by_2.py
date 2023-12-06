#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nw_dict = dict()
    for i, j in a_dictionary.items():
        nw_dict[i] = j*2
    return nw_dict

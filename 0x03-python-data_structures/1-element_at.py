#!/usr/bin/python3
def element_at(my_list, idx):
    if 0 <= idx < len(my_list) :
        print("Element at index {:d} is {}".format(idx, my_list[idx]))
    else :
        return None

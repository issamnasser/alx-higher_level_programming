#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    t_f = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            t_f.append(True)
        else:
            t_f.append(False)
    return t_f

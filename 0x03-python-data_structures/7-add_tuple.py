#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    tpl1 = tuple_a + (0, 0)
    tpl2 = tuple_b + (0, 0)
    tuple_c = tpl1[0] + tpl2[0], tpl1[1] + tpl2[1]
    return tuple_c

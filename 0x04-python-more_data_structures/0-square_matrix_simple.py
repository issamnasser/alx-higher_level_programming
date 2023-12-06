#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = []
    for i in matrix:
        sq_list = list(map(lambda x: x**2, i))
        sq_matrix.append(sq_list)
    return sq_matrix

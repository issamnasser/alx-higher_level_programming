#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = []
    sq = lambda x: x**2
    for i in matrix:
        sq_list = list(map(sq, i))
        sq_matrix.append(sq_list)
    return sq_matrix

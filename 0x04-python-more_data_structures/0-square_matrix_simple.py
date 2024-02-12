#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """ To compute the squares values of all integer in matrix"""
    new_matrix = [[x ** 2 for x in row] for row in matrix]
    return new_matrix

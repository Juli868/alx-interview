#!/usr/bin/python3
"""Rotate a matrix."""


def rotate_2d_matrix(matrix):
    """Rotate the matrix 90 clokwise."""
    result = [[]]
    column = 0
    row = 0
    length = len(matrix)
    for i in range(length):
        result.append([])
    for i in range(length):
        for j in range(length):
            result[i].insert(0,matrix[j].pop(0))
    matrix = result

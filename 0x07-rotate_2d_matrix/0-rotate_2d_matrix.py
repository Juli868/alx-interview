#!/usr/bin/python3
"""Rotate a matrix."""


def rotate_2d_matrix(matrix):
    """Rotate the matrix 90 clokwise."""
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

#!/usr/bin/python3
"""Matrix divided"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix"""
    if not isinstance(div, (int, float)) or div is None:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    error = "matrix must be a matrix (list of lists) of integers/floats"
    size = None
    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix

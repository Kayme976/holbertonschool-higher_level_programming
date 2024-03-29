#!/usr/bin/python3
"""This module defines the matrix_divided function"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix."""
    if isinstance(matrix, list) is False:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if all(isinstance(i, list) and len(i) != 0 for i in matrix) is False:
        raise TypeError("Each row of the matrix must have the same size")
    if all(len(row) == len(matrix[0]) for row in matrix) is False:
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    matrix1 = [row[:] for row in matrix]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            if isinstance(matrix1[i][j], (int, float)) is False:
                raise TypeError(
                    "matrix must be a matrix \
(list of lists) of integers/floats")
            matrix1[i][j] = round(matrix1[i][j]/div, 2)

    return matrix1
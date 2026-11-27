#!/usr/bin/python3
"""Module that defines a matrix division function.

Provides matrix_divided which validates a rectangular matrix of numbers
and divides every element by a non-zero divisor rounded to 2 decimals.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimals."""
    msg_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) and len(row) > 0 for row in matrix)):
        raise TypeError(msg_matrix)
    for row in matrix:
        if not all(type(el) in (int, float) for el in row):
            raise TypeError(msg_matrix)
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(el / div, 2) for el in row] for row in matrix]

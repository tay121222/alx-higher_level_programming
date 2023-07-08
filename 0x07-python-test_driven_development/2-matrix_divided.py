#!/usr/bin/python3
"""Contains function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
            if len(row) != row_size:
                raise TypeError
                ("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]

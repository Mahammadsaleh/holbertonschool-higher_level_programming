#!/usr/bin/python3
"""2-matrix_divided.py and tests/2-matrix_divided.txt"""


def matrix_divided(matrix, div):
    """
    divides matrix elements
    """
    new_matrix = [row[:] for row in matrix]
    row_set = set()
    index = 0
    error = 'matrix must be a matrix (list of lists) of integers/floats'
    if not isinstance(matrix, (list)):
        raise TypeError(error)
    if div == 0 or div == 0.0:
        raise ZeroDivisionError('division by zero')
    for row in matrix:
        j = 0
        row_set.add(len(row))
        if len(row_set) > 1:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error)
            if not isinstance(div, (int, float)):
                raise TypeError('div must be a number')
            rounded_div = round(element / div, 2)
            new_matrix[index][j] = rounded_div
            j += 1
        index += 1
    return new_matrix

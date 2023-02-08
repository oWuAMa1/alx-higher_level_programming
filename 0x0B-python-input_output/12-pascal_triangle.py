#!/usr/bin/python3
"""pascal_triangle

"""


def pascal_triangle(n):
    """ends of each list in the matrix are summed to display the next list

    until the middle of the list. The number '1' is always at both ends.

    """

    matrix = []

    if n <= 0:

        return(matrix)

    for i in range(n):

        matrix.append([])

        matrix[i].append(1)

        for j in range(1, i):

            matrix[i].append(matrix[i - 1][j - 1] + matrix[i - 1][j])

        if (i != 0):

            matrix[i].append(1)

    return(matrix)

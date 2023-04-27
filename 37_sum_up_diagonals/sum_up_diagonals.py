def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    # Get the length of the matrix
    n = len(matrix)

    # Initialize the sum of the diagonals to 0
    diagonal_sum = 0

    # Add the elements in the top-left to bottom-right diagonal
    for i in range(n):
        diagonal_sum += matrix[i][i]

    # Add the elements in the bottom-left to top-right diagonal
    for i in range(n):
        diagonal_sum += matrix[i][n - i - 1]

    return diagonal_sum
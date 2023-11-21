def sum_up_diagonals(matrix):
    n = len(matrix)
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += matrix[i][i] 
        diagonal_sum += matrix[i][n - 1 - i] 
    
    if n % 2 ==1:
        diagonal_sum -= matrix[n//2][n//2]
    return diagonal_sum

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
from sympy import Matrix, sympify
from typing import List

def matrix_to_string_list(matrix: Matrix) -> List[str]:
    return [" ".join(str(cell.evalf()) if cell.is_Float else str(cell) for cell in row)
            for row in matrix.tolist()]

def string_list_to_matrix(data: List[str]) -> Matrix:
    rows = [[sympify(cell) for cell in row.split()] for row in data]
    return Matrix(rows)

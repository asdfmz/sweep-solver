from sympy import Matrix, sympify
from typing import List

def matrix_to_json_serializable(matrix: Matrix) -> List[List[str]]:
    return [
        [str(cell.evalf()) if cell.is_Float else str(cell) for cell in row]
        for row in matrix.tolist()
    ]

def matrix_from_json_serializable(data: List[List[str]]) -> Matrix:
    rows = [[sympify(cell) for cell in row] for row in data]
    return Matrix(rows)

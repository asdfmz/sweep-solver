from sympy import Matrix
from typing import List, Tuple
from models.query import Query, OperationType
from services.row_operations import apply_and_simplify


def gaussian_elimination_steps(matrix: Matrix) -> List[Tuple[Matrix, Query]]:
    steps: List[Tuple[Matrix, Query]] = []
    m = matrix.copy()
    rows, cols = m.rows, m.cols
    pivot_row = 0

    for col in range(cols):
        # Step 1: Find a non-zero pivot and swap
        pivot_found = False
        for r in range(pivot_row, rows):
            if m[r, col] != 0:
                if r != pivot_row:
                    q_swap = Query(OperationType.SWAP, pivot_row, "1", r)
                    m = apply_and_simplify(m, q_swap)
                    steps.append((m.copy(), q_swap))
                pivot_found = True
                break

        if not pivot_found:
            continue

        # Step 2: Normalize pivot row
        pivot_val = m[pivot_row, col]
        if pivot_val != 1:
            q_norm = Query(OperationType.MULTIPLY, pivot_row, f"1/({pivot_val})")
            m = apply_and_simplify(m, q_norm)
            steps.append((m.copy(), q_norm))

        # Step 3: Eliminate below
        for r in range(pivot_row + 1, rows):
            if m[r, col] != 0:
                factor = f"-{m[r, col]}"
                q_elim = Query(OperationType.ADD, r, factor, pivot_row)
                m = apply_and_simplify(m, q_elim)
                steps.append((m.copy(), q_elim))

        pivot_row += 1
        if pivot_row >= rows:
            break

    return steps

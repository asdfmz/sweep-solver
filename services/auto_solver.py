from sympy import Matrix
from typing import List, Tuple
from models.query import Query, OperationType
from services.row_operations import apply_and_simplify


def gaussian_elimination_steps(matrix: Matrix) -> List[Tuple[Matrix, Query]]:
    m = matrix.copy()
    rows, cols = m.shape
    steps = []
    pivot_row = 0

    for col in range(cols):
        # ピボット選択
        pivot = None
        for row in range(pivot_row, rows):
            if m[row, col] != 0:
                pivot = row
                break

        if pivot is None:
            continue

        # 行を入れ替え
        if pivot != pivot_row:
            q = Query(OperationType.SWAP, pivot_row, "1", pivot)
            m = apply_and_simplify(m, q)
            steps.append((m.copy(), q))

        # ピボットを1に正規化
        if m[pivot_row, col] != 1:
            factor = f"1/({m[pivot_row, col]})"
            q = Query(OperationType.MULTIPLY, pivot_row, factor)
            m = apply_and_simplify(m, q)
            steps.append((m.copy(), q))

        # 下を0に
        for row in range(pivot_row + 1, rows):
            if m[row, col] != 0:
                factor = f"-{m[row, col]}"
                q = Query(OperationType.ADD, row, factor, pivot_row)
                m = apply_and_simplify(m, q)
                steps.append((m.copy(), q))

        pivot_row += 1

    # 後退消去（上を0に）
    for col in reversed(range(cols)):
        # ピボット行を探す
        pivot_r = None
        for r in range(rows):
            if m[r, col] == 1 and all(m[r, c] == 0 for c in range(col)):
                pivot_r = r
                break

        if pivot_r is None:
            continue

        # 上を0に
        for r in range(0, pivot_r):
            if m[r, col] != 0:
                factor = f"-{m[r, col]}"
                q = Query(OperationType.ADD, r, factor, pivot_r)
                m = apply_and_simplify(m, q)
                steps.append((m.copy(), q))

    return steps

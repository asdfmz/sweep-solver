from sympy import Matrix, simplify
from models.query import Query, OperationType


def apply_and_simplify(matrix: Matrix, query: Query) -> Matrix:
    m = matrix.copy()
    t = query.target
    f = simplify(query.factor)
    r = query.other

    if query.op == OperationType.MULTIPLY:
        m.row_op(t, lambda v, _: f * v)

    elif query.op == OperationType.ADD:
        if r is None:
            raise ValueError("ADD operation requires another row index.")
        m.row_op(t, lambda v, j: v + f * m[r, j])

    elif query.op == OperationType.SWAP:
        if r is None:
            raise ValueError("SWAP operation requires another row index.")
        m.row_swap(t, r)

    else:
        raise ValueError(f"Unsupported operation: {query.op}")

    return m.applyfunc(simplify)

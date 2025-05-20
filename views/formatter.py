from models.query import Query, OperationType
from sympy import Matrix


class QueryFormatter:
    @staticmethod
    def to_latex(query: Query) -> str:
        t = query.target + 1  # 1-indexed表示
        if query.op == OperationType.MULTIPLY:
            return f"R_{{{t}}} \\to {query.factor} R_{{{t}}}"
        elif query.op == OperationType.ADD:
            r = query.other + 1
            return f"R_{{{t}}} \\to R_{{{t}}} + {query.factor} R_{{{r}}}"
        elif query.op == OperationType.SWAP:
            r = query.other + 1
            return f"R_{{{t}}} \\leftrightarrow R_{{{r}}}"
        return ""

    @staticmethod
    def to_human(query: Query) -> str:
        t = query.target + 1
        if query.op == OperationType.MULTIPLY:
            return f"{t}行目を{query.factor}倍する"
        elif query.op == OperationType.ADD:
            r = query.other + 1
            return f"{t}行目に{query.factor}倍した{r}行目を加える"
        elif query.op == OperationType.SWAP:
            r = query.other + 1
            return f"{t}行目と{r}行目を入れ替える"
        return ""

class MatrixFormatter:
    @staticmethod
    def to_latex(matrix: Matrix) -> str:
        return "\\begin{bmatrix}" + " \\\\ ".join(
            [" & ".join(map(str, row)) for row in matrix.tolist()]
        ) + "\\end{bmatrix}"

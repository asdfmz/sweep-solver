from models.query import Query, OperationType
from sympy import Matrix, latex, sympify


class QueryFormatter:
    @staticmethod
    def to_latex(query: Query) -> str:
        t = query.target
        if query.op == OperationType.MULTIPLY:
            factor_latex = latex(sympify(query.factor))
            return f"R_{{{t}}} \\leftarrow {factor_latex} R_{{{t}}}"
        elif query.op == OperationType.ADD:
            r = query.other
            factor_latex = latex(sympify(query.factor))
            return f"R_{{{t}}} \\leftarrow R_{{{t}}} + {factor_latex} R_{{{r}}}"
        elif query.op == OperationType.SWAP:
            r = query.other
            return f"R_{{{t}}} \\leftrightarrow R_{{{r}}}"
        return ""

    @staticmethod
    def to_human(query: Query) -> str:
        t = query.target
        if query.op == OperationType.MULTIPLY:
            return f"{t}行目を{query.factor}倍する"
        elif query.op == OperationType.ADD:
            r = query.other
            return f"{t}行目に{query.factor}倍した{r}行目を加える"
        elif query.op == OperationType.SWAP:
            r = query.other
            return f"{t}行目と{r}行目を入れ替える"
        return ""

class MatrixFormatter:
    @staticmethod
    def to_latex(matrix: Matrix) -> str:
        return latex(matrix, mode="equation")
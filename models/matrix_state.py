from sympy import Matrix
from typing import Optional
from models.query import Query
from utils import sympy_codec


class MatrixState:
    def __init__(self, matrix: Matrix, query: Optional[Query] = None):
        self.matrix = matrix
        self.query = query

    def to_dict(self) -> dict:
        return {
            "matrix": sympy_codec.matrix_to_string_list(self.matrix),
            "query": self.query.to_dict() if self.query else None
        }

    @classmethod
    def from_dict(cls, data: dict) -> "MatrixState":
        matrix = sympy_codec.string_list_to_matrix(data["matrix"])
        query = Query.from_dict(data["query"]) if data["query"] else None
        return cls(matrix, query)

    def __eq__(self, other):
        return (
            isinstance(other, MatrixState)
            and self.matrix.equals(other.matrix)
            and self.query == other.query
        )

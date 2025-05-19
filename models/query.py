from enum import Enum
from typing import Optional
from sympy import Matrix, eye, sympify


class OperationType(Enum):
    MULTIPLY = "m"
    ADD = "a"
    SWAP = "s"


class Query:
    def __init__(self, op: OperationType, target: int, factor: str, other: Optional[int] = None):
        self.op = op
        self.target = target
        self.factor = factor
        self.other = other

    @classmethod
    def from_dict(cls, d: dict) -> "Query":
        r_raw = d.get("r", "")
        r_str = str(r_raw).strip()
        return cls(
            OperationType(d["o"]),
            int(d["t"]),
            d["f"],
            int(r_str) if r_str else None
        )

    def to_dict(self) -> dict:
        return {
            "o": self.op.value,
            "t": str(self.target),
            "f": self.factor,
            "r": str(self.other) if self.other is not None else ""
        }

    def to_elementary_matrix(self, size: int) -> Matrix:
        E = eye(size)
        i = self.target
        if self.op == OperationType.MULTIPLY:
            E[i, i] = sympify(self.factor)
        elif self.op == OperationType.ADD:
            j = self.other
            E[i, j] = sympify(self.factor)
        elif self.op == OperationType.SWAP:
            j = self.other
            E.row_swap(i, j)
        return E

    def __eq__(self, other):
        return (
            isinstance(other, Query)
            and self.op == other.op
            and self.target == other.target
            and self.factor == other.factor
            and self.other == other.other
        )

    def __repr__(self):
        return f"Query({self.op}, target={self.target}, factor='{self.factor}', other={self.other})"

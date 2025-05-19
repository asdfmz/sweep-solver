import pytest
from sympy import Matrix
from services.row_operations import apply_and_simplify
from models.query import Query, OperationType


def test_multiply_row():
    mat = Matrix([[1, 2], [3, 4]])
    q = Query(OperationType.MULTIPLY, target=0, factor="2")
    result = apply_and_simplify(mat, q)
    expected = Matrix([[2, 4], [3, 4]])
    assert result == expected


def test_add_row():
    mat = Matrix([[1, 2], [3, 4]])
    q = Query(OperationType.ADD, target=1, factor="-1", other=0)
    result = apply_and_simplify(mat, q)
    expected = Matrix([[1, 2], [2, 2]])
    assert result == expected


def test_swap_rows():
    mat = Matrix([[1, 2], [3, 4]])
    q = Query(OperationType.SWAP, target=0, factor="1", other=1)
    result = apply_and_simplify(mat, q)
    expected = Matrix([[3, 4], [1, 2]])
    assert result == expected


def test_add_without_other_raises():
    mat = Matrix([[1, 2], [3, 4]])
    q = Query(OperationType.ADD, target=1, factor="1", other=None)
    with pytest.raises(ValueError):
        apply_and_simplify(mat, q)


def test_swap_without_other_raises():
    mat = Matrix([[1, 2], [3, 4]])
    q = Query(OperationType.SWAP, target=0, factor="1", other=None)
    with pytest.raises(ValueError):
        apply_and_simplify(mat, q)

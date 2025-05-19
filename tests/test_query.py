import pytest
from sympy import Matrix, eye
from models.query import Query, OperationType

def test_from_dict_and_to_dict_roundtrip():
    data = {"o": "a", "t": "1", "f": "2", "r": "0"}
    q = Query.from_dict(data)
    assert q.op == OperationType.ADD
    assert q.target == 1
    assert q.factor == "2"
    assert q.other == 0
    assert q.to_dict() == data 

def test_to_elementary_matrix_multiply():
    q = Query(OperationType.MULTIPLY, target=2, factor="3")
    E = q.to_elementary_matrix(4)
    expected = eye(4)
    expected[2, 2] = 3
    assert E == expected

def test_to_elementary_matrix_add():
    q = Query(OperationType.ADD, target=1, factor="-2", other=0)
    E = q.to_elementary_matrix(3)
    expected = eye(3)
    expected[1, 0] = -2
    assert E == expected

def test_to_elementary_matrix_swap():
    q = Query(OperationType.SWAP, target=0, factor="1", other=2)
    E = q.to_elementary_matrix(3)
    expected = eye(3)
    expected.row_swap(0, 2)
    assert E == expected

def test_query_equality():
    q1 = Query(OperationType.ADD, 1, "2", 0)
    q2 = Query(OperationType.ADD, 1, "2", 0)
    q3 = Query(OperationType.SWAP, 1, "2", 0)
    assert q1 == q2
    assert q1 != q3

def test_from_dict_handles_empty_r():
    data = {"o": "s", "t": 0, "f": "1", "r": ""}
    q = Query.from_dict(data)
    assert q.op == OperationType.SWAP
    assert q.other is None
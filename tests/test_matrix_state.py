from sympy import Matrix
from models.matrix_state import MatrixState
from models.query import Query, OperationType


def test_to_dict_and_from_dict_roundtrip():
    matrix = Matrix([[1, 2], [3, 4]])
    query = Query(OperationType.ADD, target=1, factor="2", other=0)
    state = MatrixState(matrix, query)
    
    data = state.to_dict()
    restored = MatrixState.from_dict(data)
    
    assert restored == state


def test_to_dict_and_from_dict_with_none_query():
    matrix = Matrix([[1, 0], [0, 1]])
    state = MatrixState(matrix, None)
    
    data = state.to_dict()
    restored = MatrixState.from_dict(data)
    
    assert restored == state
    assert restored.query is None

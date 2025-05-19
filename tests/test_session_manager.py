import pytest
from sympy import Matrix
from models.query import Query, OperationType
from models.matrix_state import MatrixState
from models.session_manager import SessionManager


def make_state(val: int) -> MatrixState:
    matrix = Matrix([[val]])
    query = Query(OperationType.MULTIPLY, target=0, factor=str(val))
    return MatrixState(matrix, query)


def test_push_and_current():
    sm = SessionManager([make_state(1)], current_step=0)
    new_matrix = Matrix([[2]])
    new_query = Query(OperationType.ADD, 0, "3", 0)
    sm.push(new_matrix, new_query)

    assert sm.current().matrix == Matrix([[2]])
    assert sm.current().query == new_query
    assert len(sm.history) == 2


def test_jump_to_valid_index():
    sm = SessionManager([make_state(1), make_state(2), make_state(3)], current_step=0)
    sm.jump_to(2)
    assert sm.current().matrix == Matrix([[3]])
    assert sm.current().query.factor == "3"


def test_jump_to_invalid_index_raises():
    sm = SessionManager([make_state(1), make_state(2)], current_step=0)
    with pytest.raises(IndexError):
        sm.jump_to(5)


def test_to_session_and_from_session_roundtrip():
    original = SessionManager(
        [make_state(10), make_state(20), make_state(30)],
        current_step=1
    )
    session_data = original.to_session()
    restored = SessionManager.from_session(session_data)
    assert restored.current_step == 1
    assert restored.history[1].matrix == Matrix([[20]])
    assert restored == original


def test_branching_truncates_future():
    # 初期履歴3ステップ
    sm = SessionManager([make_state(1), make_state(2), make_state(3)], current_step=1)

    # push（2番目から分岐）→ 未来（3番目）は切り捨てられるはず
    new_matrix = Matrix([[99]])
    new_query = Query(OperationType.ADD, 0, "1", 0)
    sm.push(new_matrix, new_query)

    # 履歴の長さは3になる（0, 1, 新たな2）
    assert len(sm.history) == 3
    assert sm.current_step == 2
    assert sm.history[2].matrix == Matrix([[99]])
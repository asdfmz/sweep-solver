from sympy import Matrix
from models.query import Query, OperationType
from models.matrix_state import MatrixState
from models.session_manager import SessionManager
from views.history_view_model import MatrixHistoryViewModel


def test_view_model_structure_and_content():
    history = [
        MatrixState(Matrix([[1, 0], [0, 1]]), None),
        MatrixState(Matrix([[2, 0], [0, 1]]), Query(OperationType.MULTIPLY, 0, "2")),
        MatrixState(Matrix([[2, 0], [0, 2]]), Query(OperationType.MULTIPLY, 1, "2")),
    ]
    session = SessionManager(history, current_step=2)
    view = MatrixHistoryViewModel(session)
    data = view.to_dict()

    # 検証
    assert data["current_step"] == 2
    assert len(data["entries"]) == 3
    assert data["entries"][2]["is_current"]
    assert data["entries"][0]["query_latex"] is None
    assert data["entries"][1]["query_human"] == "1行目を2倍する"
    assert data["entries"][2]["query_latex"] == "R_{2} \\to 2 R_{2}"

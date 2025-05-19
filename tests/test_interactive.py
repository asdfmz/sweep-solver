import pytest
from flask import Flask
from app import app as flask_app
from models.query import Query, OperationType
from models.session_manager import SessionManager
from models.matrix_state import MatrixState
from sympy import Matrix


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        with flask_app.app_context():
            yield client


def init_session(client, matrix):
    session_manager = SessionManager([MatrixState(matrix)], 0)
    with client.session_transaction() as sess:
        sess["m"] = session_manager.to_session()


def test_index_route(client):
    q = Query(OperationType.ADD, target=1, factor="2", other=0)
    s = SessionManager([MatrixState(Matrix([[1, 2], [3, 4]]), q)], 0)
    with client.session_transaction() as sess:
        sess["m"] = s.to_session()
    response = client.get("/")
    text = response.data.decode("utf-8")
    assert response.status_code == 200
    assert "行目" in text or "R_" in text  # latex or human-readable


def test_apply_route(client):
    q = Query(OperationType.ADD, target=1, factor="2", other=0)
    s = SessionManager([MatrixState(Matrix([[1, 2], [3, 4]]), q)], 0)
    with client.session_transaction() as sess:
        sess["m"] = s.to_session()
    response = client.post("/apply", data={
        "o": "m", "t": 0, "f": "2", "r": ""
    }, follow_redirects=True)
    text = response.data.decode("utf-8")
    assert response.status_code == 200
    assert "2倍" in text or "2 R_{" in text


def test_auto_route(client):
    q = Query(OperationType.ADD, target=1, factor="2", other=0)
    s = SessionManager([MatrixState(Matrix([[2, 3], [1, 4]]), q)], 0)
    with client.session_transaction() as sess:
        sess["m"] = s.to_session()
    response = client.post("/auto", follow_redirects=True)
    text = response.data.decode("utf-8")
    assert response.status_code == 200
    assert "R_" in text  # latex present
    assert "加える" in text or b"\\to" in text


def test_jump_route(client):
    m1 = Matrix([[1, 0], [0, 1]])
    m2 = Matrix([[2, 0], [0, 1]])
    sm = SessionManager([MatrixState(m1), MatrixState(m2)], 0)
    with client.session_transaction() as sess:
        sess["m"] = sm.to_session()

    response = client.get("/jump/1", follow_redirects=True)
    text = response.data.decode("utf-8")
    assert response.status_code == 200
    assert "2" in text or "2倍" in text

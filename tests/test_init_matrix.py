import pytest
from sympy import Matrix
from app import app as flask_app
from models.session_manager import SessionManager


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        with flask_app.app_context():
            yield client


def test_size_form_display(client):
    response = client.get("/init/size")
    assert response.status_code == 200
    assert "行列サイズの指定" in response.data.decode("utf-8")


def test_input_form_display(client):
    response = client.post("/init/input", data={"rows": "2", "cols": "3"})
    assert response.status_code == 200
    html = response.data.decode("utf-8")
    assert "行列の値を入力" in html
    assert "cell_0_0" in html
    assert "cell_1_2" in html


def test_start_session_initializes(client):
    # Step 1: input form post with a valid 2x2 matrix
    form_data = {
        "rows": "2",
        "cols": "2",
        "cell_0_0": "1",
        "cell_0_1": "2",
        "cell_1_0": "3",
        "cell_1_1": "4"
    }
    response = client.post("/init/start", data=form_data, follow_redirects=True)
    assert response.status_code == 200

    with client.session_transaction() as sess:
        assert "m" in sess
        manager = SessionManager.from_session(sess["m"])
        matrix = manager.current().matrix
        assert matrix == Matrix([[1, 2], [3, 4]])

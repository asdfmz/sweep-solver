from flask import Blueprint, request, session, redirect, render_template, url_for
from sympy import Matrix
from models.matrix_state import MatrixState
from models.session_manager import SessionManager
from utils.sympy_codec import matrix_from_json_serializable

bp = Blueprint("init_matrix", __name__)

@bp.route("/")
def index_redirect():
    return redirect(url_for("init_matrix.size_form"))

@bp.route("/size", methods=["GET"])
def size_form():
    return render_template("matrix_size.html")


@bp.route("/input", methods=["POST"])
def input_form():
    try:
        rows = int(request.form["rows"])
        cols = int(request.form["cols"])
        if not (1 <= rows <= 10 and 1 <= cols <= 10):
            raise ValueError("size out of range")
    except Exception:
        return redirect(url_for("init_matrix.size_form"))

    return render_template("matrix_input.html", rows=rows, cols=cols)


@bp.route("/start", methods=["POST"])
def start_session():
    try:
        rows = int(request.form["rows"])
        cols = int(request.form["cols"])
        data = []

        for i in range(rows):
            row = []
            for j in range(cols):
                cell = request.form.get(f"cell_{i}_{j}", "0")
                row.append(cell.strip())
            data.append(row)  # ← 行をそのままappend（空白結合しない）

        matrix = matrix_from_json_serializable(data)
        manager = SessionManager([MatrixState(matrix)], 0)
        session["m"] = manager.to_session()

        return redirect(url_for("interactive.index"))

    except Exception:
        return redirect(url_for("init_matrix.size_form"))


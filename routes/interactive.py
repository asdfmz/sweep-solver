from flask import Blueprint, request, session, redirect, render_template, url_for
from sympy import Matrix
from models.query import Query
from models.session_manager import SessionManager
from services.query_normalizer import from_ui_indexed
from services.row_operations import apply_and_simplify
from services.auto_solver import gaussian_elimination_steps
from views.history_view_model import MatrixHistoryViewModel
import config

bp = Blueprint("interactive", __name__)


@bp.route("/")
def index():
    manager = SessionManager.from_session(session["m"])
    view = MatrixHistoryViewModel(manager)

    # 現在の行列の行数を取得（例：3行×4列なら 3）
    current_matrix = view.entries[view.current_index]["matrix"]
    row_count = len(current_matrix)

    return render_template(
        "interactive.html",
        view=view.to_dict(),
        config=config,
        max_index=row_count - 1
    )


@bp.route("/apply", methods=["POST"])
def apply():
    manager = SessionManager.from_session(session["m"])
    query = Query.from_dict(request.form)
    query = from_ui_indexed(query)
    matrix = manager.current().matrix
    result = apply_and_simplify(matrix, query)
    manager.push(result, query)
    session["m"] = manager.to_session()
    return redirect(url_for("interactive.index"))


@bp.route("/auto", methods=["POST"])
def auto():
    manager = SessionManager.from_session(session["m"])
    initial_matrix = manager.current().matrix
    steps = gaussian_elimination_steps(initial_matrix)
    for matrix, query in steps:
        manager.push(matrix, query)
    session["m"] = manager.to_session()
    return redirect(url_for("interactive.index"))


@bp.route("/jump/<int:step>")
def jump(step):
    manager = SessionManager.from_session(session["m"])
    manager.jump_to(step)
    session["m"] = manager.to_session()
    return redirect(url_for("interactive.index"))

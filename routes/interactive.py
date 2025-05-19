from flask import Blueprint, request, session, redirect, render_template, url_for
from sympy import Matrix
from models.query import Query
from models.session_manager import SessionManager
from services.row_operations import apply_and_simplify
from services.auto_solver import gaussian_elimination_steps
from views.history_view_model import MatrixHistoryViewModel

bp = Blueprint("interactive", __name__)


@bp.route("/")
def index():
    manager = SessionManager.from_session(session["m"])
    view = MatrixHistoryViewModel(manager)
    return render_template("interactive.html", view=view.to_dict())


@bp.route("/apply", methods=["POST"])
def apply():
    manager = SessionManager.from_session(session["m"])
    query = Query.from_dict(request.form)
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

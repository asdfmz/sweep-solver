from flask import Blueprint, redirect, url_for

bp = Blueprint("main", __name__)

@bp.route("/")
def root_redirect():
    return redirect(url_for("init_matrix.size_form"))

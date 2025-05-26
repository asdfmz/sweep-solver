from flask import Blueprint, render_template, redirect, url_for

bp = Blueprint("main", __name__)

@bp.route("/")
def root_redirect():
    return render_template("index.html")

from flask import render_template
from flask.blueprints import Blueprint

bp = Blueprint("default", __name__)


@bp.route('/')
def main():
    return render_template("main.html")

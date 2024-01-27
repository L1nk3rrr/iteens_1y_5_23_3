from flask import Blueprint, render_template
from sqlalchemy import select

from app.database import Session
from app.models import Post


bp = Blueprint("default", __name__)


@bp.route("/index")
@bp.route("/")
def index():
    with Session() as session:
        query = select(Post)
        posts = session.scalars(query).all()
    return render_template("main.html", posts=posts)

# https://openweathermap.org/
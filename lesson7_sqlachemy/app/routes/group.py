from flask import render_template, request
from flask.blueprints import Blueprint
from sqlalchemy import select

from app.database import Session
from app.models import Group

bp = Blueprint("group", __name__)


@bp.route('/', methods=["GET", "POST"])
def group_add():
    with Session() as session:
        if request.method == "POST":
            new_group = Group(name=request.form.get("name"))
            session.add(new_group)
            session.commit()

        groups = session.query(Group).all()
    return render_template("group/managment.html", groups=groups)


@bp.route('/<int:id>', methods=["GET"])
def group_get(id):
    with Session() as session:
        query = select(Group).where(Group.id == id)
        print(query)
        data = session.scalars(query).first()
    return render_template("main.html", content=data)
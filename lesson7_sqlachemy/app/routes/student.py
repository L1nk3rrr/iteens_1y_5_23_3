from datetime import datetime

from flask import render_template, request
from flask.blueprints import Blueprint
from sqlalchemy import select

from app.database import Session
from app.models import Student, Group

bp = Blueprint("student", __name__)


def get_age(birhdate):
    birhdate = datetime.strptime(birhdate, "%Y-%m-%d")
    current_date = datetime.now()
    age = current_date.year - birhdate.year - (
            (current_date.month, current_date.day) < (birhdate.month, birhdate.day)
    )
    return age


@bp.route('/', methods=["GET", "POST"])
def student_add():
    with Session() as session:
        if request.method == "POST":
            print(request.form.get("groups"))
            items_groups = session.query(Group).where(Group.id.in_([request.form.get("groups"), ])).all()
            new_student = Student(
                name=request.form.get("name"),
                surname=request.form.get("surname"),
                age=get_age(request.form.get("birthdate")),
                address=request.form.get("address"),
                groups=items_groups,
            )
            session.add(new_student)
            session.commit()

        students = session.query(Student).all()
        groups = session.query(Group).all()
    return render_template("student/managment.html", students=students, groups=groups)


@bp.route('/<int:id>', methods=["GET"])
def student_get(id):
    with Session() as session:
        query = select(Student).where(Student.id == id)
        print(query)
        data = session.scalars(query).first()
    return render_template("main.html", content=data)
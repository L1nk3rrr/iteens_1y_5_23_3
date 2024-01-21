from flask import (
    Blueprint,
    render_template,
    url_for,
    redirect,
    flash
)
from flask_login import login_user

from app.database import Session
from app.models import User
from app.forms import LoginForm, SignupForm

from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint("auth", __name__)


@bp.route('/signup/', methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        with Session() as session:
            user = session.query(User)\
                          .where(
                                 User.email == form.email.data
            ).first()
            if user:
                print("User currently exists")
                return redirect(url_for("auth.login"))
            pwd = generate_password_hash(form.password.data)
            user = User(
                nickname=form.email.data,
                email=form.email.data,
                password=pwd,
            )
            session.add(user)
            session.commit()

    return render_template("form_template.html", form=form)


@bp.route('/login/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        with Session() as session:
            user = session.query(User)\
                          .where(
                                 User.nickname == form.nickname.data
            ).first()
            if user:
                if check_password_hash(user.password, form.password.data):
                    print(user)
                    login_user(user)
                    return redirect(url_for("default.index"))
                print("Wrong password")
                return redirect(url_for("auth.login"))
            print("Wrong password nickname")
            return redirect(url_for("auth.login"))
    return render_template("form_template.html", form=form)
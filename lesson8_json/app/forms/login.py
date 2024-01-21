from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField


class LoginForm(FlaskForm):
    nickname = StringField("Nickname", validators=[validators.DataRequired()])
    password = PasswordField("Password", validators=[validators.DataRequired()])
    submit = SubmitField("Log In")
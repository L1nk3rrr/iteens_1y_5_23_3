from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField


class SignupForm(FlaskForm):
    email = StringField("Email", validators=[validators.DataRequired(), validators.Email(), ])
    password = PasswordField("Password", validators=[validators.DataRequired()])
    submit = SubmitField("Sign up")

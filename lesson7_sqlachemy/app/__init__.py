from flask import Flask
from app.database import create_db, drop_db


def create_app():
    app = Flask(__name__)

    from app.routes import default_bp, group_bp, student_bp

    app.register_blueprint(default_bp, url_prefix="/")
    app.register_blueprint(group_bp, url_prefix="/groups/")
    app.register_blueprint(student_bp, url_prefix="/students/")

    from app import models
    create_db() # створення табличок
    # drop_db() # дропнути всі таблички

    return app
import binascii, os

from flask import Flask, render_template
from flask_login import LoginManager

from app.database import create_db, drop_db, Session


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = binascii.hexlify(os.urandom(24))
    login_manager = LoginManager()
    login_manager.login_view = "login"
    login_manager.init_app(app)

    from app.routes import auth_bp, default_bp

    app.register_blueprint(default_bp, url_prefix="/")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    from app import models
    create_db() # створення табличок
    # drop_db() # дропнути всі таблички

    @app.errorhandler(403)
    @app.errorhandler(404)
    @app.errorhandler(405)
    @app.errorhandler(500)
    def handler(e):
        return render_template('error.html', code=e.code)

    @login_manager.user_loader
    def load_user(user_id: int):
        with Session() as session:
            return session.query(models.User).where(models.User.id == user_id).first()

    return app
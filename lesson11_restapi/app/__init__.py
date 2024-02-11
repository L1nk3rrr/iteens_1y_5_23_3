import os

from flask import Flask, render_template
from flask_restful import Api
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

from app.database import create_db, drop_db, Session

SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config["SECRET_KEY"] = os.urandom(12).hex()
    api = Api(app)

    from app.api import PostApi
    api.add_resource(PostApi, "/api/v1.0/post/<int:id>", "/api/v1.0/post")

    cors = CORS(app, resources={r'/api/*': {"origins": "*"}})

    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': 'Access Api'}
    )
    
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    from app import models
    create_db() # створення табличок
    with Session() as session:
        post = models.Post(title="test1", content="test1", author="test1")
        session.add(post)
        session.commit()
    # drop_db() # дропнути всі таблички

    @app.errorhandler(403)
    @app.errorhandler(404)
    @app.errorhandler(405)
    @app.errorhandler(500)
    def handler(e):
        return render_template('error.html', code=e.code)

    return app
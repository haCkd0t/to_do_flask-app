from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///pr.db'
    db.init_app(app)
    from app.routes.register import reg_bp
    from app.routes.login import auth_bp
    from app.routes.tasks import tasks_bp
    app.register_blueprint(reg_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    return app

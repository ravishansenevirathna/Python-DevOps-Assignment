from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    from .routes.task import task_bp
    app.register_blueprint(task_bp, url_prefix='/api')

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
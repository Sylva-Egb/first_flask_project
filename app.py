from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy 
from config import Config
from models import db
from routes import init_routes

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    init_routes(app)
    return app


if __name__ == "__main__":
    app = create_app()  
    app.run(debug=True)
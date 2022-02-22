from distutils.command.config import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")

    db.init_app(app)

    app.db = db

    # models import
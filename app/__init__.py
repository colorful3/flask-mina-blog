# -*- coding: utf8 -*-
from .app import Flask

__author__ = 'Colorful'
__date__ = '2018/8/19 下午12:54'


def register_blueprint(app):
    from app.api import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(app):
    from app.models.base import db
    db.init_app(app=app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprint(app)
    register_plugin(app)
    return app
"""
Initialize app
"""

import os
import logging
from logging.handlers import RotatingFileHandler


from config import config
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template


api = Api()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    api.init_app(app)

    with app.app_context():

        from .task import task as task_blueprint
        app.register_blueprint(task_blueprint)

        if app.debug and not app.testing:
            if not os.path.exists('logs'):
                os.mkdir('logs')

            file_handler = RotatingFileHandler('logs/logging.log', maxBytes=10240, backupCount=10)
            file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)

            app.logger.addHandler(file_handler)
            app.logger.setLevel(logging.INFO)
            app.logger.info('running app')

        return app

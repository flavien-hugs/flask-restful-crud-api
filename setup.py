"""
Application entry point.
"""

import os
import logging as lg

from apps import create_app, db

from dotenv import load_dotenv
from flask_migrate import Migrate

from apps.task.models import Task


dotenv_path = os.path.join(os.path.dirname(__file__), '.flaskenv')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


app = create_app(os.getenv('FLASK_CONFIG') or 'dev')
migrate = Migrate(app, db, render_as_batch=True)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Task=Task)


@app.cli.command('init_db')
def init_db():
    db.create_all()
    db.session.commit()
    lg.warning('Database initialized !')


if __name__ == "__main__":
    app.run()

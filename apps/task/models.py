from .. import db

from datetime import datetime


class Task(db.Model):
    """Task model"""

    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text(80), nullable=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    def __repr__(self):
        return f"Task(id={self.id!r}, name={self.name!r})"

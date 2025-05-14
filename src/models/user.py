"""src/models/user.py
"""

from datetime import datetime

from src.models import db


class User(db.Model):
    """User
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        """to_dict
        """
        return {
            'id': self.id,
            'name': self.name,
        }

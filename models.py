"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

DEFAULT_URL = 'https://tinyurl.com/demo-cupcake'

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Table of cupcake instance"""

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, 
        primary_key=True,
        autoincrement=True)

    flavor = db.Column(db.Text,
        nullable=False)

    size = db.Column(db.Text,
        nullable=False)

    rating = db.Column(db.Integer,
        nullable=False)

    image = db.Column(db.Text,
        nullable=False,
        default=DEFAULT_URL)

    def __repr__(self):
        return f'< Cupcake. {self.id}, {self.flavor}, {self.size}, {self.rating}. >'
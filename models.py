
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


"""Models for Blogly."""


class User(db.Model):
    """ User """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column(db.Text, nullable=False)

    last_name = db.Column(db.Text, nullable=False)

    img_url = db.Column(db.Text, nullable=True,
                        default='https://premium.wpmudev.org/blog/wp-content/uploads/2012/04/mystery-man-small.jpg')

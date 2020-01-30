
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

    post_bridge = db.relationship('Post', backref='user_bridge')

class Post(db.Model):
    """ Posts """

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

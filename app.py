"""Blogly application."""

from flask import Flask, redirect, render_template, request
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
# db.create_all()

app.config['SECRET_KEY'] = "poiawhefiusiuawe"
debug = DebugToolbarExtension(app)


@app.route("/")
def index():
    """ Redirect to list of users """
    
    return render_template('user-listing.html')


# @app.route("/users")
#     """ Show all users.
#     Make these links to view the detail page for the user.
#     Have a link here to the add-user form. """


# @app.route("/users/new")
#     """ Show an add form for users """


# @app.route("/users/new", methods=["POST"])
#     """ Process the add form, adding a new user and going back to /users """


# @app.route("/users/<int:user_id>")
#     """ Show information about the given user. 
#     Have a button to get to their edit page, and to delete the user. """


# @app.route("/users/<int:user_id>/edit")
#     """ Show the edit page for a user. 
#     Have a cancel button that returns to the detail page for a user, 
#     and a save button that updates the user. """


# @app.route("/users/<int:user_id>/edit", methods=["POST"])
#     """ Process the edit form, returning the user to the /users page. """


# @app.route("/users/<int:user_id>/delete", methods=["POST"])
#     """ Delete the user. """

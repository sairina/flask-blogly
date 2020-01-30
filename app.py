"""Blogly application."""

from flask import Flask, redirect, render_template, request, flash
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "poiawhefiusiuawe"
debug = DebugToolbarExtension(app)

# def get_user_data(user_id) {

# }

@app.route("/")
def index():
    """ Redirect to list of users """
    return redirect("users")


@app.route("/users")
def user_list():
    """ Show all users.
    Make these links to view the detail page for the user.
    Have a link here to the add-user form. """
    users = User.query.all()
    return render_template('user-listing.html', users=users)

@app.route("/users/new")
def show_form():
    """ Show an add form for users """

    return render_template('/new-user-form.html')


@app.route("/users/new", methods=["POST"])
def create_user():
    """ Process the add form, adding a new user and going back to /users """
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    img_url = request.form.get('img_url')
    img_url = img_url if img_url else None
    user = User(first_name=first_name, last_name=last_name, img_url=img_url)
    db.session.add(user)
    db.session.commit()

    return redirect("/")


@app.route("/users/<int:user_id>")
def show_user_profile(user_id):
    """ Show information about the given user. 
    Have a button to get to their edit page, and to delete the user. """
    user = User.query.get_or_404(user_id)
    return render_template("user-detail-page.html", user=user)



@app.route("/users/<int:user_id>/edit")
def edit_user(user_id):
    """ Show the edit page for a user. 
    Have a cancel button that returns to the detail page for a user, 
    and a save button that updates the user. """
    user = User.query.get_or_404(user_id)
    return render_template("user-edit-page.html", user=user)


@app.route("/users/<int:user_id>/edit", methods=["POST"])
def edit_user_post(user_id):
    this_user = User.query.get(user_id)
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    img_url = request.form.get('img_url')
    img_url = img_url if img_url else None
    this_user.first_name = first_name
    this_user.last_name = last_name
    this_user.img_url = img_url
    db.session.commit()

    return redirect("/users/" + str(user_id))
    """ Process the edit form, returning the user to the /users page. """


@app.route("/users/<int:user_id>/delete", methods=["POST", "GET"])
def delete_user(user_id):
    """ Delete the user. """
    User.query.filter_by(id=user_id).delete()
    db.session.commit()

    return redirect("/users")

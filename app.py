"""Blogly application."""

from flask import Flask, redirect, render_template, request, flash
from models import db, connect_db, User, Post, Tag, PostTag
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "poiawhefiusiuawe"
debug = DebugToolbarExtension(app)


@app.route("/")
def index():
    """ Redirect to list of users """
    return redirect("users")


@app.route("/users")
def user_list():
    """ Show all users.
    Make these links to view the detail page for the user.
    Have a link here to the add-user form. """

    return render_template('user-listing.html', users=User.query.all())


@app.route("/users/new")
def show_form():
    """ Show an add form for users """

    return render_template('/new-user-form.html')


@app.route("/users/new", methods=["POST"])
def create_user():
    """ Process the add form, adding a new user and going back to /users """

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    img_url = request.form.get('img_url') or None
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
    """ Process the edit form, returning the user to the /users page. """

    # (grabbing info for POST)
    this_user = User.query.get_or_404(user_id)
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    img_url = request.form.get('img_url') or None

    # (POST)
    this_user.first_name = first_name
    this_user.last_name = last_name
    this_user.img_url = img_url
    db.session.commit()

    return redirect(f"/users/{user_id}")


@app.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    """ Delete the user. """

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")


""" PART 2 """


@app.route("/users/<int:user_id>/posts/new")
def new_post_form(user_id):
    """Show form to add a post for that user."""

    user = User.query.get_or_404(user_id)
    return render_template("new-post-form.html", user=user)


@app.route("/users/<int:user_id>/posts/new", methods=["POST"])
def submit_post_form(user_id):
    """Handle add form; add post and redirect to the user detail page."""

    title = request.form.get('title')
    content = request.form.get('content')

    post = Post(title=title, content=content, user_id=user_id)
    db.session.add(post)
    db.session.commit()

    return redirect(f"/users/{user_id}")


@app.route("/posts/<int:post_id>")
def show_post(post_id):
    """ Show a post, show buttons to edit and delete posts """

    post = Post.query.get_or_404(post_id)
    return render_template("post-detail-page.html", post=post)


@app.route("/posts/<int:post_id>/edit")
def show_edit_post_form(post_id):
    """Show form to edit a post; and cancel back to user page."""

    post = Post.query.get_or_404(post_id)
    return render_template("post-edit-page.html", post=post)


@app.route("/posts/<int:post_id>/edit", methods=["POST"])
def submit_post_edit(post_id):
    """ Handle editing of a post. Redirect back to the post view. """

    post = Post.query.get_or_404(post_id)
    post.title = request.form.get("title")
    post.content = request.form.get("content")
    db.session.commit()

    return redirect(f"/posts/{post_id}")


@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    """ Delete the post. """

    post = Post.query.get_or_404(post_id)
    user = post.user_bridge
    db.session.delete(post)

    db.session.commit()

    return redirect(f"/users/{user.id}")


""" PART 3 """


@app.route("/tags")
def get_tags():
    """ Lists all tags, with links to the tag detail page. """

    # need to set up links to tag detail page
    return render_template("list-tag.html", tags=Tag.query.all())


# @app.route("/tags/<tag_id>")
# """ Show detail about a tag. Have links to edit form and to delete."""


# @app.route("/tags/new")
# """ Shows a form to add a new tag. """


# @app.route("/tags/new", methods=["POST"])
# """ Process add form, adds tag, and redirect to tag list. """


# @app.route("/tags/[tag-id]/edit")
# """ Show edit form for a tag. """


# @app.route("/tags/[tag-id]/edit", methods=["POST"])
# """ Process edit form, edit tag, and redirects to the tags list. """


# @app.route("/tags/[tag-id]/delete", methods=["POST"])
# """ Delete a tag. """

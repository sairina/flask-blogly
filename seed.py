"""Seed file to make sample data for users db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
whiskey = User(first_name='Whiskey', last_name='Dog',
               img_url='https://www.rithmschool.com/assets/team/whiskey-9b3a868a98c344edc42ce3ea87c26595f2e2e72328fc96eef9263ced6ba42fd4.jpg')
john = User(first_name='John', species="Smith", img_url=NULL)

# Add new objects to session, so they'll persist
db.session.add(whiskey)
db.session.add(john)

# Commit--otherwise, this never gets saved!
db.session.commit()

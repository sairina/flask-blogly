from unittest import TestCase
from app import app
from models import db, connect_db, User

app.config["TESTING"] = True
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'

db.drop_all()
db.create_all()

class UserTests(TestCase):
    def setUp(self):
# drop all data from tables
# add dummy data

    def test_add_user(self):
        """ Tests if user gets added to the user listing page """
        with app.test_client() as client:
            resp = client.post(
                "/users/new", data={'first_name': 'Mathilda', 'last_name': 'Jones'}, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Mathilda Jones', html)

    # def test_valid_fields_add_user(self):
    #      """ NOT WORKING! Test that form inputs are valid on create user page """
    #      with app.test_client() as client:
    #          resp = client.post("/users/new", data={'first_name':'','last_name':5},follow_redirects=True)
    #          html = resp.get_data(as_text=True)

    def test_delete_user(self):
        """ Tests if user is removed from user listing page """
        with app.test_client() as client:
            user = User.query.filter(User.first_name == 'Mathilda').first()
            # user_id_string = str(user.id)
            resp = client.post(
                # fstring
                "/users/" + user_id_string + "/delete", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertNotIn('Mathilda Jones', html)

            # test unhappy path - view function w/delete

    def test_index_redirect(self):
        """ Tests if root page redirects to user listing page """
        with app.test_client() as client:
            resp = client.get("/", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Users</h1>', html)

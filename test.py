from app import app
from unittest import TestCase
from models import db, connect_db, User

app.config["TESTING"] = True
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]

class UserTests(TestCase):
    def setup(self):
        self.client = app.test_client()

    """ Unit Tests """

    def test_add_user(self):
        """ Tests if user gets added to the database """


    """ Integration Tests """

    def test_index_redirect(self):
        """ Tests if root page redirects to user listing page """
        with app.test_client() as client:
            resp = client.get("/", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Users</h1>', html)

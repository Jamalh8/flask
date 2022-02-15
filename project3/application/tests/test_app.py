from flask import url_for
from flask_testing import TestCase

# import the app's classes and objects
from application import app, db
from application.models import Tasks

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    # Will be called before every test
    def setUp(self):
        # Create table
        db.create_all()
        # Create test registree
        task1 = Tasks(name="new task", description= "this new task")
        # save users to database
        db.session.add(task1)
        db.session.commit()

    # Will be called after every test
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()

# Write a test class to test Read functionality
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'new task', b'this new task', response.data)

class TestPost(TestBase):
    def test_create_tasks(self):
        response = self.client.post(url_for('create'), 
        data =dict(name="new task1", description = "this new task1")
        ,follow_redirects=True
        )
        self.assertIn(b"new task1", response.data)

class TestUpdate(TestBase):
    def test_update_task(self):
        response = self.client.post(url_for('update', name="new task"), 
        data =dict(name="new task updated", description = "this new task updated", completed=True),
        follow_redirects=True
        )
        self.assertIn(b"new task updated", b"this new task updated"), (response.data)

class TestDelete(TestBase):
    def test_delete_task(self):
        response = self.client.post(url_for('delete', name="new task"),follow_redirects=True)
        self.assertNotIn("new task", str(response.data))


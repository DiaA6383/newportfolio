# Import necessary modules
import unittest
import requests
from newportfolio.app import TimelinePost  # Import the TimelinePost model
from peewee import *

# Define a list of all model classes used in the tests
MODELS = [TimelinePost]

# Create an in-memory SQLite database for testing
test_db = SqliteDatabase(':memory:')

# Define a test case class that inherits from unittest.TestCase
class TestTimelinePost(unittest.TestCase):

    # This method is called before each test method
    def setUp(self):
        # Bind model classes to the test database
        # bind_refs=False and bind_backrefs=False mean we don't need to recursively bind dependencies
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        # Connect to the test database
        test_db.connect()
        # Create tables in the test database for the model classes
        test_db.create_tables(MODELS)

    # This method is called after each test method
    def tearDown(self):
        # Drop tables from the test database
        test_db.drop_tables(MODELS)
        # Close the connection to the test database
        test_db.close()

    # Define a test method to check the TimelinePost model
    def test_timeline_post(self):
        # Create two TimelinePost instances with some initial data
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content="Hello world, I'm John!")
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content="Hello world, I'm Jane!")

        # Assert that the id of the first post is 1
        assert first_post.id == 1
        # Assert that the id of the second post is 2
        assert second_post.id == 2


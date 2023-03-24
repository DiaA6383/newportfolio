# Import necessary libraries
from peewee import *
from datetime import datetime
import os
import re
from playhouse.shortcuts import model_to_dict
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create Flask application instance
app = Flask(__name__)

# Initialize a MySQL database instance using environment variables
mydb = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306,
)

# Define a model for the timeline using Peewee ORM
class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = mydb


# Connect to the database if this script is being run as the main program
if __name__ == "__main__":
    initialize_app()
# Define a route for the home page
@app.route("/")
def index():
    return render_template("index.html", title="MLH Fellow", url=os.getenv("URL"))


# Define a route for posting a new timeline post
@app.route("/api/timeline_post", methods=["POST"])
def post_time_line_post():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    content = request.form.get("content", "").strip()

    if not name:
        return "Invalid name", 400

    if not content:
        return "Invalid content", 400

    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_regex, email):
        return "Invalid email", 400

    name = request.form["name"]
    email = request.form["email"]
    content = request.form["content"]
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)


# Define a route for retrieving all timeline posts
@app.route("/api/timeline_post", methods=["GET"])
def get_time_line_post():
    return {
        "timeline_posts": [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }


# Define a route for displaying the timeline posts
@app.route("/timeline")
def timeline_post():
    return render_template("timeline.html", title="Timeline")


def initialize_database():
    if os.getenv("TESTING") == "true":
        print("Running in test mode")
        test_db = SqliteDatabase(":memory:")
        test_db.bind([TimelinePost], bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables([TimelinePost], safe=True)
    else:
        mydb.init(
            os.getenv("MYSQL_DATABASE"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            host=os.getenv("MYSQL_HOST"),
            port=3306,
        )

        # Connect to the database and create the tables if they don't exist
        mydb.connect()
        mydb.create_tables([TimelinePost], safe=True)


def initialize_app():
    initialize_database()
    app.run(host="0.0.0.0", port=5000)

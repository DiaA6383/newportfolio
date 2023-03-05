from peewee import *
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
db = MySQLDatabase(os.getenv("MYSQL_DATABASE"), host=os.getenv("MYSQL_HOST"), user=os.getenv("MYSQL_USER"), password=os.getenv("MYSQL_PASSWORD"))

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

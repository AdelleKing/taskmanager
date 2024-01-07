from flask import render_template
from taskmanager import app, db
from .models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")
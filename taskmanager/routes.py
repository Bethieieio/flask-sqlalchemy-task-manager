from email.mime import base
from flask import render_template
from taskmanager import app

@app.route("/")
# something
def home():
    print("hello")
    return render_template("base.html")

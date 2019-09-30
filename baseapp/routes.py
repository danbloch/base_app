from flask import render_template, url_for, redirect, request
from baseapp import app

@app.route("/", methods=["GET","POST"])
def index():
    return render_template('index.html', title='index')

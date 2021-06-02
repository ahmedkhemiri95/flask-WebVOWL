from application import app
import os 
from flask import Flask,render_template
from application.owl2vowl import convert


@app.route("/")
@app.route("/index")
def index():
    convert()
    return render_template('index.html')



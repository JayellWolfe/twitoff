"""Minimal Flask App"""

from flask import Flask, render_template

#Make the application
app = Flask(__name__)

#Make the route
@app.route("/")

#Now define a funcion
def hello():
    return render_template('home.html')

#Make second route
@app.route("/about")

#Now make the function that goes with about
def preds():
    return render_template('about.html')

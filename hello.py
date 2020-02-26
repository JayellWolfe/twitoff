"""Minimal Flask App"""

from flask import Flask

#Make the application
app = Flask(__name__)

#Make the route
@app.route("/")

#Now define a funcion
def hello:
    return "Hello World!"

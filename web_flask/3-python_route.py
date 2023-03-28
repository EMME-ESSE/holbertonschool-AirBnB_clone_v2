#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def tasktwo(text):
    t = text.replace("_", " ")
    return "C" + " " + t


@app.route('/python/<text>', strict_slashes=False)
def taskthree(text = 'is cool'):
    if text = None:
        text = text.replace("_", " ")
        return "Python " + text
    else:
        text = text.replace("_", " ")
        return "Python " + text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""script that starts an incredible Flask web application"""
from flask import Flask, render_template


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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def taskthree(text="is cool"):
    text = text.replace("_", " ")
    return "Python " + text


@app.route('/number/<int:n>', strict_slashes=False)
def taskfor(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def taskfive(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def tasksix(n):
    if n % 2 == 0:
        result = 'even'
    else:
        result = 'odd'
    return render_template("6-number_odd_or_even.html", n=n, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hi():
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def gm(text):
    return ('C {}'.format(text.replace('_', ' ')))


@app.route('/python/<text>', strict_slashes=False)
def pyth(text="is cool"):

    return ('Python {}'.format(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    return ('{} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def temp(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

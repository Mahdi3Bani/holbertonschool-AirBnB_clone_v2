#!/usr/bin/python3
""""
starting web flask app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """"hello flask"""
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hi():
    """"hi hbnb"""
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def gm(text):
    """"c is fun"""
    return ('C {}'.format(text.replace('_', ' ')))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyth(text="is cool"):
    """"python is cool"""

    return ('Python {}'.format(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """" number"""

    return ('{} is a number'.format(n))


@app.route('/number_template/<int:n>>', strict_slashes=False)
def temp(n):
    """"template number"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

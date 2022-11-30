#!/usr/bin/python3
""""
start web flask app
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """"hello"""
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hi():
    """"hbnb"""
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def gm(text):
    """"gm"""
    return ('C {}'.format(text.replace('_', ' ')))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyth(text="is cool"):
    """"pyth"""
    return ('Python {}'.format(text.replace('_', ' ')))


@app.route('/number/<int: n>', strict_slashes=False)
def num(n):
    """"num"""
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

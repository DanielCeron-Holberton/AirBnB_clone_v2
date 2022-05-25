#!/usr/bin/python3
"""FLASK MODULE"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_flask():
    """String to display"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """String to display in another route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """GET Route /c and <text> to print"""
    text = text.replace("_", " ")
    return 'C {}'.format(text)


@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    """Print the text on the route"""
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
    )

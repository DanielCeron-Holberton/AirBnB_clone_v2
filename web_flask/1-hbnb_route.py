#!/usr/bin/python3
"""FLASK MODULES"""

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


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
    )

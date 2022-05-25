#!/usr/bin/python3
"""FLASK MODULE"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_flask():
    """String to display"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
    )

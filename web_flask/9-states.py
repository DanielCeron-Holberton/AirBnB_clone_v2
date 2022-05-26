#!/usr/bin/python3
"""Module using flask to get routes"""


from flask import Flask, render_template
from models import *
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Returns a rendered template with a list of states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states, id=False)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Returns a rendered template with the specified id"""
    states = storage.all(State)
    for state in states.values():
        if state.id == str(id):
            return render_template('9-states.html', states=state)
    return render_template('9-states.html', no_found=True)


@app.teardown_appcontext
def storage_close(self):
    '''Close current session'''
    storage.close()


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
    )

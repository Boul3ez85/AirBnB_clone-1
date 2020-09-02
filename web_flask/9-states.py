#!/usr/bin/python3
""" display a HTML page with the list of all State, and with the list
    of City objects linked to State.
"""

from flask import Flask
from flask import render_template
from models import storage

app = Falsk(__name__)


@app.route("/states", strict_slashes=False)
def state_db():
    """displays all states of a HTML page."""
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """displays HTML page with id info."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
        return render_template("9-states.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')

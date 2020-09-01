#!/usr/bin/python3
""" a script that starts a Flask web application:
        Web application must be listening on 0.0.0.0, port 5000.
        Routes:
            /: display “Hello HBNB!”.
            /hbnb: display “HBNB”.
            /c/<text>: display “C ” followed by the value of the text.
            variable (replace underscore _ symbols with a space).
            /python/(<text>): display “Python ”, followed by the value.
            of the text variable (replace underscore _ symbols with a space).
                The default value of text is “is cool”.
            /number/<n>: display “n is a number” only if n is an integer.
            /number_template/<n>: display a HTML page only if n is an integer:
                H1 tag: “Number: n” inside the tag BODY.
            /number_odd_or_even/<n>: display a HTML page only if n is
            an integer:
                H1 tag: “Number: n is even|odd” inside the tag BODY.
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_holbies():
    """
    Displays 'Hello HBNB!'
        Arguments:
            None
        Returns:
            (str)
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_peers():
    """
    Displays 'HBNB'
        Arguments:
            None
        Returns:
            (str)
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_isfun(text):
    """
    Displays 'HBNB'
        Arguments:
            text: variable name
        Returns:
            (str)
    """
    return "C %s" % text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_iscool(text='is cool'):
    """
    Dispalys 'Python'
        Arguments:
            text: variable name
        Returns:
            (str)
    """
    return "Python %s" % text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """
    Displays n
        Arguments:
            n: (int) variable name
        Returns:
            (integer)
    """
    return '{} is a number'.format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def template_n(n):
    """Displays an HTML page only if <n> is an integer."""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    """
    Displays an HTML page only if <n> is an integer.
    States whether <n> is odd or even in the body.
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

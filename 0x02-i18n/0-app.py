#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """Greetings

    Returns:
         Initial template html
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

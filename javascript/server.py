"""Flask server for Javascript assessment.

IMPORTANT: you don't need to change this file at all to finish
the assessment!
"""

from random import randint
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def show_index():
    """Show the index page"""

    return render_template("index.html")


@app.route("/assessment")
def show_assessment():
    """Show the assessment page."""

    return render_template("js-assessment.html")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

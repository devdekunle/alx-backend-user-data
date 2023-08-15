#!/usr/bin/env python3
"""
A flask application
"""
from flask import Flask, jsonify, make_response


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    index page of the application
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

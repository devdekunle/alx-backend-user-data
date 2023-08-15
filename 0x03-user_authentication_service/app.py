#!/usr/bin/env python3
"""
A flask application
"""
from flask import Flask, jsonify, make_response, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    index page of the application
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """
    endpoint to register a new user
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        new_user = AUTH.register_user(email, password)
        if new_user:
            return jsonify({"email": new_user.email,
                           "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

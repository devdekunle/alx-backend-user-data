#!/usr/bin/env python3
"""
test module
"""
import requests


def register_user(email: str, password: str) -> None:
    """
    tests the register user endpoint
    """
    response = requests.post('http://localhost:5000/users',
                             data={"email": email, "password": password})

    assert response.json() == {"email": email,
                               "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """
    test log in with wrong password
    """
    response = requests.post('http://localhost:5000/sessions',
                             data={"email": email, "password": password})

    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """
    tests valid login and return response
    """
    response = requests.post('http://localhost:5000/sessions',
                             data={"email": email, "password": password})
    assert response.json() == {"email": email, "message": "logged in"}

    session_id = response.cookies.get('session_id')
    return session_id


def profile_unlogged() -> None:
    """
    test unlogged profile
    """
    response = requests.get('http://localhost:5000/profile')
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """
    test access to resource for logged in user
    """
    request_cookies = dict(session_id=session_id)
    response = requests.get('http://localhost:5000/profile',
                            cookies=request_cookies)
    assert response.json() == {'email': 'guillaume@holberton.io'}
    assert response.status_code == 200


def log_out(session_id) -> None:
    """
    test logout route
    """
    request_cookies = dict(session_id=session_id)
    response = requests.delete('http://localhost:5000/sessions',
                               cookies=request_cookies)

    assert response.json() == {'message': 'Bienvenue'}


def reset_password_token(email: str) -> str:
    """
    get reset password token
    """
    response = requests.post('http://localhost:5000/reset_password',
                             data={"email": email})
    reset_token = response.json().get("reset_token")
    assert response.json() == {"email": email, "reset_token": reset_token}
    assert response.status_code == 200
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    test update password
    """
    response = requests.put('http://localhost:5000/reset_password',
                            data={"email": email, "reset_token": reset_token,
                                  "new_password": new_password})
    assert response.status_code == 200
    assert response.json() == {"email": email,
                               "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)

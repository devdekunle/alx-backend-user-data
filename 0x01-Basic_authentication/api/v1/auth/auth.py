#!/usr/bin/env python3
"""
Module for handling the user authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    class for handling authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        checks if the path requuires a user authentication or not
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path.endswith('/'):
            if path in excluded_paths:
                return False
            else:
                return True
        else:
            path = path + ('/')
            if path in excluded_paths:
                return False
            else:
                return True

    def authorization_header(self, request=None) -> str:
        """
        returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns None
        """
        return None

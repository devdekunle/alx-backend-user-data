#!/usr/bin/env python3
"""
Module for implementation of Basic authentication
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    class that handles implementation of basic authentication
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        extracts the authentication header and returns it
        """
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if authorization_header.startswith('Basic ') is False:
            return None
        else:
            token = authorization_header.split(' ')[1]
            return token

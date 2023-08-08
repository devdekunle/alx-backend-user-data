#!/usr/bin/env python3
"""
Module for implementation of Basic authentication
"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) -> str:
        """
        decode the encoded authorization header value
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            decoded_token = base64.b64decode(base64_authorization_header,
                                             validate=True)
            return decoded_token.decode('utf-8')
        except base64.binascii.Error:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """
        extracts the user credentials from the base64decoded value
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) != str:
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        user_details = decoded_base64_authorization_header.split(":")
        return tuple(user_details)

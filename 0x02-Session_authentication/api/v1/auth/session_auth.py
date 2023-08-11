#!/usr/bin/env python3
"""
Module that implements session authentication
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    class for handling session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a session id for a user
        """
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        returns a user_id bases on the session_id
        """
        if session_id is None:
            return None
        if type(session_id) is not str:
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)

#!/usr/bin/env python3
import bcrypt


def hash_password(password: str) -> bytes:
    """
    function that hashes a password
    """
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed_password

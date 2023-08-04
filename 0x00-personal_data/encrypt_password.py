#!/usr/bin/env python3
import bcrypt


def hash_password(password: str) -> bytes:
    """
    function that hashes a password
    """
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    validates a password
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)

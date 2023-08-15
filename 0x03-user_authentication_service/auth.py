#!/usr/bin/env python3
"""
implement hashing a password
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    hash a password and return its bytes format
    """
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

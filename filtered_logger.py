#!/usr/bin/env python3
"""
Handling User Data
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str,) -> str:
    return re.sub(r'({0})=([^{1}]+)'.format('|'.join(fields), separator),
                  r'\1={0}'.format(redaction), message)

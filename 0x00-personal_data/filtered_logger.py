#!/usr/bin/env python3
"""
Handling User Data
"""
from typing import List
import re
import logging
import os
import mysql.connector


PERSONAL_DATA_DB_USERNAME = os.getenv('PERSONAL_DATA_DB_USERNAME')
PERSONAL_DATA_DB_PASSWORD = os.getenv('PERSONAL_DATA_DB_PASSWORD')
PERSONAL_DATA_DB_HOST = os.getenv('PERSONAL_DATA_DB_HOST')
PERSONAL_DATA_DB_NAME = os.getenv('PERSONAL_DATA_DB_NAME')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str,) -> str:
    """
    function to obfuscate a string
    """
    return re.sub(r'({0})=([^{1}]+)'.format('|'.join(fields), separator),
                  r'\1={0}'.format(redaction), message)


# personally identifiable information(pii)
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """
    method that creates a new logger, configures it and returns a
    new logging.Logger object
    """
    # create a new logger and configure
    logger = logging.getLogger('user_data')
    logger.propagate = False
    # configure loggingLevel
    logger.setLevel(logging.INFO)

    # configure logging stream(output)
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)

    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    create a connector to the database and return a connector
    object
    """
    connector = mysql.connector.connect(host=PERSONAL_DATA_DB_HOST,
                                        database=PERSONAL_DATA_DB_NAME,
                                        password=PERSONAL_DATA_DB_PASSWORD,
                                        user=PERSONAL_DATA_DB_USERNAME)
    return connector


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        instantiate RedactingFormatter instance
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        method for formatting logging
        """
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            message, self.SEPARATOR)

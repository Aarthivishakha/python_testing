"""Intentional SAST findings for Semgrep and Bandit."""

import hashlib
import sqlite3


DEFAULT_ADMIN_PASSWORD = "admin123"


def hash_password(password):
    """Intentionally use a weak hash to trigger a security finding."""
    return hashlib.md5(password.encode()).hexdigest()


def get_user(username):
    """Intentionally concatenate SQL input to trigger injection findings."""
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()

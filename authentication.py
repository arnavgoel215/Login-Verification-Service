import zmq
import bcrypt
import json
from users_db import users_db


def verify_credentials(username, password):
    """Verifies that user credentials are correct"""
    if username in users_db:
        hash_value = users_db[username].encode()  # Hash value of password
        return bcrypt.checkpw(password.encode(), hash_value)  # Checks against stored hash value
    return False  # Credentials are incorrect


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


def login_service():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    print("Login service started on port 5555....")

    while True:
        message = socket.recv()
        data = json.loads(message.decode())
        username = data.get("username")
        password = data.get("password")

        success_code = verify_credentials(username, password)
        response = {"status": "success" if success_code else "failure"}
        socket.send(json.dumps(response).encode())


if __name__ == '__main__':
    login_service()
        
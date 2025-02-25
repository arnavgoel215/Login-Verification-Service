# This file is for storing user credentials and contains sample credentials
# Please change values in users_db for production use

import bcrypt

users_db = {
    "user1": bcrypt.hashpw("password123".encode(), bcrypt.gensalt()).decode(),
    "user2": bcrypt.hashpw("password456".encode(), bcrypt.gensalt()).decode()
}


def add_user(username, password):
    if username in users_db:
        return False  # unable to add user if username is already present in db
    users_db[username] = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def change_pw(username, old_password, new_password):
    if username not in users_db:
        return False
    old_pw_hash = users_db[username].encode()
    if bcrypt.checkpw(old_password, old_pw_hash) is True:
        users_db[username] = new_password
        return True
    return False  # unable to change password
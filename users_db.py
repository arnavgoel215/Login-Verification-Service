# This file is for storing user credentials and contains sample credentials
# Please change values in users_db for production use

import bcrypt

users_db = {
    "user1": bcrypt.hashpw("password123".encode(), bcrypt.gensalt()).decode(),
    "user2": bcrypt.hashpw("password456".encode(), bcrypt.gensalt()).decode()
}
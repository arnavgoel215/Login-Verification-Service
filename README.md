# Login-Verification-Service
Login verification microservice to allow verification of user credentials.

## Prerequisites
### Python 3.8 or later
https://www.python.org/downloads/

### PyZMQ (ZeroMQ for Python)
Used to enable communication between client program and microservice.
</br>
https://github.com/zeromq/pyzmq </br>
</br>
Install by typing ```pip install pyzmq``` into Terminal or Command Prompt

### bcrypt
Used to encrypt and decrypt passwords to ensure user credentials are kept secure
</br>
https://pypi.org/project/bcrypt/ </br>
</br>
Install by typing ```pip install bcrypt``` into Terminal or Command Prompt

## How to use
First download the source code files from this respository. Be sure your client program is enabled for communication to the service using ZeroMQ. Be sure the data is sent to the server as a JSON object containing the username and password. There is already a template provided with sample data in users_db.py for how to do this.
</br>
</br>
When the server receives the username and password it will verify them and send back a response in the form of a JSON object which will either be ```{"status": "success"}``` if the username and password are successfully verified or ```{"status": "failure"}``` if it is unable to verify the username and/or password.

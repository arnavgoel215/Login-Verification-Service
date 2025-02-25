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
First download the source code files from this respository.
</br>
</br>
The client program should connect using ZeroMQ using the correct port number.
</br>
</br>
Example:
</br>
```
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
```

</br>
It should then send the username and password over ZeroMQ as a JSON formatted string.
</br>
</br>
Example:
</br>

```
request = json.dumps({"username": username, "password": password})
socket.send(request.encode())
```
</br>
Once the username and password are verified it will send back a response which can be recieved by the client using 

```response = socket.recv()``` and the response itself will either be 
```{status: "success"}``` if it is succesfully verified otherwise it will return ```{status: "failure"}```

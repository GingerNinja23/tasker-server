# tasker-server
### Disclaimer
This repository is intended for my own personal use, because of which the code is not generic.
This repository contains code of a HTTP server, which I use along with Tasker (Android App).
The tasker app can be used to trigger a task based on an event (like NFC Tap) which sends a GET request to the server.
The server takes appropriate action based on the query parameters sent in the GET request. Currently the server has two actions :
 
 * Playing a random FRIENDS episode from a directory
 * Locking the PC (Windows)<br>

This repo is not intended for any one else to use , but if you can gain/extract something from this, you are more than welcome to fork and use it.
The code is not generic and contains configurations and variables which pertain to my system. So you modify the code according to your needs.

### Usage
The code is written purely in Python and has no other dependencies. The usage of the server is as follows:
```
python server.py
```
This command runs the server on Port 8081 by default. The port number can be changed by modifying the following line in the code:
```
PORT_NUMBER = 8081
```

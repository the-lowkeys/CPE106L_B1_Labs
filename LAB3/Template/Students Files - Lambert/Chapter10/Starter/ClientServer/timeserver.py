"""
File: timeserver.py
Project 10.3
Server for providing the day and time.
Allows the server to be shut down gracefully.
Uses a thread for the server and waits for user
input to shut down.
"""

from socket import *
from timeclienthandler import TimeClientHandler

HOST = "localhost"
PORT = 5000
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

# The server now just waits for connections from clients
# and hands sockets off to client handlers
while True:
    print("Waiting for connection . . .")
    client, address = server.accept()
    print("... connected from: ", address)
    handler = TimeClientHandler(client)
    handler.start()

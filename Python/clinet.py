#!/usr/bin/env python3

import socket
import os

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 2999        # The port used by the server

pwd = os.getcwd()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'sh ../Shell/download.sh usec.io Security')
    data = s.recv(1024)

print('Received', repr(data))
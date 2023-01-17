import sys
import socket
import os
import time

HOST = "10.0.0.133"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

BUFFER_SIZE = 4096

def sendCircuit(filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(f"{filename}".encode())
        print('filename sent')
        with open(filename, "r") as f:
            data = f.read()
            f.close()
            s.sendall(data.encode())
            print("circuit sent")
            response = s.recv(BUFFER_SIZE).decode()
            print(response)
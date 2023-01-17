from app import app
from app.sendCircuit import sendCircuit

from flask import (
    render_template,
)

import sys
import socket
import os
import time

HOST = "124.188.226.203"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

BUFFER_SIZE = 4096

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sendCircuit")
def sendCircuit():
    filename = 'cif.qasm'
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
    return render_template('index.html')
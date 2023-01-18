from app import app

from flask import (
    render_template,
    request
)

import sys
import socket
import os
import time

HOST = "120.16.15.81"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

BUFFER_SIZE = 4096

def send_circuit(file):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(f"{file.filename}".encode())
        print('filename sent')
        s.sendall(file.read())
        print("circuit sent")
        response = s.recv(BUFFER_SIZE).decode()
        return response

ALLOWED_EXTENSIONS = {'qasm'}

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/submit")
def submit():
    return render_template('submit.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if 'file' not in request.files:
        return 'No file uploaded'
    file = request.files['file']
    if file.filename == '':
        return 'No file selected'
    if file and allowed_file(file.filename):
        result = send_circuit(file)
        return render_template('result.html', result=result)
    return 'Invalid file type'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)
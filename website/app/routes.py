import os 
os.environ['MPLCONFIGDIR'] = '/var/www/.config/matplotlib'

from app import app

from flask import (
    render_template,
    request
)

from subprocess import call
from qiskit import QuantumCircuit
from time import time

import sys
import socket
import ast

import base64
from io import BytesIO

HOST = "124.188.226.203"  # The server's hostname or IP address
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

@app.route("/qcintro")
def qcintro():
    call(['jupyter', 'nbconvert', '--to', 'html', '/data/Pawsey_SpinQ/website/app/static/jupyter/qc_introduction.ipynb'])
    return render_template('qcintro.html')

@app.route("/spinqintro")
def spinqintro():
    call(['jupyter', 'nbconvert', '--to', 'html', '/data/Pawsey_SpinQ/website/app/static/jupyter/using_spinQ.ipynb'])
    return render_template('spinqintro.html')

@app.route("/qaoa")
def qaoa():
    call(['jupyter', 'nbconvert', '--to', 'html', '/data/Pawsey_SpinQ/website/app/static/jupyter/qaoa.ipynb'])
    return render_template('qaoa.html')

@app.route("/create")
def create():
    return render_template('create.html')

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
        # Get result from SpinQ
        result = send_circuit(file)
        result_dict = ast.literal_eval(result)

        keys = list(result_dict.keys())
        qubits = len(keys[0])
        parsed_results = {state:0 for state in get_binary_numbers(qubits)}

        for key in result_dict.keys():
            parsed_results[key] = result_dict[key]

        labels = list(parsed_results.keys()),
        labels = labels[0]
        values = list(parsed_results.values())

        # Render circuit as image
        file.seek(0)
        qasm_circuit = file.read().decode()
        qiskit_circuit = QuantumCircuit.from_qasm_str(qasm_circuit)
        fig = qiskit_circuit.draw(output='mpl')
        buf = BytesIO()
        fig.savefig(buf, format="jpg")
        circuit = base64.b64encode(buf.getbuffer())

        #return f"<img src='data:image/png;base64,{circuit}'/>"
        print('hi')
        #return render_template('test.html', circuit=circuit.decode('utf-8'))
        return render_template('result.html', labels=labels, values=values, circuit=circuit.decode('utf-8'))
    return 'Invalid file type'

@app.route("/contact")
def contact():
    return render_template('contact.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_binary_numbers(n):
    format_str = f"0{n}b"
    max_binary_number = 2**n
    binlist = [list(format(i, format_str)) for i in range(max_binary_number)]
    return ["".join(l) for l in binlist]

if __name__ == '__main__':
    app.run(debug=True)
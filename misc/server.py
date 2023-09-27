# execute circuit with SpinQ basic simulator
from spinqkit import get_compiler, get_basic_simulator, BasicSimulatorConfig

def exec_circuit(filename):
    engine = get_basic_simulator()
    comp = get_compiler('qasm')
    ir = comp.compile(filename, 0)

    config = BasicSimulatorConfig()
    config.configure_shots(1024)

    result = engine.execute(ir, config)
    return result.probabilities

# execute circuit with SpinQ Triangulum
from spinqkit import get_triangulum, TriangulumConfig

def exec_triangulum(filename):
    engine = get_triangulum()
    comp = get_compiler('qasm')
    exe = comp.compile(filename, 0)

    config = TriangulumConfig()
    config.configure_shots(1024)
    config.configure_ip("127.0.0.1")
    config.configure_port(55444)
    config.configure_account("luketest", "test")
    config.configure_task("task1", "GHZ")

    result = engine.execute(exe, config)
    print(result.probabilities)

import socket
import os
import threading

# thread function
def handle_client(conn, addr):
    print(f"Connected by {addr}")
    with conn:
        filename = conn.recv(BUFFER_SIZE).decode()
        print("filename received")   
        with open(filename, "w") as f:
            data = conn.recv(BUFFER_SIZE).decode()
            f.write(data)
            print('circuit copied')
            f.close()
            result = str(exec_circuit(filename))
            conn.send(result.encode())
            print('result sent')
    conn.close()

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

BUFFER_SIZE = 4096

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    all_threads = []

    try:
        while True:
            conn, addr = s.accept()
    
            # start a new thread
            t = threading.Thread(target=handle_client, args=(conn, addr,))
            t.start()
            all_threads.append(t) 

    except KeyboardInterrupt:
        print('stopped by user')
    finally:
        if s:
            s.close()
        for t in all_threads:
            t.join()
from spinqkit import get_basic_simulator, get_compiler, Circuit,TriangulumConfig, get_triangulum
from spinqkit import H, CX, Rx
from math import pi

# Write the program
circ = Circuit()
q = circ.allocateQubits(3)
circ << (Rx, q[0], pi)
circ << (H, q[1])
circ << (CX, (q[0], q[1]))

# Choose the compiler and backend
comp = get_compiler("native")

# Compile
optimization_level = 0
exe = comp.compile(circ, optimization_level)

# Run
engine = get_triangulum()
config = TriangulumConfig()
config.configure_ip("106.68.218.154")
config.configure_port(55444)
config.configure_account("test", "test")
config.configure_task("task2", "Bell")
result = engine.execute(exe, config)
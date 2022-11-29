from spinqkit import get_basic_simulator, get_compiler, Circuit, BasicSimulatorConfig
from spinqkit import H, CX, Rx
from math import pi

# Write the program
circ = Circuit()
q = circ.allocateQubits(2)
circ << (Rx, q[0], pi)
circ << (H, q[1])
circ << (CX, (q[0], q[1]))

# Choose the compiler and backend
comp = get_compiler("native")
engine = get_basic_simulator()

# Compile
optimization_level = 0
exe = comp.compile(circ, optimization_level)

# Run
config = BasicSimulatorConfig()
config.configure_shots(1024)
result = engine.execute(exe, config)

print(result.counts)
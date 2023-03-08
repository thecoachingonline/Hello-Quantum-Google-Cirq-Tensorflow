import cirq

# Create a circuit with one qubit
circuit = cirq.Circuit()
qubit = cirq.LineQubit(0)
circuit.append(cirq.X(qubit))
circuit.append(cirq.measure(qubit, key='result'))

# Simulate the circuit using the Cirq simulator
simulator = cirq.Simulator()
result = simulator.run(circuit)

# Print the result of the simulation
print(result.measurements['result'])
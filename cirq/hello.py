import os

try:
    import cirq
    import cirq_google
except ImportError:
    print("installing cirq...")
    os.system("pip install cirq-google")
    print("installed cirq.")
    import cirq
    import cirq_google

# Pick a qubit.
qubit = cirq.GridQubit(0, 0)

# Create a circuit
circuit = cirq.Circuit(
    cirq.X(qubit)**0.5,  # Square root of NOT.
    cirq.measure(qubit, key='m')  # Measurement.
)
print("Circuit:")
print(circuit)

# Simulate the circuit several times.
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)
print("Results:")
print(result)

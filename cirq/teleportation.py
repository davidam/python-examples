# https://quantumai.google/cirq/experiments/textbook_algorithms#quantum_teleportation

import os

try:
    import cirq
except ImportError:
    print("installing cirq...")
    os.system("pip install cirq-google")
    import cirq
    print("installed cirq.")

import random
import matplotlib.pyplot as plt
import numpy as np


def make_quantum_teleportation_circuit(gate):
    """Returns a circuit for quantum teleportation.

    This circuit 'teleports' a random qubit state prepared by
    the input gate from Alice to Bob.
    """
    circuit = cirq.Circuit()

    # Get the three qubits involved in the teleportation protocol.
    msg = cirq.NamedQubit("Message")
    alice = cirq.NamedQubit("Alice")
    bob = cirq.NamedQubit("Bob")

    # The input gate prepares the message to send.
    circuit.append(gate(msg))

    # Create a Bell state shared between Alice and Bob.
    circuit.append([cirq.H(alice), cirq.CNOT(alice, bob)])

    # Bell measurement of the Message and Alice's entangled qubit.
    circuit.append([cirq.CNOT(msg, alice), cirq.H(msg), cirq.measure(msg, alice)])

    # Uses the two classical bits from the Bell measurement to recover the
    # original quantum message on Bob's entangled qubit.
    circuit.append([cirq.CNOT(alice, bob), cirq.CZ(msg, bob)])

    return circuit

# Gate to put the message qubit in some state to send.
gate = cirq.X**0.25

# Create the teleportation circuit.
circuit = make_quantum_teleportation_circuit(gate)
print("Teleportation circuit:\n")
print(circuit)


message = cirq.Circuit(gate.on(cirq.NamedQubit("Message"))).final_state_vector()
message_bloch_vector = cirq.bloch_vector_from_state_vector(message, index=0)
print("Bloch vector of message qubit:")
print(np.round(message_bloch_vector, 3))


"""Simulate the teleportation circuit and get the final state of Bob's qubit."""

# Get a simulator.
sim = cirq.Simulator()

# Simulate the teleportation circuit.
result = sim.simulate(circuit)

# Get the Bloch vector of Bob's qubit.
bobs_bloch_vector = cirq.bloch_vector_from_state_vector(result.final_state_vector, index=1)
print("Bloch vector of Bob's qubit:")
print(np.round(bobs_bloch_vector, 3))

# Verify they are the same state!
np.testing.assert_allclose(bobs_bloch_vector, message_bloch_vector, atol=1e-6)

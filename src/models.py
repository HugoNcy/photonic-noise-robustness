import perceval as pcvl
import torch
import torch.nn as nn

import merlin

# Inherits nn.Module so we can use it in a torch circuit
class QuantumCircuit(nn.Module):
    """Quantum circuit represented as an object so we can just call it."""

    # Initialization
    def __init__(self, modes: int=6, photons: int=3):
        super().__init__()

        # We build the circuit
        circuit = merlin.CircuitBuilder(n_modes=modes)
        
        # First mesh of MZI
        circuit.add_entangling_layer(model="mzi", trainable=True)

        # Input Phase Shifters:
        circuit.add_angle_encoding(name="x")

        # Second mesh of MZI
        circuit.add_entangling_layer(model="mzi", trainable=True)

        # We want the probabilities as the output
        output = merlin.MeasurementStrategy.probs(merlin.ComputationSpace.FOCK)

        # Now we can define the actual quantum layer
        self.quantum_layer = merlin.QuantumLayer(
            input_size = modes, # Number of input parameters (in our case, 6)
            builder = circuit,
            n_photons = photons, # Number of photons going through the circuit
            measurement_strategy = output # What is the output
        )

    # Making the quantum layer callable
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.quantum_layer(x)

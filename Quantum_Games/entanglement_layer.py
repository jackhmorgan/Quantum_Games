from qiskit import QuantumCircuit

def entanglement_layer(num_qubits):
    '''Simple linear entanglement layer.'''
    circuit = QuantumCircuit(num_qubits)
    circuit.h(0)
    for i in range(num_qubits-1):
        circuit.cx(i,i+1)
    return circuit
from qiskit import QuantumCircuit
from .entanglement_layer import entanglement_layer

def game_circuit(players, 
                 referee_ansatz=None,
                 insert_barriers=False):
    '''Function to generate quantum circuit implementing prisoner's dillema circuit with multiple plauers '''
    circuit = QuantumCircuit()
    for player in players:
        circuit.add_register(player.creg)
        circuit.add_register(player.qreg)
    
    e_layer = entanglement_layer(circuit.num_qubits)

    circuit.compose(e_layer, circuit.qubits, inplace=True)
    
    if insert_barriers==True:
        circuit.barrier()

    for player in players:
        circuit.compose(player.pick_strategy(), qubits = player.qreg, inplace=True)
 
    if insert_barriers==True:
        circuit.barrier()

    if not referee_ansatz is None:
        circuit.compose(referee_ansatz, qubits = circuit.qubits, inplace=True)
        if insert_barriers==True:
            circuit.barrier()

    circuit.compose(e_layer.inverse(), circuit.qubits, inplace=True)

    if insert_barriers==True:
        circuit.barrier()

    for player in players:
        circuit.measure(player.qreg, player.creg)

    return circuit
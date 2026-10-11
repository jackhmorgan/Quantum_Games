'''
Copyright 2026 Jack Morgan

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''

from qiskit import QuantumCircuit
from .entanglement_layer import entanglement_layer

def game_circuit(players, 
                 #referee_ansatz=None,
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

    # if not referee_ansatz is None:
    #     circuit.compose(referee_ansatz, qubits = circuit.qubits, inplace=True)
    #     if insert_barriers==True:
    #         circuit.barrier()

    circuit.compose(e_layer.inverse(), circuit.qubits, inplace=True)

    if insert_barriers==True:
        circuit.barrier()

    for player in players:
        circuit.measure(player.qreg, player.creg)

    return circuit

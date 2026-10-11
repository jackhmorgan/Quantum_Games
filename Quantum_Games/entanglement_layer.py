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

def entanglement_layer(num_qubits):
    '''Simple linear entanglement layer.'''
    circuit = QuantumCircuit(num_qubits)
    circuit.h(0)
    for i in range(num_qubits-1):
        circuit.cx(i,i+1)
    return circuit

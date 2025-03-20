from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import EfficientSU2
from qiskit.circuit import Gate
import numpy as np

class player:
    '''This class represents a given player of a quantum game. The player is created with a list of strategies, or a number of qubits with which to create 
    a random strategy'''
    def __init__(self,
                 name: str = 'player',
                 strategies: list[QuantumCircuit] = None,
                 probabilities: list[float] = None,
                 num_qubits: int = None,
                 ):
        '''
        Args:
            name: Name of this particular player. Will be used to name the classical and quantum registers associated with the player.
            strategies: List of quantum circuits implementing the possible quantum strategies of the player.
            num_qubits: Number of qubits in the quantum strategy circuit. Will be used to generate a random strategy is no strategy is provided. Equal to log2 of the classical strategies available.
        
        Raises:
            ValueError: If neither strategies nor num_qubits are provided.
        '''

        self.name=name
        self.outcome_history = []
        self.strategy_history = []
        
        # Generate Random strategy if none is provided
        self.strategies=strategies
        if strategies == None:
            if num_qubits==None:
                raise ValueError('Either at least one strategy or num_qubits must be provided')
            
            self.strategies = [EfficientSU2(num_qubits=num_qubits,    
                                           su2_gates=['x','z'],
                                           reps=0,
                                           name=name)]
        self.probabilities = probabilities

        # Set num_qubits
        if num_qubits == None:
            num_qubits = self.strategies[0].num_qubits

        # Set register names
        self.creg = ClassicalRegister(size=num_qubits, name=name)
        self.qreg = QuantumRegister(size=num_qubits, name=name+'_q')

    def pick_strategy(self,
                    index=0,
                    probabilities=None):
        """The pick_strategy method will select one of the initialized strategies for the player. The selection is either made via the index, or a random 
        draw is made using the assigned probabilities in the case of a mixed strategy"""
        if not probabilities==None:
            mixed_strategy_index = np.random.choice(len(probabilities), p=probabilities)
            strategy = self.strategies[mixed_strategy_index]

        elif not self.probabilities==None:
            mixed_strategy_index = np.random.choice(len(self.probabilities), p=self.probabilities)
            strategy = self.strategies[mixed_strategy_index]
 
        else:
            strategy = self.strategies[index]

        strategy.name=self.name
        self.strategy_history.append(strategy)

        if not isinstance(strategy, Gate):
            strategy = strategy.to_gate()

        return strategy
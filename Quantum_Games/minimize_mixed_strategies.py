import pandas as pd
import numpy as np
from scipy.optimize import minimize
from typing import Callable, Iterable
from qiskit import QuantumCircuit
from qiskit.primitives.containers import PrimitiveResult
from qiskit.primitives.containers.sampler_pub import SamplerPubLike
from qiskit.circuit.library import UnitaryGate

from .player import player
from .get_aer_result import get_aer_result
from .game_circuit import game_circuit


class minimize_mixed_strategies:
    def __init__(self, 
                 payoff_func: Callable[[pd.DataFrame], pd.DataFrame],
                 result_getter: Callable[[Iterable[SamplerPubLike]], pd.DataFrame] = None,
                 strategies: list[QuantumCircuit] = None,
                 n_players: int = 2,
                 n_shots: int = 1,
                 n_circuits: int = 5):
        self._validate_function(payoff_func)
        self.payoff_func = payoff_func

        if result_getter == None:
            result_getter = get_aer_result
        self.result_getter = result_getter

        if strategies == None:
            long = UnitaryGate([[1, 0], [0, 1]])
            short = UnitaryGate([[0, 1], [-1, 0]])
            quantum_long = UnitaryGate([[1j, 0], [0, -1j]])
            quantum_short = UnitaryGate([[0, -1j],[-1j, 0]])
            strategies = [long, quantum_long, quantum_short, short]
        self.strategies = strategies

        self.n_players = n_players
        self.n_shots = n_shots
        self.n_circuits = n_circuits


    def _validate_function(self, func):
        # Test the function with a sample dataframe to check if it returns a DataFrame
        sample_df = pd.DataFrame({"a": [0, 1], "b": [1, 0]})
        result = func(sample_df)

        if not isinstance(result, pd.DataFrame):
            raise TypeError("Payoff function must return a pandas DataFrame.")

        if not result.columns.equals(sample_df.columns):
            raise TypeError("Payoff function must return data for each provided player.")

    def optimizer_objective(self, theta) -> float:
        players = []

        probs = theta.tolist()
        norm = sum(probs)

        if norm >= 1:
            return norm
        
        if min(theta) < 0:
            return 1-min(theta)
        
        probs.append(1-norm)
        for i in range(self.n_players):
            players.append(player(name = f'player_{i}', strategies=self.strategies, probabilities=probs))

        circuits = [game_circuit(players=players) for _ in range(self.n_circuits)]
        #circuit = game_circuit(players=players)
        result = self.result_getter(circuits, num_shots=self.n_shots)
        payoffs = self.payoff_func(result)
        ave_payoff = -payoffs.values.mean()
        return ave_payoff
        
    def minimize(self, **kwargs):

        if 'x0' in kwargs.keys():
            x0 = kwargs['x0']
        else:
            x0 = np.random.rand(2*self.n_players)
            x0 = x0/sum(x0)
            x0 = x0 [:-1]
        
        kwargs.setdefault('fun', self.optimizer_objective)
        kwargs.setdefault('x0', x0)

        if not 'method' in kwargs.keys():
            kwargs.setdefault('method', 'Nelder-Mead')

        result = minimize(**kwargs)
        return result
# Quantum Games

A collection of interactive Jupyter Notebooks exploring **quantum game theory**, classical and quantum strategies, and optimization techniques for strategic games. The notebooks focus on the *Prisoner’s Dilemma* and with an arbitrary number of players, with pure and mixed strategies, and fixed vs iterative strategies.

This project provides tools and demonstrations for analyzing how quantum strategies can influence classic game-theoretic scenarios and strategic optimization.

The QuantumGames folder contains the python module that is leveraged in all of the notebooks to test different strategies and game spaces. The underlying code uses Qiskit >= 1.0 to simulate quantum games with the AerSimulator.

### Notebook Summaries

| File | Description |
|------|-------------|
| `iterative_strategies.ipynb` | Demonstrates how strategies evolve over repeated plays using iterative update rules. |
| `minimize_mixed_strategies_example.ipynb` | Shows how to compute optimal mixed strategies via numerical optimization. |
| `n_prisoners_dilemma.ipynb` | Extends the classic Prisoner’s Dilemma to *n* players and analyzes outcomes. |
| `prisoners_dilemma_optimizer.ipynb` | Implements optimization (e.g., gradient-based or heuristic) to find payoff-maximizing strategies. |

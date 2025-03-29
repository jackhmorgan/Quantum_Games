from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import SamplerV2 as Sampler

def get_aer_result(circuits, num_shots=1000):
    if not isinstance(circuits, list):
        circuits = [circuits]
    backend = AerSimulator()
    sampler = Sampler(mode=backend)
    transpiled = transpile(circuits, backend=backend)
    #result = sampler.run(transpiled, shots = num_shots).result()[0].data
    
    result = sampler.run(transpiled, shots = num_shots).result()
    dict_results = {player : [] for player in result[0].data.keys()}
    for trial in result.values():
        for player, results in trial.items():
            dict_results[player].append(results.array.flatten().tolist())

    #mixed_strategy_results = result[trial].data
    #dict_results = {player : [] for player in result.keys()}
    #for player in result.keys():
    #    dict_results[player]=result[player].array.flatten().tolist()

    return dict_results
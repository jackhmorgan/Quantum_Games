from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import SamplerV2 as Sampler
import pandas as pd

def get_aer_result(circuits, num_shots=10):
    if not isinstance(circuits, list):
        circuits = [circuits]
    backend = AerSimulator()
    sampler = Sampler(mode=backend)
    transpiled = [transpile(circuit, backend=backend) for circuit in circuits]
    #result = sampler.run(transpiled, shots = num_shots).result()[0].data
    
    result = sampler.run(transpiled, shots = num_shots).result()
    dict_results = {player : [] for player in result[0].data.keys()}
    for pub_result in result:
        for player in dict_results.keys():
            dict_results[player].extend(pub_result.data[player].array.flatten().tolist())

    #mixed_strategy_results = result[trial].data
    #dict_results = {player : [] for player in result.keys()}
    #for player in result.keys():
    #    dict_results[player]=result[player].array.flatten().tolist()
    df_results = pd.DataFrame(dict_results)
    return df_results
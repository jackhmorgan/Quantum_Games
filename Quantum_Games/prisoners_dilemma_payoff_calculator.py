import pandas as pd
import numpy as np

def prisoners_dilemma_payoff_calculator(results_df : pd.DataFrame):
    payoff_df = pd.DataFrame(index=results_df.index)
    n_players = results_df.shape[1]
    for col in results_df:
        payoff_df[col] = None
    
    for shot in results_df.iterrows():
        n_long = np.count_nonzero(shot[1].values == 1)
        for col_shot, col_payoff in zip(results_df, payoff_df):
            # If th
            if results_df[col_shot][shot[0]] == 0:
                payoff_df.loc[shot[0], col_payoff] = 2*n_long/n_players
            else:
                payoff_df.loc[shot[0], col_payoff] = (2*n_long-n_players)/n_players

    return payoff_df
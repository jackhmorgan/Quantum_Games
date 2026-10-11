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

import pandas as pd
import numpy as np

def prisoners_dilemma_payoff_calculator(results_df : pd.DataFrame):
    '''Calculates the payoff for an n player prisoners dilemma game as seen in Table 1 
    of 'Quantum volunteer's dilemma' by Koh et al. '''
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

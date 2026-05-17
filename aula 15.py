# Excluir colunas e linhas usando drop()

import pandas as pd

dados = pd.read_csv('/kaggle/input/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results/athlete_events.csv')

dados.head()

dados.drop('ID', axis = 1)

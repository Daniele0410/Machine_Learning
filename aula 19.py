# Lidando com dados faltantes

import pandas as pd

dados = pd.read_csv('/kaggle/input/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results/athlete_events.csv')

faltando = dados.isnull()

dados['Height'].fillna(dados['Height'].mean())

dados.head()

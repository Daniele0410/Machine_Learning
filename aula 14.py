# Manipulando colunas de dataframes no pandas

import pandas as pd

dados = pd.read_csv('/kaggle/input/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results/athlete_events.csv')

dados.head()

dados.rename(columns={'Name':'Nome', 'Sex':'Sexo', 'Age':'Idade', 'Height':'Altura'}, inplace = True)

altura = dados['Altura']

type(altura)

dados['Sexo'].value_counts()

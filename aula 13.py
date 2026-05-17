# Filtrando linhas e colunas

import pandas as pd

alunos = {
    'nome':['Ricardo', 'Pedro', 'Maria', 'Fernanda'],
    'nota':[4, 7, 5.5, 9],
    'aprovado':['não', 'sim', 'não', 'sim']}

df = pd.DataFrame(alunos)

n = df['nome']

l = df.loc[1:3]

lc = df.loc[df['nome']== 'Maria']

print(lc)

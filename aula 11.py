#introdução ao pandas

import pandas as pd

alunos = {
    'nome':['Ricardo', 'Pedro', 'Maria'],
    'nota':[4, 7, 5.5],
    'aprovado':['não', 'sim', 'não']}

df = pd.DataFrame(alunos)
print(df)

obj = pd.Series([2, 6, 9, 10, 6])
print(obj)

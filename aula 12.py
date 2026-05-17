# Comandos uteis no pandas
import pandas as pd

alunos = {
    'nome':['Ricardo', 'Pedro', 'Maria'],
    'nota':[4, 7, 5.5],
    'aprovado':['não', 'sim', 'não']}

df = pd.DataFrame(alunos)

df.shape

df.describe()

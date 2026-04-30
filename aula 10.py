import pandas as pd

dados = pd.read_excel('/kaggle/input/datasets/danielesantos27/arquivo-xlsx/arquivo.xlsx.xlsx')
dados.head()

dados2 = pd.read_csv('/kaggle/input/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results/athlete_events.csv')
dados2.head(60)

print(dados)
print(dados2)

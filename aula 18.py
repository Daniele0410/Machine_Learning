# Criando Graficos

import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('/kaggle/input/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results/athlete_events.csv')

masc = dados.loc[dados['Sex']=='M']

x = masc['Height']
y = masc['Weight']

plt.scatter(x, y)
plt.show()

# Criando um histograma

import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('/kaggle/input/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results/athlete_events.csv')
dados.head()

dados.hist(column='Age', bins=100)
plt.show()

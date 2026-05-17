# Criando um bloxplot

import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('/kaggle/input/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results/athlete_events.csv')
dados.head()

dados.boxplot(column='Weight')
plt.show()

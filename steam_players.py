import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('steam_players.csv')

df['country'].hist(bins = 5)

plt.title('Количество игроков Steam')
plt.xlabel('В сотнях тысяч')
plt.ylabel('Наши циферки в тысячах')

plt.show()
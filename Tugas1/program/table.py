import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/steam.csv')

price = data['price'].sort_values(ascending=True)

price_filtered = list(price[price > 1])

bins = pd.cut(price_filtered, bins=10)

frekuensi = bins.value_counts().sort_index().reset_index()

list = [['Harga (Dolar)', 'Frekuensi']]

for x in range(len(frekuensi['index'])):
    list.append([frekuensi['index'][x], frekuensi['count'][x]])

fig, ax = plt.subplots(figsize=(6, 4))

table = ax.table(cellText=list, loc='center', cellLoc='center')

table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1, 1.5)

ax.axis('off')

plt.show()


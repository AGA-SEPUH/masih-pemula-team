import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('../data/steam.csv')

data = data[data['platforms'].str.contains(';mac')]

data['release_date'] = pd.to_datetime(data['release_date'])

years = list(data['release_date'].dt.year.drop_duplicates())

years.sort()

rows = []

for x in years :
    rows.append(len(data[data['release_date'].dt.year == x]))

x = years
y = rows

plt.figure(figsize=(8, 5))

plt.plot(x, y)

plt.xlabel('Tahun')
plt.ylabel('Jumlah Game')

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Baca data dari file CSV
data = pd.read_csv('../data/game.csv')

# Ambil kolom 'Tahun' sebagai sumbu x dan kolom 'Jumlah_Game' sebagai sumbu y
tahun = data['Tahun']
jumlah_game = data['game']

# Buat histogram
plt.figure(figsize=(10, 5))
plt.bar(tahun, jumlah_game, color='skyblue')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Game')
plt.title('Diagram Histogram berapa game yang rilis 5 tahun terakhir')
plt.xticks(rotation=45)

# Tampilkan histogram
plt.show()

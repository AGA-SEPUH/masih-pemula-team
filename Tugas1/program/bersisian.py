import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Baca data dari file CSV
data = pd.read_csv('../data/bersisian.csv')

# Pisahkan kolom Kategori dari data
kategori = data['Category']

# Pisahkan kolom A, B, dan C dari data
a = data['a']
b = data['b']

# Buat posisi bar untuk masing-masing kategori
x = np.arange(len(kategori))

# Lebar setiap bar
width = 0.2

# Buat diagram batang bersisian dengan setiap kategori terpisah
plt.figure(figsize=(12, 6))
plt.bar(x - width, a, width=width, label='positive rating', color='g')
plt.bar(x, b, width=width, label='negative rating', color='r')

# Atur label sumbu x dan legend
plt.xticks(x, kategori)
plt.xlabel('Diagram Batang Bersisian')
plt.ylabel('Nilai')
plt.title('10 Perbandingan Game Antara Positif Dan Negatif Rating Diambil Dari Data Rating Positif Terbanyak')

# Tampilkan legend di luar plot
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Tampilkan diagram
plt.tight_layout()
plt.show()

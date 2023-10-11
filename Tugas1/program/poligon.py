import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = pd.read_csv('../data/Genre.csv')

# Mengubah kolom 'Tahun' menjadi tipe data datetime
data['tahun'] = pd.to_datetime(data['tahun'])

# Mengurutkan data berdasarkan tahun
data = data.sort_values(by='tahun')

# Mengambil kolom 'Tahun' sebagai sumbu x
tahun = data['tahun']

# Mengambil kolom 'Banyaknya' sebagai sumbu y
banyaknya = data['jmlh']

# Membuat diagram poligon
plt.figure(figsize=(10, 6))
plt.fill_between(tahun, banyaknya, alpha=0.7, color='b')
plt.plot(tahun, banyaknya, marker='o', color='b', linestyle='-')
plt.title('Diagram Poligon Banyaknya Game bergenre Action dalam 5 tahun terakhir')
plt.xlabel('Tahun')
plt.ylabel('Banyaknya')
plt.grid(True)
plt.xticks(rotation=45)

# Menampilkan diagram poligon
plt.tight_layout()
plt.show()

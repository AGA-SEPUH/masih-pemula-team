import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = pd.read_csv('../data/steam.csv')

# Mengkonversi kolom 'release_date' ke dalam format datetime
data['release_date'] = pd.to_datetime(data['release_date'])

# Membuat kolom baru 'release_year' berdasarkan tahun rilis
data['release_year'] = data['release_date'].dt.year

# Memfilter data untuk 5 tahun terakhir
recent_data = data[data['release_year'] >= (data['release_year'].max() - 4)]

# Mengurutkan data berdasarkan rata-rata waktu bermain secara menurun
data_sorted_by_playtime = recent_data.sort_values(by='average_playtime', ascending=False)

# Mengambil 10 data teratas
top_10_playtime = data_sorted_by_playtime.head(6)

# Membuat Diagram Pareto
plt.figure(figsize=(10, 6))
plt.bar(top_10_playtime['name'], top_10_playtime['average_playtime'], color='g')
plt.xticks(rotation=90)
plt.title('Top 10 Games by Average Playtime (Pareto Chart)')
plt.xlabel('Game Name')
plt.ylabel('Average Playtime (minutes)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Menampilkan diagram
plt.show()

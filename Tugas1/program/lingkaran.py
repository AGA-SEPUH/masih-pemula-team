import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = pd.read_csv('../data/steam.csv')

# Mengkonversi kolom 'release_date' ke dalam format datetime
data['release_date'] = pd.to_datetime(data['release_date'])

# Membuat kolom baru 'release_year' berdasarkan tahun rilis
data['release_year'] = data['release_date'].dt.year

# Memfilter data untuk 10 tahun terakhir (dari 2019 ke bawah)
recent_data = data[data['release_year'] >= 2010]

# Menghitung jumlah game yang dikembangkan oleh setiap developer
developer_counts = recent_data['developer'].value_counts().head(5)

# Membuat diagram lingkaran
plt.figure(figsize=(8, 8))
plt.pie(developer_counts, labels=developer_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Top 5 Developers by Number of Games (Last 10 Years)')
plt.axis('equal')  # Mengatur aspek menjadi lingkaran
plt.tight_layout()

# Menampilkan diagram
plt.show()

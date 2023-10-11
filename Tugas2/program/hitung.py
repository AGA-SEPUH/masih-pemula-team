import numpy as np
import matplotlib.pyplot as plt

# Data Tahun dan Frekuensi
tahun = [1998, 1999, 2000, 2001, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
frekuensi = [1, 2, 2, 2, 2, 5, 2, 14, 11, 11, 67, 62, 70, 133, 217, 666, 1128, 1504, 1739, 1964, 450]

# Menghitung mean
mean = sum(tahun[i] * frekuensi[i] for i in range(len(tahun))) / sum(frekuensi)

# Menghitung median
sorted_data = sorted([(tahun[i], frekuensi[i]) for i in range(len(tahun))])
n = sum(frekuensi)
middle = n / 2
median = None
cumulative = 0
for data in sorted_data:
    cumulative += data[1]
    if cumulative >= middle:
        median = data[0]
        break

# Menghitung min dan max
min_value = min(tahun)
max_value = max(tahun)

# Menghitung modus
modus = tahun[frekuensi.index(max(frekuensi))]

# Menghitung Quartile 1 dan Quartile 3
q1 = np.percentile(tahun, 25)
q3 = np.percentile(tahun, 75)

# Menghitung Desil ke-6
desil_6 = np.percentile(tahun, 60)

# Menghitung Persentil ke-65
persentil_65 = np.percentile(tahun, 65)

# Menghitung Hamparan (Range)
hamparan = max_value - min_value

# Menghitung Simpangan Quartil
simpangan_quartil = q3 - q1

# Menghitung Simpangan Rata-rata (Mean Deviation)
mean_deviation = sum(abs(t - mean) * f for t, f in zip(tahun, frekuensi)) / sum(frekuensi)

# Menghitung Standar Deviasi
variance = sum(f * (t - mean) ** 2 for t, f in zip(tahun, frekuensi)) / sum(frekuensi)
standar_deviasi = variance ** 0.5

# Menghitung Jangkauan (Range)
range_data = max(tahun) - min(tahun)

# Membuat Boxplot
plt.figure(figsize=(10, 6))
plt.boxplot(tahun, vert=False)
plt.title('Boxplot Data Tahun')
plt.xlabel('Tahun')
plt.grid()
plt.show()

# Menampilkan hasil
print("Mean:", mean)
print("Median:", median)
print("Min:", min_value)
print("Max:", max_value)
print("Modus:", modus)
print("Quartile 1 (Q1):", q1)
print("Quartile 3 (Q3):", q3)
print("Desil ke-6:", desil_6)
print("Persentil ke-65:", persentil_65)
print("Hamparan (Range):", hamparan)
print("Simpangan Quartil:", simpangan_quartil)
print("Simpangan Rata-rata (Mean Deviation):", mean_deviation)
print("Standar Deviasi:", standar_deviasi)
print("Jangkauan (Range):", range_data)
print("Boxplot:")



import matplotlib.pyplot as plt
import numpy as np
import statistics

# Data Tahun dan Frekuensi
tahun = [1998, 1999, 2000, 2001, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
frekuensi = [1, 2, 2, 2, 2, 5, 2, 14, 11, 11, 67, 62, 70, 133, 217, 666, 1128, 1504, 1739, 1964, 450]

# Hitung Mean, Median, dan Modus
mean = statistics.mean(tahun)
median = statistics.median(tahun)
# Menghitung Quartile 1 dan Quartile 3
q1 = np.percentile(tahun, 25)
q3 = np.percentile(tahun, 75)

# Menghitung Desil ke-6
desil_6 = np.percentile(tahun, 60)

# Menghitung Persentil ke-65
persentil_65 = np.percentile(tahun, 65)
try:
    modus = tahun[frekuensi.index(max(frekuensi))]
except statistics.StatisticsError:
    modus = None

# Tentukan frekuensi maksimum
max_frekuensi = max(frekuensi)

# Buat Diagram Garis
plt.figure(figsize=(10, 6))
plt.plot(tahun, frekuensi, marker='o', linestyle='-', color='b', label='Frekuensi')
plt.axvline(mean, color='r', linestyle='--', label=f'Mean ({mean:.2f})', ymin=0, ymax=max_frekuensi)
plt.axvline(median, color='g', linestyle='--', label=f'Median ({median})', ymin=0, ymax=max_frekuensi)
if modus is not None:
    plt.axvline(modus, color='y', linestyle='--', label=f'Modus ({modus})', ymin=0, ymax=max_frekuensi)
plt.axvline(q1, color='m', linestyle='--', label=f'Quartil 1 ({q1})', ymin=0, ymax=max_frekuensi)
plt.axvline(q3, color='c', linestyle='--', label=f'Quartil 3 ({q3})', ymin=0, ymax=max_frekuensi)
plt.axvline(desil_6, color='orange', linestyle='--', label=f'Desil ke-6 ({desil_6})', ymin=0, ymax=max_frekuensi)
plt.axvline(persentil_65, color='purple', linestyle='--', label=f'Persentil ke-65 ({persentil_65})', ymin=0, ymax=max_frekuensi)

# Label dan judul
plt.xlabel('Tahun')
plt.ylabel('Frekuensi')
plt.title('Diagram Garis dengan Mean, Median, dan Modus')
plt.legend()

# Tampilkan diagram
plt.grid()
plt.show()

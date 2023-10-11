import matplotlib.pyplot as plt
import statistics
import numpy as np

def soal1():
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

def soal2():
  # Data kelompok dan frekuensi
  kelompok = ["0,59 - 43,11", "43,11 - 85,21", "85,21 - 127,30", "127,30 - 169,40", "169,40 - 211,50", "211,50 - 253,60", "253,60 - 295,70", "295,70 - 337,79", "337,79 - 379,89", "379,89 - 421,99"]
  frekuensi = [21365, 98, 3, 7, 1, 0, 0, 1, 0, 1]

  # Menghitung statistik
  mean = 22
  median = 10734
  quartil_1 = 10.77522724
  quartil_3 = 32.14568172
  desil_6 = 4
  persentil_65 = 27.87159083
  jangkauan = 0.21
  hamparan = 21.37
  simpangan_kuartil = quartil_3 - quartil_1
  simpangan_rata_rata = statistics.mean([abs(x - mean) for x in frekuensi])
  variance = statistics.variance(frekuensi)
  standar_deviasi = statistics.stdev(frekuensi)

  # Plot histogram
  plt.figure(figsize=(10, 6))
  bars = plt.bar(kelompok, frekuensi, color='blue', alpha=0.7)

  # Label dan judul
  plt.xlabel('Kelompok Nilai Uang Dolar')
  plt.ylabel('Frekuensi (Fi)')
  plt.title('Histogram Data Kelompok Nilai Uang Dolar')

  # Tampilkan informasi statistik di atas batang histogram
  for bar in bars:
      height = bar.get_height()
      plt.text(
          bar.get_x() + bar.get_width() / 2,
          height + 1,  # Posisi teks di atas batang
          f'{height:.2f}',  # Tampilkan frekuensi dengan 2 angka desimal
          ha='center',  # Pusatkan teks horizontal
          va='bottom'  # Posisikan teks di atas batang
      )

  # Tampilkan informasi statistik di bawah batang histogram
  plt.text(-0.5, 1500, f'Mean ({mean})', fontsize=10, color='black')
  plt.text(-0.5, 2500, f'Median ({median})', fontsize=10, color='black')
  plt.text(-0.5, 3500, f'Quartil 1 ({quartil_1:.2f})', fontsize=10, color='black')
  plt.text(-0.5, 4500, f'Quartil 3 ({quartil_3:.2f})', fontsize=10, color='black')
  plt.text(-0.5, 5500, f'Desil ke-6 ({desil_6})', fontsize=10, color='black')
  plt.text(-0.5, 6500, f'Persentil ke-65 ({persentil_65:.2f})', fontsize=10, color='black')
  plt.text(-0.5, 7500, f'Jangkauan ({jangkauan})', fontsize=10, color='black')
  plt.text(-0.5, 8500, f'Hamparan ({hamparan})', fontsize=10, color='black')
  plt.text(-0.5, 9500, f'Simpangan Kuartil ({simpangan_kuartil:.2f})', fontsize=10, color='black')
  plt.text(-0.5, 10500, f'Simpangan Rata-Rata ({simpangan_rata_rata:.2f})', fontsize=10, color='black')
  plt.text(-0.5, 11500, f'Variance ({variance:.6f})', fontsize=10, color='black')
  plt.text(-0.5, 12500, f'Standar Deviasi ({standar_deviasi:.6f})', fontsize=10, color='black')

  # Tampilkan diagram histogram
  plt.xticks(rotation=45)
  plt.grid(axis='y')
  plt.tight_layout()
  plt.show()




soal1()
soal2()
# UNTUK MENCARI DATA DARI CSV DAN DI BENTUK DALAM TABEL
def get_all_data():
    import matplotlib.pyplot as plt
    import pandas as pd

    data = pd.read_csv('../data/steam.csv')

    data = data[data['platforms'].str.contains(';mac')]

    data['release_date'] = pd.to_datetime(data['release_date'])

    years = list(data['release_date'].dt.year.drop_duplicates())

    years.sort()

    rows = []

    for x in years:
        rows.append(len(data[data['release_date'].dt.year == x]))

    # Membuat DataFrame dari tahun dan frekuensi
    df = pd.DataFrame({'Tahun': years, 'Frekuensi': rows})

    # Menampilkan tabel
    print(df)


# UNTUK KONVERT KE DALAM GAMBAR
def print_gambar() :
    import matplotlib.pyplot as plt
    import pandas as pd

    # DataFrame dari contoh sebelumnya
    df = pd.DataFrame({'Tahun': [1998, 1999, 2000, 2001, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
                    'Frekuensi': [1,2,2,2,2,5,2,14,11,11,67,62,70,133,217,666,1128,1504,1739,1964,460]})

    # Membuat gambar tabel
    plt.figure(figsize=(8, 5))
    plt.axis('off')  # Menghilangkan sumbu
    plt.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center', colColours=['#f2f2f2']*len(df.columns))
    plt.title('Tabel Frekuensi Jumlah Game per Tahun')

    # Menyimpan gambar sebagai file gambar (opsional)
    plt.savefig('tabel_game_per_tahun.png', bbox_inches='tight')

    # Menampilkan gambar
    plt.show()


get_all_data()
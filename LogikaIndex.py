import pandas as pd

def update_index_kejahatan(df_kejahatan, df_rw):
    # Ubah 'tanggal_kejadian' ke format datetime dengan errors='coerce'
    df_kejahatan['tanggal_kejadian'] = pd.to_datetime(df_kejahatan['tanggal_kejadian'], errors='coerce')

    # Hapus baris dengan nilai NaT (Not a Time)
    df_kejahatan = df_kejahatan.dropna(subset=['tanggal_kejadian'])

    # Mengambil data berdasarkan status "Terverifikasi"
    verified_complaints = df_kejahatan[df_kejahatan['status_pengaduan'] == 'Terverifikasi']

    # Menghitung jumlah pengaduan per RW dalam satu bulan terakhir
    last_month = pd.to_datetime('today') - pd.DateOffset(months=1)
    filtered_data = verified_complaints[verified_complaints['tanggal_kejadian'] >= last_month]
    complaints_per_rw = filtered_data['id_rw'].value_counts()

    # Mengupdate index_kejahatan di df_rw berdasarkan jumlah pengaduan
    for index, count in complaints_per_rw.items():
        if count == 0:
            df_rw.loc[df_rw['id_rw'] == index, 'index_kejahatan'] = 'Hijau'
        elif count== 1 or 2:
            df_rw.loc[df_rw['id_rw'] == index, 'index_kejahatan'] = 'Kuning'
        elif count >= 3:
            df_rw.loc[df_rw['id_rw'] == index, 'index_kejahatan'] = 'Merah'
        

    return df_rw

# Memuat data dari file CSV
file_path_kejahatan = "Database/pengaduan.csv"
file_path_rw = "Database/rw.csv"
df_kejahatan = pd.read_csv(file_path_kejahatan)
df_rw = pd.read_csv(file_path_rw)

# Mengupdate index_kejahatan pada df_rw
df_rw_updated = update_index_kejahatan(df_kejahatan, df_rw)

# Menyimpan df_rw yang telah diperbarui ke rw.csv
df_rw_updated.to_csv(file_path_rw, index=False)
print("Index kejahatan in rw.csv has been updated based on verified complaints.")

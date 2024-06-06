import pandas as pd

# Load the data from the CSV file
file_path = "Database/rw.csv"
df_kejahatan = pd.read_csv(file_path)

# Create
def create_data():
    global df_kejahatan  # Declare df_kejahatan as a global variable
    id_rw = int(input("Masukkan ID_RW: "))
    no_rw = int(input("Masukkan NO_RW: "))
    index_kejahatan = input("Masukkan Index Kejahatan (Merah, Hijau, atau Kuning): ")

    # Validate index_kejahatan
    if index_kejahatan.lower() not in ['merah', 'hijau', 'kuning']:
        print("Index kejahatan tidak valid. Hanya diperbolehkan Merah, Hijau, atau Kuning.")
        return

    new_data = {'id_rw': id_rw, 'no_rw': no_rw, 'index_kejahatan': index_kejahatan}
    df_kejahatan = df_kejahatan._append(new_data, ignore_index=True)
    df_kejahatan.to_csv(file_path, index=False)
    print("Data berhasil ditambahkan.")

# Read
def read_data():
    return df_kejahatan

# Update
def update_data():
    read_data()
    global df_kejahatan  # Declare df_kejahatan as a global variable
    id_rw = int(input("Masukkan ID_RW yang ingin diupdate: "))
    new_index_kejahatan = input("Masukkan Index Kejahatan yang baru (Merah, Hijau, atau Kuning): ")

    # Validate index_kejahatan
    if new_index_kejahatan.lower() not in ['merah', 'hijau', 'kuning']:
        print("Index kejahatan tidak valid. Hanya diperbolehkan Merah, Hijau, atau Kuning.")
        return

    df_kejahatan.loc[df_kejahatan['id_rw'] == id_rw, 'index_kejahatan'] = new_index_kejahatan
    df_kejahatan.to_csv(file_path, index=False)
    print("Data berhasil diupdate.")

# Delete
def delete_data():
    read_data()
    global df_kejahatan  # Declare df_kejahatan as a global variable
    id_rw = int(input("Masukkan ID_RW yang ingin dihapus: "))

    # Validate if ID_RW exists
    if id_rw not in df_kejahatan['id_rw'].values:
        print(f"ID_RW {id_rw} tidak ditemukan.")
        return

    df_kejahatan.drop(df_kejahatan[df_kejahatan['id_rw'] == id_rw].index, inplace=True)
    df_kejahatan.to_csv(file_path, index=False)
    print("Data berhasil dihapus.")

# Menu
while True:
    print("\nMENU:")
    print("1. Read Data")
    print("2. Create Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Exit")

    choice = input("Pilih menu (1-5): ")

    if choice == '1':
        print("Current Data:")
        print(read_data())
    elif choice == '2':
        create_data()
    elif choice == '3':
        print("Available Data:")
        print(read_data())
        update_data()
    elif choice == '4':
        print("Available Data:")
        print(read_data())
        delete_data()
    elif choice == '5':
        print("Keluar dari aplikasi. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")
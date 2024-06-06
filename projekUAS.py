import pandas as pd
import datetime as dt

df_pengaduan = pd.read_csv("Database/pengaduan.csv")
df_rw = pd.read_csv("Database/rw.csv")
df_artikel = pd.read_csv("Database/artikel.csv")
file_artikel = "Database/artikel.csv"
def main():

    def laporanKriminalitas(id_acc, status):
            #Form Pelaporan
            print("FORM PELAPORAN")
            print("------Informasi umum------")
            print("note: inputan dengan angka")
            day = int(input("Tanggal: "))
            month = int(input("Bulan: "))
            year = int(input("Tahun: "))
            date = dt.date(year, month, day)
            hour = int(input("Jam: "))
            minute = int(input("Menit: "))
            time = dt.time(hour, minute)
            loc = input("Lokasi: ")
            rt = int(input("RT: "))
            rw = int(input("RW: "))
            idx_rw = df_rw.set_index(['no_rw']).loc[rw] #Mencari rw dari id rw
            id_rw = idx_rw['id_rw'] #Mengambil nilai id_rw
            print("\n")
            print("------Informasi khusus------")
            reporterName = input("Nama pelapor: ")
            victimName = input("Nama korban: ")
            insidentDesc = input("Deskripsi kejadian: ")

            id_pengaduan = (len(df_pengaduan) + 1)
            newReport = {'id_pengaduan' : id_pengaduan, 'nama_pengadu' : reporterName, 'nama_korban' : victimName, 'lokasi_TKP' : loc, 'no_rt' : rt, 'id_rw' : id_rw, 'deskripsi' : insidentDesc, 'tanggal_kejadian' : date, 'waktu_kejadian' : time, 'id_akun' : id_acc, 'status_pengaduan' : status}
            df_pengaduan.loc[len(df_pengaduan)] = newReport
            df_pengaduan.to_csv("Database/pengaduan.csv", index=False)

    # pengguna
    def user():
        print("========= Menu User =========")

        #Fungsi menu pengguna
        def geolokasi():
            print
        
        def lihatArtikel():
            def sorting_terbaru_user(df_artikel):
                df_artikel['tanggal_publish'] = pd.to_datetime(df_artikel['tanggal_publish'])
                n = len(df_artikel)
                for i in range(n - 1):
                    for j in range(0, n - i - 1):
                        if df_artikel['tanggal_publish'][j] < df_artikel['tanggal_publish'][j + 1]:
                            df_artikel.loc[j], df_artikel.loc[j + 1] = df_artikel.loc[j + 1].copy(), df_artikel.loc[j].copy()     
                return 
            
            df_artikel = pd.read_csv(file_artikel)
            sorting_terbaru_user(df_artikel)
            print(df_artikel)
          
        #fungsi menu pengguna akhir

        print("Selamat Datang di Aplikasi Crime!")
        while True:
            menuAdmin = int(input("1. Geolokasi \n2. Lihat Artikel \n3. Laporkan! \n4. Log out \nPilih Menu :"))
            if (menuAdmin == 1):
                geolokasi()
            elif (menuAdmin == 2):
                lihatArtikel()
            elif (menuAdmin == 3):
                laporanKriminalitas(0, "Belum Terverifikasi")
            elif (menuAdmin == 4):
                break
            else:
                continue
        
        

    # Admin
    def admin():

        # fungsi gabung
        '''def login():
            username = "kii123"
            password = "123"

            chance = 3

            for i in range (chance, 0, -1):
                print(f"\nLogin dengan {i} kali kesempatan Admin")
                if(i >= 3):
                    inputUsername = input("username: ")
                    inputPassword = input("password: ")
                    if(inputUsername == username and inputPassword == password):
                        print("Halo admin!")
                        break
                    else:
                        continue
                else:
                    print("\nAkses dihentikan")
                i -= 1

        login()'''
        print("========= Menu Admin =========")

        # Fungsi menu Admin
        def dataLaporan():
            print("DATA LAPORAN")
            dataPengaduanFilter = df_pengaduan.filter(items= ['id_pengaduan', 'lokasi_TKP', 'no_rt', 'deskripsi', 'tanggal_kejadian', 'waktu_kejadian', 'status_pengaduan'])
            print(dataPengaduanFilter)

            while True:
                pilDL = int(input("\n1. Sorting laporan \n2. Ubah status \n3. Hapus data \n4. Keluar menu \nPilih tindakan yang akan anda lakukan? "))
                if (pilDL == 1):
                    pilSort = int(input("Sorting apa yang ingin anda lakukan? 1. Terverifikasi  2. Belum terverifikasi? "))
                    if (pilSort == 1):
                        print(dataPengaduanFilter.set_index(['status_pengaduan']).loc['Terverifikasi'])
                        continue
                    elif (pilSort == 2):
                        print(dataPengaduanFilter.set_index(['status_pengaduan']).loc['Belum Terverifikasi'])
                        continue
                elif (pilDL == 2):
                    pilUbah = int(input("Masukan id pengaduan yang ingin Anda verifikasi: "))
                    idx = pilUbah - 1 #membuat index dari id
                    df_pengaduan.loc[idx, 'status_pengaduan'] = 'Terverifikasi'
                    df_pengaduan.to_csv("Database/pengaduan.csv", index=False)
                    continue
                elif (pilDL == 3):
                    pilHapus = int(input("Masukan id pengaduan yang ingin Anda hapus: "))
                    idx = pilHapus - 1 #membuat index dari id
                    df_pengaduan.drop(idx, axis=0, inplace=True)
                    df_pengaduan.to_csv("Database/pengaduan.csv", index=False)
                    continue
                elif (pilDL == 4):
                    break
                else:
                    continue
        
        def tulisArtikel():
            print("BUAT ARTIKEL")
            judulArtikel = input("Judul: ")
            penulis = input("Nama Penulis: ")
            konten = input("Masukan Konten: ")
            tanggalPublish = dt.date.today()
            print("\nARTIKEL TERIMPAN")

            index_artikel = (len(df_artikel) + 1)
            hasil_artikel = {'id_artikel': index_artikel, 'judul': judulArtikel, 'penulis': penulis, 'konten': konten, 'tanggal_publish': tanggalPublish}
            df_artikel.loc[len(df_artikel)] = hasil_artikel
            df_artikel.to_csv("Database/artikel.csv", index=False)


        def updateArtikel():
            def update_artikel(csv_file, artikel_id, new_title, new_author, new_content, new_publish_date):
                df_artikel = pd.read_csv(csv_file)
                if artikel_id in df_artikel['id_artikel'].values:
                    df_artikel.loc[df_artikel['id_artikel'] == artikel_id, ['judul', 'penulis', 'konten', 'tanggal_publish']] = [new_title, new_author, new_content, new_publish_date]
                    df_artikel.to_csv(csv_file, index=False)

                    print(f"Artikel dengan id {artikel_id} telah di update")
                else:
                    print(f"Artikel dengan id {artikel_id} tidak ditemukan")

            csv_file_path = 'Database/artikel.csv' 
            df_artikel = pd.read_csv(file_artikel)
            print(df_artikel)
            user_update = int(input("Masukan id artikel yang ingin diupdate: "))

            print("\nUPDATE ARTIKEL")

            new_title = input("Judul: ")
            new_author = input("Penulis: ")
            new_content = input("Konten: ")
            new_publish_date = dt.date.today()

            update_artikel(csv_file_path, user_update, new_title, new_author, new_content, new_publish_date)



        def hapusArtikel():
            df_artikel = pd.read_csv(file_artikel)
            print(df_artikel)
            def delete_article(csv_file, article_id): 
                df = pd.read_csv(csv_file)
          
                if article_id in df['id_artikel'].values:                 
                    df = df[df['id_artikel'] != article_id]             
                    df.to_csv(csv_file, index=False)
                    print(f"\nArtikel dengan id {article_id} telah dihapus\n")
                else:
                    print(f"\nartikel dengan id  {article_id} tidak ada\n")
 
            csv_file_path = 'Database/artikel.csv'  
            user_delete = int(input("Masukan id untuk menghapus artikel: "))
            delete_article(csv_file_path, user_delete)

        def listArtikel():
            def sorting_terbaru_admin(df_artikel):
                df_artikel['tanggal_publish'] = pd.to_datetime(df_artikel['tanggal_publish'])
                n = len(df_artikel)
                for i in range(n - 1):
                    for j in range(0, n - i - 1):
                        if df_artikel['tanggal_publish'][j] < df_artikel['tanggal_publish'][j + 1]:
                            df_artikel.loc[j], df_artikel.loc[j + 1] = df_artikel.loc[j + 1].copy(), df_artikel.loc[j].copy()
                return df_artikel
            df_artikel = pd.read_csv(file_artikel)
            sorting_terbaru_admin(df_artikel)
            print(df_artikel)

        def mencariArtikel():
                df_artikel = pd.read_csv(file_artikel)
                print(df_artikel)
                def search_artikel(id_artikel):
                    hasil = df_artikel[df_artikel['id_artikel'] == id_artikel]
                    return hasil


                cari_nilai = int(input("masukan id artikel yang ingin dicari: "))

                hasil_id = search_artikel(cari_nilai)

                if not hasil_id.empty:
                    print(f"\nBerikut hasil pencarian artikel berdasarkan id: {cari_nilai}\n")
                    print(hasil_id)
                else:
                    print("\nArtikel tidak ada\n")
                    


        # Akhir fungsi menu Admin

        # Perulangan menu admin
        while True:
            menuAdmin = int(input("1. Lapor Kriminal \n2. Data Laporan \n3. Tulis Artikel \n4. List Artikel \n5. Search Artikel \n6. Hapus Artikel \n7. Update Artikel \n8. Log out\nPilih Menu : "))
            if (menuAdmin == 1):
                while True:
                    print("\n\n")
                    laporanKriminalitas(1, "Terverifikasi")
                    cont = int(input("Apakah anda ingin melaporkan kembali?  1. Ya  2. Tidak? "))
                    if (cont == 1):
                        print("\n")
                        continue
                    else:
                        break
            elif (menuAdmin == 2):
                dataLaporan()
                '''while True:
                    print("\n\n")
                    dataLaporan()
                    cont = int(input("Apakah anda ingin tetap di menu ini?  1. Ya  2. Tidak? "))
                    if (cont == 1):
                        print("\n")
                        continue
                    else:
                        break'''
            elif (menuAdmin == 3):
                tulisArtikel()
            elif (menuAdmin == 4):
                listArtikel()
            elif (menuAdmin == 5):
                mencariArtikel()
            elif (menuAdmin == 6):
                hapusArtikel()
            elif (menuAdmin == 7):
                updateArtikel()
            elif (menuAdmin == 8):
                break
            else:
                continue
        
    
    # Perulangan menu utama
    while True:
        haveAcc = int(input("Apakah anda mempunyai akun?  1. Ya  2. Tidak  3. Keluar? "))
        if (haveAcc == 1):
            admin()
        elif (haveAcc == 2):
            user()
        elif (haveAcc == 3):
            print("Anda telah keluar dari aplikasi")
            break
        else:
            continue

main()
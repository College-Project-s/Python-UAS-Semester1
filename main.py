from lowongan.mainLowongan import mainMenuLowongan
from pelamar.mainPelamar import mainMenuPelamar
from seleksi.mainSeleksi import mainMenuSeleksi
from penawaran.mainPenawaran import mainMenuPenawaran

# ========================== Menu Utama ==========================
def menuUtama():
    while True:
        print("\n")
        print("=" * 45)
        print("          SISTEM REKRUTMEN KARYAWAN")
        print("=" * 45)
        print("1. Manajemen Lowongan")
        print("2. Manajemen Pelamar")
        print("3. Manajemen Penawaran")
        print("4. Proses Seleksi")
        print("5. Keluar")
        print("=" * 45)
        pilihan = input("Pilih menu [1-5]: ")
        print("\n")

        if pilihan == '1':
            mainMenuLowongan()
        elif pilihan == '2':
            mainMenuPelamar()
        elif pilihan == '3':
            mainMenuPenawaran()
        elif pilihan == '4':
            mainMenuSeleksi()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan sistem rekrutmen.")
            break

if __name__ == "__main__":
    menuUtama()

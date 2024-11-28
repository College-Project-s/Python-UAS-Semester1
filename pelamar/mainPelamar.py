from pelamar.functionPelamar.tambahPelamar import functionTambahPelamar
from pelamar.functionPelamar.tampilPelamar import functionTampilPelamar
from pelamar.functionPelamar.editPelamar import functionEditPelamar
from pelamar.functionPelamar.deletePelamar import functionHapusPelamar
# ========================== Manajemen Pelamar ==========================
def mainMenuPelamar():
    print("\n")
    print("=" * 45)
    print("          MANAJEMEN PELAMAR PEKERJAAN")
    print("=" * 45)
    print("1. Tambah Pelamar")
    print("2. Tampil Pelamar")
    print("3. Update Pelamar")
    print("4. Hapus  Pelamar")
    print("5. Kembali")
    print("=" * 45)
    subPilihan = input("Pilih menu [1-5]: ")
    print("\n")
    if subPilihan == '1':
        functionTambahPelamar()
        mainMenuPelamar()
    elif subPilihan == '2':
        functionTampilPelamar()
        mainMenuPelamar()
    elif subPilihan == '3':
        functionEditPelamar()
        mainMenuPelamar()
    elif subPilihan == '4':
        functionHapusPelamar()
        mainMenuPelamar()
    elif subPilihan == '5':
        return
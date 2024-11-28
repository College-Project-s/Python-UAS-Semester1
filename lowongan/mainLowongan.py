from lowongan.functionLowongan.tambahLowongan import functionTambahLowongan
from lowongan.functionLowongan.tampilLowongan import functionTampilLowongan
from lowongan.functionLowongan.editLowongan import functionEditLowongan
from lowongan.functionLowongan.deleteLowongan import functionHapusLowongan
# ========================== Manajemen Lowongan ==========================

def mainMenuLowongan():
    print("\n")
    print("=" * 45)
    print("          MANAJEMEN LOWONGAN PEKERJAAN")
    print("=" * 45)
    print("1. Tambah Lowongan")
    print("2. Tampil Lowongan")
    print("3. Update Lowongan")
    print("4. Hapus  Lowongan")
    print("5. Kembali")
    print("=" * 45)
    subPilihan = input("Pilih menu [1-5]: ")
    print("\n")
    if subPilihan == '1':
        functionTambahLowongan()
        mainMenuLowongan()
    elif subPilihan == '2':
        functionTampilLowongan()
        mainMenuLowongan()
    elif subPilihan == '3':
        functionEditLowongan()
        mainMenuLowongan()
    elif subPilihan == '4':
        functionHapusLowongan()
        mainMenuLowongan()
    elif subPilihan == '5':
        return
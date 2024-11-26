from penawaran.functionPenawaran.tambahPenawaran import functionTambahPenawaran
from penawaran.functionPenawaran.tampilPenawaran import functionTampilPenawaran
from penawaran.functionPenawaran.editPenawaran import functionEditPenawaran
from penawaran.functionPenawaran.deletePenawaran import functionHapusPenawaran
# ========================== Manajemen Pelamar ==========================
def mainMenuPenawaran():
    print("\n")
    print("=" * 45)
    print("          MANAJEMEN BENEFIT PEKERJAAN")
    print("=" * 45)
    print("1. Tambah Benefit")
    print("2. Tampil Benefit")
    print("3. Update Benefit")
    print("4. Hapus  Benefit")
    print("5. Kembali")
    print("=" * 45)
    subPilihan = input("Pilih menu [1-5]: ")
    print("\n")
    if subPilihan == '1':
        functionTambahPenawaran()
        mainMenuPenawaran()
    elif subPilihan == '2':
        functionTampilPenawaran()
        mainMenuPenawaran()
    elif subPilihan == '3':
        functionEditPenawaran()
        mainMenuPenawaran()
    elif subPilihan == '4':
        functionHapusPenawaran()
        mainMenuPenawaran()
    elif subPilihan == '5':
        return
from wawancara.functionWawancara.tambahWawancara import functionTambahWawancara
from wawancara.functionWawancara.tampilWawancara import functionTampilWawancara
from wawancara.functionWawancara.editWawancara import functionEditWawancara
from wawancara.functionWawancara.deleteWawancara import functionHapusWawancara

def mainMenuWawancara():
    print("\n")
    print("=" * 45)
    print("          MANAJEMEN Wawancara PENDAFTAR")
    print("=" * 45)
    print("1. Tambah Jadwal Wawancara")
    print("2. Tampil Jadwal Wawancara")
    print("3. Edit Jadwal Wawancara")
    print("4. Hapus Jadwal Wawancara")
    print("5. Kembali")
    print("=" * 45)
    subPilihan = input("Pilih menu [1-5]: ")
    print("\n")
    if subPilihan == '1':
        functionTambahWawancara()
        mainMenuWawancara()
    elif subPilihan == '2':
        functionTampilWawancara()
        mainMenuWawancara()
    elif subPilihan == '3':
        functionEditWawancara()
        mainMenuWawancara()
    elif subPilihan == '4':
        functionHapusWawancara()
        mainMenuWawancara()
    elif subPilihan == '5':
        return
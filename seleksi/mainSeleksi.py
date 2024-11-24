from seleksi.functionSeleksi.rekrutPelamar import functionRekrutPelamar
from seleksi.functionSeleksi.tampilKandidatDiterima import functionTampilKandidatDiterima

def mainMenuSeleksi():
    print("\n")
    print("=" * 45)
    print("          MANAJEMEN SELEKSI PENDAFTAR")
    print("=" * 45)
    print("1. Rekrut Pelamar")
    print("2. Tampil Kandidat Diterima")
    print("3. Kembali")
    print("=" * 45)
    subPilihan = input("Pilih menu [1-3]: ")
    print("\n")
    if subPilihan == '1':
        functionRekrutPelamar()
        mainMenuSeleksi()
    elif subPilihan == '2':
        functionTampilKandidatDiterima()
        mainMenuSeleksi()
    # elif subPilihan == '3':
    #     functionEditPelamar()
    #     mainMenuSeleksi()
    # elif subPilihan == '4':
    #     functionHapusPelamar()
    #     mainMenuSeleksi()
    elif subPilihan == '5':
        return
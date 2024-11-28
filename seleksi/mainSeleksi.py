from seleksi.functionSeleksi.updateStatusWawancara import functionUpdateStatusWawancara
from seleksi.functionSeleksi.rekrutPelamar import functionRekrutPelamar
from seleksi.functionSeleksi.tampilKandidatDiterima import functionTampilKandidatDiterima

def mainMenuSeleksi():
    print("\n")
    print("=" * 45)
    print("          MANAJEMEN SELEKSI PENDAFTAR")
    print("=" * 45)
    print("1. Seleksi Lolos Wawancara")
    print("2. Rekrut Pelamar")
    print("3. Tampil Kandidat Diterima")
    print("4. Kembali")
    print("=" * 45)
    subPilihan = input("Pilih menu [1-4]: ")
    print("\n")
    if subPilihan == '1':
        functionUpdateStatusWawancara()
        mainMenuSeleksi()
    elif subPilihan == '2':
        functionRekrutPelamar()
        mainMenuSeleksi()
    elif subPilihan == '3':
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
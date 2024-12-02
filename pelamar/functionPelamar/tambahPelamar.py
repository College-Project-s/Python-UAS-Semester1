from moduleExcel import FILE_NAME, cekApakahAdaExcel, os, openpyxl

# Function untuk menambah pelamar
def functionTambahPelamar():
    nama = input("Masukkan nama pelamar: ")
    kontak = input("Masukkan kontak pelamar: ")

    if not os.path.exists(FILE_NAME):
        print("File data rekrutmen tidak ditemukan.")
        return

    workbook = openpyxl.load_workbook(FILE_NAME)

    if 'Lowongan' not in workbook.sheetnames:
        print("Sheet Lowongan tidak ditemukan. Harap tambahkan data lowongan terlebih dahulu.")
        workbook.close()
        return

    sheet_lowongan = workbook['Lowongan']
    posisi_tersedia = [row[1] for row in sheet_lowongan.iter_rows(min_row=2, values_only=True) if row[4] == 'Dibuka']

    if not posisi_tersedia:
        print("Tidak ada lowongan yang dibuka. Harap tambahkan lowongan terlebih dahulu.")
        workbook.close()
        return

    # Tampilkan daftar posisi yang tersedia
    print("\nPosisi yang tersedia untuk dilamar:")
    for posisi in posisi_tersedia:
        print(f"- {posisi}")

    # Validasi input posisi
    while True:
        posisi = input("Masukkan posisi yang dilamar: ")
        if posisi in posisi_tersedia:
            break
        print("Posisi tidak valid atau tidak tersedia. Silakan coba lagi.")

    # Tambahkan data pelamar ke sheet Pelamar
    sheet_pelamar = cekApakahAdaExcel(workbook, 'Pelamar', ['Kode Pelamar', 'Nama', 'Kontak', 'Posisi Dilamar', 'Status Wawancara'])
    kode = f"P{sheet_pelamar.max_row:03d}"
    status_wawancara = "Belum"  # Status wawancara otomatis terisi dengan "Belum"
    sheet_pelamar.append([kode, nama, kontak, posisi, status_wawancara])
    workbook.save(FILE_NAME)
    workbook.close()
    print("Pelamar berhasil ditambahkan.")

from moduleExcel import FILE_NAME, os, openpyxl

def functionTampilWawancara():
    if not os.path.exists(FILE_NAME):
        print("File data rekrutmen tidak ditemukan.")
        return

    workbook = openpyxl.load_workbook(FILE_NAME)

    # Pastikan sheet Wawancara ada
    if 'Wawancara' not in workbook.sheetnames:
        print("Sheet Wawancara belum ada.")
        workbook.close()
        return

    sheet_wawancara = workbook['Wawancara']

    # Periksa apakah ada data di sheet Wawancara
    if sheet_wawancara.max_row == 1:  # Hanya header yang ada
        print("Belum ada data wawancara.")
        workbook.close()
        return

    # Pastikan sheet Lowongan ada
    if 'Lowongan' not in workbook.sheetnames:
        print("Sheet Lowongan belum ada. Tidak dapat menampilkan nama lowongan.")
        workbook.close()
        return

    sheet_lowongan = workbook['Lowongan']

    # Buat dictionary untuk kode lowongan dan nama/posisi lowongan
    info_lowongan = {}
    for row in sheet_lowongan.iter_rows(min_row=2, values_only=True):
        kode_lowongan = row[0]  # Kolom kode lowongan
        posisi = row[1]         # Kolom posisi/nama lowongan
        info_lowongan[kode_lowongan] = posisi

    # Dapatkan daftar lowongan yang memiliki data wawancara
    lowongan_terdaftar = set(row[0] for row in sheet_wawancara.iter_rows(min_row=2, values_only=True))

    if not lowongan_terdaftar:
        print("Tidak ada lowongan dengan data wawancara.")
        workbook.close()
        return

    # Tampilkan daftar lowongan
    print("\nDaftar Lowongan dengan Data Wawancara:")
    for kode_lowongan in lowongan_terdaftar:
        posisi = info_lowongan.get(kode_lowongan, "Posisi Tidak Diketahui")  # Jika posisi tidak ditemukan, tampilkan pesan default
        print(f"- {kode_lowongan} ({posisi})")

    # Input kode lowongan
    while True:
        kode_lowongan = input("\nMasukkan kode lowongan untuk melihat data wawancara (atau ketik 'CANCEL' untuk keluar): ")
        if kode_lowongan.upper() == 'CANCEL':
            print("Proses selesai.")
            workbook.close()
            return

        if kode_lowongan in lowongan_terdaftar:
            break
        print("Kode lowongan tidak valid. Silakan pilih dari daftar.")

    # Tampilkan data wawancara untuk lowongan yang dipilih
    print(f"\nDaftar Wawancara untuk Lowongan {kode_lowongan} ({info_lowongan.get(kode_lowongan, 'Posisi Tidak Diketahui')}):")
    ada_data = False
    for row in sheet_wawancara.iter_rows(min_row=2, values_only=True):
        if row[0] == kode_lowongan:  # Cocokkan kode lowongan
            print(f"Kode Pelamar: {row[1]}, Nama: {row[2]}, Posisi: {row[3]}, Tanggal: {row[4]}, Jam: {row[5]}")
            ada_data = True

    if not ada_data:
        print(f"Tidak ada data wawancara untuk lowongan dengan kode {kode_lowongan}.")

    workbook.close()

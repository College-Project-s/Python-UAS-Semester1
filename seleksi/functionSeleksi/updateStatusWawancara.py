from moduleExcel import FILE_NAME, os, openpyxl

def functionUpdateStatusWawancara():
    if not os.path.exists(FILE_NAME):
        print("File data rekrutmen tidak ditemukan.")
        return

    workbook = openpyxl.load_workbook(FILE_NAME)

    # Pastikan sheet Pelamar ada
    if 'Pelamar' not in workbook.sheetnames:
        print("Sheet Pelamar belum ada.")
        workbook.close()
        return

    # Pastikan sheet Seleksi ada
    if 'Seleksi' not in workbook.sheetnames:
        print("Sheet Seleksi belum ada.")
        workbook.close()
        return

    sheet_pelamar = workbook['Pelamar']
    sheet_seleksi = workbook['Seleksi']

    # Dapatkan daftar kode pelamar yang sudah ada di sheet Seleksi
    kode_pelamar_seleksi = set(row[0] for row in sheet_seleksi.iter_rows(min_row=2, values_only=True))

    # Periksa apakah ada data di sheet Pelamar
    if sheet_pelamar.max_row == 1:  # Hanya header yang ada
        print("Belum ada data pelamar.")
        workbook.close()
        return

    while True:
        # Filter pelamar dengan status wawancara "Proses" dan belum ada di sheet Seleksi
        pelamar_proses = [
            (row[0].value, row[1].value, row[3].value)  # Kode Pelamar, Nama, Posisi
            for row in sheet_pelamar.iter_rows(min_row=2)
            if row[4].value == "Proses" and row[0].value not in kode_pelamar_seleksi  # Status Wawancara = "Proses" dan belum di Seleksi
        ]

        if not pelamar_proses:
            print("Tidak ada pelamar dengan status wawancara 'Proses' yang belum masuk seleksi.")
            workbook.close()
            return

        # Tampilkan daftar pelamar dengan status wawancara "Proses" yang belum ada di Seleksi
        print("\nDaftar Pelamar dengan Status Wawancara 'Proses':")
        for kode, nama, posisi in pelamar_proses:
            print(f"Kode: {kode}, Nama: {nama}, Posisi: {posisi}")

        # Input kode pelamar untuk diupdate
        kode_pelamar = input("\nMasukkan kode pelamar untuk mengupdate status wawancara menjadi 'Selesai' (atau ketik 'CANCEL' untuk keluar): ")
        if kode_pelamar.upper() == 'CANCEL':
            print("Proses selesai.")
            workbook.close()
            return

        # Cari dan update status wawancara
        pelamar_ditemukan = False
        for row in sheet_pelamar.iter_rows(min_row=2):
            if row[0].value == kode_pelamar:  # Kode Pelamar
                pelamar_ditemukan = True
                row[4].value = "Selesai"  # Update status wawancara
                print(f"Status wawancara untuk pelamar {kode_pelamar} berhasil diperbarui menjadi 'Selesai'.")
                break

        if not pelamar_ditemukan:
            print(f"Tidak ditemukan pelamar dengan kode {kode_pelamar}. Silakan coba lagi.")
            continue

        # Simpan workbook setelah update
        workbook.save(FILE_NAME)

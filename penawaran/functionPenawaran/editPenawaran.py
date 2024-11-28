from moduleExcel import FILE_NAME, os, openpyxl

def functionEditPenawaran():
    if not os.path.exists(FILE_NAME):
        print("File data rekrutmen tidak ditemukan.")
        return

    workbook = openpyxl.load_workbook(FILE_NAME)

    # Pastikan sheet Penawaran ada
    if 'Penawaran' not in workbook.sheetnames:
        print("Sheet Penawaran belum ada.")
        workbook.close()
        return

    sheet_penawaran = workbook['Penawaran']
    sheet_lowongan = workbook['Lowongan']

    if sheet_penawaran.max_row == 1:
        print("Belum ada data Penawaran.")
        workbook.close()
        return

    # Buat dictionary kode pekerjaan -> nama posisi dari sheet Lowongan
    posisi_pekerjaan = {
        row[0]: row[1]  # row[0] = Kode Pekerjaan, row[1] = Nama/Posisi
        for row in sheet_lowongan.iter_rows(min_row=2, values_only=True)
    }
            
    while True:
        # Dapatkan daftar kode pekerjaan yang memiliki penawaran
        kode_pekerjaan_tersedia = set(row[0] for row in sheet_penawaran.iter_rows(min_row=2, values_only=True))

        if not kode_pekerjaan_tersedia:
            print("Tidak ada kode pekerjaan dengan data penawaran.")
            workbook.close()
            return

        # Tampilkan daftar kode pekerjaan dengan nama posisi
        print("\nDaftar Kode Pekerjaan dengan Penawaran:")
        for kode_pekerjaan in kode_pekerjaan_tersedia:
            posisi = posisi_pekerjaan.get(kode_pekerjaan, "Posisi Tidak Diketahui")  # Default jika posisi tidak ditemukan
            print(f"- {kode_pekerjaan} ({posisi})")
            
        # Masukkan kode pekerjaan
        kode_pekerjaan = input("\nMasukkan kode pekerjaan untuk mengedit benefit (atau ketik 'CANCEL' untuk keluar): ")
        if kode_pekerjaan.upper() == 'CANCEL':
            print("Proses selesai.")
            break

        # Filter benefit berdasarkan kode pekerjaan
        benefit_pekerjaan = [
            (index, row[1])  # Index (baris di Excel) dan benefit
            for index, row in enumerate(sheet_penawaran.iter_rows(min_row=2, values_only=True), start=2)
            if row[0] == kode_pekerjaan
        ]

        if not benefit_pekerjaan:
            print(f"Tidak ada benefit untuk pekerjaan dengan kode {kode_pekerjaan}.")
            continue

        # Tampilkan daftar benefit
        print(f"\nBenefit untuk pekerjaan dengan kode {kode_pekerjaan}:")
        for i, (index, benefit) in enumerate(benefit_pekerjaan, start=1):
            print(f"{i}. {benefit}")

        # Pilih benefit yang ingin diedit
        while True:
            try:
                pilihan = int(input("Pilih nomor benefit yang ingin diedit (atau ketik '0' untuk membatalkan): "))
                if pilihan == 0:
                    print("Proses edit dibatalkan.")
                    break

                if 1 <= pilihan <= len(benefit_pekerjaan):
                    baris_excel, benefit_lama = benefit_pekerjaan[pilihan - 1]
                    break

                print("Pilihan tidak valid. Masukkan nomor yang sesuai.")
            except ValueError:
                print("Input harus berupa angka.")

        if pilihan == 0:
            continue

        # Masukkan benefit baru
        benefit_baru = input(f"Masukkan benefit baru untuk menggantikan '{benefit_lama}' (atau ketik 'CANCEL' untuk membatalkan): ")
        if benefit_baru.upper() == 'CANCEL':
            print("Proses edit dibatalkan.")
            continue

        # Update benefit di file Excel
        sheet_penawaran.cell(row=baris_excel, column=2).value = benefit_baru
        print(f"Benefit '{benefit_lama}' berhasil diperbarui menjadi '{benefit_baru}'.")

    # Simpan workbook setelah selesai
    workbook.save(FILE_NAME)
    workbook.close()
    print("Data penawaran berhasil disimpan.")

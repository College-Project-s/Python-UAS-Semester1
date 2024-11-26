from moduleExcel import FILE_NAME, os, openpyxl

def functionHapusPenawaran():
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

    if sheet_penawaran.max_row == 1:
        print("Belum ada data Penawaran.")
        workbook.close()
        return

    while True:
        # Masukkan kode lowongan
        kode_lowongan = input("\nMasukkan kode lowongan untuk menghapus benefit (atau ketik 'CANCEL' untuk keluar): ")
        if kode_lowongan.upper() == 'CANCEL':
            print("Proses selesai.")
            break

        # Filter benefit berdasarkan kode lowongan
        benefit_lowongan = [
            (index, row[1])  # Index (baris di Excel) dan benefit
            for index, row in enumerate(sheet_penawaran.iter_rows(min_row=2, values_only=True), start=2)
            if row[0] == kode_lowongan
        ]

        if not benefit_lowongan:
            print(f"Tidak ada benefit untuk lowongan dengan kode {kode_lowongan}.")
            continue

        # Tampilkan daftar benefit
        print(f"\nBenefit untuk lowongan dengan kode {kode_lowongan}:")
        for i, (index, benefit) in enumerate(benefit_lowongan, start=1):
            print(f"{i}. {benefit}")

        # Pilih benefit yang ingin dihapus
        while True:
            try:
                pilihan = int(input("Pilih nomor benefit yang ingin dihapus (atau ketik '0' untuk membatalkan): "))
                if pilihan == 0:
                    print("Proses penghapusan dibatalkan.")
                    break

                if 1 <= pilihan <= len(benefit_lowongan):
                    baris_excel, benefit_dipilih = benefit_lowongan[pilihan - 1]
                    break

                print("Pilihan tidak valid. Masukkan nomor yang sesuai.")
            except ValueError:
                print("Input harus berupa angka.")

        if pilihan == 0:
            continue

        # Konfirmasi penghapusan
        konfirmasi = input(f"Yakin ingin menghapus benefit '{benefit_dipilih}'? (y/n): ").lower()
        if konfirmasi == 'y':
            sheet_penawaran.delete_rows(baris_excel)
            print(f"Benefit '{benefit_dipilih}' berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")

    # Simpan workbook setelah selesai
    workbook.save(FILE_NAME)
    workbook.close()
    print("Data penawaran berhasil diperbarui.")

from moduleExcel import FILE_NAME, os, openpyxl

# Function untuk menampilkan penawaran berdasarkan kode pekerjaan
def functionTampilPenawaran():
    if not os.path.exists(FILE_NAME):
        print("File data rekrutmen tidak ditemukan.")
        return

    workbook = openpyxl.load_workbook(FILE_NAME)

    # Pastikan sheet Penawaran dan Lowongan ada
    if 'Penawaran' not in workbook.sheetnames:
        print("Sheet Penawaran belum ada.")
        workbook.close()
        return

    if 'Lowongan' not in workbook.sheetnames:
        print("Sheet Lowongan belum ada.")
        workbook.close()
        return

    sheet_penawaran = workbook['Penawaran']
    sheet_lowongan = workbook['Lowongan']

    if sheet_penawaran.max_row == 1:  # Jika hanya header yang ada
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

        # Input kode pekerjaan
        kode_pekerjaan = input("\nMasukkan kode pekerjaan untuk melihat benefit (atau ketik 'CANCEL' untuk keluar): ")

        if kode_pekerjaan.upper() == 'CANCEL':
            print("Proses selesai.")
            break

        # Filter benefit berdasarkan kode pekerjaan
        benefit_pekerjaan = [
            row[1]  # Kolom 'Benefit'
            for row in sheet_penawaran.iter_rows(min_row=2, values_only=True)
            if row[0] == kode_pekerjaan  # Kolom 'Kode Pekerjaan'
        ]

        if not benefit_pekerjaan:
            print(f"Tidak ada benefit untuk pekerjaan dengan kode {kode_pekerjaan}.")
        else:
            posisi = posisi_pekerjaan.get(kode_pekerjaan, "Posisi Tidak Diketahui")
            print(f"\nBenefit untuk pekerjaan dengan kode {kode_pekerjaan} ({posisi}):")
            for benefit in benefit_pekerjaan:
                print(f"- {benefit}")

    workbook.close()

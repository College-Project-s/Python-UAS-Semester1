from moduleExcel import FILE_NAME, os, openpyxl

# Function untuk menampilkan penawaran berdasarkan kode pekerjaan
def functionTampilPenawaran():
    if not os.path.exists(FILE_NAME):
        print("File data rekrutmen tidak ditemukan.")
        return

    workbook = openpyxl.load_workbook(FILE_NAME)
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
            print(f"\nBenefit untuk pekerjaan dengan kode {kode_pekerjaan}:")
            for benefit in benefit_pekerjaan:
                print(f"- {benefit}")

    workbook.close()

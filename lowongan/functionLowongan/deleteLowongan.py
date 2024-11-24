from moduleExcel import FILE_NAME, os, openpyxl

# Function untuk menghapus lowongan
def functionHapusLowongan():
    if not os.path.exists(FILE_NAME):
        print("File data rekrutmen tidak ditemukan.")
        return

    workbook = openpyxl.load_workbook(FILE_NAME)
    if 'Lowongan' not in workbook.sheetnames:
        print("Sheet Lowongan belum ada.")
        return

    sheet = workbook['Lowongan']
    kode = input("Masukkan kode lowongan yang ingin dihapus (atau ketik 'CANCEL' untuk kembali): ")

    if kode.upper() == 'CANCEL':
        print("Proses penghapusan dibatalkan.")
        workbook.close()
        return

    lowongan_ditemukan = False

    for row_index, row in enumerate(sheet.iter_rows(min_row=2), start=2):
        if row[0].value == kode:
            lowongan_ditemukan = True
            konfirmasi = input(f"Yakin ingin menghapus lowongan dengan kode {kode}? (y/n): ")
            if konfirmasi.lower() == 'y':
                sheet.delete_rows(row_index)
                print(f"Lowongan dengan kode {kode} berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")
            break

    if not lowongan_ditemukan:
        print("Kode lowongan tidak ditemukan.")

    workbook.save(FILE_NAME)
    workbook.close()

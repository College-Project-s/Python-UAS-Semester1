from moduleExcel import FILE_NAME, os, openpyxl

# Function untuk menghapus pelamar
def functionHapusPelamar():
    if not os.path.exists(FILE_NAME):
        print("File data rekrutmen tidak ditemukan.")
        return

    workbook = openpyxl.load_workbook(FILE_NAME)
    if 'Pelamar' not in workbook.sheetnames:
        print("Sheet Pelamar belum ada.")
        return

    sheet = workbook['Pelamar']
    kode = input("Masukkan kode Pelamar yang ingin dihapus (atau ketik 'CANCEL' untuk kembali): ")

    if kode.upper() == 'CANCEL':
        print("Proses penghapusan dibatalkan.")
        workbook.close()
        return

    pelamar_ditemukan = False

    for row_index, row in enumerate(sheet.iter_rows(min_row=2), start=2):
        if row[0].value == kode:
            pelamar_ditemukan = True
            konfirmasi = input(f"Yakin ingin menghapus pelamar dengan kode {kode}? (y/n): ")
            if konfirmasi.lower() == 'y':
                sheet.delete_rows(row_index)
                print(f"Pelamar dengan kode {kode} berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")
            break

    if not pelamar_ditemukan:
        print("Kode pelamar tidak ditemukan.")

    workbook.save(FILE_NAME)
    workbook.close()

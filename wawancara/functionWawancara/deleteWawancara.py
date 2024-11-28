from moduleExcel import FILE_NAME, os, openpyxl

# Function untuk menghapus wawancara
def functionHapusWawancara():
    if not os.path.exists(FILE_NAME):
        print("File data rekrutmen tidak ditemukan.")
        return

    workbook = openpyxl.load_workbook(FILE_NAME)
    if 'Wawancara' not in workbook.sheetnames:
        print("Sheet Wawancara belum ada.")
        return

    sheet = workbook['Wawancara']
    print("---List Data Wawancara---")
    for row in sheet.iter_rows(min_row=2, values_only=True):
        print(f"Kode Pelamar: {row[1]}, Nama: {row[2]}, Posisi: {row[3]}, Tanggal: {row[4]}, Jam: {row[5]}")
        
    kode = input("\nMasukkan kode Pelamar yang ingin dihapus (atau ketik 'CANCEL' untuk kembali): ")

    if kode.upper() == 'CANCEL':
        print("Proses penghapusan dibatalkan.")
        workbook.close()
        return

    pelamar_ditemukan = False

    for row_index, row in enumerate(sheet.iter_rows(min_row=2), start=2):
        if row[1].value == kode:
            pelamar_ditemukan = True
            konfirmasi = input(f"Yakin ingin menghapus wawancara pelamar dengan kode {kode}? (y/n): ")
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

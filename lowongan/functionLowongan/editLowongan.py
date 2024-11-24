from moduleExcel import FILE_NAME, os, openpyxl

# Function untuk mengedit lowongan
def functionEditLowongan():
    if not os.path.exists(FILE_NAME):
        print("File data rekrutmen tidak ditemukan.")
        return

    workbook = openpyxl.load_workbook(FILE_NAME)
    if 'Lowongan' not in workbook.sheetnames:
        print("Sheet Lowongan belum ada.")
        return

    sheet = workbook['Lowongan']
    kode = input("Masukkan kode lowongan yang ingin diedit (atau ketik 'CANCEL' untuk kembali): ")

    if kode.upper() == 'CANCEL':
        print("Proses mengedit dibatalkan.")
        workbook.close()
        return
    
    lowongan_ditemukan = False

    for row in sheet.iter_rows(min_row=2):
        if row[0].value == kode:
            lowongan_ditemukan = True
            print(f"Data saat ini: Posisi = {row[1].value}, Deskripsi = {row[2].value}, Status = {row[3].value}")
            row[1].value = input("Masukkan posisi baru (kosongkan jika tidak ingin mengubah): ") or row[1].value
            row[2].value = input("Masukkan deskripsi baru (kosongkan jika tidak ingin mengubah): ") or row[2].value
            row[3].value = input("Masukkan status baru (Dibuka/Ditutup, kosongkan jika tidak ingin mengubah): ") or row[3].value
            print("Lowongan berhasil diperbarui.")
            break

    if not lowongan_ditemukan:
        print("Kode lowongan tidak ditemukan.")

    workbook.save(FILE_NAME)
    workbook.close()

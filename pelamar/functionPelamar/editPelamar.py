from moduleExcel import FILE_NAME, os, openpyxl

# Function untuk mengedit pelamar
def functionEditPelamar():
    if not os.path.exists(FILE_NAME):
        print("File data rekrutmen tidak ditemukan.")
        return

    workbook = openpyxl.load_workbook(FILE_NAME)
    if 'Pelamar' not in workbook.sheetnames:
        print("Sheet Pelamar belum ada.")
        return

    sheet = workbook['Pelamar']
    # Tampilkan data pelamar
    if sheet.max_row == 1:  # Hanya header yang ada
        print("Belum ada data pelamar.")
        workbook.close()
        return

    print("\nDaftar Pelamar:")
    for row in sheet.iter_rows(min_row=2, values_only=True):
        print(f"Kode: {row[0]}, Nama: {row[1]}, Kontak: {row[2]}, Posisi Dilamar: {row[3]}")
        
    kode = input("\nMasukkan kode pelamar yang ingin diedit (atau ketik 'CANCEL' untuk kembali): ")

    if kode.upper() == 'CANCEL':
        print("Proses mengedit dibatalkan.")
        workbook.close()
        return
    
    pelamar_ditemukan = False

    for row in sheet.iter_rows(min_row=2):
        if row[0].value == kode:
            pelamar_ditemukan = True
            'Nama', 'Kontak', 'Posisi Dilamar'
            print(f"Data saat ini: Nama = {row[1].value}, Kontak = {row[2].value}, Posisi Dilamar = {row[3].value}")
            row[1].value = input("Masukkan Nama baru (kosongkan jika tidak ingin mengubah): ") or row[1].value
            row[2].value = input("Masukkan Kontak baru (kosongkan jika tidak ingin mengubah): ") or row[2].value
            row[3].value = input("Masukkan Posisi Dilamar baru (kosongkan jika tidak ingin mengubah): ") or row[3].value
            print("Pelamar berhasil diperbarui.")
            break

    if not pelamar_ditemukan:
        print("Kode pelamar tidak ditemukan.")

    workbook.save(FILE_NAME)
    workbook.close()
